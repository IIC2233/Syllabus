import json
import socket
import sys
from threading import Lock, Thread
from time import sleep

import parametros as p
from partida import Partida
from protocolo import enviar, recibir


class Jugador:
    """Un cliente conectado. Tiene lado solo mientras está en la sala."""

    def __init__(self, socket_cliente: socket.socket) -> None:
        self.socket = socket_cliente
        self.nombre = None
        self.lado = None
        # Dos threads pueden enviarle a este cliente a la vez, y sin este lock
        # los bytes de ambos mensajes se mezclan y rompen el protocolo
        self.lock_envio = Lock()


class Servidor:
    def __init__(self, host: str, port: int) -> None:
        # La sala y la partida son compartidas por todos los threads
        self.sala = []
        self.partida = None
        self.piden_revancha = set()
        self.lock_sala = Lock()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen()

    def escuchar_conexiones(self) -> None:
        host, port = self.sock.getsockname()[:2]
        print(f"Servidor escuchando en {host}:{port}. Ctrl+C para cerrar.")
        while True:
            socket_cliente, direccion = self.sock.accept()
            print("Conexión aceptada desde", direccion)
            jugador = Jugador(socket_cliente)
            Thread(target=self.escuchar_cliente, args=(jugador,), daemon=True).start()

    def escuchar_cliente(self, jugador: Jugador) -> None:
        try:
            while True:
                mensaje = recibir(jugador.socket).decode("utf-8")
                try:
                    self.procesar_mensaje(jugador, json.loads(mensaje))
                except (ValueError, KeyError, TypeError, AttributeError) as error:
                    # Un mensaje mal formado no debe botar la partida del otro
                    print(f"[{jugador.nombre}] mensaje inválido: {mensaje!r} ({error!r})")
        except (ConnectionError, OSError):
            pass
        finally:
            self.desconectar(jugador)
            jugador.socket.close()

    def procesar_mensaje(self, jugador: Jugador, mensaje: dict) -> None:
        comando = mensaje["comando"]
        if comando == "unirse":
            self.unirse(jugador, mensaje["nombre"])
        elif comando == "mover":
            self.mover(jugador, mensaje["y"])
        elif comando == "pausa":
            self.pausar(jugador)
        elif comando == "revancha":
            self.pedir_revancha(jugador)
        else:
            print(f"[{jugador.nombre}] comando desconocido: {comando!r}")

    def unirse(self, jugador: Jugador, nombre: str) -> None:
        nombre = nombre.strip()
        with self.lock_sala:
            if jugador in self.sala:
                return
            if not nombre:
                razon = "El nombre no puede estar vacío"
            elif len(self.sala) == 2:
                razon = "La sala está llena"
            elif nombre in [otro.nombre for otro in self.sala]:
                razon = "Ese nombre ya está en uso"
            else:
                razon = None

            if razon is None:
                ocupados = [otro.lado for otro in self.sala]
                jugador.nombre = nombre
                jugador.lado = "izquierda" if "izquierda" not in ocupados else "derecha"
                self.sala.append(jugador)
                listos = len(self.sala) == 2

        if razon is not None:
            self.enviar(jugador, {"tipo": "rechazado", "razon": razon})
            return

        print(f"{nombre} entró a la sala por la {jugador.lado}")
        self.enviar(jugador, {"tipo": "aceptado"})
        if listos:
            self.iniciar_partida()

    def iniciar_partida(self) -> None:
        with self.lock_sala:
            self.piden_revancha.clear()
            izquierda, derecha = sorted(self.sala, key=lambda j: j.lado != "izquierda")
            jugadores = (izquierda, derecha)
            nombres = [izquierda.nombre, derecha.nombre]
            self.partida = Partida(nombres)
            partida = self.partida

        for jugador in jugadores:
            self.enviar(jugador, {
                "tipo": "inicio",
                "nombres": nombres,
                "duracion": p.DURACION_PARTIDA,
            })
        Thread(target=self.loop_partida, args=(partida,), daemon=True).start()

    def loop_partida(self, partida: Partida) -> None:
        """Hace avanzar una partida hasta que termine o sea reemplazada."""
        while True:
            sleep(1 / p.TICKS_POR_SEGUNDO)
            with self.lock_sala:
                if self.partida is not partida:
                    return
                # Se serializa dentro del lock para no enviar un estado a medias
                mensajes = [json.dumps(mensaje) for mensaje in partida.avanzar()]
                jugadores = list(self.sala)
                terminada = partida.terminada

            for mensaje in mensajes:
                self.enviar_a_todos(mensaje, jugadores)
            if terminada:
                return

    def mover(self, jugador: Jugador, y: int) -> None:
        with self.lock_sala:
            if self.partida is not None and jugador in self.sala:
                self.partida.mover_paleta(jugador.lado, y)

    def pausar(self, jugador: Jugador) -> None:
        with self.lock_sala:
            if self.partida is None or self.partida.terminada or jugador not in self.sala:
                return
            self.partida.en_pausa = not self.partida.en_pausa
            mensaje = json.dumps({
                "tipo": "pausa",
                "activa": self.partida.en_pausa,
                "nombre": jugador.nombre,
            })
            jugadores = list(self.sala)
        self.enviar_a_todos(mensaje, jugadores)

    def pedir_revancha(self, jugador: Jugador) -> None:
        with self.lock_sala:
            if self.partida is None or not self.partida.terminada or jugador not in self.sala:
                return
            self.piden_revancha.add(jugador)
            ambos = len(self.piden_revancha) == 2
            rivales = [otro for otro in self.sala if otro is not jugador]

        if ambos:
            self.iniciar_partida()
        else:
            for rival in rivales:
                self.enviar(rival, {"tipo": "revancha", "nombre": jugador.nombre})

    def desconectar(self, jugador: Jugador) -> None:
        with self.lock_sala:
            if jugador not in self.sala:
                return
            self.sala.remove(jugador)
            rivales = list(self.sala)
            # Sin rival no hay partida: el otro jugador también sale de la sala
            self.sala.clear()
            self.partida = None
            self.piden_revancha.clear()

        print(f"{jugador.nombre} se desconectó")
        for rival in rivales:
            self.enviar(rival, {"tipo": "rival_desconectado"})

    def enviar(self, jugador: Jugador, mensaje: dict) -> None:
        self.enviar_texto(jugador, json.dumps(mensaje))

    def enviar_a_todos(self, mensaje: str, jugadores: list) -> None:
        for jugador in jugadores:
            self.enviar_texto(jugador, mensaje)

    def enviar_texto(self, jugador: Jugador, mensaje: str) -> None:
        try:
            with jugador.lock_envio:
                enviar(jugador.socket, mensaje.encode("utf-8"))
        except OSError:
            # Ese cliente se desconectó: su propio thread se hace cargo
            pass


if __name__ == "__main__":
    # Si le entregas un número, el servidor usa ese puerto en vez del de parámetros
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else p.PORT
    servidor = Servidor(p.HOST, puerto)
    try:
        servidor.escuchar_conexiones()
    except KeyboardInterrupt:
        print("\nCerrando el servidor...")
    finally:
        servidor.sock.close()

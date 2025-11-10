from socket import socket
from queue import Queue
from random import randint
import parametros as p
import threading
import json
import time


class ThreadCliente(threading.Thread):
    """
    Clase que representa un cliente aceptado por el servidor.
    """

    def __init__(self, id_cliente: int, socket_cliente: socket, address: tuple) -> None:
        super().__init__()

        self.chunk_size = 2**16
        self.id_cliente = id_cliente
        self.socket = socket_cliente
        self.address = address

        self.dificultad = None
        self.rangos = [0, 0]
        self.ciudadanos = p.POBLACION_MAXIMA

        self.mensajes_a_enviar = Queue()

        # Debe ser daemon para que en caso que el servidor finalice su ejecución
        # este Thread también finalice
        self.daemon = True

        # Creamos un thread encargado de enviar cualquier mensaje
        self.enviar_mensajes_thread = threading.Thread(
            target=self.procesar_mensajes_a_enviar, daemon=True
        )

        # Creamos un thread encargado de crear meteoritos
        self.crear_meteoritos_thread = threading.Thread(
            target=self.crear_meteoritos, daemon=True
        )

    def procesar_mensajes_a_enviar(self) -> None:
        """
        Método encargado de ir enviando 1 mensaje a la vez si es que la cola
        para enviar mensajes tiene algo pendiente.
        """
        while True:
            # Recordar en una Queue, el get se queda esperando hasta que exista un elemento
            # y utiliza lock por dentro para asegurar que solo 1 elemento acceda a ella a la vez
            mensaje = self.mensajes_a_enviar.get()
            print(f"[Cliente {self.id_cliente}] Enviando {mensaje}")

            try:
                # Enviar mensaje
                bytes_mensaje = json.dumps(mensaje).encode("UTF-8")
                largo_mensaje = len(bytes_mensaje).to_bytes(4, "big")
                self.socket.sendall(largo_mensaje)
                self.socket.sendall(bytes_mensaje)

                # Avisamos que ya terminamos de procesar el elemento retirado
                self.mensajes_a_enviar.task_done()

            except BrokenPipeError:
                # Error cuando intentemos enviar algo y el socket ya se desconectó
                # Avisamos de todas formas que ya terminamos de procesar el elemento retirado
                self.mensajes_a_enviar.task_done()
                break

    def crear_meteoritos(self):
        """
        Método encargado de crear meteoritos según la dificultad dada
        """
        while self.ciudadanos > 0:
            x = randint(*self.rangos)
            mensaje = {"comando": "crear-meteorito", "data": x}
            self.mensajes_a_enviar.put(mensaje)
            time.sleep(p.DIFICULTAD[self.dificultad])

    def recibir_bytes(self, cantidad: int) -> bytearray:
        """
        Este método de recibir bytes desde el cliente hasta completar una cantidad
        específica, y pasarlos a un bytearray. [Mismo código de la EX4]
        """

        bytes_leidos = bytearray()
        while len(bytes_leidos) < cantidad:
            cantidad_restante = cantidad - len(bytes_leidos)
            bytes_leer = min(self.chunk_size, cantidad_restante)
            # Importante recv(N) va a leer hasta N bytes que le manden. Si le mandan
            # menos, por ejemplo, K (con K < N) entonces respuesta será de largo K
            respuesta = self.socket.recv(bytes_leer)
            if len(respuesta) < bytes_leer:
                # Si me llega más chico de lo esperado, algo pasó con el cliente,
                # retorno lo que llevo para intentar ver el mensaje
                return bytes_leidos
            bytes_leidos.extend(respuesta)
        return bytes_leidos

    def run(self) -> None:
        """
        Este método se encarga de escuchar los mensajes
         y utilizar el protocolo para decodificar el mensaje recibido.
        """

        self.enviar_mensajes_thread.start()
        while True:
            print(f"Cliente [{self.id_cliente}] Recibiendo largo del siguiente mensaje")

            # Recibamos primero el largo del mensaje:
            bytes_mensaje_parte_1 = self.recibir_bytes(4)
            largo_mensaje = int.from_bytes(bytes_mensaje_parte_1, "big")

            # Mensaje de largo 0, se cerró el cliente de golpe
            if largo_mensaje == 0:
                print(f"Cliente [{self.id_cliente}] Cliente desconectado")
                break

            # Ahora sabiendo el largo, recibamos el mensaje en sí:
            bytes_mensaje_parte_2 = self.recibir_bytes(largo_mensaje)

            try:
                mensaje = json.loads(bytes_mensaje_parte_2.decode("UTF-8"))
                self.procesar_mensaje(mensaje)

            except Exception as e:
                # En este caso, da lo mismo el tipo de error que ocurra, si el mensaje
                # del cliente provoca un error, se elimina su información y se deja de escuchar
                # de este modo el servidor sigue funcionando
                print(
                    f"[{self.id_cliente}] Cliente desconectado por el siguiente error {e}"
                )
                break

    def procesar_mensaje(self, mensaje: dict) -> None:
        """
        Si hay un mensaje, lo analizo según corresponde.
        """
        # empezar: Me dan los parámetros iniciales para empezar el juego
        if mensaje["comando"] == "empezar":
            self.rangos = mensaje["data"]["rangos"]
            self.dificultad = mensaje["data"]["dificultad"]

            # respondo que debe empezar con juego y empiezo el thread
            # encargado de crear meteoritos
            respuesta = {"comando": "empezar-juego"}
            self.mensajes_a_enviar.put(respuesta)
            self.crear_meteoritos_thread.start()

        # caer-meteorito: Reducir la cantidad de ciudadanos de la ciudad
        elif mensaje["comando"] == "caer-meteorito":
            afectados = randint(1, p.AFECTADOS)
            self.ciudadanos = max(self.ciudadanos - afectados, 0)
            mensaje = {"comando": "reducir-ciudadanos", "data": self.ciudadanos}
            self.mensajes_a_enviar.put(mensaje)

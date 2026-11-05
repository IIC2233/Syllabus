"""
Rival de prueba, para que puedas probar tu cliente sin abrir un segundo cliente.
Se ejecuta desde esta carpeta, con el servidor ya corriendo:

    python3 bot.py

No usa PyQt: es un programa de consola. Sigue a la pelota con un poco de error,
así que a veces se equivoca. Si pides revancha, siempre la acepta.

Para probar el bonus, ejecútalo con la opción bonus:

    python3 bot.py bonus

Así, 8 segundos después de empezar pausa la partida, 2 segundos más tarde la
reanuda, y 2 segundos después del fin pide revancha.
"""
import json
import socket
import sys
from random import uniform
from threading import Lock, Thread, Timer
from time import sleep

import parametros as p
from protocolo import enviar, recibir

VELOCIDAD_BOT = 6  # píxeles por iteración
ESPERA_BOT = 0.02  # segundos entre iteraciones
ERROR_BOT = 75  # píxeles que puede errar, como máximo, en cada jugada


class Bot:
    def __init__(self, puerto: int, bonus: bool) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((p.HOST, puerto))
        self.y = (p.ALTO_CANCHA - p.ALTO_PALETA) // 2
        self.objetivo = self.y
        self.error = 0
        self.ultimo_x = 0
        self.va_a_la_derecha = True
        self.en_juego = False
        self.conectado = True
        self.bonus = bonus
        self.en_pausa = False
        # Cambia con cada inicio y fin, para ignorar lo que quedó programado antes
        self.ronda = 0
        # Se envía desde dos threads, igual que en el servidor
        self.lock_envio = Lock()

    def mandar(self, mensaje: dict) -> None:
        with self.lock_envio:
            enviar(self.sock, json.dumps(mensaje).encode("utf-8"))

    def escuchar(self) -> None:
        try:
            while True:
                self.procesar(json.loads(recibir(self.sock).decode("utf-8")))
        except (ConnectionError, OSError):
            print("Se cerró la conexión con el servidor")
            self.conectado = False

    def procesar(self, mensaje: dict) -> None:
        tipo = mensaje["tipo"]
        if tipo == "aceptado":
            print("Bot aceptado, esperando rival...")
        elif tipo == "rechazado":
            print(f"Bot rechazado: {mensaje['razon']}")
        elif tipo == "inicio":
            self.en_juego = True
            self.en_pausa = False
            self.ronda += 1
            print(f"Empieza la partida: {mensaje['nombres']}")
            if self.bonus:
                self.programar(8, self.cambiar_pausa, True)
                self.programar(10, self.cambiar_pausa, False)
        elif tipo == "estado":
            self.apuntar(*mensaje["pelota"])
        elif tipo == "gol":
            print(f"Gol de {mensaje['goleador']}: {mensaje['marcador']}")
        elif tipo == "pausa":
            self.en_pausa = mensaje["activa"]
            self.en_juego = not mensaje["activa"]
        elif tipo == "fin":
            self.en_juego = False
            self.ronda += 1
            print(f"Fin de la partida. Ganador: {mensaje['ganador']}")
            if self.bonus:
                self.programar(2, self.pedir_revancha)
        elif tipo == "revancha":
            self.mandar({"comando": "revancha"})
        elif tipo == "rival_desconectado":
            self.en_juego = False
            self.ronda += 1
            print("El rival se desconectó. Volviendo a la sala...")
            self.mandar({"comando": "unirse", "nombre": "PepaBot"})

    def programar(self, segundos: int, accion, *argumentos) -> None:
        temporizador = Timer(segundos, self.ejecutar, [self.ronda, accion, *argumentos])
        temporizador.daemon = True
        temporizador.start()

    def ejecutar(self, ronda: int, accion, *argumentos) -> None:
        try:
            if ronda == self.ronda:
                accion(*argumentos)
        except OSError:
            pass

    def cambiar_pausa(self, activa: bool) -> None:
        if self.en_pausa != activa:
            self.mandar({"comando": "pausa"})

    def pedir_revancha(self) -> None:
        self.mandar({"comando": "revancha"})

    def apuntar(self, x: int, y: int) -> None:
        # Elige un nuevo error cada vez que la pelota cambia de dirección
        va_a_la_derecha = x > self.ultimo_x
        if x != self.ultimo_x and va_a_la_derecha != self.va_a_la_derecha:
            self.va_a_la_derecha = va_a_la_derecha
            self.error = uniform(-ERROR_BOT, ERROR_BOT)
        self.ultimo_x = x
        self.objetivo = y + p.TAMAÑO_PELOTA / 2 - p.ALTO_PALETA / 2 + self.error

    def jugar(self) -> None:
        self.mandar({"comando": "unirse", "nombre": "PepaBot"})
        Thread(target=self.escuchar, daemon=True).start()
        while self.conectado:
            sleep(ESPERA_BOT)
            if not self.en_juego:
                continue
            diferencia = self.objetivo - self.y
            paso = max(-VELOCIDAD_BOT, min(VELOCIDAD_BOT, diferencia))
            self.y = max(0, min(self.y + paso, p.ALTO_CANCHA - p.ALTO_PALETA))
            try:
                self.mandar({"comando": "mover", "y": int(self.y)})
            except OSError:
                return


if __name__ == "__main__":
    argumentos = sys.argv[1:]
    bonus = "bonus" in argumentos
    puertos = [a for a in argumentos if a != "bonus"]
    puerto = int(puertos[0]) if puertos else p.PORT
    try:
        Bot(puerto, bonus).jugar()
    except ConnectionError:
        print("No me pude conectar: ¿está corriendo el servidor?")
    except KeyboardInterrupt:
        print("\nCerrando el bot...")

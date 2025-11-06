import socket
import json
from threading import Thread
from PyQt5.QtCore import QThread, pyqtSignal


class Cliente(Thread):
    """
    Clase que representa un cliente del distribuidor de archivos.
    En cuanto se instancia trata de conectarse al servidor y
    posee métodos para comunicarse con este.

    Esta clase tiene un error
    TODO: Ronda 1.1
    """

    senal_empezar_juego = pyqtSignal()
    senal_aparecer_meteorito = pyqtSignal(int)
    senal_actualizar_poblacion = pyqtSignal(int)

    def __init__(self, port: int, host: str) -> None:
        """
        Inicializador de la clase y entabla conexión con el servidor.
        """
        super().__init__()

        self.port = port
        self.host = host
        self.chunk_size = 2**16
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Vamos a tratar de conectarnos. Si no funciona
        # cerramos todo
        try:
            self.socket.connect((self.host, self.port))
            print("[BACK] Conectado correctamente al servidor.")

        except ConnectionError:
            print("[BACK] No se logró conectar")
            self.socket.close()
            exit()

    def recibir_bytes(self, cantidad: int) -> bytearray:
        """
        Recibe N cantidad de bytes, los concatena y retorna como un
        único bytearray. [Mismo código de la EX4]
        """
        bytes_leidos = bytearray()
        while len(bytes_leidos) < cantidad:
            cantidad_restante = cantidad - len(bytes_leidos)
            bytes_leer = min(self.chunk_size, cantidad_restante)
            # Importante recv(N) va a leer hasta N bytes que le manden. Si le mandan
            # menos, por ejemplo, K (con K < N) entonces respuesta será de largo K
            respuesta = self.socket.recv(bytes_leer)
            bytes_leidos += respuesta
        return bytes_leidos

    def run(self) -> None:
        """
        Atento a cualquier mensaje del servidor.

        En este método hay 1 error 😱.
        TODO: Ronda 2.2
        """
        while True:
            largo = int.from_bytes(self.recibir_bytes(4), "big")
            mensaje = json.loads(self.recibir_bytes(largo).decode("UTF-8"))
            print(f"[BACK] Mensaje servidor: {mensaje}")

            if mensaje["comando"] == "empezar-juego":
                self.senal_empezar_juego()
            elif mensaje["comando"] == "crear-meteorito":
                self.senal_aparecer_meteorito.emit(mensaje["data"])
            elif mensaje["comando"] == "reducir-ciudadanos":
                self.senal_actualizar_poblacion.emit(mensaje["data"])

    def enviar_mensaje(self, mensaje: dict) -> None:
        """
        Serializar un mensaje y enviarlo al servidor siguiendo
        el formato necesario.
        """
        bytes_mensaje = json.dumps(mensaje).encode("UTF-8")
        largo_mensaje = len(bytes_mensaje).to_bytes(4, "big")
        self.socket.sendall(largo_mensaje)
        self.socket.sendall(bytes_mensaje)

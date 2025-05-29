from random import choice, random
from time import sleep
import threading
import socket

class Cliente:
    def __init__(self, port: int, host: str) -> None:
        # Inicializa el cliente, establece la conexión al servidor y crea un hilo para hacer preguntas
        print("Inicializando cliente...")
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.connect_to_server()
            self.listen()
            self.thread_preguntas = threading.Thread(target=self.consultar)
            self.thread_preguntas.start()  # Inicia las preguntas
            
        except ConnectionError:
            print("Conexión terminada.")
            self.socket_client.close()
            exit()

    def connect_to_server(self) -> None:
        # conecta el cliente al servidor
        self.socket_client.connect((self.host, self.port))
        print("Cliente conectado exitosamente al servidor.")


    def listen(self) -> None:
        # crea e inicializa un thread para comunicarse con el cliente
        thread = threading.Thread(target=self.listen_thread)
        thread.start()


    def send(self, msg: str) -> None:
        # codifica un str en bytes y lo envia al servidor
        msg_bytes = msg.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        self.socket_client.sendall(msg_length + msg_bytes)


    def listen_thread(self) -> None:
        # Thread que recibe respuestas del servidor
        while True:
            response_bytes_length = self.socket_client.recv(4)
            response_length = int.from_bytes(response_bytes_length, byteorder='big')
            response = bytearray()

            while len(response) < response_length:
                read_length = min(4096, response_length - len(response))
                response.extend(self.socket_client.recv(read_length))

            print(f"Respuesta recibida: {response.decode()}\n>>> ", end='')


    def consultar(self):
        while True:
            duda = choice(["Retiro de dinero", "Apertura de cuenta", "Prestamo"])
            print(f"Cliente solicita: {duda}")  # Imprimir tipo de pregunta
            self.send(duda)
            sleep(random() * 5 + 1)  # Espera entre 1 y 6 segundos



if __name__ == "__main__":
    port = 8081
    host = 'localhost'
    client = Cliente(port, host)
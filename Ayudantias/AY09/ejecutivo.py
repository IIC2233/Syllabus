import requests
from random import choice
import socket
import threading

class Ejecutivo:
    def __init__(self, port: int, host: str) -> None:
        # inicializa el servidor y comienza a escuchar conexiones de clientes
        print("Inicializando servidor...")
        self.host = host
        self.port = port
        self.respuestas = [" No puedes abrir una cuenta",
                            " Estás en dicom, no podemos procesar tu solicitud",
                            " Estamos en mantinimiento, vuelva mañana",
                            " Cuenta abierta"]
        
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()
        self.accept_connections()


    def bind_and_listen(self) -> None:
        # Enlaza el servidor al puerto especificado
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")


    def accept_connections(self) -> None:
        # inicializa un thread para escuchar conexiones entrantes y aceptarlas
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()


    def accept_connections_thread(self) -> None:
        # Función target que permitirá aceptar conexiones
        # crea un thread por cada cliente aceptado para poder escucharlo
        print("Servidor aceptando conexiones...")
        while True:
            client_socket, ip = self.socket_server.accept()
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket, ))
            listening_client_thread.start()


    def send(self, value: any, sock: socket.socket) -> None:
        # Envía respuestas al cliente
        stringified_value = str(value)
        msg_bytes = stringified_value.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        sock.sendall(msg_length + msg_bytes)


    def listen_client_thread(self, client_socket: socket.socket) -> None:
        # Recibe solicituds desde el cliente, las procesa y las responde
        print("Servidor conectado a un nuevo cliente...")
        while True:
            # Recibe los bytes
            response_bytes_length = client_socket.recv(4)
            response_length = int.from_bytes(response_bytes_length, byteorder='big')
            solicitud = client_socket.recv(response_length).decode()


            print(f"Recibimos una solicitud: {solicitud}")
            if solicitud == "Apertura de cuenta":
                respuesta = choice(self.respuestas)
                self.send(respuesta, client_socket)
                print("solicitud respondida al cliente")


            elif solicitud == "Prestamo":
                # Pedir respuesta al profesor
                URL = "http://localhost:4444/respuesta"
                respuesta = requests.get(URL)
                status = respuesta.status_code
                print(f"SOLICITUD AL JEFE: {status}")
                print(respuesta.json())
                self.send(respuesta.json()["texto"], client_socket)



if __name__ == "__main__":
    port = 8080
    host = 'localhost'
    server = Ejecutivo(port, host)
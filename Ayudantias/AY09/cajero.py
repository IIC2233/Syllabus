import socket
import threading
import requests

class Cajero:
    # Inicia el cliente y el servidor
    def __init__(self, host: str, port: int, datos_otro_cliente: dict) -> None:
        print("Inicializando Cajero P2P (2)...")
        self.host = host
        self.port = port
        self.datos_otro_cliente = datos_otro_cliente

        # Al ser P2P necesitamos un socket para ser cliente y un socket para ser servidor
        self.sockets = {
            'server': socket.socket(socket.AF_INET, socket.SOCK_STREAM),
            'client': socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        }
        self.bind_and_listen()
        self.accept_connections()

        try:
            self.connect_to_server()
        except ConnectionError:
            print("Conexión terminada por Error de Conexion.")
            self.sockets['client'].close()
            exit()


    def bind_and_listen(self) -> None:
        # enlaza y habilita el servidor para comenzar a escuchar conexiones entrantes
        self.sockets['server'].bind((self.host, self.port))
        self.sockets['server'].listen()
        print(f"Cajero P2P (2) escuchando en {self.host}:{self.port}...")


    def accept_connections(self) -> None:
        # Inicializa un thread que se encargara de aceptar conexiones entrantes
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self) -> None:
        # funcion target que acepta conexiones entrantes y les da un thread para poder escucharlos
        while True:
            client_socket, _ = self.sockets['server'].accept()
            threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket,),
                daemon=True
            ).start()


    def listen_client_thread(self, client_socket: socket.socket) -> None:
        # funcion target que recibe el contenido del cliente y lo procesa para darle una respuesta
        while True:
            try:
                response_bytes_length = client_socket.recv(4)
                response_length = int.from_bytes(response_bytes_length, byteorder='big')
                pregunta = client_socket.recv(response_length).decode()

                print(f"Recibimos una Solicitud: {pregunta}")

                if pregunta == "Retiro de dinero":
                    self.answer_client("Cajero: Girando y entregando dinero al Cliente", client_socket)
                else:
                    threading.Thread(
                        target=self.subir_solicitud,
                        args=(pregunta, client_socket),
                        daemon=True
                    ).start()

            except ConnectionResetError:
                print("Conexión con el cliente cerrada.")
                break

    def subir_solicitud(self, solicitud: str, client_socket: socket.socket) -> None:
        # Consulta a Tareo y responde al cliente con la respuesta obtenida
        respuesta = self.consultar_a_superiores(solicitud)
        self.answer_client(f"Respuesta del Jefe: {respuesta}", client_socket)
        self.notificar_profesor()


    def answer_client(self, value: str, sock: socket.socket) -> None:
        # envia respuesta al cliente correspondiente
        msg_bytes = value.encode()
        sock.sendall(len(msg_bytes).to_bytes(4, byteorder='big') + msg_bytes)


    # Metodos del cliente
    def connect_to_server(self) -> None:
        # Conecta el Docencio (como cliente) al Tareo (el servidor)
        self.sockets['client'].connect(
            (self.datos_otro_cliente['host'], self.datos_otro_cliente['port'])
        )
        print("Cliente conectado exitosamente al otro cliente.")


    def consultar_a_superiores(self, pregunta: str) -> str:
        # Envia preguntas a Ejecutivo y espera la respuesta
        self.send(pregunta)
        response = self.sockets['client'].recv(4096).decode()
        return response

    def send(self, msg: str) -> None:
        # manda mensaje al Tareo (Servidor)
        msg_bytes = msg.encode()
        self.sockets['client'].sendall(len(msg_bytes).to_bytes(4, byteorder='big') + msg_bytes)


    def notificar_profesor(self) -> None:
        # Le indica al profesor (Server Flask) que ya contesto una pregunta correctamente
        try:
            response = requests.post("http://localhost:4444/preguntas")
            if response.status_code == 200:
                print(f"Contador de preguntas actualizado: {response.json()['texto']}")
        except requests.RequestException as e:
            print(f"Error al conectar con el profesor: {e}")


if __name__ == "__main__":
    host = 'localhost'
    port = 8081
    datos_otro_cliente = {'port': 8080, 'host': 'localhost'}
    client = Cajero(host, port, datos_otro_cliente)
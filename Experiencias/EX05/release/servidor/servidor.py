import socket
import sys
from thread_cliente import ThreadCliente


class Servidor:
    """
    Clase que representa un servidor distribuidor de archivos.
    En cuanto se instancia levanta un socket para escuchar potenciales
    clientes.
    """

    id_clientes = 0

    def __init__(self, port: int, host: str) -> None:
        """
        Inicializar el servidor.
        """
        self.host = host
        self.port = port
        self.clientes = {}
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_listen(self) -> None:
        """
        Método que conecta el servidor al host y port dado.
        """
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host} : {self.port}")

    def accept_connections_thread(self) -> None:
        """
        Función encargada de aceptar clientes y asignarles un Thread para su atención.
        """
        while True:
            socket_cliente, address = self.socket_server.accept()
            print(f"Nuevo cliente conectado: {socket_cliente} {address}")

            # Creamos nuestro "minion" encargado de escuchar exclusivamente al cliente.
            listening_client_thread = ThreadCliente(
                self.id_clientes, socket_cliente, address
            )

            # Siempre se recomienda guardar la info del cliente para fácil acceso
            # (administrar clientes, cortar conexiones, etc.)
            self.clientes[self.id_clientes] = listening_client_thread

            self.id_clientes += 1
            listening_client_thread.start()


if __name__ == "__main__":
    # Recibimos el puerto y host por consola, pero si no llega damos valores
    # por defecto.
    PORT = 4444 if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = "localhost" if len(sys.argv) < 3 else sys.argv[2]
    """
    Ahora podemos ejecutar el archivo de la siguientes 3 formas:
     - python3 servidor.py
     - python3 servidor.py 4441
     - python3 servidor.py 1133 localhost

    OJO: recordar que el puerto debemos pasarlo siempre como int, no str.
    """
    server = Servidor(PORT, HOST)
    server.bind_listen()
    print("Presione Control+C para detener el servidor")
    try:
        server.accept_connections_thread()
    except KeyboardInterrupt:
        print("Cerrando servidor")

    server.socket_server.close()
    exit(1)

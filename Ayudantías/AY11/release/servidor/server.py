from os import listdir, path
import socket
import threading
import json
import os
import base64


class Server:
    def __init__(self, host: str, port: int, file_dir: str):
        self.host = host
        self.port = port
        self.file_dir = file_dir

        if not path.exists(self.file_dir):
            os.makedirs(self.file_dir)
            print(f"Directorio '{self.file_dir}' creado.")

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_info = {}
        self.info_lock = threading.Lock()

        self.bind_and_listen()
        self.accept_connections()

    def bind_and_listen(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

    def accept_connections(self) -> None:
        print("Servidor aceptando conexiones...")

        while True:
            try:
                client_socket, addr = self.server_socket.accept()

                with self.info_lock:
                    self.client_info[addr] = {"socket": client_socket, "username": "Desconocido"}

                listening_client_thread = threading.Thread(
                    target=self.client_connection,
                    args=(client_socket, addr),
                    daemon=True)
                listening_client_thread.start()
            except OSError:
                print("Error al aceptar conexiones (servidor cerrándose).")
                break

        print("Cerrando servidor...")
        with self.info_lock:
            for info in self.client_info.values():
                info["socket"].close()
        self.server_socket.close()

    def client_connection(self, client_socket: socket.socket, addr: tuple) -> None:
        print(f"Nuevo cliente conectado al servidor: {addr}")

        local_username = "Desconocido"  # Nombre interno asignado al usuario

        try:
            while True:
                operation, file_name = None, None
                try:
                    # TODO: Recibir request
                    pass

                except (ConnectionError, OSError) as e:
                    print(
                        f"Conexión perdida con el cliente {addr} (Usuario: {local_username}). Error: {e}")
                    break
                except (UnicodeDecodeError, json.JSONDecodeError):
                    self.send_data(json.dumps(
                        {"type": "error", "mensaje": "JSON enviado inválido."}), client_socket)
                    continue
                except (AttributeError, ValueError, TypeError):
                    self.send_data(json.dumps(
                        {"type": "error", "mensaje": "Data del JSON enviado inválida."}), client_socket)
                    continue

                if operation == 'carga':
                    # TODO: Manejar operación
                    pass

                elif operation == 'descarga':
                    # TODO: Manejar operación
                    pass

                elif operation == 'listar_usuarios':
                    # TODO: Manejar operación
                    pass

                elif operation == 'mensaje_directo':
                    # TODO: Manejar operación
                    pass

                else:
                    self.send_data(json.dumps(
                        {"type": "error", "mensaje": f"Operación '{operation}' no reconocida."}), client_socket)

        finally:
            print(f"Cerrando conexión y limpiando socket para {addr} (Usuario: {local_username})")
            client_socket.close()
            with self.info_lock:
                if addr in self.client_info:
                    del self.client_info[addr]

    def send_data(self, data: str, client_socket: socket.socket) -> None:
        # TODO: Completar método
        pass


if __name__ == "__main__":
    server = Server("localhost", 8080, "./archivos_servidor")

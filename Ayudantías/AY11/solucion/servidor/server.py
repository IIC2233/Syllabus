from os import path
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
                    target=self.client_conection,
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

    def client_conection(self, client_socket: socket.socket, addr: tuple) -> None:
        print(f"Nuevo cliente conectado al servidor: {addr}")

        local_username = "Desconocido"

        try:
            while True:
                command, file_name = None, None
                try:
                    json_size_bytes = client_socket.recv(4)
                    if not json_size_bytes:
                        print(
                            f"Cliente {addr} (Usuario: {local_username}) desconectado (conexión cerrada).")
                        break

                    json_size = int.from_bytes(
                        json_size_bytes, byteorder='big')

                    current_bytes = bytearray()
                    while len(current_bytes) < json_size:
                        read_length = min(1024, json_size - len(current_bytes))
                        chunk = client_socket.recv(read_length)
                        if not chunk:
                            raise ConnectionError(
                                f"Conexión perdida con {addr} (Usuario: {local_username}) mientras se leía JSON.")
                        current_bytes.extend(chunk)

                    data = json.loads(current_bytes.decode('utf-8'))
                    command = data.get('comando')

                    client_reported_name = data.get('username')
                    if client_reported_name:
                        local_username = client_reported_name
                        with self.info_lock:
                            if addr in self.client_info:
                                self.client_info[addr]["username"] = client_reported_name

                except (ConnectionError, OSError) as e:
                    print(
                        f"Conexión perdida con el cliente {addr} (Usuario: {local_username}). Error: {e}")
                    break
                except (UnicodeDecodeError, json.JSONDecodeError):
                    self.send_data(json.dumps(
                        {"tipo": "error", "descripcion": "JSON enviado inválido."}), client_socket)
                    continue
                except (AttributeError, ValueError, TypeError):
                    self.send_data(json.dumps(
                        {"tipo": "error", "descripcion": "Data del JSON enviado inválida."}), client_socket)
                    continue

                if command == 'carga':
                    try:
                        file_name = data.get('file_name')
                        file_content_b64 = data.get('file_content_b64')

                        if not file_name or file_content_b64 is None:
                            raise ValueError("Faltan 'file_name' o 'file_content_b64'.")

                        file_bytes = base64.b64decode(file_content_b64)

                    except (ValueError, base64.binascii.Error) as e:
                        self.send_data(json.dumps(
                            {"tipo": "error", "descripcion": f"Parámetros inválidos para la carga. {e}"}), client_socket)
                        continue
                    except (ConnectionError, OSError) as e:
                        print(
                            f"Conexión perdida con el cliente {addr} (Usuario: {local_username}) durante la carga. Error: {e}")
                        break

                    file_path = path.join(self.file_dir, file_name)
                    try:
                        with open(file_path, 'wb') as file:
                            file.write(file_bytes)

                        self.send_data(json.dumps(
                            {"tipo": "confirmacion", "descripcion": f"Archivo {file_name} subido por {local_username}!"}), client_socket)
                    except IOError as e:
                        print(f"Error al escribir archivo {file_name}: {e}")
                        self.send_data(json.dumps(
                            {"tipo": "error", "descripcion": f"Error interno al guardar {file_name}."}), client_socket)

                elif command == 'descarga':
                    try:
                        file_name = data.get('file_name')
                        file_path = path.join(self.file_dir, file_name)
                        file_exists = path.exists(file_path) and path.isfile(file_path)

                        if not file_name or not file_exists:
                            self.send_data(json.dumps(
                                {"tipo": "error", "descripcion": f"Archivo '{file_name}' no existe en el servidor."}), client_socket)
                            continue

                    except (FileNotFoundError, PermissionError, OSError, TypeError):
                        self.send_data(json.dumps(
                            {"tipo": "error", "descripcion": "No se pudo obtener el archivo indicado."}), client_socket)
                        continue

                    try:
                        with open(file_path, 'rb') as file:
                            file_bytes = file.read()
                            file_b64 = base64.b64encode(file_bytes).decode('utf-8')

                        response = {
                            "tipo": "archivo_descargado",
                            "file_name": file_name,
                            "file_content_b64": file_b64,
                            "username": "Servidor"
                        }
                        self.send_data(json.dumps(response), client_socket)

                    except IOError as e:
                        print(f"Error al leer archivo {file_name}: {e}")
                        self.send_data(json.dumps(
                            {"tipo": "error", "descripcion": f"Error interno al leer {file_name}."}), client_socket)

                elif command == 'listar_usuarios':
                    lista_nombres = []
                    with self.info_lock:
                        lista_nombres = [info["username"] for info in self.client_info.values()]

                    response = {
                        "tipo": "lista_usuarios",
                        "usuarios": lista_nombres,
                        "username": "Servidor"
                    }
                    self.send_data(json.dumps(response), client_socket)

                elif command == 'mensaje_directo':
                    destinatario = data.get("destinatario")
                    mensaje = data.get("mensaje")

                    if not destinatario or not mensaje:
                        self.send_data(json.dumps(
                            {"tipo": "error", "descripcion": "Falta 'destinatario' o 'mensaje'."}), client_socket)
                        continue

                    target_socket = None
                    with self.info_lock:
                        for info in self.client_info.values():
                            if info["username"] == destinatario:
                                target_socket = info["socket"]
                                break

                    if target_socket:
                        payload = {
                            "tipo": "mensaje_entrante",
                            "remitente": local_username,
                            "mensaje": mensaje,
                            "username": "Servidor"
                        }
                        self.send_data(json.dumps(payload), target_socket)
                        self.send_data(json.dumps(
                            {"tipo": "confirmacion", "descripcion": f"Mensaje enviado a {destinatario}."}), client_socket)
                    else:
                        self.send_data(json.dumps(
                            {"tipo": "error", "descripcion": f"Usuario '{destinatario}' no encontrado o desconectado."}), client_socket)

                else:
                    self.send_data(json.dumps(
                        {"tipo": "error", "descripcion": f"Operación '{command}' no reconocida."}), client_socket)

        finally:
            print(f"Cerrando conexión y limpiando socket para {addr} (Usuario: {local_username})")
            client_socket.close()
            with self.info_lock:
                if addr in self.client_info:
                    del self.client_info[addr]

    def send_data(self, data: str, client_socket: socket.socket) -> None:
        try:
            data_bytes = data.encode('utf-8')
            data_length = len(data_bytes)
            client_socket.sendall(data_length.to_bytes(4, byteorder='big'))
            client_socket.sendall(data_bytes)

        except (ConnectionError, OSError):
            print("[send_data] Conexión interrumpida con un cliente durante el envío.")


if __name__ == "__main__":
    server = Server("localhost", 8080, "./archivos_servidor")

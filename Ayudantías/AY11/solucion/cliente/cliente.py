import socket
import threading
import json
import sys
import os
import base64


COMMANDS_INFO = [
    ("lista", "Ver usuarios conectados"),
    ("msg <usuario> <mensaje>", "Enviar mensaje directo"),
    ("carga <ruta_archivo>", "Subir un archivo al servidor"),
    ("descargar <nombre_archivo>", "Descargar un archivo del servidor"),
    ("quit", "Salir"),
]


class Cliente:

    def __init__(self, port, host, nombre_cliente):
        print(f"Creando cliente '{nombre_cliente}'")
        self.port = port
        self.host = host
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nombre_cliente = nombre_cliente
        self.is_connected = False

        try:
            self.connect_to_server()
            self.listen()
        except ConnectionRefusedError:
            print(f'Error: No se pudo conectar al servidor en {host}:{port}')
            self.socket_cliente.close()
            raise

    def connect_to_server(self):
        self.socket_cliente.connect((self.host, self.port))
        self.is_connected = True
        print(f'Cliente conectado a servidor {self.host}:{self.port}')

    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def listen_thread(self):
        while self.is_connected:
            try:
                header = self.socket_cliente.recv(4)
                if not header:
                    print("Servidor cerró la conexión (header vacío).")
                    break

                msg_length = int.from_bytes(header, byteorder='big')

                chunks = []
                bytes_recibidos = 0
                while bytes_recibidos < msg_length:
                    chunk_size = min(msg_length - bytes_recibidos, 1024)
                    chunk = self.socket_cliente.recv(chunk_size)
                    if not chunk:
                        print("Servidor cerró la conexión (chunk vacío).")
                        raise ConnectionError("Conexión perdida")
                    chunks.append(chunk)
                    bytes_recibidos += len(chunk)

                data = b''.join(chunks)

                decoded_data = data.decode('utf-8')
                data_json = json.loads(decoded_data)

                self.decode_msg_from_server(data_json)

            except json.JSONDecodeError:
                print(f"Error: Se recibió un JSON mal formado: {decoded_data}")
            except (ConnectionError, ConnectionResetError, OSError):
                print("Conexión con el servidor perdida.")
                self.is_connected = False
            except UnicodeDecodeError:
                print(f"Error: Se recibió data que no es UTF-8. ({len(data)} bytes)")

        print("Hilo de escucha terminado.")
        self.is_connected = False

    def send_json(self, msg: dict):
        if not self.is_connected:
            print("Error: No conectado.")
            return
        try:
            if "username" not in msg:
                msg["username"] = self.nombre_cliente

            json_msg = json.dumps(msg)
            msg_to_send = json_msg.encode('utf-8')
            length = len(msg_to_send)

            self.socket_cliente.sendall(
                length.to_bytes(4, byteorder='big') + msg_to_send)

        except (ConnectionResetError, OSError) as e:
            print(f"Error al enviar: {e}")
            self.is_connected = False

    def decode_msg_from_server(self, msg: dict):

        tipo = msg.get("tipo")
        username = msg.get("username", "Sistema")

        if tipo == "lista_usuarios":
            usuarios = msg.get('usuarios', [])
            print(f"\n[Usuarios Conectados]: {', '.join(usuarios)}\n> ", end="")

        elif tipo == "mensaje_entrante":
            remitente = msg.get('remitente', '??')
            mensaje = msg.get('mensaje', '')
            print(f"\n[Mensaje de {remitente}]: {mensaje}\n> ", end="")

        elif tipo == "archivo_descargado":
            file_name = msg.get('file_name', 'descarga_default.dat')
            file_b64 = msg.get('file_content_b64')

            if file_b64:
                try:
                    file_bytes = base64.b64decode(file_b64)
                    with open(file_name, 'wb') as f:
                        f.write(file_bytes)
                    print(
                        f"\n[Sistema]: Archivo '{file_name}' descargado correctamente.\n> ", end="")
                except Exception as e:
                    print(
                        f"\n[Error]: No se pudo decodificar o guardar el archivo '{file_name}': {e}\n> ", end="")
            else:
                print(f"\n[Error]: El servidor envió un archivo vacío ('{file_name}').\n> ", end="")

        elif tipo == "confirmacion":
            print(f"\n[Sistema]: {msg.get('descripcion')}\n> ", end="")

        elif tipo == "error":
            print(f"\n[Error del Servidor]: {msg.get('descripcion')}\n> ", end="")

        else:
            pass

    def mandar_solicitud_archivo(self, tipo, nombre_archivo):

        if tipo == "descarga":
            print(f"Solicitando descarga de '{nombre_archivo}'...")
            control_message = {
                "comando": "descarga",
                "file_name": nombre_archivo
            }
            self.send_json(control_message)

        elif tipo == "carga":
            try:
                with open(nombre_archivo, 'rb') as f:
                    file_bytes = f.read()

                file_b64 = base64.b64encode(file_bytes).decode('utf-8')

                nombre_archivo_servidor = os.path.basename(nombre_archivo)

                print(f"Enviando '{nombre_archivo_servidor}' ({len(file_bytes)} bytes)...")

                control_message = {
                    "comando": "carga",
                    "file_name": nombre_archivo_servidor,
                    "file_content_b64": file_b64
                }
                self.send_json(control_message)

            except FileNotFoundError:
                print(f"[Error Local]: No se encontró el archivo '{nombre_archivo}'")
            except Exception as e:
                print(f"[Error Local]: No se pudo leer o codificar el archivo: {e}")

    def mandar_solicitud_alumnos(self):
        print("Solicitando lista de alumnos...")
        control_message = {
            "comando": "listar_usuarios"
        }
        self.send_json(control_message)

    def mandar_mensaje_alumno(self, destinado, msg):
        print(f"Enviando mensaje a {destinado}...")
        control_message = {
            "comando": "mensaje_directo",
            "destinatario": destinado,
            "mensaje": msg
        }
        self.send_json(control_message)


if __name__ == '__main__':
    port = 8080
    host = 'localhost'

    try:
        nombre = input("Ingresa tu nombre de usuario: ")
        if not nombre:
            nombre = "Invitado"

        client = Cliente(port, host, nombre)

        print("\n--- Cliente Conectado ---")
        print("Comandos disponibles:")
        for cmd, desc in COMMANDS_INFO:
            print(f"  {cmd:28} - {desc}")
        print("--------------------------")

        while client.is_connected:
            accion = input("> ")
            if not accion:
                continue

            partes = accion.split(' ', 1)
            comando = partes[0].lower()

            if comando == 'quit':
                print("Desconectando...")
                client.is_connected = False
                client.socket_cliente.close()
                break

            elif comando == 'lista':
                client.mandar_solicitud_alumnos()

            elif comando == 'msg' and len(partes) > 1:
                partes_msg = partes[1].split(' ', 1)
                if len(partes_msg) == 2:
                    destinatario, mensaje = partes_msg
                    client.mandar_mensaje_alumno(destinatario, mensaje)
                else:
                    print("Uso: msg <usuario> <mensaje>")

            elif comando == 'carga' and len(partes) > 1:
                client.mandar_solicitud_archivo("carga", partes[1])

            elif comando == 'descargar' and len(partes) > 1:
                client.mandar_solicitud_archivo("descarga", partes[1])

            elif comando in ['msg', 'carga', 'descargar']:
                print(f"Comando '{comando}' incompleto. Revisa el uso.")

            else:
                if comando not in ['lista']:
                    print(f"Comando '{comando}' no reconocido.")

    except ConnectionRefusedError:
        print("No se pudo iniciar el cliente. ¿El servidor está corriendo?")
    except KeyboardInterrupt:
        print("\nCerrando cliente (Ctrl+C)...")
    finally:
        print("Programa terminado.")

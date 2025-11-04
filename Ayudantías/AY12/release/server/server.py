from gato import Partida
import threading
import socket
import json


class Server:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_sockets = {}
        self.client_events = {}
        self.en_espera = []
        self.partidas = {}
        self.info_lock = threading.Lock()

        self.bind_and_listen()
        self.accept_connections()

    def bind_and_listen(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(8)
        print(f"Servidor escuchando en {self.host}:{self.port}")

    def accept_connections(self) -> None:
        print("Servidor aceptando conexiones...")

        while True:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"Nueva conexión desde {addr}")

                with self.info_lock:
                    self.en_espera.append(addr)
                    self.client_sockets[addr] = client_socket
                    # PARTE 1: COMPLETAR

                self.send_json(client_socket, {
                    "accion": "espera",
                    "mensaje": "Esperando oponente..."
                })

                threading.Thread(
                    target=self.client_connection,
                    args=(client_socket, addr),
                    daemon=True
                ).start()

                if len(self.en_espera) >= 2:
                    # PARTE 1: COMPLETAR
                    j1 = self.en_espera.pop(0)
                    j2 = self.en_espera.pop(0)
                    self.crear_partida(j1, j2)

            except OSError:
                print("Error al aceptar conexiones (servidor cerrándose).")
                break

        print("Cerrando servidor...")
        with self.info_lock:
            for socket_ in self.client_sockets.values():
                socket_.close()
        self.server_socket.close()

    def crear_partida(self, addr_1, addr_2):
        partida = Partida(addr_1, addr_2)
        key = (addr_1, addr_2)
        with self.info_lock:
            self.partidas[key] = partida
        print(f"Partida creada entre {addr_1} y {addr_2}")
        self.send_json(self.client_sockets[addr_1], {"accion": "inicio", "simbolo": "X"})
        self.send_json(self.client_sockets[addr_2], {"accion": "inicio", "simbolo": "O"})
        self.broadcast(partida, {"accion": "turno", "simbolo": "X"})

    def client_connection(self, client_socket, addr):
        try:
            while True:
                size_bytes = client_socket.recv(4)
                if not size_bytes:
                    break
                data_length = int.from_bytes(size_bytes, byteorder='big')
                data = client_socket.recv(data_length).decode('utf-8')
                msg = json.loads(data)
                self.procesar_mensaje(addr, msg)

        except (ConnectionResetError, ConnectionAbortedError):
            print(f"Cliente {addr} desconectado.")
        finally:
            self.jugador_desconectado(addr)
            client_socket.close()

    def procesar_mensaje(self, addr, msg):
        accion = msg.get("accion")

        if accion == "jugada":
            # PARTE 2: COMPLETAR
            pass
        
        # PARTE 1: COMPLETAR

    def jugador_desconectado(self, addr):
        partida = self.obtener_partida(addr)
        if partida:
            oponente_addr = partida.obtener_oponente(addr)
            if oponente_addr:
                self.send_json(self.client_sockets[oponente_addr], {"accion": "abandono",})
            self.eliminar_partida(partida)

        with self.info_lock:
            if addr in self.client_sockets.keys():
                del self.client_sockets[addr]
            if addr in self.en_espera:
                self.en_espera.remove(addr)

    def obtener_partida(self, addr):
        for ids, partida in self.partidas.items():
            if addr in ids:
                return partida
        return None

    def eliminar_partida(self, partida):
        for key, p in list(self.partidas.items()):
            if p == partida:
                with self.info_lock:
                    del self.partidas[key]
                    break

    def send_json(self, client_socket: socket.socket, data: dict) -> None:
        try:
            data_bytes = json.dumps(data).encode('utf-8')
            data_length = len(data_bytes)
            client_socket.sendall(data_length.to_bytes(4, byteorder='big'))
            client_socket.sendall(data_bytes)
        except (ConnectionError, OSError):
            print("[send_json] Error enviando datos al cliente.")

    def broadcast(self, partida: Partida, data: dict):
        for addr in partida.jugadores:
            self.send_json(self.client_sockets[addr], data)


if __name__ == "__main__":
    server = Server("localhost", 8080)

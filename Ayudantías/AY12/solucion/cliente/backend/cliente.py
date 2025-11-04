from PyQt5.QtCore import QObject, pyqtSignal
import threading
import socket
import json

class Cliente(QObject):
    senal_inicio = pyqtSignal()
    senal_turno = pyqtSignal(str)
    senal_jugador = pyqtSignal(str)
    senal_actualizar_tablero = pyqtSignal(int, int, str)
    senal_fin = pyqtSignal(str, str)

    def __init__(self, host: str, port: int):
        super().__init__()
        self.host = host
        self.port = port
        self.simbolo = None
        self.turno = False
        self.tablero = [["" for _ in range(3)] for _ in range(3)]

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.connect_to_server()
            self.listen()
        except ConnectionRefusedError:
            print(f'Error: No se pudo conectar al servidor en {host}:{port}')
            self.socket.close()
        
    def connect_to_server(self):
        self.socket.connect((self.host, self.port))
        self.is_connected = True
        print(f'Cliente conectado a servidor {self.host}:{self.port}')
    
    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def listen_thread(self):
        while self.is_connected:
            try:
                header = self.socket.recv(4)
                if not header:
                    print("Servidor cerró la conexión (header vacío).")
                    break
    
                msg_length = int.from_bytes(header, byteorder='big')

                data = self.socket.recv(msg_length)
                if not data:
                    break

                decoded_data = data.decode('utf-8')
                data_json = json.loads(decoded_data)

                self.procesar_mensaje(data_json)

            except json.JSONDecodeError:
                print(f"Error: Se recibió un JSON mal formado: {decoded_data}")
            except (ConnectionError, ConnectionResetError, OSError):
                print("Conexión con el servidor perdida.")
                self.is_connected = False

        print("Hilo de escucha terminado.")
        self.is_connected = False

    def procesar_mensaje(self, msg: dict):
        tablero = msg.get("tablero")

        if tablero:
            self.actualizar_tablero(tablero)
        
        if msg["accion"] == "inicio":
            self.simbolo = msg["simbolo"]
            print(f"Símbolo {self.simbolo}")
            self.senal_inicio.emit()
            self.senal_jugador.emit(self.simbolo)
        
        if msg["accion"] == "turno":
            self.senal_turno.emit(msg["simbolo"])
            if msg["simbolo"] == self.simbolo:
                self.turno = True
        
        if msg["accion"] == "ganador":
            if msg["simbolo"] == self.simbolo:
                self.senal_fin.emit(self.simbolo, "ganaste")
            else:
                self.senal_fin.emit(self.simbolo, "perdiste")
        
        if msg["accion"] == "empate":
            self.senal_fin.emit(self.simbolo, "empataste")

        if msg["accion"] == "abandono":
            self.senal_fin.emit(self.simbolo, "oponente desconectado")
    
    def actualizar_tablero(self, nuevo_tablero):
        for i in range(3):
            for j in range(3):
                nuevo = nuevo_tablero[i][j]
                if self.tablero[i][j] != nuevo:
                    self.tablero[i][j] = nuevo
                    self.senal_actualizar_tablero.emit(i, j, nuevo)

    def jugar(self, fil, col):
        if self.turno and not self.tablero[fil][col]:
            self.send_json({"accion": "jugada", "fila": fil, "columna": col})
            self.turno = False

    def send_json(self, data):
        try:
            data_bytes = json.dumps(data).encode('utf-8')
            data_length = len(data_bytes)
            self.socket.sendall(data_length.to_bytes(4, byteorder='big'))
            self.socket.sendall(data_bytes)
        except (ConnectionError, OSError):
            print("[send_json] Error enviando datos al cliente.")
    
    def setup_listo(self):
        self.send_json({"accion": "setup listo"})


if __name__ == '__main__':
    cliente = Cliente("localhost", 8080)
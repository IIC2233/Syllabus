import json
import socket

from PyQt6.QtCore import QObject, Qt, QTimer, pyqtSignal

import parametros as p
from protocolo import enviar, recibir


class EscucharQThread:
    # Completar
    pass


class Logica(QObject):
    # VentanaInicio
    senal_vi_avisar = pyqtSignal(str)
    senal_vi_habilitar = pyqtSignal(bool)
    senal_vi_cerrar = pyqtSignal()
    # VentanaJuego
    senal_vj_empezar = pyqtSignal(list, str)
    senal_vj_actualizar_estado = pyqtSignal(int, int, int, int)
    senal_vj_actualizar_marcador = pyqtSignal(int, int)
    senal_vj_actualizar_reloj = pyqtSignal(str)
    senal_vj_mensaje_temporal = pyqtSignal(str)
    senal_vj_terminar = pyqtSignal(str)
    # Solo para el bonus
    senal_vj_pausa = pyqtSignal(bool, str)
    senal_vj_aviso_revancha = pyqtSignal(str)
    senal_vj_mostrar_revancha = pyqtSignal()

    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread_escuchar = None

        self.en_ventana_juego = False
        self.y = (p.ALTO_CANCHA - p.ALTO_PALETA) // 2
        self.teclas = set()
        self.segundos_restantes = 0

        self.timer_movimiento = QTimer(self)
        self.timer_reloj = QTimer(self)
        self.timer_reloj.setTimerType(Qt.TimerType.PreciseTimer)
        # Completar: configuración de los timers

    def conectar_a_servidor(self) -> bool:
        try:
            self.socket_cliente.connect((self.host, self.port))
        except ConnectionError:
            print('No me pude conectar al servidor.')
            return False

        # Completar: inicia la escucha del servidor
        return True

    def enviar_comando(self, mensaje: dict) -> None:
        try:
            enviar(self.socket_cliente, json.dumps(mensaje).encode('utf-8'))
        except (ConnectionError, OSError):
            self.manejar_desconexion()

    def unirse(self, nombre: str) -> None:
        # Completar: valida el nombre y pide entrar a la sala
        pass

    def procesar_mensaje(self, mensaje: dict) -> None:
        # Completar: procesa un mensaje del servidor
        # Bonus: procesa pausa y revancha, y ofrece la revancha al terminar
        pass

    def empezar_partida(self, mensaje: dict) -> None:
        # Completar: prepara la partida y cambia de ventana
        # Bonus: reinicia el estado de la paleta
        pass

    def terminar_partida(self, texto: str) -> None:
        self.timer_movimiento.stop()
        self.timer_reloj.stop()
        self.senal_vj_terminar.emit(texto)

    def pedir_pausa(self) -> None:
        # Solo para el bonus
        self.enviar_comando({'comando': 'pausa'})

    def pedir_revancha(self) -> None:
        # Solo para el bonus
        self.enviar_comando({'comando': 'revancha'})

    def cambiar_pausa(self, activa: bool, nombre: str) -> None:
        # Bonus: pausa o reanuda la partida
        pass

    def manejar_desconexion(self) -> None:
        if self.en_ventana_juego:
            self.terminar_partida('Se perdió la conexión con el servidor')
        else:
            self.senal_vi_avisar.emit('Se perdió la conexión con el servidor')
            self.senal_vi_habilitar.emit(False)

    def actualizar_tecla(self, direccion: int, presionada: bool) -> None:
        if presionada:
            self.teclas.add(direccion)
        else:
            self.teclas.discard(direccion)

    def mover_paleta(self) -> None:
        # Completar: mueve la paleta según las teclas presionadas
        pass

    def avanzar_reloj(self) -> None:
        if self.segundos_restantes > 0:
            self.segundos_restantes -= 1
        # Completar: avisa a la ventana el tiempo restante

    def texto_reloj(self) -> str:
        minutos, segundos = divmod(self.segundos_restantes, 60)
        return f'{minutos:02d}:{segundos:02d}'

    def cerrar(self) -> None:
        self.timer_movimiento.stop()
        self.timer_reloj.stop()
        # shutdown despierta al recv que está bloqueado en el otro thread
        try:
            self.socket_cliente.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        self.socket_cliente.close()
        if self.thread_escuchar is not None:
            self.thread_escuchar.wait()

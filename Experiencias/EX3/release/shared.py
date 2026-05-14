# shared.py
# -----------------------------------------------------------------------------
# Código común a clientes y servidor.
#
# Contiene:
#   - Stats: snapshot del estado del servidor, se envía picklado.
#   - ServerState: estado persistente del servidor (se guarda con pickle).
#   - Protocolo de framing: send_message / recv_exactly / recv_message.
#
# -----------------------------------------------------------------------------

import socket
import threading
import time

# ── Clases serializables ─────────────────────────────────────────────────────


class Stats:
    """Snapshot del estado del servidor enviado a los clientes de monitoreo."""

    def __init__(self, total: int, rps: int) -> None:
        self.total = total
        self.rps = rps

    def __repr__(self) -> str:
        return f"Stats(total={self.total}, rps={self.rps})"


class ServerState:
    """
    Estado persistente del servidor de peticiones.

    Se guarda en disco con pickle cuando el servidor se apaga limpiamente
    y se intenta recargar al iniciar.
    """

    def __init__(self) -> None:
        self.total: int = 0  # contador acumulado de peticiones
        self.window: int = 0  # peticiones en la ventana actual de 0.1 s
        self.lock = threading.Lock()

    def increment(self) -> None:
        """
        Incremento NO atómico sobre una variable. Está escrito como
        lectura-modificación-escritura explícita con un `time.sleep(0)`
        intermedio para que la carrera sea VISIBLE en pocos segundos.

        En código real con `x += 1`, la carrera existe igual (el bytecode es
        LOAD–ADD–STORE y el GIL puede cambiar de thread entre cualquiera de
        esos pasos), pero pasa tan rápido que es difícil notarla. Acá el
        yield explícito exagera el problema.

        NO MODIFICAR ESTE CÓDIGO.
        """
        total = self.total
        time.sleep(0)
        total = total + 1
        time.sleep(0)
        self.total = total
        time.sleep(0)
        window = self.window
        time.sleep(0)
        window = window + 1
        time.sleep(0)
        self.window = window

    def get_total(self) -> int:
        """
        Retorna el total actual. No es atómico,
        pero no importa porque es solo para debug.
        """
        return self.total

    def get_window(self, time: float) -> int:
        """
        Retorna el window actual. No es atómico,
        pero no importa porque es solo para debug.
        """
        return int(self.window / time) if time > 0 else 0

    def reset_window(self) -> None:
        self.window = 0


# ── Protocolo de framing ─────────────────────────────────────────────────────
# Cada mensaje en la red se ve así en bytes:
#
#   ┌────────────────┬───────────────────────────┐
#   │  largo (4 B)   │     payload (largo bytes) │
#   │  big-endian    │                           │
#   └────────────────┴───────────────────────────┘
#
# Esto resuelve el problema de que TCP es un stream sin límites de mensaje.
# (Notebook 4 de Semana 11 — "Envío de muchos datos")


def send_message(sock: socket.socket, payload: bytes) -> None:
    """
    Envía un mensaje completo: 4 bytes de largo (big-endian) + payload.
    TODO PARTE 1.1: implementar.
    """
    raise NotImplementedError("send_message (PARTE 1.1)")


def recv_exactly(sock: socket.socket, n: int) -> bytes:
    """
    Lee EXACTAMENTE `n` bytes del socket. Si recv() devuelve menos de lo
    pedido (cosa que puede pasar perfectamente en TCP), debe seguir
    leyendo en chunks hasta acumular los n bytes.

    Lanza ConnectionError si el peer cierra antes de completar.

    TODO PARTE 1.2: implementar.
    """
    raise NotImplementedError("recv_exactly (PARTE 1.2)")


def recv_message(sock: socket.socket) -> bytes:
    """
    Lee un mensaje completo del protocolo (largo + payload).

    TODO PARTE 1.3: implementar.
    """
    raise NotImplementedError("recv_message (PARTE 1.3)")

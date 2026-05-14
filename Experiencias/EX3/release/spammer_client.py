# spammer_client.py
# -----------------------------------------------------------------------------
# Cliente TCP multi-threaded que bombardea el servidor con mensajes "PING".
# Solo usa `socket` y `threading` de la stdlib.
# -----------------------------------------------------------------------------

import socket
import threading
import time

from shared import recv_message, send_message

# ── Configuración ────────────────────────────────────────────────────────────
HOST = "localhost"
PORT = 24601
NUM_THREADS = 500
DELAY = 0


# ─────────────────────────────────────────────────────────────────────────────

# ── Estado compartido ────────────────────────────────────────────────────────
class State:
    state_lock = threading.Lock()

    def __init__(self) -> None:
        self.sent_count = 0
        self.error_count = 0

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
    def increment_sent(self) -> None:
        old = self.sent_count
        time.sleep(0)  # libera el GIL → otro thread puede leer `old`
        old = old + 1
        time.sleep(0)
        self.sent_count = old

    def increment_error(self) -> None:
        old = self.error_count
        time.sleep(0)  # libera el GIL → otro thread puede leer `old`
        old = old + 1
        time.sleep(0)
        self.error_count = old


def _increment(name: str, state: State) -> None:
    if name == "sent":
        state.increment_sent()
    elif name == "error":
        state.increment_error()
    else:
        raise ValueError(f"unknown counter: {name}")


def worker(thread_id: int, state: State, stop_event: threading.Event) -> None:
    """
    Abre su propia conexión TCP al servidor, envía pings framed y lee
    las respuestas hasta que stop_event se active.

    FIXME PARTE 2.2.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
    except ConnectionError as e:
        print(f"[Thread-{thread_id}] no se pudo conectar: {e}")
        return

    try:
        while not stop_event.is_set():
            try:
                send_message(sock, b"PING")
                recv_message(sock)  # b"OK <total>"
                _increment("sent", state)
            except ConnectionError as exc:
                _increment("error", state)
                print(f"[Thread-{thread_id}] error: {exc}")
                break

            if DELAY > 0:
                time.sleep(DELAY)
    finally:
        sock.close()


def stats_printer(state: State, stop_event: threading.Event) -> None:
    """Imprime una línea cada segundo con la tasa, total y errores."""
    prev_total = 0
    while not stop_event.is_set():
        time.sleep(1)

        current_total = state.sent_count
        current_errors = state.error_count

        rate = current_total - prev_total
        prev_total = current_total

        print(
            f"[stats] {rate:>5} req/s  |  "
            f"total sent: {current_total:>8}  |  "
            f"errors: {current_errors}"
        )


if __name__ == "__main__":
    print(f"[client] targeting tcp://{HOST}:{PORT}")
    print(f"[client] {NUM_THREADS} threads, {DELAY}s delay each")
    print("[client] press Ctrl+C to stop\n")

    threads: list[threading.Thread] = []
    state = State()
    stop_event = threading.Event()

    for i in range(NUM_THREADS):
        t = threading.Thread(
            target=worker,
            args=(i, state, stop_event),
            daemon=True,
            name=f"worker-{i}",
        )
        t.start()
        threads.append(t)

    printer = threading.Thread(
        target=stats_printer,
        args=(state, stop_event),
        daemon=True,
        name="stats-printer",
    )
    printer.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n[client] deteniendo…")
        stop_event.set()

    for t in threads:
        t.join(timeout=2)

    print(
        "[client] done. total sent: "
        f"{state.sent_count}, errors: {state.error_count}"
    )

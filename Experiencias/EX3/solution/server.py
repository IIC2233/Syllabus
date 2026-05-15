# server.py
# -----------------------------------------------------------------------------
# Servidor TCP que cuenta peticiones de clientes (puerto 24601).
#
# Protocolo (por cada cliente):
#   Cliente → Servidor: mensaje framed con payload `b"PING"`.
#   Servidor → Cliente: mensaje framed con payload `f"OK {total}".encode()`.
#
# Cada conexión es atendida en su propio thread. El estado compartido vive
# en una instancia de ServerState que se persiste a disco con pickle al
# apagar el proceso, y se intenta recargar al iniciar.
# -----------------------------------------------------------------------------

import pickle
import socket
import sys
import threading
from pathlib import Path
from time import sleep
from typing import Tuple

import monitor_server
from shared import ServerState, recv_message, send_message

PORT = 24601
STATE_FILE = Path(__file__).parent / "server_state.pkl"


# ── Persistencia ─────────────────────────────────────────────────────────────


def load_state() -> ServerState:
    """Intenta recuperar el ServerState anterior desde disco."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "rb") as f:
                state = pickle.load(f)
            print(f"[server] estado recuperado: total={state.total}")
            return state
        except Exception as e:
            print(f"[server] no se pudo cargar {STATE_FILE.name}: {e}")
    return ServerState()


def save_state(state: ServerState) -> None:
    """Persiste el ServerState con pickle."""
    with open(STATE_FILE, "wb") as f:
        pickle.dump(state, f)
    print(f"[server] estado guardado: total={state.total}")


# ── Manejo de un cliente ─────────────────────────────────────────────────────


def handle_client(
    conn: socket.socket, addr: Tuple[str, int], state: ServerState
) -> None:
    """
    Loop por cliente: recibe pings y responde con el total acumulado.
    Termina cuando el cliente cierra o hay error de conexión.
    """
    try:
        print(f"[server] cliente conectado: {addr}")
        while True:
            recv_message(conn)

            with state.lock:
                state.increment()

            response = f"OK {state.total}".encode("utf-8")
            send_message(conn, response)

    except ConnectionError:
        pass
    finally:
        conn.close()


# ── Accept loop ──────────────────────────────────────────────────────────────


def run_accept_loop(
    state: ServerState, host: str = "0.0.0.0", port: int = PORT
) -> None:
    """
    Crea el socket servidor, bind, listen y acepta conexiones para siempre.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    try:
        while True:
            conn, addr = sock.accept()
            threading.Thread(
                target=handle_client,
                args=(conn, addr, state),
                daemon=True,
            ).start()
    finally:
        sock.close()


# -- Muestra de estado compartido ---------------------------------------------


def _show_counter(state: ServerState) -> None:
    """Muestra el total cada segundo (para debug)."""
    while True:
        sleep(1)
        print(f"[counter] total={state.total}", end="\r")


# ── Punto de entrada ─────────────────────────────────────────────────────────


if __name__ == "__main__":
    state = load_state()

    # Monitor server (broadcaster a GUIs) corre en un thread daemon.
    threading.Thread(
        target=monitor_server.run,
        args=(state,),
        daemon=True,
        name="monitor-server",
    ).start()

    # Este thread muestra el contador cada segundo.
    threading.Thread(
        target=_show_counter,
        args=(state,),
        daemon=True,
        name="state-printer",
    ).start()

    try:
        run_accept_loop(state)
    except KeyboardInterrupt:
        print("\n[server] apagando…")
    finally:
        save_state(state)
        sys.exit(0)

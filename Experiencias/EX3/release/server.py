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
    # DESCOMENTAR DESPUES DE IMPLEMENTAR PARTE 3.1
    # if STATE_FILE.exists():
    #     try:
    #         with open(STATE_FILE, "rb") as f:
    #             state = pickle.load(f)
    #         print(f"[server] estado recuperado: total={state.total}")
    #         return state
    #     except Exception as e:
    #         print(f"[server] no se pudo cargar {STATE_FILE.name}: {e}")
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

    FIXME PARTE 2.2.
    """
    try:
        print(f"[server] cliente conectado: {addr}")
        while True:
            recv_message(conn)

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

    TODO PARTE 2.1: completar el accept loop.
    Pasos:
      1. Crear el socket
      2. Activar SO_REUSEADDR con setsockopt (para reiniciar sin esperar).
      3. bind y listen.
      4. En un loop infinito:
           Aceptar conexiones.
           Lanzar thread daemon para cada cliente, que ejecute handle_client(conn, addr, state).
      5. Terminar y cerrar el socket servidor.
    """
    # TODO PARTE 2.1
    raise NotImplementedError("accept loop (PARTE 2.1)")


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
        # DESCOMENTAR ANTES DE IMPLEMENTAR PARTE 3.1
        # save_state(state)
        sys.exit(0)

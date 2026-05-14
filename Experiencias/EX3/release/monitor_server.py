# monitor_server.py
# -----------------------------------------------------------------------------
# Servidor TCP en el puerto 3090 que cada 0.1 s envía un objeto Stats
# serializado con pickle a todos los clientes conectados (las GUIs).
#
# Protocolo en cada broadcast:
#   Servidor → Cliente: [4 bytes largo][estadística serializada]
#
# Corre en un thread daemon dentro del proceso de server.py, compartiendo el
# mismo ServerState.
# -----------------------------------------------------------------------------

import pickle
import socket
import threading
import time
from typing import List

from shared import ServerState, Stats, send_message

PORT = 3090
WINDOW_SECS = 0.1

_clients: list[socket.socket] = []
_clients_lock = threading.Lock()


def _handle_client(conn: socket.socket, addr: tuple[str, int]) -> None:
    """Registra el cliente y espera a que se desconecte."""
    print(f"[monitor] conectado: {addr}")
    with _clients_lock:
        _clients.append(conn)
    try:
        while conn.recv(256):
            pass
    except OSError:
        pass
    finally:
        with _clients_lock:
            if conn in _clients:
                _clients.remove(conn)
        conn.close()
        print(f"[monitor] desconectado: {addr}")


def _broadcast_loop(state: ServerState) -> None:
    """
    Cada WINDOW_SECS construye un Stats con el resumen, lo serializa con
    pickle y lo envía a cada cliente con el protocolo framed.

    TODO PARTE 4.1: implementar el broadcast loop.
    Pasos:
      1. Loop infinito
      2. Snapshot atómico
      3. Construir el objeto
      4. Serializar
      5. Recorrer clientes y enviar mensaje
         Si el enviar el mensaje lanza OSError, marca el conn como caído.
      6. Eliminar los caídos de clientes.
    """
    # TODO PARTE 4.1


def run(state: ServerState, host: str = "0.0.0.0", port: int = PORT) -> None:
    """Inicia el broadcaster y acepta conexiones entrantes."""
    # DESCOMENTAR DESPUES DE IMPLEMENTAR PARTE 4.1
    # threading.Thread(
    #     target=_broadcast_loop, args=(state,), daemon=True, name="broadcaster"
    # ).start()

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((host, port))
    srv.listen(16)
    print(f"[monitor] escuchando en {host}:{port}")

    while True:
        conn, addr = srv.accept()
        threading.Thread(
            target=_handle_client, args=(conn, addr), daemon=True
        ).start()

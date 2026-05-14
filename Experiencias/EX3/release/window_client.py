# window_client.py
# -----------------------------------------------------------------------------
# App PyQt6 que se conecta al monitor_server (puerto 3090) y muestra el RPS
# y el total de peticiones en tiempo real.
#
# Cada mensaje en la red es:
#   [4 bytes largo][estadística serializada]
#
# Arquitectura:
#   - QTimer dispara cada 100 ms en el hilo GUI.
#   - Lee bytes del socket en modo NO bloqueante, los acumula y extrae
#     mensajes framed completos.
#   - Deserializa con pickle.loads → instancia de Stats.
# -----------------------------------------------------------------------------

import pickle
import socket
import sys

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QProgressBar,
    QVBoxLayout,
    QWidget,
)

from shared import Stats  # necesario para que pickle pueda deserializar

HOST = "localhost"
PORT = 3090


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Monitor de peticiones")
        self.setStyleSheet("background:#111; color:#eee;")

        self.lbl_rps = QLabel("RPS: –")
        self.lbl_total = QLabel("Total: –")

        for lbl in (self.lbl_rps, self.lbl_total):
            lbl.setFont(QFont("monospace", 22, QFont.Weight.Bold))
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress = QProgressBar()
        self.progress.setRange(0, 1000)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.progress.setFixedHeight(24)
        self._set_bar_color(0)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setSpacing(8)
        layout.addWidget(self.lbl_rps)
        layout.addWidget(self.lbl_total)
        layout.addWidget(self.progress)
        self.setCentralWidget(container)
        self.resize(600, 380)

        try:
            self._sock = socket.create_connection((HOST, PORT))
            self._sock.setblocking(False)
            self._buf = bytearray()
            self._timer = QTimer(self)
            self._timer.setInterval(100)
            self._timer.timeout.connect(self._poll)  # type: ignore
            self._timer.start()
        except Exception as e:
            self.lbl_rps.setText("Sin conexión")
            self.lbl_total.setText(str(e))

    def _poll(self) -> None:
        """
        Llamado por QTimer cada 100 ms.

        TODO PARTE 5.1: implementar el polling no bloqueante con framing.
        El método se divide en dos pasos:

        PASO 1 — leer bytes disponibles sin bloquear:
          - Loop intentando self._sock.recv(4096):
              * Si lanza BlockingIOError → break (no hay más datos por ahora).
              * Si retorna b"" → el servidor cerró: detén el timer, muestra
                "Desconectado" y return.
              * Si retorna chunk → self._buf.extend(chunk) y vuelve a leer.
          - Captura excepciones generales para mostrar errores en la GUI.

        PASO 2 — extraer mensajes framed completos del buffer y renderizarlos:
          - Mientras haya al menos 4 bytes en el buffer:
              * Extraer los primeros 4 bytes → largo del payload.
              * Si el buffer tiene al menos (4 + largo) bytes → extraer payload
                y eliminar del buffer.
              * Deserializar payload.
              * Llamar a self._render(stats).
          Tienes que implementarlo tú.

        Nota: el buffer existe entre llamadas a _poll porque los mensajes
        pueden llegar partidos en varios chunks de TCP.
        """
        # Paso 1
        try:
            while True:
                chunk = self._sock.recv(4096)
                if not chunk:  # peer cerró la conexión
                    self._timer.stop()
                    self.lbl_rps.setText("Desconectado")
                    return
                self._buf.extend(chunk)
        except BlockingIOError:
            pass  # se acabaron los datos disponibles en este momento
        except Exception as e:
            self._timer.stop()
            self.lbl_rps.setText("Error")
            self.lbl_total.setText(str(e))
            return

        # Paso 2
        # TODO PARTE 5.1
        pass

    def _render(self, stats: Stats) -> None:
        self.lbl_rps.setText(f"RPS: {stats.rps}")
        self.lbl_total.setText(f"Total: {stats.total}")
        self.progress.setValue(min(stats.rps, 1000))
        self._set_bar_color(stats.rps)

    def _set_bar_color(self, rps: int) -> None:
        if rps < 500:
            color = "#00cc44"
        elif rps < 1000:
            color = "#ff8800"
        else:
            color = "#ff2222"
        style = f"{{ background-color: {color}; border-radius: 3px; }}"
        self.progress.setStyleSheet(
            f"QProgressBar::chunk {style}"
            "QProgressBar { border: 1px solid #444; "
            "border-radius: 3px; background: #222; }"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

"""Ejercicio A: código base para probar el uso de un Lock."""

from io import StringIO
from threading import Lock, Thread


class Escritor(Thread):
    var_lock = Lock()

    def __init__(self, archivo: StringIO) -> None:
        super().__init__()
        self.archivo = archivo

    def run(self) -> None:
        with self.var_lock:
            self.archivo.write(
                "Hola, soy un escritor escribiendo en un archivo de texto.\n"
            )


def main() -> None:
    archivo = StringIO()
    escritores = [Escritor(archivo), Escritor(archivo)]

    for escritor in escritores:
        escritor.start()
    for escritor in escritores:
        escritor.join()

    print(archivo.getvalue(), end="")


if __name__ == "__main__":
    main()

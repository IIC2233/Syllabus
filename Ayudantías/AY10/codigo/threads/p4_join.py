"""Ejercicio D: iniciar ambos threads antes de esperar con join."""

from threading import Thread
from time import sleep


def tarea(nombre: str, duracion: int) -> None:
    print(f"{nombre} comenzó")
    sleep(duracion)
    print(f"{nombre} terminó")


def main() -> None:
    t1 = Thread(target=tarea, args=("Tarea 1", 3))
    t2 = Thread(target=tarea, args=("Tarea 2", 3))

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    print("Programa terminado")


if __name__ == "__main__":
    main()

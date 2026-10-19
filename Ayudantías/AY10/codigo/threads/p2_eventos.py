"""Ejercicio B: código base para probar la comunicación mediante Event."""

from threading import Event, Thread
from time import sleep


def main() -> None:
    senal_a = Event()
    senal_b = Event()

    def thread_a() -> None:
        sleep(5)
        print("A-listo")
        senal_b.wait()
        sleep(1)
        print("A-continuo")
        senal_a.set()
        sleep(1)
        print("A-termino")

    def thread_b() -> None:
        sleep(2)
        print("B-listo")
        senal_b.set()
        sleep(1)
        print("B-continuo")
        senal_a.wait()
        sleep(5)
        print("B-termino")

    t_a = Thread(target=thread_a)
    t_b = Thread(target=thread_b)
    t_a.start()
    t_b.start()
    t_a.join()
    t_b.join()


if __name__ == "__main__":
    main()

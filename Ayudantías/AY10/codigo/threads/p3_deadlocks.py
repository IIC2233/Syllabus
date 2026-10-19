"""Ejercicio C: códigos base para probar esperas circulares."""

import sys
import threading
import time


def fragmento_i() -> None:
    lock_a = threading.Lock()
    lock_b = threading.Lock()

    def tarea_1() -> None:
        with lock_a:
            time.sleep(0.1)
            with lock_b:
                print("Tarea 1 lista")

    def tarea_2() -> None:
        with lock_b:
            time.sleep(0.1)
            with lock_a:
                print("Tarea 2 lista")

    t1 = threading.Thread(target=tarea_1)
    t2 = threading.Thread(target=tarea_2)
    t1.start()
    t2.start()


def fragmento_ii() -> None:
    evento_a = threading.Event()
    evento_b = threading.Event()

    def tarea_3() -> None:
        evento_b.wait()
        evento_a.set()
        print("Tarea 3 lista")

    def tarea_4() -> None:
        evento_a.wait()
        evento_b.set()
        print("Tarea 4 lista")

    t3 = threading.Thread(target=tarea_3)
    t4 = threading.Thread(target=tarea_4)
    t3.start()
    t4.start()


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"1", "2"}:
        raise SystemExit("Uso: python p3_deadlocks.py 1|2")
    if sys.argv[1] == "1":
        fragmento_i()
    else:
        fragmento_ii()

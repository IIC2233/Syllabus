import threading
import time


def mision(nombre: str, duracion: float) -> None:
    time.sleep(duracion)
    print(f"🌟 {nombre}: misión completada")


t_rapido = threading.Thread(target=mision, args=("Corto", 1), daemon=True)
t_lento  = threading.Thread(target=mision, args=("Largo", 5), daemon=True)

t_rapido.start()
t_lento.start()

t_rapido.join()
print("Programa principal terminado")

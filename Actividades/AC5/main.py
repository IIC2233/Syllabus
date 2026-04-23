from threading import Thread, Event
from clases import Carrera, Atleta, Equipo

if __name__ == "__main__":
    # Simular carrera
    carrera = Carrera()
    tiempos_por_equipo = carrera.simular_carrera()
    for eq, delta in tiempos_por_equipo.items():
        print(f"Equipo {eq}: {delta}s")
    
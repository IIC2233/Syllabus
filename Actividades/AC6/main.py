import time

from random import random, randint
from threading import Event, Lock, Thread


class Bandera:

    def __init__(self) -> None:
        self.nombre_dueño = None

    def actualizar_dueño(self, nombre_jugador: str) -> None:
        self.nombre_dueño = nombre_jugador


class Jugador(Thread):

    TIEMPO_ESPERA = 0.2       # Tiempo entre avances del jugador
    PORCENTAJE_MIN = 50       # Mínimo avance del jugador
    PORCENTAJE_MAX = 100      # Máximo avance del jugador
    PROBABILIDAD_ROBAR = 0.3  # Probabilidad de robar la bandera
    DISTANCIA_AVANZAR = 10    # Distancia a avanzar

    def __init__(
        self,
        nombre: str,
        bandera: Bandera,
        lock_bandera: Lock,
        senal_inicio: Event,
        senal_fin: Event,
        lock_carrera: Lock,
    ) -> None:
        super().__init__(name=nombre)
        self.daemon = False

        # Referencias al lock de la bandera y las señales propias de la carrera
        self.bandera = bandera
        self.senal_inicio = senal_inicio
        self.senal_fin = senal_fin
        self.lock_bandera = lock_bandera
        self.lock_carrera = lock_carrera

        # Otros atributos
        self.rivales = list()
        self.tiene_bandera = False
        self.puntaje = 0

        self._posicion = 0
        self._correr = True

    @property
    def posicion(self) -> float:
        return self._posicion

    @posicion.setter
    def posicion(self, nueva_posicion: int) -> None:
        # La posicion no puede aumentar más allá de la meta
        self._posicion = min(nueva_posicion, 100)

    @property
    def dist_avance(self) -> float:
        # El jugador reduce su velocidad si lleva la bandera
        if self.tiene_bandera:
            return Jugador.DISTANCIA_AVANZAR * 0.5
        return Jugador.DISTANCIA_AVANZAR

    def agregar_rival(self, rival: "Jugador") -> None:
        self.rivales.append(rival)

    def avanzar(self) -> None:
        # Se mueve una cantidad aleatoria dependiente de la distancia de avance
        cantidad_avanzar = randint(self.PORCENTAJE_MIN, self.PORCENTAJE_MAX) / 100
        self.posicion += self.dist_avance * cantidad_avanzar
        # Luego de avanzar imprime su posición
        print(f"{self.name}: Avancé a {self.posicion:.2f}")

    def perder_bandera(self) -> None:
        if self.tiene_bandera:
            self.tiene_bandera = False
            print(f"{self.name}: Perdí la bandera :(")

    def capturar_bandera(self) -> None:
        for rival in self.rivales:
            rival.perder_bandera()
        self.bandera.actualizar_dueño(self.name)
        self.tiene_bandera = True

    def intentar_capturar_bandera(self) -> None:
        # TODO: Parte I

        if self.tiene_bandera:
            print(f"{self.name}: ¡Capturé la bandera!")

    def intentar_robar_bandera(self) -> bool:
        # TODO: Parte I
        # PROBABILIDAD_ROBAR de robar la bandera
        if random() < self.PROBABILIDAD_ROBAR:
            print(f"{self.name}: ¡Robé la bandera!")
            return "COMPLETAR"
        else:
            return "COMPLETAR"

    def correr_primera_mitad(self):
        self.avanzar()
        time.sleep(Jugador.TIEMPO_ESPERA)

    def correr_segunda_mitad(self) -> bool | None:
        # TODO: Parte I
        pass

    def run(self) -> None:
        # 1. Espera el inicio de la carrera (COMPLETAR)
        # TODO: Parte I

        # 2. Durante los primeros 50 metros, solamente avanza (NO MODIFICAR)
        while self.posicion < 50:
            self.correr_primera_mitad()

        # 3. Cuando llega a la bandera, intenta capturarla (NO MODIFICAR)
        self.intentar_capturar_bandera()

        # 4. Ejecuto segunda mitad (NO MODIFICAR)
        while self._correr:
            self.correr_segunda_mitad()


class Carrera(Thread):
    def __init__(
        self,
        jugadores: list[Jugador],
        senal_inicio: Event,
        senal_fin: Event,
    ) -> None:
        super().__init__()
        # TODO: Parte II
        self.daemon = "COMPLETAR"

        # NO MODIFICAR el resto de los atributos

        # Referencias a las señales propias de la carrera
        self.senal_inicio = senal_inicio
        self.senal_fin = senal_fin

        # Guarda los jugadores y los asigna como rivales
        self.jugadores = jugadores

        for i, jugador_i in enumerate(self.jugadores):
            for j, jugador_j in enumerate(self.jugadores):
                if i != j:
                    jugador_i.agregar_rival(jugador_j)

    def run(self) -> None:
        # TODO: Parte II
        pass

    def entregar_ganador(self) -> None:
        # Código que encuentra e imprime el ganador.
        jugadores = self.jugadores
        for jugador in jugadores:
            if jugador.tiene_bandera:
                jugador.puntaje += 5
            if jugador.posicion >= 100:
                jugador.puntaje += 5
            print(f"{jugador.name}: {jugador.puntaje}, {jugador.posicion}")
        jugadores.sort(key=lambda j: j.puntaje, reverse=True)

        print(
            f"\n¡¡{jugadores[0].name} ha ganado la carrera con {jugadores[0].puntaje} puntos!!"
        )
        if jugadores[2].puntaje != jugadores[1].puntaje:
            print(
                f"{jugadores[1].name} quedó en segundo lugar con {jugadores[1].puntaje} puntos"
            )
            print(f"Más suerte para la próxima {jugadores[2].name}")
        else:
            msg = "{0} y {1} empataron con {2} puntos"
            print(
                msg.format(jugadores[1].name,
                           jugadores[2].name, jugadores[1].puntaje)
            )


if __name__ == "__main__":
    # IMPORTANT: NO MODIFICAR
    # Instancia una bandera y las señales
    bandera = Bandera()
    lock_bandera = Lock()
    lock_carrera = Lock()
    senal_inicio = Event()
    senal_fin = Event()

    # Instancia los jugadores y la carrera
    j1 = Jugador("Alice", bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera)
    j2 = Jugador("Asuna", bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera)
    j3 = Jugador("Shion", bandera, lock_bandera, senal_inicio, senal_fin, lock_carrera)
    carrera = Carrera([j1, j2, j3], senal_inicio, senal_fin)

    # Inicia la carrera y pausa el main thread hasta que termine
    carrera.start()
    carrera.join()

    # Obtiene e imprime al ganador
    carrera.entregar_ganador()

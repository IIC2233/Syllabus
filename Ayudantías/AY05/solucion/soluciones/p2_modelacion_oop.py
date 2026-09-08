from abc import ABC, abstractmethod


class Personaje(ABC):
    def __init__(self, nombre: str, nivel: int, puntos_de_vida: int):
        self.nombre = nombre
        self.nivel = nivel
        self.puntos_de_vida = puntos_de_vida

    @property
    def nivel(self) -> int:
        return self._nivel

    @nivel.setter
    def nivel(self, valor: int) -> None:
        if valor < 1:
            self._nivel = 1
        else:
            self._nivel = valor

    @abstractmethod
    def atacar(self) -> int:
        pass

    def recibir_dano(self, dano: int) -> None:
        pass


class Heroe(Personaje):
    def __init__(self, nombre: str, nivel: int, puntos_de_vida: int):
        super().__init__(nombre, nivel, puntos_de_vida)
        self.inventario = []

    def atacar(self) -> int:
        return self.nivel

    def usar_objeto(self, objeto) -> None:
        pass


class Enemigo(Personaje):
    def __init__(self, nombre: str, nivel: int, puntos_de_vida: int, dificultad: str):
        super().__init__(nombre, nivel, puntos_de_vida)
        self.dificultad = dificultad

    def atacar(self) -> int:
        if self.dificultad == "fácil":
            return 5
        return 15

    def huir(self) -> bool:
        pass


class Partida:
    def __init__(self, heroe: Heroe):
        self.heroe = heroe
        self.enemigos = []

    def iniciar_juego(self) -> None:
        pass

    def finalizar_juego(self) -> None:
        pass

from random import choice, uniform

import parametros as p


class Partida:
    """
    Reglas del juego. Esta clase no sabe nada de sockets ni de threads: quien
    la usa llama a avanzar() en cada tick y envía los mensajes que retorna.
    """

    def __init__(self, nombres: list) -> None:
        # nombres[0] juega a la izquierda y nombres[1] a la derecha
        self.nombres = nombres
        self.marcador = [0, 0]
        centro = (p.ALTO_CANCHA - p.ALTO_PALETA) // 2
        self.paletas = {"izquierda": centro, "derecha": centro}
        self.ticks_restantes = p.DURACION_PARTIDA * p.TICKS_POR_SEGUNDO
        self.en_pausa = False
        self.terminada = False
        self.sacar(choice((-1, 1)))

    def sacar(self, direccion: int) -> None:
        """Deja la pelota en el centro, esperando para salir."""
        self.x = (p.ANCHO_CANCHA - p.TAMAÑO_PELOTA) / 2
        self.y = (p.ALTO_CANCHA - p.TAMAÑO_PELOTA) / 2
        self.vx = p.VELOCIDAD_INICIAL * direccion
        self.vy = uniform(-3, 3)
        self.ticks_espera = int(p.ESPERA_SAQUE * p.TICKS_POR_SEGUNDO)

    def mover_paleta(self, lado: str, y: int) -> None:
        if not self.en_pausa and not self.terminada:
            self.paletas[lado] = max(0, min(int(y), p.ALTO_CANCHA - p.ALTO_PALETA))

    def avanzar(self) -> list:
        """Avanza un tick y retorna los mensajes que se deben enviar a ambos."""
        if self.en_pausa or self.terminada:
            return []

        self.ticks_restantes -= 1
        if self.ticks_espera > 0:
            self.ticks_espera -= 1
        else:
            self.mover_pelota()

        mensajes = []
        gol = self.revisar_gol()
        if gol is not None:
            mensajes.append(gol)
        if self.ticks_restantes <= 0 or max(self.marcador) >= p.GOLES_PARA_GANAR:
            self.terminada = True
            mensajes.append(self.mensaje_fin())
        else:
            mensajes.insert(0, self.mensaje_estado())
        return mensajes

    def mover_pelota(self) -> None:
        self.x += self.vx
        self.y += self.vy

        # Rebote en los bordes superior e inferior
        if self.y <= 0 or self.y >= p.ALTO_CANCHA - p.TAMAÑO_PELOTA:
            self.y = max(0, min(self.y, p.ALTO_CANCHA - p.TAMAÑO_PELOTA))
            self.vy *= -1

        # Rebote en las paletas
        if self.vx < 0 and self.choca_con("izquierda"):
            self.rebotar("izquierda")
        elif self.vx > 0 and self.choca_con("derecha"):
            self.rebotar("derecha")

    def x_paleta(self, lado: str) -> int:
        if lado == "izquierda":
            return p.MARGEN_PALETA
        return p.ANCHO_CANCHA - p.MARGEN_PALETA - p.ANCHO_PALETA

    def choca_con(self, lado: str) -> bool:
        x_paleta = self.x_paleta(lado)
        y_paleta = self.paletas[lado]
        return (
            self.x <= x_paleta + p.ANCHO_PALETA
            and self.x + p.TAMAÑO_PELOTA >= x_paleta
            and self.y <= y_paleta + p.ALTO_PALETA
            and self.y + p.TAMAÑO_PELOTA >= y_paleta
        )

    def rebotar(self, lado: str) -> None:
        # Mientras más lejos del centro de la paleta choca, más sale desviada
        centro_paleta = self.paletas[lado] + p.ALTO_PALETA / 2
        centro_pelota = self.y + p.TAMAÑO_PELOTA / 2
        self.vy = (centro_pelota - centro_paleta) / (p.ALTO_PALETA / 2) * 6

        velocidad = min(abs(self.vx) + p.AUMENTO_POR_REBOTE, p.VELOCIDAD_MAXIMA)
        self.vx = velocidad if lado == "izquierda" else -velocidad

    def revisar_gol(self) -> dict | None:
        if self.x + p.TAMAÑO_PELOTA < 0:
            indice_goleador = 1
        elif self.x > p.ANCHO_CANCHA:
            indice_goleador = 0
        else:
            return None

        self.marcador[indice_goleador] += 1
        # Saca hacia quien recibió el gol
        self.sacar(1 if indice_goleador == 1 else -1)
        return {
            "tipo": "gol",
            "goleador": self.nombres[indice_goleador],
            "marcador": self.marcador,
        }

    def mensaje_estado(self) -> dict:
        return {
            "tipo": "estado",
            "pelota": [int(self.x), int(self.y)],
            "paletas": self.paletas,
        }

    def mensaje_fin(self) -> dict:
        ganador = None
        if self.marcador[0] != self.marcador[1]:
            ganador = self.nombres[0 if self.marcador[0] > self.marcador[1] else 1]
        return {"tipo": "fin", "ganador": ganador, "marcador": self.marcador}

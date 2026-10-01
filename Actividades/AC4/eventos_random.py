"""
Funciones que determinan los tiempos y el azar de la simulación.

NO MODIFICAR.
"""
from random import random, uniform


def random_tiempo_picado() -> float:
    """Segundos que demora un cocinero picando los ingredientes."""
    return uniform(1.0, 2.0)


def random_tiempo_coccion() -> float:
    """Segundos que demora un plato en la estufa."""
    return uniform(2.0, 3.0)


def random_tiempo_emplatado() -> float:
    """Segundos que demora un cocinero emplatando."""
    return uniform(0.5, 1.0)


def random_se_quema_plato() -> bool:
    """True con 25% de probabilidad (el plato se quemó), False con 75%."""
    return random() < 0.25


def random_tiempo_extra() -> float:
    """Segundos que se pierden rehaciendo un plato quemado."""
    return uniform(1.0, 2.0)

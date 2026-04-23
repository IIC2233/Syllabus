import random

def random_se_cae_testigo() -> bool:
    """
    Retorna True con probabilidad 30%
    """
    return random.random() < 0.3

def random_tiempo_perdido() -> float:
    """
    Retorna un numero float entre 1 y 2
    """
    return random.uniform(1, 2)

def random_tiempo_corriendo() -> float:
    """
    Retorna un numero float entre 10 y 12
    """
    return random.uniform(10, 12)
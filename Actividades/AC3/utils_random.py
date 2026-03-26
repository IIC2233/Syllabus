from random import choice, random

def elegir_gen() -> int:
    """
    Elige 0 o 1 con 50% chances
    """
    return choice([0, 1])

def elegir_con_probabilidades(opciones: list[tuple[str, float]]) -> str:
    """
    Elige un float entre 0 y 1 de manera aleatoria
    """
    random_float = random()

    acumulado = 0
    for valor, prob in opciones:
        acumulado += prob
        if random_float <= acumulado:
            return valor
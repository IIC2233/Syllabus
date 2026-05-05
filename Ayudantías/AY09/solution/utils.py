AUTH_TOKEN = 'IIC2233'

"""NO MODFICAR: Función para comparar dos juegos según su rating y horas de juego"""
def comparar_juegos(juego_1: dict, juego_2: dict) -> dict:
    r1, r2 = juego_1['stats']['rating'], juego_2['stats']['rating']
    if r1 != r2:
        return juego_1 if r1 > r2 else juego_2
    h1, h2 = juego_1['stats']['horas_juego'], juego_2['stats']['horas_juego']
    return juego_1 if h1 >= h2 else juego_2


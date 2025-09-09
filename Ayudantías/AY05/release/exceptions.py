class CoordenadaOcupada(Exception):
    def __init__(self, x, y, elemento):
        super().__init__(f'⚠️ERROR: La coordenada {x}, {y} del mapa se encuentra ocupada por {elemento}')

class CoordenadaInvalida(Exception):
    def __init__(self, x, y):
        super().__init__(f'⚠️ERROR: La coordenada {x}, {y} se encuentra fuera del mapa')

class CofreBomba(Exception):
    def __init__(self):
        super().__init__("💣 Has muerto debido a que no manejaste la excepción de la explosión de un cofre bomba.")

class CofreVeneno(Exception):
    def __init__(self):
        super().__init__("☠️ Moriste por envenenamiento al abrir un cofre y no manejar la excepción.")

class CofreMaldicion(Exception):
    def __init__(self):
        super().__init__("🔮 Moriste al recibir una maldición de un cofre y no manejar la excepción.")

class NoEsCofre(Exception):
    def __init__(self, x, y, mapa):
        super().__init__(f'No hay un cofre en las coordenadas {x}, {y} del mapa {mapa.nombre}')
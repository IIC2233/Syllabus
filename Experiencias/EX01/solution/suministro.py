from random import choice


class Suministro:
    def __init__(self, nombre, valor_de_satisfaccion):
        self.nombre = nombre
        self.valor_de_satisfaccion = valor_de_satisfaccion * choice([-1, 1])

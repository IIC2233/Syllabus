class Item:
    # Item necesita un nombre, un precio y los puntos que obtiene el usuario al comprarlo
    def __init__(self, nombre: str, precio: int, puntos: int):
        self.nombre = nombre
        self.puntos = puntos
        self.precio = precio

class Usuario:
    # Usuario tiene o no subscripción
    # Además, por defecto tiene una canasta vacía y 0 puntos adquiridos
    def __init__(self, esta_subscrito: bool):
        self.suscripcion = esta_subscrito
        self.canasta = []
        self.puntos = 0

    # Definimos un método para agregar un objeto Item a la canasta
    def agregar_item(self, item: Item):
        # Si el usuario está subscrito, recibe el doble de puntos
        if self.suscripcion:
            item.puntos *= 2
        # Luego, agregamos el item a la canasta
        self.canasta.append(item)

    # Definimos un método para comprar todos los Items de la canasta
    # y agregar los puntos ganados por la compras
    def comprar(self):
        # Por cada item, aumentamos la cantidad de puntos que tenemos
        for item in self.canasta:
            # Aquí hacemos una interacción entre una instancia Usuario con la instancia Item
            self.puntos += item.puntos
        # Limpiamos nuestra canasta
        self.canasta = []

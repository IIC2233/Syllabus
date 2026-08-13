class Producto:
    def __init__(self, nombre: str, precio: int, stock: int) -> None:
        pass

    def descripcion(self) -> str:
        return f'{self.nombre}: ${self.precio} (stock: {self._stock})'

    def vender(self) -> None:
        pass

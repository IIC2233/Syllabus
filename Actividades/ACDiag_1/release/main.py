import os


def cargar_productos(ruta: str) -> list:
    productos = []
    return productos


def simular_ventas(productos: list) -> None:
    for producto in productos:
        producto.vender()


if __name__ == '__main__':
    ruta = os.path.join('data', 'menu.txt')
    productos = cargar_productos(ruta)
    print('=== DCCafeteria ===')
    for producto in productos:
        print(producto.descripcion())
    print(f'Productos registrados: {Producto.total_productos}')
    simular_ventas(productos)
    simular_ventas(productos)

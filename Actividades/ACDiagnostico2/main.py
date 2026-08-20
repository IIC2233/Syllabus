import os
from collections import defaultdict

class Inventario:
    def __init__(self, path):
        self.precios = {}
        self.disponibles = {}
        with open(path, "r") as file:
            for line in file.readlines():
                values = line.strip().split(",")
                self.precios[values[0]] = int(values[1])
                self.disponibles[values[0]] = int(values[2])

class Cliente:
    def __init__(self, rut):
        self.rut = rut
        self.cantidad_productos = defaultdict(int)
        self.stack_productos = []
        self.costo_carro = 0

    def print_info(self, info):
        print(f"[{self.rut}] {info}")

    def agregar_al_carro(self, product_name, inventario: Inventario):
        if not product_name in inventario.disponibles:
            self.print_info(f"No existe producto {product_name}")
        elif inventario.disponibles[product_name] == 0:
            self.print_info(f"No quedan unidades de {product_name}")
        else:
            self.cantidad_productos[product_name] += 1
            inventario.disponibles[product_name] -= 1
            self.costo_carro += inventario.precios[product_name]
            self.stack_productos.append(product_name)
            self.print_info(f"{product_name} agregado al carro")

    def sacar_del_carro(self, inventario: Inventario):
        if len(self.stack_productos) == 0:
            self.print_info("No quedan productos en el carro para sacar")
        else:
            product_name = self.stack_productos.pop()
            self.cantidad_productos[product_name] -= 1
            self.costo_carro -= inventario.precios[product_name]
            inventario.disponibles[product_name] += 1
            self.print_info(f"{product_name} sacado del carro")

    def cerrar_sesion(self, inventario: Inventario):
        self.print_info(f"Sesión cerrada. Productos liberados {self.stack_productos}")
        for product_name in self.stack_productos:
            inventario.disponibles[product_name] += 1
        self.stack_productos = []
        self.costo_carro = 0
        self.cantidad_productos = defaultdict(int)

    def pagar(self):
        if len(self.stack_productos) == 0:
            self.print_info(f"No hay nada que pagar")
        else:
            self.print_info(f"Pagado carro. Total de compra: {self.costo_carro}")
            self.stack_productos = []
            self.costo_carro = 0
            self.cantidad_productos = defaultdict(int)

if __name__ == "__main__":
    carpeta = input("Ingrese nombre de carpeta: ")
    productos_path = os.path.join(carpeta, "productos.txt")
    inventario = Inventario(productos_path)
    acciones_path = os.path.join(carpeta, "acciones.txt")

    clientes = {}
    with open(acciones_path, "r") as acciones_file:
        for accion_line in acciones_file.readlines():
            values = accion_line.strip().split(",")
            
            accion = values[0]
            rut = values[1]
            if not rut in clientes:
                clientes[rut] = Cliente(rut)
            cliente = clientes[rut]

            if accion == "Agregar al carro":
                product_name = values[2]
                cliente.agregar_al_carro(product_name, inventario)
            elif accion == "Sacar del carro":
                cliente.sacar_del_carro(inventario)
            elif accion == "Cerrar sesion":
                cliente.cerrar_sesion(inventario)
            elif accion == "Pagar":
                cliente.pagar()
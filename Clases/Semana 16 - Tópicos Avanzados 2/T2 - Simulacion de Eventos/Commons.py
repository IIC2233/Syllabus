from collections import deque

import json
import numpy as np


def ProbabilidadUniforme(min, max) -> float:
    return round(np.random.rand(), 1) * (max - min) + min


class Persona:
    pid = 0

    def __init__(self) -> None:
        self.pid = Persona.pid
        Persona.pid += 1

        self.dinero = ProbabilidadUniforme(2000, 6000)
        self.almuerzo_comprado = False

        self.locales_revisados = set()

    def __repr__(self) -> str:
        '''
        Retorna el id de la persona.
        '''
        return f'({self.pid:0>3d})'

    def escoger_puesto(self, puestos: set) -> str:
        '''
        Escoge un puesto dentro de los puestos de comida que no ha revisado.
        En caso de ya haber revisado todos los puestos, retorna un str vacío.
        '''
        puestos = puestos.difference(self.locales_revisados)
        if not puestos:
            print(f'[{" " * 21}]	 El cliente {self} ya revisó todos los '
                  'puestos y no encontró almuerzo. Volverá con hambre a su casa.')
            return ''
        local = np.random.choice(list(puestos))
        self.locales_revisados.add(local)
        return local

    def escoger_producto(self, productos_precio) -> str:
        '''
        A partir de un lista de tuplas producto-precio,
        identifica los productos que la persona puede comprar a partir
        de su dinero. Si hay más de un producto posible, elige uno al azar.
        Si no hay productos posibles, retorna un sting vacío. 
        '''
        productos_posibles = [producto for producto, precio in productos_precio
                              if precio <= self.dinero]
        if not productos_posibles:
            return ''
        return np.random.choice(productos_posibles)

    def comprar_producto(self, precio) -> bool:
        '''
        Si tiene el dinero suficiente, compra el producto, marca que compró
        el almuerzo y retorna True. Caso contrario, retorna False.
        '''
        if precio <= self.dinero:
            self.dinero -= precio
            self.almuerzo_comprado = True
            return True
        return False


class PuestoComida:
    def __init__(self, nombre: str, productos: dict) -> None:
        self.nombre = nombre
        self.ganancias = 0
        self.productos_vendidos = 0
        self.cola_clientes = deque()

        self.productos_precios = {p['nombre']: p['precio'] for p in productos}
        self.productos_stock = {p['nombre']: p['stock'] for p in productos}

    def __str__(self) -> str:
        '''
        Retorna el nombre del puesto de comida.
        '''
        return f'[{self.nombre:^21}]'

    def __repr__(self) -> str:
        '''
        Retorna un string con el nombre del Puesto de Comida,
        la cantidad total de productos en stock y las ganancias del local.
        '''
        stock_total = sum(self.productos_stock.values())
        return f'PuestoComida({self.nombre}, {stock_total}, {self.ganancias})'

    def recibir_cliente(self, cliente: Persona) -> None:
        '''
        Agrega una cliente al final de la cola de cliente.
        '''
        self.cola_clientes.append(cliente)

        print(f'{self}\t El cliente {cliente} se a unido a la cola. '
              f'Hay {len(self.cola_clientes)} clientes esperando.')

    def atender_cliente(self) -> tuple[bool, Persona]:
        '''
        Saca a la primera cliente de la cola, escoge el producto que va a comprar,
        se realiza la compra y se entrega el producto.
        Si se logra completar la compra, se retorna True y el cliente;
        en caso contrario, se retorna False y el cliente. 
        '''
        cliente = self.cola_clientes.popleft()
        print(f'{self}\t El cliente {cliente} empezó a ser atendido.')

        producto = cliente.escoger_producto(self.productos_precios.items())
        if not producto:
            print(f'{self}\t El cliente {cliente} no encontró un producto que '
                  'pudiese comprar. Se retira decepcionado.')
            return False, cliente

        if not self.productos_stock[producto]:
            print(f'{self}\t El cliente {cliente} quería comprar un {producto}, '
                  'pero no está disponible. Se retira decepcionado.')
            return False, cliente

        compra = cliente.comprar_producto(self.productos_precios[producto])
        if not compra:
            print(f'{self}\t El cliente {cliente} quería comprar un "{producto}", '
                  'pero no tenia dinero suficiente. Se retira decepcionado.')
            return False, cliente

        self.vender_producto(producto)
        print(f'{self}\t El cliente {cliente} compró un "{producto}". '
              f'El local ganó ${self.productos_precios[producto]}')
        return True, cliente

    def vender_producto(self, nombre_producto: str) -> None:
        '''
        Resta el producto del stock, aumenta las ganancias.
        '''
        self.productos_stock[nombre_producto] -= 1
        self.ganancias += self.productos_precios[nombre_producto]
        self.productos_vendidos += 1


def cargar_puestos_comida(path_archivo: str) -> list:
    with open(path_archivo, 'r', encoding='utf-8') as file:
        data = json.load(file)

    puestos = [PuestoComida(**p) for p in data]
    return puestos

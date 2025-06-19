from Commons import (Persona as CommonPersona, cargar_puestos_comida)

import numpy as np
import pandas as pd


class ProbabilidadWeibull:
    def __init__(self, shape: float, delta: float) -> None:
        self.shape = shape
        self.delta = delta

    def weibull(self, x: float) -> float:
        '''
        Calcula la probabilidad correspondiente a un valor en el eje X.
        '''
        return (self.shape / self.delta) * (x / self.delta) ** (self.shape - 1) * \
                np.exp(-(x / self.delta) ** self.shape)

    def calcular_probabilidad(self, tick: float) -> float:
        '''
        Normaliza el valor asociado al tick y calcula su probabilidad.
        '''
        tick_normalizado = tick / (60 * 5)
        return self.weibull(tick_normalizado) / 300


class Persona(CommonPersona):
    prob_ir_comprar = ProbabilidadWeibull(15, 1).calcular_probabilidad

    def ir_a_comprar(self, t: float) -> bool:
        '''
        Si no ha comprado almuerzo, evalúa si va a comprar almuerzo.
        Retorna un booleano indicando si fue a comprar almuerzo o no.
        '''
        if self.almuerzo_comprado:
            return False

        if np.random.random() < Persona.prob_ir_comprar(t):
            return True
        return False


class Simulación:
    def __init__(self, n: int = 100) -> None:
        self.tick = 0
        self.delta_tick = 1

        self.puestos_comida = {p.nombre: p for p in
                               cargar_puestos_comida('PuestoComida.json')}
        self.personas_pendientes = {Persona() for _ in range(n)}
        self.personas_nuevo_intento = set()
        self.personas_listas = set()
        self.personas_fallos = set()

        self.stats = {}

    @property
    def hora(self) -> str:
        '''
        Retorna el tick actual en su formato de hora,
        donde el tick 0 corresponde a las 8:30 am.
        '''
        h = (self.tick + 30) // 60 + 8
        m = (self.tick + 30) % 60
        return f'{h:0>2d}:{m:0>2d}'

    def avanzar_tick(self) -> None:
        '''
        Primeramente, imprime la hora. Después, identifica las personas
        "dispuestas" a comprar un almuerzo y las agrega a la cola de
        cada puesto de comida. Posteriormente, cada puesto atiende una 
        cierta cantidad de clientes en su cola (en este caso 4).
        '''
        print(f'\n{self.hora:-^100}')

        compradores = set(filter(lambda p: p.ir_a_comprar(self.tick),
                                 self.personas_pendientes))
        compradores.update(self.personas_nuevo_intento)
        self.personas_pendientes = self.personas_pendientes.difference(compradores)
        self.personas_nuevo_intento = set()

        for persona in compradores:
            puesto = persona.escoger_puesto(set(self.puestos_comida.keys()))
            if not puesto:
                self.personas_fallos.add(persona)
            else:
                self.puestos_comida[puesto].recibir_cliente(persona)

        for _, puesto in self.puestos_comida.items():
            for _ in range(4):
                if puesto.cola_clientes:
                    venta_realizada, persona = puesto.atender_cliente()
                    if venta_realizada:
                        self.personas_listas.add(persona)
                    else:
                        self.personas_nuevo_intento.add(persona)
                else:
                    break

        self.tick += self.delta_tick

    def start(self, cantidad_ticks) -> None:
        print(f'{"INICIO SIMULACIÓN":^100}\n')

        for _ in range(cantidad_ticks):
            self.avanzar_tick()

        print(f'\n{"FIN SIMULACIÓN":^100}\n')
        self.calcular_stats()

    def calcular_stats(self) -> None:
        self.stats['atención_clientes'] = self.calcular_atención_clientes()
        self.stats['ventas_locales'] = self.calcular_ventas_locales()

    def calcular_atención_clientes(self) -> pd.DataFrame:
        '''
        Calcula cuantas personas lograron comprar su almuerzo,
        y en caso de que no pudieran, los subdivide según la razón.
        Genera un DataFrame con toda la información.  
        '''
        df = pd.DataFrame(columns=['Caso', 'Cantidad'])

        df.loc[len(df.index)] = ['Compraron almuerzo',
                                 len(self.personas_listas)]
        df.loc[len(df.index)] = ['No fueron a comprar almuerzo',
                                 len(self.personas_pendientes)]
        df.loc[len(df.index)] = ['No encontraron almuerzo',
                                 len(self.personas_fallos)]
        df.loc[len(df.index)] = ['Les faltó tiempo',
                                 len(self.personas_nuevo_intento)]
        return df

    def calcular_ventas_locales(self) -> pd.DataFrame:
        '''
        Calcula las ganancias y la cantidad de ventas de cada Puesto de Comida.
        Genera un DataFrame con toda la información.
        '''
        df = pd.DataFrame(columns=['Puesto', 'Ganancias', 'Cant. Ventas'])

        for puesto in self.puestos_comida.values():
            df.loc[len(df.index)] = [puesto.nombre,
                                     puesto.ganancias,
                                     puesto.productos_vendidos]

        return df


if __name__ == '__main__':
    simulación = Simulación(600)
    simulación.start(601)

from Commons import (Persona, cargar_puestos_comida)

import numpy as np
import pandas as pd


class Evento:
    def __init__(self, tick: int, evento: str, **kwargs) -> None:
        self.tick = tick
        self.evento = evento
        self.argumentos = kwargs
        self.argumentos['tick'] = tick

    @property
    def hora(self) -> str:
        '''
        Retorna el tick actual en su formato de hora,
        donde el tick 0 corresponde a las 8:30 am.
        '''
        h = int((self.tick + 30) // 60 + 8)
        m = int((self.tick + 30) % 60)
        s = int((self.tick - int(self.tick)) * 60)
        return f'{h:0>2d}:{m:0>2d}:{s:0>2d}'

    def __repr__(self) -> str:
        return f'Evento({self.hora}, {self.evento}, {self.argumentos})'


class Simulación:
    def __init__(self, n: int = 100) -> None:
        self.eventos = [
            Evento(0, 'distribuir_clientes', shape=15),
        ]

        self.puestos_comida = {p.nombre: p for p in
                               cargar_puestos_comida('PuestoComida.json')}
        self.personas_pendientes = {Persona() for _ in range(n)}
        self.personas_nuevo_intento = set()
        self.personas_listas = set()
        self.personas_fallos = set()

        self.listado_eventos = {
            'distribuir_clientes': self.distribuir_clientes,
            'agregar_a_cola_puesto': self.agregar_a_cola_puesto,
            'atender_cliente': self.atender_cliente,
        }

        self.stats = {}

    def procesar_evento(self, evento: Evento) -> None:
        '''
        Recibe un evento y llama el método que se encarga de
        manejar dicho evento.
        '''
        if evento.evento not in self.listado_eventos:
            return
        self.listado_eventos[evento.evento](**evento.argumentos)

    def distribuir_clientes(self, shape: float, **_) -> None:
        '''
        Distribuye las personas a lo largo del tiempo (ticks)
        para que vayan a comprar almuerzo e ingresen a la cola de un puesto.  
        '''
        distribución = np.random.weibull(shape, len(self.personas_pendientes))
        ticks = distribución * 300.0

        for tick, persona in zip(ticks, self.personas_pendientes):
            evento = Evento(tick, 'agregar_a_cola_puesto', persona=persona)
            self.eventos.append(evento)

        print()

    def agregar_a_cola_puesto(self, tick: int, persona: Persona) -> None:
        '''
        Agrega una persona a un puesto. Si el puesto tenia la cola vacía,
        entonces agrega un evento para que el puesto empiece a atender
        a sus clientes. 
        '''
        self.personas_pendientes = self.personas_pendientes.difference(set((persona,)))

        puesto = persona.escoger_puesto(set(self.puestos_comida.keys()))
        if not puesto:
            self.personas_fallos.add(persona)
        else:
            if not self.puestos_comida[puesto].cola_clientes:
                evento = Evento(tick + 0.25, 'atender_cliente', puesto=puesto)
                self.eventos.append(evento)
            self.puestos_comida[puesto].recibir_cliente(persona)

    def atender_cliente(self, puesto: str, tick: float, **_) -> None:
        venta_realizada, persona = self.puestos_comida[puesto].atender_cliente()
        if venta_realizada:
            self.personas_listas.add(persona)
        else:
            evento = Evento(tick + 0.01, 'agregar_a_cola_puesto', persona=persona)
            self.eventos.append(evento)

        if len(self.puestos_comida[puesto].cola_clientes):
            evento = Evento(tick + 0.25, 'atender_cliente', puesto=puesto)
            self.eventos.append(evento)

    def start(self) -> None:
        print(f'{"INICIO SIMULACIÓN":^100}\n')
        hora_ultimo_evento = '08:30:00'

        while self.eventos:
            self.eventos.sort(key=lambda e: e.tick, reverse=True)
            evento = self.eventos.pop()
            if hora_ultimo_evento != evento.hora:
                print(f'\n{evento.hora:-^100}')
            self.procesar_evento(evento)
            hora_ultimo_evento = evento.hora

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
    simulación.start()

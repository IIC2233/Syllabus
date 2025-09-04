from __future__ import annotations
from typing import Self

import copy


class NodoCliente:
    identificador = 0

    def __init__(self, preferencial: bool) -> None:
        self.identificador = NodoCliente.identificador
        NodoCliente.identificador += 1

        self.preferencial = preferencial
        self.siguiente = None

    def agregar_nodo(self, nuevo_nodo: NodoCliente) -> None:
        '''
        TODO: Parte I
        '''
        pass

    def __str__(self) -> str:
        '''
        TODO: Parte I
        '''
        pass

    def __len__(self) -> int:
        '''
        TODO: Parte I
        '''
        pass


class SistemaColas:
    def __init__(self) -> None:
        self.cola_preferencial = None
        self.cola_normal = None

    def __str__(self) -> str:
        return f'Preferencial: {self.cola_preferencial}\n' \
               f'Normal:       {self.cola_normal}'

    def agregar_persona(self, preferencial: bool) -> None:
        '''
        TODO: Parte II
        '''
        pass

    def __len__(self) -> int:
        '''
        TODO: Parte II
        '''
        pass

    def __iter__(self) -> IteradorSistemaColas:
        '''
        TODO: Parte III
        '''
        pass


class IteradorSistemaColas:
    def __init__(self, cola_preferencial, cola_normal) -> None:
        self.cola_preferencial = cola_preferencial
        self.cola_normal = cola_normal
        self.contador_preferencial = 0

    def __iter__(self) -> Self:
        '''
        TODO: Parte III
        '''
        pass

    def __next__(self) -> NodoCliente:
        '''
        TODO: Parte III
        '''
        pass



if __name__ == '__main__':
    print('----- NODO CLIENTE -----')

    persona_1 = NodoCliente(True)
    persona_2 = NodoCliente(True)
    persona_3 = NodoCliente(True)
    persona_4 = NodoCliente(True)

    persona_1.agregar_nodo(persona_2)
    persona_1.agregar_nodo(persona_3)
    persona_1.agregar_nodo(persona_4)

    print('Cola: ', persona_1)
    print('Largo:', len(persona_1))
    print()


    print('----- SISTEMA COLAS -----')

    sistema_colas = SistemaColas()
    sistema_colas.cola_preferencial = persona_1

    sistema_colas.agregar_persona(True)
    sistema_colas.agregar_persona(False)
    sistema_colas.agregar_persona(False)

    print(sistema_colas)
    print()


    print('----- ITERACIÓN SISTEMA -----')

    estados = {True: 'Preferencial', False: 'Normal'}

    for cliente in sistema_colas:
        print(f'> Avanza Cliente({cliente.identificador}, {estados[cliente.preferencial]})')
    print('< Se acabó la cola')

from __future__ import annotations
from copy import deepcopy
from utils import NodoUrgencia, Urgencia


class ListaUrgencias:
    def __init__(self) -> None:
        self.cabeza = None

    def __repr__(self) -> str:
        return f'{self.cabeza}'

    def __iter__(self) -> IteradorListarUrgencias:
        '''
        TODO: Parte II
        '''
        pass

    def agregar_urgencia(self, urgencia: Urgencia) -> None:
        '''
        TODO: Parte I
        '''
        pass

    def quitar_urgencia(self, paciente: str) -> Urgencia:
        '''
        TODO: Parte I
        '''
        pass


class IteradorListarUrgencias:
    def __init__(self, lista_urgencias: ListaUrgencias) -> None:
        self.lista_urgencias = lista_urgencias

    def __iter__(self) -> IteradorListarUrgencias:
        '''
        TODO: Parte II
        '''
        pass

    def __next__(self) -> Urgencia:
        '''
        TODO: Parte II
        '''
        pass



if __name__ == '__main__':
    # PARTE I: agregar urgencia

    # Lista vacía
    lista_urgencias = ListaUrgencias()
    print(lista_urgencias)

    # Agregar elemento a la lista vacía
    urg_agr_1 = Urgencia('Paciente1', 17.2)
    lista_urgencias.agregar_urgencia(urg_agr_1)
    print(lista_urgencias)

    # Agregar elemento a una lista con más elementos
    n2 = NodoUrgencia(Urgencia('Paciente2', 13.0))
    n3 = NodoUrgencia(Urgencia('Paciente3', 7.0))
    n4 = NodoUrgencia(Urgencia('Paciente4', 3.2))
    n5 = NodoUrgencia(Urgencia('Paciente5', 1.2))

    lista_urgencias.cabeza.siguiente = n2
    n2.siguiente = n3
    n3.siguiente = n4
    n4.siguiente = n5

    urg_agr_6 = Urgencia('Paciente6', 5.0)
    lista_urgencias.agregar_urgencia(urg_agr_6)

    print(lista_urgencias)

    # -----------------------------------------
    # PARTE I: agregar quitar

    # Lista de la parte anterior
    print(lista_urgencias)

    # Quitar paciente de la lista
    urg_quit_1 = lista_urgencias.quitar_urgencia('Paciente6')
    print(urg_quit_1)
    print(lista_urgencias)

    # Quitar paciente que no esta en la lista
    try:
        urg_quit_2 = lista_urgencias.quitar_urgencia('Paciente7')
        print(urg_quit_2)
        print(lista_urgencias)
    except ValueError as error:
        print(error)

    # -----------------------------------------
    # PARTE II: Iterable e iterador

    # Lista desordenada
    lista_urgencias = ListaUrgencias()

    n1 = NodoUrgencia(Urgencia('Paciente1', 17.2))
    n2 = NodoUrgencia(Urgencia('Paciente3', 7.0))
    n3 = NodoUrgencia(Urgencia('Paciente5', 1.2))
    n4 = NodoUrgencia(Urgencia('Paciente4', 3.2))
    n5 = NodoUrgencia(Urgencia('Paciente2', 13.0))

    n1.siguiente = n2
    n2.siguiente = n3
    n3.siguiente = n4
    n4.siguiente = n5

    lista_urgencias.cabeza = n1
    print(lista_urgencias)

    for urg in lista_urgencias:
        print(urg)

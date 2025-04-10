from __future__ import annotations
from typing import Callable, Any

import functools


def revisas_tipo_input(operacion: str) -> Callable:
    '''
    Decorador que revisa que el argumento recibido por la función sea
    del tipo que el self.
    '''
    def decorador(func) -> Callable:
        @functools.wraps(func)
        def wrapper(ref_self, otro_valor) -> Any:
            instancia_esperada = type(ref_self)
            if not isinstance(otro_valor, instancia_esperada):
                texto = f"'{operacion}' not supported between instances of " \
                        f"'{instancia_esperada.__name__}' and " \
                        f"'{type(otro_valor).__name__}'"
                raise TypeError(texto)

            return func(ref_self, otro_valor)
        return wrapper
    return decorador


class Urgencia:
    def __init__(self, paciente: str, nivel_urgencia: float):
        self.paciente = paciente
        self.nivel_urgencia = nivel_urgencia

    def __repr__(self):
        return f'U({self.nivel_urgencia}, {self.paciente})'

    @revisas_tipo_input('==')
    def __eq__(self, otra_urgencia: Urgencia) -> bool:
        '''
        Override del método encargado de la operación ==.
        Permite comparar dos instancias de Urgencias, 
        si recibe otro tipo de instancia, levanta una excepción 
        '''
        return self.nivel_urgencia == otra_urgencia.nivel_urgencia

    @revisas_tipo_input('>')
    def __gt__(self, otra_urgencia: Urgencia) -> bool:
        '''
        Override del método encargado de la operación >.
        Permite comparar dos instancias de Urgencias. 
        si recibe otro tipo de instancia, levanta una excepción 
        '''
        return self.nivel_urgencia > otra_urgencia.nivel_urgencia

    @revisas_tipo_input('>=')
    def __ge__(self, otra_urgencia: Urgencia) -> bool:
        '''
        Override del método encargado de la operación >=.
        Permite comparar dos instancias de Urgencias. 
        si recibe otro tipo de instancia, levanta una excepción 
        '''
        return self.nivel_urgencia >= otra_urgencia.nivel_urgencia

    @revisas_tipo_input('<')
    def __lt__(self, otra_urgencia: Urgencia) -> bool:
        '''
        Override del método encargado de la operación <.
        Permite comparar dos instancias de Urgencias.
        si recibe otro tipo de instancia, levanta una excepción 
        '''
        return self.nivel_urgencia < otra_urgencia.nivel_urgencia

    @revisas_tipo_input('<=')
    def __le__(self, otra_urgencia: Urgencia) -> bool:
        '''
        Override del método encargado de la operación <=.
        Permite comparar dos instancias de Urgencias. 
        si recibe otro tipo de instancia, levanta una excepción 
        '''
        return self.nivel_urgencia <= otra_urgencia.nivel_urgencia


class NodoUrgencia:
    def __init__(self, urgencia: Urgencia) -> None:
        self.urgencia = urgencia
        self.siguiente = None

    def __repr__(self) -> str:
        return f'{self.urgencia} -> {self.siguiente}'


if __name__ == '__main__':
    urg1 = Urgencia('Paciente 1', 7.0)
    urg2 = Urgencia('Paciente 2', 4.5)

    if urg1 > urg2:
        print(urg1.paciente, 'es más urgente')
    else:
        print(urg2.paciente, 'es más urgente')

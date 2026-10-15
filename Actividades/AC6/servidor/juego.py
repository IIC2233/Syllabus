import random

class JuegoOrdenarNumeros:
    '''
    Clase que modela el juego de Ordenar los números.
    '''

    def __init__(self, cantidad_elementos: int = 5) -> None:
        self.elementos = None
        self.cantidad_elementos = cantidad_elementos
        self.desordenar_elementos()

    def desordenar_elementos(self) -> None:
        '''
        General la respuesta esperada según la cantidad de elementos.
        La respuesta esperada consistirá en un lista de números desordenados 
        desde 1 hasta 'cantidad_elementos'.
        '''
        self.elementos = list(map(lambda x: x + 1, range(self.cantidad_elementos)))
        random.shuffle(self.elementos)

    def comprobar_elementos(self, respuesta: list) -> int:
        '''
        Comprueba la cantidad de aciertos de la respuesta recibida y
        la respuesta esperada.
        '''
        aciertos = 0

        for (v_elemento, v_respuesta) in zip(self.elementos, respuesta):
            if v_elemento == v_respuesta:
                aciertos += 1

        return aciertos


if __name__ == '__main__':
    random.seed(3276)

    print('1. Tablero inicial')
    juego = JuegoOrdenarNumeros()
    print(juego.elementos)

    print()
    print('2. Comprobar respuesta')
    respuesta = [5, 2, 3, 1, 4]
    cantidad_aciertos = juego.comprobar_elementos(respuesta)
    print('  i.', respuesta, cantidad_aciertos)

    respuesta = [4, 1, 2, 3, 5]
    cantidad_aciertos = juego.comprobar_elementos(respuesta)
    print(' ii.', respuesta, cantidad_aciertos)

    respuesta = [3, 1, 2, 5, 4]
    cantidad_aciertos = juego.comprobar_elementos(respuesta)
    print('iii.', respuesta, cantidad_aciertos)

    print()
    print('3. Reiniciar juego')
    juego.desordenar_elementos()
    print(juego.elementos)

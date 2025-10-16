from __future__ import annotations
from random import random
from threading import Event, Lock, Thread
from time import sleep
from typing import Callable


class DCClub(Thread):

    DURACION_CLUB_ABIERTO = 3
    TIEMPO_ESPERA_INSTRUMENTOS = 0.2
    TIEMPO_ESPERA_MESA_SONIDO = 0.3
    PROBABILIDAD_ERROR_MESA_SONIDO = 0.6

    def __init__(self, capacidad: int, artista: str, instrumentos: list) -> None:
        super().__init__()

        self.capacidad_actual = 0
        self.capacidad_maxima = capacidad
        self.senal_abierto = Event()
        self.lock_capacidad = Lock()

        self.artista = artista
        self.instrumentos = instrumentos

    def revisar_mesa_sonido(self) -> bool:
        print('[Mesa Sonido]\t Empezando revisión')

        # Se espera el tiempo correspondiente.
        sleep(self.TIEMPO_ESPERA_MESA_SONIDO)

        # Si ocurre un error, se espera el tiempo correspondiente y
        # se verifica si hay un nuevo error.
        while random() < self.PROBABILIDAD_ERROR_MESA_SONIDO:
            print('[Mesa Sonido]\t Hubo un error, la revisión tomará un tiempo adicional')
            sleep(self.TIEMPO_ESPERA_MESA_SONIDO)

        print('[Mesa Sonido]\t Revisión completada')
        return True

    def revisar_instrumentos(self) -> bool:
        print('[Instrumentos]\t Empezando revisión')

        # Por cada instrumento se espera el tiempo correspondiente.
        for instrumento in self.instrumentos:
            print(f'[Instrumentos]\t Revisando {instrumento}')
            sleep(self.TIEMPO_ESPERA_INSTRUMENTOS)

        print('[Instrumentos]\t Revisión completada')
        return True

    def preparar_escenario(self) -> bool:
        # TODO: Parte I
        pass

    def llegada_cliente(self, cliente: Cliente) -> None:
        self.capacidad_actual += 1
        print(f'[DCClub]\t Entra el cliente {cliente.id}. ' \
              f'Capacidad actual: {self.capacidad_actual} de {self.capacidad_maxima}')

    def salida_cliente(self, cliente: Cliente) -> None:
        self.capacidad_actual -= 1
        print(f'[DCClub]\t Sale el cliente {cliente.id}. ' \
              f'Capacidad actual: {self.capacidad_actual} de {self.capacidad_maxima}')

    def manejar_llegada_cliente(self, cliente: Cliente) -> bool:
        # TODO: Parte I
        pass

    def manejar_salida_cliente(self, cliente: Cliente) -> bool:
        # TODO: Parte I
        pass

    def run(self) -> None:
        # TODO: Parte I
        print('[DCClub]\t Preparando escenario')
        print('[DCClub]\t Escenario preparado')
        print('[DCClub]\t Abre el DCClub a los clientes')
        print('[DCClub]\t Cierra el DCClub')
        pass


class Cliente(Thread):

    ID = 0
    TIEMPO_ESPERA_NUEVO_INTENTO = 1
    MIN_TIEMPO_EN_CLUB = 0.1
    RANGO_TIEMPO_EN_CLUB = 5

    def __init__(self, senal_abrio_club: Event, metodo_llega: Callable,
                 metodo_salida: Callable) -> None:
        super().__init__()
        self.daemon = None  # TODO: Parte II

        self.senal_abrio_club = senal_abrio_club
        self.entrar_al_club = metodo_llega
        self.salir_del_club = metodo_salida

        self.id = Cliente.ID
        Cliente.ID += 1

    def calcular_tiempo_en_club(self) -> float:
        return random() * self.RANGO_TIEMPO_EN_CLUB + self.MIN_TIEMPO_EN_CLUB

    def intentar_entrar_dcclub(self) -> bool:
        # TODO: Parte II
        pass

    def intentar_salir_dcclub(self) -> bool:
        # TODO: Parte II
        pass

    def run(self) -> None:
        # TODO: Parte II
        print(f'[Cliente {self.id}]\t Esperando para entrar al DCClub')
        print(f'[Cliente {self.id}]\t Ahora quiero ingresar al DCClub')
        print(f'[Cliente {self.id}]\t Ya estoy disfrutando del DCClub')
        print(f'[Cliente {self.id}]\t Ahora quiero salir al DCClub')
        print(f'[Cliente {self.id}]\t Ya me fui del DCClub')
        pass


if __name__ == '__main__':
    dcclub = DCClub(
        2,
        'PepaBand',
        ['GuitarraEléctrica', 'Bajo', 'Batería', 'Teclado', 'Sintetizador']
    )

    clientes = []

    for _ in range(5):
        cliente = Cliente(dcclub.senal_abierto,
                          dcclub.manejar_llegada_cliente,
                          dcclub.manejar_salida_cliente)
        clientes.append(cliente)
        cliente.start()

    dcclub.start()

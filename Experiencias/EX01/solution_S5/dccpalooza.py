from parametros import PROBABILIDAD_EVENTO, PUBLICO_EXITO, PUBLICO_INICIAL, \
                       PUBLICO_TERREMOTO, AFINIDAD_OLA_CALOR, \
                       AFINIDAD_LLUVIA, PUBLICO_OLA_CALOR
from random import random, choice


class DCCPalooza:

    def __init__(self):
        self.artista_actual = ''
        self.__dia = 1
        self.line_up = []
        self.cant_publico = PUBLICO_INICIAL
        self.artistas = []
        self.prob_evento = PROBABILIDAD_EVENTO
        self.suministros = []

    @property
    def dia(self):
        return self.__dia

    @property
    def funcionando(self):
        return self.exito_del_concierto and self.dia <= 3

    @property
    def exito_del_concierto(self):
        return self.cant_publico >= PUBLICO_EXITO

    def imprimir_estado(self):
        print(f"Día: {self.__dia}\nCantidad de Personas: "
              f"{self.cant_publico}\nArtistas:")
        for artista in self.line_up:
            print(f"- {artista.nombre}")

    def ingresar_artista(self, artista):
        self.line_up.append(artista)
        print(f'Se ha ingresado un nuevo artista!!!\n{artista}')

    def asignar_lineup(self):
        self.line_up = []
        for artista in self.artistas:
            if self.dia == artista.dia_presentacion:
                self.ingresar_artista(artista)

    def nuevo_dia(self):
        '''
        NOTE: Dado que __dia no tiene un setter,
              debemos modificar el atributo directamente.
        '''
        if self.exito_del_concierto:
            self.__dia += 1
        if self.__dia <= 3:
            print('Nuevo día')

    def encontrar_artista(self, nombre):
        '''
        NOTE: Método suplementario para encontrar instancia de Artista
              a partir de su nombre.
        IMPORTANT: En el enunciado aparecia que artista_actual es un str,
                   pero a nivel de código es una instancia de Artista,
                   por lo que este método no era necesario al final.
                   El enunciado fue corregido y actualizado.
        '''
        for artista in self.artistas:
            if artista.nombre == nombre:
                return artista

    def ejecutar_evento(self):
        # Verificar si ocurre el evento
        # NOTE: Es importante tener en consideración si se utiliza < o >,
        #       ya que esto afecta las probabilidades.
        if random() < self.prob_evento:
            # Sí ocurre algo
            evento = choice(('lluvia', 'terremoto', 'calor'))

            if evento == 'lluvia':
                artista = self.encontrar_artista(self.artista_actual)
                artista.afinidad_con_publico -= AFINIDAD_LLUVIA
                print('llovio :c')

            elif evento == 'terremoto':
                self.cant_publico -= PUBLICO_TERREMOTO
                print('temblo :c')

            elif evento == 'calor':
                artista = self.encontrar_artista(self.artista_actual)
                artista.afinidad_con_publico -= AFINIDAD_OLA_CALOR
                self.cant_publico -= PUBLICO_OLA_CALOR
                print('ola de calor :c')

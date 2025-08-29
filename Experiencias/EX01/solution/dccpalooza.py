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

    # Asigna el line up de cada día
    def asignar_lineup(self):
        self.line_up = []
        for artista in self.artistas:
            if self.dia == artista.dia_presentacion:
                self.ingresar_artista(artista)

    def nuevo_dia(self):
        if self.exito_del_concierto:
            self.__dia += 1
            if self.dia <= 3:
                print(f'Ha comenzado el día {self.dia} en DCCPalooza')

    # Ejecuta un evento en caso de que se cumpla la porbabilidad
    def ejecutar_evento(self):
        if random() < self.prob_evento:
            lista_eventos = ["Lluvia", "Terremoto", "Ola de calor"]
            evento = choice(lista_eventos)
            print(f"Oh no ha ocurrido el evento {evento}")
            if evento == lista_eventos[0]:
                print(f"La afinidad con el público "
                      f"ha disminuido en {AFINIDAD_LLUVIA}")
                self.artista_actual.afinidad_con_publico -= AFINIDAD_LLUVIA
            elif evento == lista_eventos[1]:
                print(f"La cantidad de público "
                      f"ha disminuido en {PUBLICO_TERREMOTO}")
                self.cant_publico -= PUBLICO_TERREMOTO
            else:
                print(f"La afinidad con el público "
                      f"ha disminuido en {AFINIDAD_OLA_CALOR}")
                self.artista_actual.afinidad_con_publico -= AFINIDAD_OLA_CALOR
                print(f"La cantidad de público "
                      f"ha disminuido en {PUBLICO_OLA_CALOR}")
                self.cant_publico -= PUBLICO_OLA_CALOR

from backend.nodo_ligado import NodoLigado
from typing import Generator
from utils import (HabitatObjeto, Juguete, JugueteHabitat, JugueteObjeto, JugueteRecurso, 
                   ObjetoRecurso, PeriodoDia, RecursoRecurso)


def cargar_juguete(path: str) -> Generator[Juguete]:
    pass


def cargar_juguete_habitat(path: str) -> Generator[JugueteHabitat]:
    pass


def cargar_habitat_objeto(path: str) -> Generator[HabitatObjeto]:
    pass


def cargar_objeto_recurso(path: str) -> Generator[ObjetoRecurso]:
    pass


def cargar_recurso_recurso(path: str) -> Generator[RecursoRecurso]:
    pass


def cargar_juguete_recurso(path: str) -> Generator[JugueteRecurso]:
    pass


def cargar_juguete_objeto(path: str) -> Generator[JugueteObjeto]:
    pass

def cargar_periodo_dia(path: str) -> Generator[PeriodoDia]:
    pass


def ahora_es(generador_perio_dia: Generator, minutos: int) -> tuple:
    pass


def recursos_a_partir_de_recurso(generador_recurso_recurso: Generator,
                                 id_recurso: int) -> Generator:
    pass


def juguetes_producen(generador_juguete_recurso: Generator, id_recurso: int) -> Generator:
    pass


def juguetes_productivos(generador_juguete_recurso: Generator,
                         minimo: float | None = None) -> Generator:
    pass


def habitats_de_interes(generador_juguete: Generator,
                        generador_juguete_habitat: Generator) -> Generator:
    pass


def cadena_creacion(generador_juguete_recurso: Generator, generador_recurso_recurso: Generator,
                    id_recurso: int) -> dict:
    pass


def juguetes_a_aparecer(generador_juguete_habitat: Generator, generador_periodo_dia: Generator,
                        id_habitat: int, momento_dia: int = 0) -> Generator:
    pass


def juguetes_autosuficientes(generador_juguete: Generator,
                             generador_juguete_objeto: Generator,
                             generador_objeto_recurso: Generator,
                             generador_juguete_recurso: Generator,
                             generador_recurso_recurso: Generator) -> Generator:
    pass


def habitat_eventualmente_creables(generador_juguete: Generator,
                                   generador_juguete_recurso: Generator,
                                   generador_recurso_recurso: Generator,
                                   generador_objeto_recurso: Generator,
                                   generador_habitat_objeto: Generator) -> Generator:
    pass

def avanzar_produccion(generador_juguete_recurso: Generator,
                       generador_juguete_objeto: Generator,
                       JugueteProductor: NodoLigado | None,
                       objetos: set,
                       minutos: int = 1) -> Generator:
    pass


def crear_recursos(generador_juguete_recurso: Generator,
                   generador_juguete_objeto: Generator) -> Generator:
    pass


def agregar_recursos(recurso: NodoLigado | None, nuevos_recursos: tuple) -> object:
    pass


def por_aparecer(generador_juguete: Generator, Habitat: NodoLigado | None, generador_juguete_habitat: Generator,
                 generador_periodo_dia: Generator, momento_dia: int = 0) -> Generator:
    pass


def habitat_creables(generador_juguete: Generator, generador_juguete_recurso: Generator,
                     generador_recurso_recurso: Generator, generador_objeto_recurso: Generator,
                     generador_habitat_objeto: Generator, Recurso: NodoLigado | None) -> Generator:
    pass


def manejo_habitat(gen_juguete: Generator,
                   gen_juguete_habitat: Generator,
                   gen_habitat_objeto: Generator,
                   gen_objeto_recurso: Generator,
                   gen_recurso_recurso: Generator,
                   gen_periodo_dia: Generator,
                   tiempo_inicial: int = 0) -> Generator:
    pass


# Simulación

def simular(generador_juguete: Generator, generador_juguete_habitat: Generator,
            generador_habitat_objeto: Generator, generador_objeto_recurso: Generator,
            generador_recurso_recurso: Generator, generador_juguete_recurso: Generator,
            generador_juguete_objeto: Generator, generador_periodo_dia: Generator) -> Generator:
    pass

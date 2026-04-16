from functools import reduce
from itertools import groupby
from typing import Callable, Generator, Iterable

from dcc137 import Persona, Ciudad, Pais


#---+--------------------------------------+
#   | Parte I: Cargar datos                |
#---+--------------------------------------+

def cargar_personas(ruta_archivo_personas: str) -> Generator:
    '''
    Retorna un generador de Persona
    '''
    pass

def cargar_territorios(ruta_archivo_territorios: str, tipo_territorio: Pais | Ciudad) -> Generator:
    '''
    Retorna un generador de Pais o Ciudad
    '''
    pass


#---+--------------------------------------+
#   | Parte II: Mostrar datos              |
#---+--------------------------------------+

def nprint(datos: Iterable, funcion_a_aplicar: Callable = lambda x: x, cantidad: int = 3) -> int:
    '''
    Imprime hasta `cantidad` de `datos` aplicando `funcion_a_aplicar`
    por cada dato antes de imprimir; cada dato usa una línea.
    Retorna la cantidad de líneas que se imprimieron.
    '''
    pass


#---+--------------------------------------+
#   | Parte III: Consultar datos           |
#---+--------------------------------------+

def sigla_de_pais_con_nombre(paises: Generator, nombre: str) -> str:
    '''
    Busca la sigla de país de nombre `nombre` dentro de `paises` y la retorna.
    '''
    pass


def ciudades_por_pais(nombre_pais: str, paises: Generator, ciudades: Generator) -> Generator:
    '''
    Retorna las ciudades que estén en el país indicado
    '''
    pass


def personas_por_pais(nombre_pais: str, paises: Generator,
                      ciudades: Generator, personas: Generator) -> Generator:
    '''
    Retorna un generador con las personas del pais de nombre indicado.
    '''
    pass


def sueldo_promedio(personas: Generator) -> float:
    '''
    Retorna el sueldo promedio de `personas`
    '''
    pass


def sueldo_promedio_por_area_de_trabajo(personas: Generator) -> dict[str, float]:
    '''
    Retorna un diccionario cuyas llaves son un área de trabajo, y el valor es el 
    sueldo promedio de esa área. 
    tip 1: Averigua de lo que hace groupby de itertools.
    tip 2: Las personas ya vienen ordenadas por área de trabajo.
    hint: Usa sueldo_promedio.
    '''



if __name__ == '__main__':
    RUTA_PAISES = "Paises.csv"
    RUTA_CIUDADES = "Ciudades.csv"
    RUTA_PERSONAS = "Personas.csv"

    parte = 1

    personas = cargar_personas(RUTA_PERSONAS)
    paises = cargar_territorios(RUTA_PAISES, Pais)
    ciudades = cargar_territorios(RUTA_CIUDADES, Ciudad)

    match parte:
        case 1:
            print("9 Personas: ", end='')
            print(', '.join(
                    f"{persona.nombre} {persona.apellido}" for _, persona in 
                    filter(lambda item: item[0] < 9, enumerate(personas))
                )
            )
            print("9 Ciudades: ", end='')
            print(', '.join(
                    ciudad.nombre for _, ciudad in 
                    filter(lambda item: item[0] < 9, enumerate(ciudades))
                )
            )
            print("9 Países: ", end='')
            print(', '.join(
                    pais.nombre for _, pais in 
                    filter(lambda item: item[0] < 9, enumerate(paises))
                )
            )

        case 2:
            print("\n3 Personas")
            nprint(personas, lambda p: (p.nombre, p.ciudad))

            print("\n3 Paises")
            nprint(paises, lambda pais: (pais.sigla, pais.nombre))

            print("\n3 Ciudades")
            nprint(ciudades, lambda ciudad: (ciudad.sigla, ciudad.nombre))

        case 3:   
            print("\n3a: sigla_de_pais_con_nombre")
            print(
                "Japón: ", sigla_de_pais_con_nombre(cargar_territorios(RUTA_PAISES, Pais), "Japan")
            )

            print('\n3b: ciudades_por_pais')
            nprint(
                ciudades_por_pais("Chile",
                              cargar_territorios(RUTA_PAISES, Pais),
                              cargar_territorios(RUTA_CIUDADES, Ciudad)),
                funcion_a_aplicar=lambda x: x.nombre
            )

            print('\n3c: personas_por_pais')
            nprint(
                personas_por_pais("Chile",
                              cargar_territorios(RUTA_PAISES, Pais),
                              cargar_territorios(RUTA_CIUDADES, Ciudad),
                              cargar_personas(RUTA_PERSONAS)
                ),
                funcion_a_aplicar=lambda x: (x.nombre, x.ciudad)
            )

            print('\n3d: sueldo_promedio')
            print('Sueldo promedio:', sueldo_promedio(cargar_personas(RUTA_PERSONAS)))

            print('\n3e: sueldo_promedio_por_area_de_trabajo')
            nprint(
                sueldo_promedio_por_area_de_trabajo(cargar_personas(RUTA_PERSONAS)).items(),
                funcion_a_aplicar=lambda informacion: f"{informacion[1]:>10.2f}: {informacion[0]:<20.20}"
            )

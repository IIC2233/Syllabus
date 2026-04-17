from functools import reduce
from itertools import groupby, product
from typing import Callable, Generator, Iterable

from dcc137 import Persona, Ciudad, Pais


#---+--------------------------------------+
#   | Parte I: Cargar datos                |
#---+--------------------------------------+

def cargar_personas(ruta_archivo_personas: str) -> Generator:
    '''
    Retorna un generador de Persona
    '''
    with open(ruta_archivo_personas, encoding='utf-8') as archivo:
        for linea in archivo:  # Equivalente archivo.readline()
            info = linea.strip('\n').split(',')
            info[2] = int(info[2])
            info[-1] = int(info[-1])
            yield Persona(*info)

def cargar_territorios(ruta_archivo_territorios: str, tipo_territorio: Pais | Ciudad) -> Generator:
    '''
    Retorna un generador de Pais o Ciudad
    '''
    archivo = open(ruta_archivo_territorios, encoding='utf-8')

    linea = archivo.readline()
    while linea:
        info = linea.strip('\n').split(',')
        yield tipo_territorio(*info)
        linea = archivo.readline() 

    archivo.close()




#---+--------------------------------------+
#   | Parte II: Mostrar datos              |
#---+--------------------------------------+

def nprint(datos: Iterable, funcion_a_aplicar: Callable = lambda x: x, cantidad: int = 3) -> int:
    '''
    Imprime hasta `cantidad` de `datos` aplicando `funcion_a_aplicar`
    por cada dato antes de imprimir; cada dato usa una línea.
    Retorna la cantidad de líneas que se imprimieron.
    '''
    for contador, valor in zip(range(cantidad), datos):
        print(funcion_a_aplicar(valor))
    return contador + 1


#---+--------------------------------------+
#   | Parte III: Consultar datos           |
#---+--------------------------------------+

def sigla_de_pais_con_nombre(paises: Generator, nombre: str) -> str:
    '''
    Busca la sigla de país de nombre `nombre` dentro de `paises` y la retorna.
    '''
    pais = next(filter(lambda x: nombre == x.nombre, paises))
    return pais.sigla


def ciudades_por_pais(nombre_pais: str, paises: Generator, ciudades: Generator) -> Generator:
    '''
    Retorna las ciudades que estén en el país indicado
    '''
    sigla_pais = sigla_de_pais_con_nombre(paises, nombre_pais)
    ciudades_filtradas = filter(lambda c: c.sigla == sigla_pais, ciudades)
    return ciudades_filtradas


def personas_por_pais(nombre_pais: str, paises: Generator,
                      ciudades: Generator, personas: Generator) -> Generator:
    '''
    Retorna un generador con las personas del pais de nombre indicado.
    '''
    ciudades_filtradas = ciudades_por_pais(nombre_pais, paises, ciudades)

    # Para comprobar si las personas son del pais que estamos buscando,
    # podemos hacer una asociación entre el generador de ciudades y
    # el generador de personas.
    # Para esto usamos: itertools.product() + filter()
    # - itertools.product() -> Entrega el producto cartesiano entre 2 iterables
    # - filter() -> Lo usamos para asegurar que queden los pares correctos,
    #               es decir, que compartan información
    
    # Obtenemos un generador con tuplas (ciudad, persona)
    producto_persona_ciudad = product(ciudades_filtradas, personas)

    # Filtramos asegurando que solo queden los pares ciudad, persona donde
    # la ciudad sea la misma en la que vive la persona
    producto_filtrado = filter(lambda t: t[0].nombre == t[1].ciudad, producto_persona_ciudad)
    personas_filtradas = map(lambda t: t[1], producto_filtrado)
    return personas_filtradas


def sueldo_promedio(personas: Generator) -> float:
    '''
    Retorna el sueldo promedio de `personas`
    '''
    sueldos = map(lambda p: p.sueldo, personas)
                                     # Promedio = suma_total / cantidad
                                               # (suma_total, cantidad  )
    suma_total, cantidad = reduce(lambda acc, s: (acc[0] + s, acc[1] + 1), sueldos, (0, 0))
    return suma_total / cantidad

def sueldo_promedio_por_area_de_trabajo(personas: Generator) -> dict[str, float]:
    '''
    Retorna un diccionario cuyas llaves son un área de trabajo, y el valor es el 
    sueldo promedio de esa área. 
    tip 1: Averigua de lo que hace groupby de itertools.
    tip 2: Las personas ya vienen ordenadas por área de trabajo.
    hint: Usa sueldo_promedio.
    '''

    # Aseguramos que las personas estén ordenadas por su área de trabajo
    # NOTA: Si los datos no están ordenados por el factor de agrupación,
    #       entonces la agrupación fallará
    personas = sorted(personas, key=lambda p: p.trabajo)

    # Agrupamos por trabajo. 
    # Esto retorna un generador con tuplas (llave de agrupación, generador con valores agrupados)
    agrupacion = groupby(personas, key=lambda p: p.trabajo)

    # Calculamos promedio sueldo y retornamos
    # NOTA: La iteración por defecto de un groupby es equivalente al items() de un diccionario
    return {trabajo: sueldo_promedio(trabajadores) for trabajo, trabajadores in agrupacion}


if __name__ == '__main__':
    RUTA_PAISES = "Paises.csv"
    RUTA_CIUDADES = "Ciudades.csv"
    RUTA_PERSONAS = "Personas.csv"

    parte = 3

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

import numpy as np
import time

def suma_de_listas(lista1, lista2):
    tiempo_inicial = time.time()

    resultado_lista = [a + b for a, b in zip(lista1, lista2)]

    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    return tiempo_ejecucion

def suma_de_arrays(array1, array2):
    tiempo_inicial = time.time()

    resultado_array = array1 + array2

    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    return tiempo_ejecucion

def promedio_de_lista(lista):
    tiempo_inicial = time.time()

    promedio = sum(lista) / len(lista)

    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    return tiempo_ejecucion

def promedio_de_array(array):
    tiempo_inicial = time.time()

    promedio = np.mean(array)

    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    return tiempo_ejecucion

def obtener_elementos_mayores_a_lista(lista, valor):
    tiempo_inicial = time.time()

    elementos_mayores = [x for x in lista if x > valor]

    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    return tiempo_ejecucion

def obtener_elementos_mayores_a_array(array, valor):
    tiempo_inicial = time.time()

    elementos_mayores = array[array > valor]

    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    return tiempo_ejecucion
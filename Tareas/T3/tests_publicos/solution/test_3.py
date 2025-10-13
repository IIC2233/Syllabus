"""
Soluciones para test_03 - Planetas con cantidad de minerales
Contiene todas las constantes con los resultados esperados para los tests de planetas con cantidad de minerales
"""

from collections import namedtuple

# Definir la estructura PlanetaMineral
PlanetaMineral = namedtuple("PlanetaMineral", ["id_planeta", "id_mineral", "cantidad_disponible", "pureza"])

# Datos de entrada para todos los tests (primeros registros de cada tamaño)
DATOS_PLANETA_MINERALES_S = [
    PlanetaMineral(id_planeta=1, id_mineral=38, cantidad_disponible=749775.785, pureza=0.884),
    PlanetaMineral(id_planeta=1, id_mineral=11, cantidad_disponible=393364.933, pureza=0.45),
    PlanetaMineral(id_planeta=1, id_mineral=32, cantidad_disponible=818605.825, pureza=0.083),
    PlanetaMineral(id_planeta=1, id_mineral=73, cantidad_disponible=863256.779, pureza=0.26),
    PlanetaMineral(id_planeta=2, id_mineral=86, cantidad_disponible=71329.77, pureza=0.255),
    PlanetaMineral(id_planeta=2, id_mineral=70, cantidad_disponible=679125.686, pureza=0.532),
    PlanetaMineral(id_planeta=2, id_mineral=28, cantidad_disponible=684518.036, pureza=0.174),
    PlanetaMineral(id_planeta=2, id_mineral=59, cantidad_disponible=184535.608, pureza=0.126),
]

DATOS_PLANETA_MINERALES_M = [
    PlanetaMineral(id_planeta=1, id_mineral=235, cantidad_disponible=41159.413, pureza=0.105),
    PlanetaMineral(id_planeta=1, id_mineral=66, cantidad_disponible=312321.388, pureza=0.865),
    PlanetaMineral(id_planeta=1, id_mineral=135, cantidad_disponible=969409.457, pureza=0.94),
    PlanetaMineral(id_planeta=2, id_mineral=229, cantidad_disponible=712160.639, pureza=0.961),
    PlanetaMineral(id_planeta=2, id_mineral=94, cantidad_disponible=668685.471, pureza=0.4),
    PlanetaMineral(id_planeta=2, id_mineral=2, cantidad_disponible=974944.305, pureza=0.769),
    PlanetaMineral(id_planeta=2, id_mineral=38, cantidad_disponible=98956.057, pureza=0.122),
]

DATOS_PLANETA_MINERALES_L = [
    PlanetaMineral(id_planeta=1, id_mineral=235, cantidad_disponible=41159.413, pureza=0.105),
    PlanetaMineral(id_planeta=1, id_mineral=66, cantidad_disponible=312321.388, pureza=0.865),
    PlanetaMineral(id_planeta=1, id_mineral=135, cantidad_disponible=969409.457, pureza=0.94),
    PlanetaMineral(id_planeta=2, id_mineral=229, cantidad_disponible=712160.639, pureza=0.961),
    PlanetaMineral(id_planeta=2, id_mineral=94, cantidad_disponible=668685.471, pureza=0.4),
    PlanetaMineral(id_planeta=2, id_mineral=2, cantidad_disponible=974944.305, pureza=0.769),
]

# Resultados esperados para cada test

# Test 0: S - mineral 38, cantidad mínima 700000
PLANETAS_CON_CANTIDAD_S_0 = [1, 4, 5, 59]  # Solo planeta 1 tiene mineral 38 con cantidad >= 700000

# Test 1: S - mineral 70, cantidad mínima 600000
PLANETAS_CON_CANTIDAD_S_1 = [4, 12, 31]

# Test 2: M - mineral 66, cantidad mínima 300000
PLANETAS_CON_CANTIDAD_M_0 = [189]  # Solo planeta 1 tiene mineral 66 con cantidad >= 300000

# Test 3: M - mineral 2, cantidad mínima 900000
PLANETAS_CON_CANTIDAD_M_1 = [2, 98, 119, 137, 154, 213]  # Solo planeta 2 tiene mineral 2 con cantidad >= 900000

# Test 4: L - mineral 135, cantidad mínima 900000
PLANETAS_CON_CANTIDAD_L_0 = []  # Solo planeta 1 tiene mineral 135 con cantidad >= 900000

# Test 5: L - mineral 229, cantidad mínima 700000
PLANETAS_CON_CANTIDAD_L_1 = [86, 389]  # Solo planeta 2 tiene mineral 229 con cantidad >= 700000

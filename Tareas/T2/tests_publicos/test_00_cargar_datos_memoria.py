import os
import unittest
from tests_publicos.test_tools import IICTest, timeout, max_memory
from backend.consultas import (
    cargar_juguete,
    cargar_juguete_habitat,
    cargar_habitat_objeto,
    cargar_objeto_recurso,
    cargar_recurso_recurso,
    cargar_juguete_recurso,
    cargar_juguete_objeto,
    cargar_periodo_dia,
)

N_SECOND = 5.0

# Margen sobre el pico medido: límite = pico_real × FACTOR
# Para calibrar: cambiar debug=False → debug=True en cada @max_memory y correr:
#   python3 -B -m unittest -v -b tests_publicos.test_00_cargar_datos_memoria
# Luego actualizar los N_MB_* con (valor_impreso × FACTOR) y volver a debug=False.
FACTOR = 3

# Límites calibrados con dataset XL (pico_medido × FACTOR).
N_MB_JUGUETE          = 0.0803 * FACTOR
N_MB_JUGUETE_HABITAT  = 0.0310 * FACTOR
N_MB_HABITAT_OBJETO   = 0.2554 * FACTOR
N_MB_OBJETO_RECURSO   = 0.1115 * FACTOR
N_MB_RECURSO_RECURSO  = 0.0845 * FACTOR
N_MB_JUGUETE_RECURSO  = 0.0209 * FACTOR
N_MB_JUGUETE_OBJETO   = 0.0212 * FACTOR
N_MB_PERIODO_DIA      = 0.0150 * FACTOR

PATH_XL = os.path.join("data", "XL")


class TestCargarDatosMemoria(IICTest):
    """
    Verifica que las funciones cargar_* usen memoria constante (O(1)) al iterar,
    sin cargar todo el archivo en una lista antes de hacer yield.
    Evaluado con el dataset XL.
    """

    @timeout(N_SECOND)
    @max_memory(mb=N_MB_JUGUETE, debug=False)
    def test_cargar_juguete_memoria(self):
        """
        Iterar cargar_juguete sobre el dataset XL no debe superar el límite de memoria.
        """
        for _ in cargar_juguete(os.path.join(PATH_XL, "juguetes.csv")):
            pass

    @timeout(N_SECOND)
    @max_memory(mb=N_MB_JUGUETE_RECURSO, debug=False)
    def test_cargar_juguete_recurso_memoria(self):
        """
        Iterar cargar_juguete_recurso sobre el dataset XL no debe superar el límite de memoria.
        """
        for _ in cargar_juguete_recurso(os.path.join(PATH_XL, "juguete_recurso.csv")):
            pass

    @timeout(N_SECOND)
    @max_memory(mb=N_MB_JUGUETE_OBJETO, debug=False)
    def test_cargar_juguete_objeto_memoria(self):
        """
        Iterar cargar_juguete_objeto sobre el dataset XL no debe superar el límite de memoria.
        """
        for _ in cargar_juguete_objeto(os.path.join(PATH_XL, "juguete_objeto.csv")):
            pass

    @timeout(N_SECOND)
    @max_memory(mb=N_MB_JUGUETE_HABITAT, debug=False)
    def test_cargar_juguete_habitat_memoria(self):
        """
        Iterar cargar_juguete_habitat sobre el dataset XL no debe superar el límite de memoria.
        """
        for _ in cargar_juguete_habitat(os.path.join(PATH_XL, "juguete_habitat.csv")):
            pass

    @timeout(N_SECOND)
    @max_memory(mb=N_MB_HABITAT_OBJETO, debug=False)
    def test_cargar_habitat_objeto_memoria(self):
        """
        Iterar cargar_habitat_objeto sobre el dataset XL no debe superar el límite de memoria.
        """
        for _ in cargar_habitat_objeto(os.path.join(PATH_XL, "habitat_objeto.csv")):
            pass

    @timeout(N_SECOND)
    @max_memory(mb=N_MB_OBJETO_RECURSO, debug=False)
    def test_cargar_objeto_recurso_memoria(self):
        """
        Iterar cargar_objeto_recurso sobre el dataset XL no debe superar el límite de memoria.
        """
        for _ in cargar_objeto_recurso(os.path.join(PATH_XL, "objeto_recurso.csv")):
            pass

    @timeout(N_SECOND)
    @max_memory(mb=N_MB_RECURSO_RECURSO, debug=False)
    def test_cargar_recurso_recurso_memoria(self):
        """
        Iterar cargar_recurso_recurso sobre el dataset XL no debe superar el límite de memoria.
        """
        for _ in cargar_recurso_recurso(os.path.join(PATH_XL, "recurso_recurso.csv")):
            pass

    @timeout(N_SECOND)
    @max_memory(mb=N_MB_PERIODO_DIA, debug=False)
    def test_cargar_periodo_dia_memoria(self):
        """
        Iterar cargar_periodo_dia sobre el dataset XL no debe superar el límite de memoria.
        """
        for _ in cargar_periodo_dia(os.path.join(PATH_XL, "periodo_dia.csv")):
            pass

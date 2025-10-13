import os
import sys
import tracemalloc
import unittest
from collections.abc import Iterable, Generator
from tests_publicos.utils import timer_decorator, memory_decorator, indexes_of
from backend.consultas import (
    cargar_astronautas,
    cargar_materiales_mision,
    cargar_minerales,
    cargar_mision,
    cargar_naves,
    cargar_planeta_minerales,
    cargar_planetas,
    cargar_tripulaciones
)

from tests_publicos.timeout_function import timeout

N_SECOND = 0.1
N_MEMORIA = 73*(2**10)

# sys.stdout = open(os.devnull, 'w', encoding='utf-8')


class TestCargarDatos(unittest.TestCase):
    def __init__(self, *args):
        self.maxDiff = 1000
        super().__init__(*args)

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_s_astronautas(self):
        """
        Verifica que los datos carguen bien con un dataset S de Astronauta.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_S", "Astronauta.csv")
        generador = cargar_astronautas(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_m_astronautas(self):
        """
        Verifica que los datos carguen bien con un dataset M de Astronauta.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_M", "Astronauta.csv")
        generador = cargar_astronautas(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_l_astronautas(self):
        """
        Verifica que los datos carguen bien con un dataset L de Astronauta.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_L", "Astronauta.csv")
        generador = cargar_astronautas(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_s_naves(self):
        """
        Verifica que los datos carguen bien con un dataset S de Naves.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_S", "Nave.csv")
        generador = cargar_naves(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_m_naves(self):
        """
        Verifica que los datos carguen bien con un dataset M de Naves.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_M", "Nave.csv")
        generador = cargar_naves(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_l_naves(self):
        """
        Verifica que los datos carguen bien con un dataset L de Naves.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_L", "Nave.csv")
        generador = cargar_naves(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_s_tripulacion(self):
        """
        Verifica que los datos carguen bien con un dataset S de Naves.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_S", "Tripulacion.csv")
        generador = cargar_tripulaciones(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_m_tripulacion(self):
        """
        Verifica que los datos carguen bien con un dataset M de Naves.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_M", "Tripulacion.csv")
        generador = cargar_tripulaciones(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_l_tripulacion(self):
        """
        Verifica que los datos carguen bien con un dataset L de Tripulaciones.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_L", "Tripulacion.csv")
        generador = cargar_tripulaciones(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_s_planetas(self):
        """
        Verifica que los datos carguen bien con un dataset S de Planetas.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_S", "Planeta.csv")
        generador = cargar_planetas(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_m_planetas(self):
        """
        Verifica que los datos carguen bien con un dataset M de Planetas.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_M", "Planeta.csv")
        generador = cargar_planetas(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_l_planetas(self):
        """
        Verifica que los datos carguen bien con un dataset L de Planetaes.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_L", "Planeta.csv")
        generador = cargar_planetas(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_s_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset S de minerales.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_S", "Mineral.csv")
        generador = cargar_minerales(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_m_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset M de minerales.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_M", "Mineral.csv")
        generador = cargar_minerales(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_l_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset L de Minerales.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_L", "Mineral.csv")
        generador = cargar_minerales(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_s_planeta_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset S de PlanetaMineral.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_S", "PlanetaMineral.csv")
        generador = cargar_planeta_minerales(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_m_planeta_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset M de PlanetaMineral.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_M", "PlanetaMineral.csv")
        generador = cargar_planeta_minerales(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_l_planeta_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset L de PlanetaMineral.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_L", "PlanetaMineral.csv")
        generador = cargar_planeta_minerales(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_s_misiones(self):
        """
        Verifica que los datos carguen bien con un dataset S de misiones.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_S", "Mision.csv")
        generador = cargar_mision(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_m_misiones(self):
        """
        Verifica que los datos carguen bien con un dataset M de misiones.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_M", "Mision.csv")
        generador = cargar_mision(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_l_misiones(self):
        """
        Verifica que los datos carguen bien con un dataset L de misiones.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_L", "Mision.csv")
        generador = cargar_mision(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_s_misiones_mineral(self):
        """
        Verifica que los datos carguen bien con un dataset S de misiones_mineral.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_S", "MisionMineral.csv")
        generador = cargar_materiales_mision(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_m_misiones_mineral(self):
        """
        Verifica que los datos carguen bien con un dataset M de misiones_mineral.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_M", "MisionMineral.csv")
        generador = cargar_materiales_mision(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

    @timeout(N_SECOND)
    def test_l_misiones_mineral(self):
        """
        Verifica que los datos carguen bien con un dataset L de misiones_mineral.
        """
        tracemalloc.start()
        path = os.path.join("data", "out_L", "MisionMineral.csv")
        generador = cargar_materiales_mision(path)
        for _ in generador:
            pass
        _, memory_peak = tracemalloc.get_traced_memory()
        self.assertLess(memory_peak, N_MEMORIA, f"Memoria excedida de {N_MEMORIA/(2**10):.2f}KB")
        tracemalloc.stop()

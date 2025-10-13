import os
import sys
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
from utilidades import (
    Astronauta, Nave, Mineral, Mision, MisionMineral, Planeta, PlanetaMineral, Tripulacion)

N_SECOND = 0.04

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
        path = os.path.join("data", "out_S", "Astronauta.csv")
        generador = cargar_astronautas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 14, 53, -1])
        *astronautas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 120)

        # Revisar posiciones aleatorias
        astronautas_esperados = [
            Astronauta(
                id_astronauta=1,
                nombre="Brandon Russell",
                estado="Vacaciones"
            ),
            Astronauta(
                id_astronauta=15,
                nombre="Stefanie Tucker",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=54,
                nombre="Evan Peterson",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=120,
                nombre="Adam Murphy",
                estado="Jubilado"
            ),
        ]

        self.assertCountEqual(astronautas_cargados, astronautas_esperados)

    @timeout(N_SECOND)
    def test_m_astronautas(self):
        """
        Verifica que los datos carguen bien con un dataset M de Astronauta.
        """
        path = os.path.join("data", "out_M", "Astronauta.csv")
        generador = cargar_astronautas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 425, 537, -1])
        *astronautas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 600)

        # Revisar posiciones aleatorias
        astronautas_esperados = [
            Astronauta(
                id_astronauta=1,
                nombre="Richard Briggs",
                estado="Jubilado"
            ),
            Astronauta(
                id_astronauta=426,
                nombre="Tamara Olson",
                estado="Vacaciones"
            ),
            Astronauta(
                id_astronauta=538,
                nombre="Keith Rogers",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=600,
                nombre="Kelly Thomas",
                estado="Vacaciones"
            ),
        ]

        self.assertCountEqual(astronautas_cargados, astronautas_esperados)

    @timeout(N_SECOND)
    def test_l_astronautas(self):
        """
        Verifica que los datos carguen bien con un dataset L de Astronauta.
        """
        path = os.path.join("data", "out_L", "Astronauta.csv")
        generador = cargar_astronautas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 691, 2000, -1])
        *astronautas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 2500)

        # Revisar posiciones aleatorias
        astronautas_esperados = [
            Astronauta(
                id_astronauta=1,
                nombre="Amber Robinson",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=692,
                nombre="Mr. Robert Brennan",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=2001,
                nombre="Matthew Cole",
                estado="Jubilado"
            ),
            Astronauta(
                id_astronauta=2500,
                nombre="Phillip Martin",
                estado="Activo"
            ),
        ]

        self.assertCountEqual(astronautas_cargados, astronautas_esperados)

    @timeout(N_SECOND)
    def test_s_naves(self):
        """
        Verifica que los datos carguen bien con un dataset S de Naves.
        """
        path = os.path.join("data", "out_S", "Nave.csv")
        generador = cargar_naves(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 16, 21, -1])
        *naves_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 30)

        # Revisar posiciones aleatorias
        naves_esperadas = [
            Nave(
                patente="N-001",
                material="Titanio",
                tamano="L",
                capacidad_astronautas=3,
                capacidad_minerales=1561.02,
                autonomia=73.97
            ),
            Nave(
                patente="N-017",
                material="Aluminio",
                tamano="XL",
                capacidad_astronautas=4,
                capacidad_minerales=392.15,
                autonomia=138.73
            ),
            Nave(
                patente="N-022",
                material="Acero Inoxidable",
                tamano="S",
                capacidad_astronautas=10,
                capacidad_minerales=1418.99,
                autonomia=107.01
            ),
            Nave(
                patente="N-030",
                material="Acero Inoxidable",
                tamano="L",
                capacidad_astronautas=8,
                capacidad_minerales=1603.11,
                autonomia=16.78
            ),
        ]

        self.assertCountEqual(naves_cargadas, naves_esperadas)

    @timeout(N_SECOND)
    def test_m_naves(self):
        """
        Verifica que los datos carguen bien con un dataset M de Naves.
        """
        path = os.path.join("data", "out_M", "Nave.csv")
        generador = cargar_naves(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 33, 76, -1])
        *naves_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 100)

        # Revisar posiciones aleatorias
        naves_esperadas = [
            Nave(
                patente="N-001",
                material="Aluminio",
                tamano="L",
                capacidad_astronautas=2,
                capacidad_minerales=306.4,
                autonomia=94.79
            ),
            Nave(
                patente="N-034",
                material="Acero Inoxidable",
                tamano="M",
                capacidad_astronautas=10,
                capacidad_minerales=520.77,
                autonomia=203.13
            ),
            Nave(
                patente="N-077",
                material="Grafeno",
                tamano="S",
                capacidad_astronautas=9,
                capacidad_minerales=277.12,
                autonomia=46.15
            ),
            Nave(
                patente="N-100",
                material="Grafeno",
                tamano="L",
                capacidad_astronautas=10,
                capacidad_minerales=1901.83,
                autonomia=203.49
            ),
        ]

        self.assertCountEqual(naves_cargadas, naves_esperadas)

    @timeout(N_SECOND)
    def test_l_naves(self):
        """
        Verifica que los datos carguen bien con un dataset L de Naves.
        """
        path = os.path.join("data", "out_L", "Nave.csv")
        generador = cargar_naves(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 476, 890, -1])
        *naves_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 1000)

        # Revisar posiciones aleatorias
        naves_esperadas = [
            Nave(
                patente="N-001",
                material="Compósito",
                tamano="S",
                capacidad_astronautas=8,
                capacidad_minerales=1753.87,
                autonomia=224.8
            ),
            Nave(
                patente="N-476",
                material="Titanio",
                tamano="M",
                capacidad_astronautas=7,
                capacidad_minerales=660.56,
                autonomia=104.25
            ),
            Nave(
                patente="N-890",
                material="Compósito",
                tamano="M",
                capacidad_astronautas=5,
                capacidad_minerales=818.28,
                autonomia=143.77
            ),
            Nave(
                patente="N-999",
                material="Grafeno",
                tamano="M",
                capacidad_astronautas=10,
                capacidad_minerales=1482.47,
                autonomia=203.57
            ),
        ]

        self.assertCountEqual(naves_cargadas, naves_esperadas)

    @timeout(N_SECOND)
    def test_s_tripulacion(self):
        """
        Verifica que los datos carguen bien con un dataset S de Naves.
        """
        path = os.path.join("data", "out_S", "Tripulacion.csv")
        generador = cargar_tripulaciones(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 8, 116, -1])
        *tripulaciones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 120)

        # Revisar posiciones aleatorias
        tripulaciones_esperadas = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-001",
                id_astronauta=5,
                rango=4
            ),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-002",
                id_astronauta=117,
                rango=3
            ),
            Tripulacion(
                id_equipo=29,
                patente_nave="N-029",
                id_astronauta=57,
                rango=3
            ),
            Tripulacion(
                id_equipo=30,
                patente_nave="N-030",
                id_astronauta=82,
                rango=3
            )
        ]

        self.assertCountEqual(tripulaciones_cargadas, tripulaciones_esperadas)

    @timeout(N_SECOND)
    def test_m_tripulacion(self):
        """
        Verifica que los datos carguen bien con un dataset M de Naves.
        """
        path = os.path.join("data", "out_M", "Tripulacion.csv")
        generador = cargar_tripulaciones(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 192, 265, -1])
        *tripulaciones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 600)

        # Revisar posiciones aleatorias
        tripulaciones_esperadas = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-001",
                id_astronauta=146,
                rango=3
            ),
            Tripulacion(
                id_equipo=32,
                patente_nave="N-032",
                id_astronauta=547,
                rango=2
            ),
            Tripulacion(
                id_equipo=43,
                patente_nave="N-043",
                id_astronauta=364,
                rango=1
            ),
            Tripulacion(
                id_equipo=100,
                patente_nave="N-100",
                id_astronauta=471,
                rango=4
            )
        ]

        self.assertCountEqual(tripulaciones_cargadas, tripulaciones_esperadas)

    @timeout(N_SECOND)
    def test_l_tripulacion(self):
        """
        Verifica que los datos carguen bien con un dataset L de Tripulaciones.
        """
        path = os.path.join("data", "out_L", "Tripulacion.csv")
        generador = cargar_tripulaciones(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 428, 1305, -1])
        *tripulaciones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 2500)

        # Revisar posiciones aleatorias
        tripulaciones_esperadas = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-001",
                id_astronauta=679,
                rango=2
            ),
            Tripulacion(
                id_equipo=530,
                patente_nave="N-530",
                id_astronauta=656,
                rango=2
            ),
            Tripulacion(
                id_equipo=168,
                patente_nave="N-168",
                id_astronauta=2233,
                rango=1
            ),
            Tripulacion(
                id_equipo=999,
                patente_nave="N-999",
                id_astronauta=1434,
                rango=1
            )
        ]

        self.assertCountEqual(tripulaciones_cargadas, tripulaciones_esperadas)

    @timeout(N_SECOND)
    def test_s_planetas(self):
        """
        Verifica que los datos carguen bien con un dataset S de Planetas.
        """
        path = os.path.join("data", "out_S", "Planeta.csv")
        generador = cargar_planetas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 30, 43, -1])
        *planetas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 60)

        # Revisar posiciones aleatorias
        planetas_esperados = [
            Planeta(
                id_planeta=1,
                nombre="P-980",
                coordenada_x=-790763.576,
                coordenada_y=192659.661,
                tamano="M",
                tipo="Plasma"
            ),
            Planeta(
                id_planeta=31,
                nombre="P-646",
                coordenada_x=58279.706,
                coordenada_y=321635.692,
                tamano="S",
                tipo="Sólido"
            ),
            Planeta(
                id_planeta=44,
                nombre="P-141",
                coordenada_x=-719393.698,
                coordenada_y=614474.127,
                tamano="M",
                tipo="Rocoso"
            ),
            Planeta(
                id_planeta=60,
                nombre="P-524",
                coordenada_x=474219.896,
                coordenada_y=-766070.792,
                tamano="S",
                tipo="Gas"
            )
        ]

        self.assertCountEqual(planetas_cargados, planetas_esperados)

    @timeout(N_SECOND)
    def test_m_planetas(self):
        """
        Verifica que los datos carguen bien con un dataset M de Planetas.
        """
        path = os.path.join("data", "out_M", "Planeta.csv")
        generador = cargar_planetas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 173, 228, -1])
        *planetas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 250)

        # Revisar posiciones aleatorias
        planetas_esperados = [
            Planeta(
                id_planeta=1,
                nombre="P-817",
                coordenada_x=983922.799,
                coordenada_y=404971.562,
                tamano="M",
                tipo="Sólido"
            ),
            Planeta(
                id_planeta=174,
                nombre="P-429",
                coordenada_x=-310830.713,
                coordenada_y=190071.174,
                tamano="XL",
                tipo="Plasma"
            ),
            Planeta(
                id_planeta=229,
                nombre="P-908",
                coordenada_x=313801.404,
                coordenada_y=-630285.219,
                tamano="M",
                tipo="Gas"
            ),
            Planeta(
                id_planeta=250,
                nombre="P-634",
                coordenada_x=616780.206,
                coordenada_y=-795370.536,
                tamano="XL",
                tipo="Plasma"
            )
        ]

        self.assertCountEqual(planetas_cargados, planetas_esperados)

    @timeout(N_SECOND)
    def test_l_planetas(self):
        """
        Verifica que los datos carguen bien con un dataset L de Planetaes.
        """
        path = os.path.join("data", "out_L", "Planeta.csv")
        generador = cargar_planetas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 655, 719, -1])
        *planetas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 1200)

        # Revisar posiciones aleatorias
        planetas_esperados = [
            Planeta(
                id_planeta=1,
                nombre="P-376",
                coordenada_x=-253987.708,
                coordenada_y=64615.541,
                tamano="S",
                tipo="Rocoso"
            ),
            Planeta(
                id_planeta=656,
                nombre="P-819",
                coordenada_x=521255.924,
                coordenada_y=817886.846,
                tamano="M",
                tipo="Rocoso"
            ),
            Planeta(
                id_planeta=720,
                nombre="P-746",
                coordenada_x=761802.007,
                coordenada_y=-999346.43,
                tamano="XL",
                tipo="Criogénico"
            ),
            Planeta(
                id_planeta=1200,
                nombre="P-273",
                coordenada_x=-487426.017,
                coordenada_y=-75815.94,
                tamano="XL",
                tipo="Criogénico"
            )
        ]

        self.assertCountEqual(planetas_cargados, planetas_esperados)

    @timeout(N_SECOND)
    def test_s_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset S de minerales.
        """
        path = os.path.join("data", "out_S", "Mineral.csv")
        generador = cargar_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 56, 78, -1])
        *minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 100)

        # Revisar posiciones aleatorias
        minerales_esperados = [
            Mineral(
                id_mineral=1,
                nombre="Min-MDG",
                simbolo_quimico="Cw",
                numero_atomico=66,
                masa_atomica=119.39
            ),
            Mineral(
                id_mineral=57,
                nombre="Min-UHL",
                simbolo_quimico="T",
                numero_atomico=48,
                masa_atomica=100.523
            ),
            Mineral(
                id_mineral=79,
                nombre="Min-VCE",
                simbolo_quimico="Sr",
                numero_atomico=109,
                masa_atomica=207.959
            ),
            Mineral(
                id_mineral=100,
                nombre="Min-SJK",
                simbolo_quimico="K",
                numero_atomico=108,
                masa_atomica=273.76
            )
        ]

        self.assertCountEqual(minerales_cargados, minerales_esperados)

    @timeout(N_SECOND)
    def test_m_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset M de minerales.
        """
        path = os.path.join("data", "out_M", "Mineral.csv")
        generador = cargar_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 137, 198, -1])
        *minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 250)

        # Revisar posiciones aleatorias
        minerales_esperados = [
            Mineral(
                id_mineral=1,
                nombre="Min-RDZ",
                simbolo_quimico="Epy",
                numero_atomico=82,
                masa_atomica=172.54
            ),
            Mineral(
                id_mineral=138,
                nombre="Min-ZAU",
                simbolo_quimico="K",
                numero_atomico=42,
                masa_atomica=104.525
            ),
            Mineral(
                id_mineral=199,
                nombre="Min-WBJ",
                simbolo_quimico="N",
                numero_atomico=47,
                masa_atomica=111.075
            ),
            Mineral(
                id_mineral=250,
                nombre="Min-YAW",
                simbolo_quimico="Vkv",
                numero_atomico=75,
                masa_atomica=163.662
            )
        ]

        self.assertCountEqual(minerales_cargados, minerales_esperados)

    @timeout(N_SECOND)
    def test_l_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset L de Minerales.
        """
        path = os.path.join("data", "out_L", "Mineral.csv")
        generador = cargar_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 796, 1233, -1])
        *minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 2000)

        # Revisar posiciones aleatorias
        minerales_esperados = [
            Mineral(
                id_mineral=1,
                nombre="Min-HVM",
                simbolo_quimico="P",
                numero_atomico=58,
                masa_atomica=119.554
            ),
            Mineral(
                id_mineral=797,
                nombre="Min-XQT",
                simbolo_quimico="Yt",
                numero_atomico=48,
                masa_atomica=115.286
            ),
            Mineral(
                id_mineral=1234,
                nombre="Min-CIN",
                simbolo_quimico="Gg",
                numero_atomico=66,
                masa_atomica=129.473
            ),
            Mineral(
                id_mineral=2000,
                nombre="Min-DFN",
                simbolo_quimico="Epq",
                numero_atomico=53,
                masa_atomica=132.311
            )
        ]

        self.assertCountEqual(minerales_cargados, minerales_esperados)

    @timeout(N_SECOND)
    def test_s_planeta_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset S de PlanetaMineral.
        """
        path = os.path.join("data", "out_S", "PlanetaMineral.csv")
        generador = cargar_planeta_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 54, 74, -1])
        *planeta_minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 223)

        # Revisar posiciones aleatorias
        planeta_minerales_esperados = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=38,
                cantidad_disponible=749775.785,
                pureza=0.884
            ),
            PlanetaMineral(
                id_planeta=13,
                id_mineral=23,
                cantidad_disponible=221774.207,
                pureza=0.673
            ),
            PlanetaMineral(
                id_planeta=17,
                id_mineral=15,
                cantidad_disponible=640058.676,
                pureza=0.642
            ),
            PlanetaMineral(
                id_planeta=60,
                id_mineral=76,
                cantidad_disponible=504040.841,
                pureza=0.717
            )
        ]

        self.assertCountEqual(planeta_minerales_cargados, planeta_minerales_esperados)

    @timeout(N_SECOND)
    def test_m_planeta_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset M de PlanetaMineral.
        """
        path = os.path.join("data", "out_M", "PlanetaMineral.csv")
        generador = cargar_planeta_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 133, 803, -1])
        *planeta_minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 861)

        # Revisar posiciones aleatorias
        planeta_minerales_esperados = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=235,
                cantidad_disponible=41159.413,
                pureza=0.105
            ),
            PlanetaMineral(
                id_planeta=36,
                id_mineral=162,
                cantidad_disponible=57617.755,
                pureza=0.971
            ),
            PlanetaMineral(
                id_planeta=234,
                id_mineral=186,
                cantidad_disponible=340093.316,
                pureza=0.108
            ),
            PlanetaMineral(
                id_planeta=250,
                id_mineral=238,
                cantidad_disponible=754882.189,
                pureza=0.896
            )
        ]

        self.assertCountEqual(planeta_minerales_cargados, planeta_minerales_esperados)

    @timeout(N_SECOND)
    def test_l_planeta_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset L de PlanetaMineral.
        """
        path = os.path.join("data", "out_L", "PlanetaMineral.csv")
        generador = cargar_planeta_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 1384, 3542, -1])
        *planeta_minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 4161)

        # Revisar posiciones aleatorias
        planeta_minerales_esperados = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=849,
                cantidad_disponible=259312.849,
                pureza=0.461
            ),
            PlanetaMineral(
                id_planeta=405,
                id_mineral=408,
                cantidad_disponible=640938.088,
                pureza=0.599
            ),
            PlanetaMineral(
                id_planeta=1021,
                id_mineral=275,
                cantidad_disponible=26655.279,
                pureza=0.661
            ),
            PlanetaMineral(
                id_planeta=1200,
                id_mineral=389,
                cantidad_disponible=633387.839,
                pureza=0.061
            )
        ]

        self.assertCountEqual(planeta_minerales_cargados, planeta_minerales_esperados)

    @timeout(N_SECOND)
    def test_s_misiones(self):
        """
        Verifica que los datos carguen bien con un dataset S de misiones.
        """
        path = os.path.join("data", "out_S", "Mision.csv")
        generador = cargar_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 23, 86, -1])
        *misiones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 150)

        # Revisar posiciones aleatorias
        misiones_esperadas = [
            Mision(
                id_mision=1,
                fecha="2023-11-12",
                hora="20:05",
                id_equipo=15,
                id_planeta=21,
                lograda=False
            ),
            Mision(
                id_mision=24,
                fecha="2023-07-04",
                hora="17:03",
                id_equipo=23,
                id_planeta=22,
                lograda=False
            ),
            Mision(
                id_mision=87,
                fecha="2024-10-20",
                hora="23:31",
                id_equipo=5,
                id_planeta=11,
                lograda=False
            ),
            Mision(
                id_mision=150,
                fecha="2022-11-04",
                hora="12:00",
                id_equipo=8,
                id_planeta=16,
                lograda=True
            )
        ]

        self.assertCountEqual(misiones_cargadas, misiones_esperadas)

    @timeout(N_SECOND)
    def test_m_misiones(self):
        """
        Verifica que los datos carguen bien con un dataset M de misiones.
        """
        path = os.path.join("data", "out_M", "Mision.csv")
        generador = cargar_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 441, 527, -1])
        *misiones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 800)

        # Revisar posiciones aleatorias
        misiones_esperadas = [
            Mision(
                id_mision=1,
                fecha="2025-05-14",
                hora="16:32",
                id_equipo=8,
                id_planeta=98,
                lograda=True
            ),
            Mision(
                id_mision=442,
                fecha="2025-04-28",
                hora="23:47",
                id_equipo=14,
                id_planeta=214,
                lograda=False
            ),
            Mision(
                id_mision=528,
                fecha="2025-09-12",
                hora="08:16",
                id_equipo=56,
                id_planeta=119,
                lograda=True
            ),
            Mision(
                id_mision=800,
                fecha="2025-02-03",
                hora="09:46",
                id_equipo=41,
                id_planeta=117,
                lograda=False
            )
        ]

        self.assertCountEqual(misiones_cargadas, misiones_esperadas)

    @timeout(N_SECOND)
    def test_l_misiones(self):
        """
        Verifica que los datos carguen bien con un dataset L de misiones.
        """
        path = os.path.join("data", "out_L", "Mision.csv")
        generador = cargar_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 623, 2948, -1])
        *misiones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 4000)

        # Revisar posiciones aleatorias
        misiones_esperadas = [
            Mision(
                id_mision=1,
                fecha="2026-06-29",
                hora="00:55",
                id_equipo=339,
                id_planeta=242,
                lograda=None
            ),
            Mision(
                id_mision=624,
                fecha="2023-01-30",
                hora="17:50",
                id_equipo=383,
                id_planeta=257,
                lograda=True
            ),
            Mision(
                id_mision=2949,
                fecha="2026-06-15",
                hora="11:17",
                id_equipo=636,
                id_planeta=966,
                lograda=None
            ),
            Mision(
                id_mision=4000,
                fecha="2022-12-18",
                hora="10:51",
                id_equipo=729,
                id_planeta=757,
                lograda=True
            )
        ]

        self.assertCountEqual(misiones_cargadas, misiones_esperadas)

    @timeout(N_SECOND)
    def test_s_misiones_mineral(self):
        """
        Verifica que los datos carguen bien con un dataset S de misiones_mineral.
        """
        path = os.path.join("data", "out_S", "MisionMineral.csv")
        generador = cargar_materiales_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 179, 247, -1])
        *misiones_mineral_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 307)

        # Revisar posiciones aleatorias
        misiones_mineral_esperadas = [
            MisionMineral(
                id_mision=4,
                id_mineral=1,
                cantidad=123.108
            ),
            MisionMineral(
                id_mision=120,
                id_mineral=58,
                cantidad=2460.185
            ),
            MisionMineral(
                id_mision=51,
                id_mineral=80,
                cantidad=3087.422
            ),
            MisionMineral(
                id_mision=41,
                id_mineral=100,
                cantidad=562.668
            )
        ]

        self.assertCountEqual(misiones_mineral_cargadas, misiones_mineral_esperadas)

    @timeout(N_SECOND)
    def test_m_misiones_mineral(self):
        """
        Verifica que los datos carguen bien con un dataset M de misiones_mineral.
        """
        path = os.path.join("data", "out_M", "MisionMineral.csv")
        generador = cargar_materiales_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 1330, 1378, -1])
        *misiones_mineral_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 1632)

        # Revisar posiciones aleatorias
        misiones_mineral_esperadas = [
            MisionMineral(
                id_mision=86,
                id_mineral=1,
                cantidad=3730.471
            ),
            MisionMineral(
                id_mision=176,
                id_mineral=207,
                cantidad=825.646
            ),
            MisionMineral(
                id_mision=601,
                id_mineral=212,
                cantidad=294.954
            ),
            MisionMineral(
                id_mision=55,
                id_mineral=250,
                cantidad=3660.326
            )
        ]

        self.assertCountEqual(misiones_mineral_cargadas, misiones_mineral_esperadas)

    @timeout(N_SECOND)
    def test_l_misiones_mineral(self):
        """
        Verifica que los datos carguen bien con un dataset L de misiones_mineral.
        """
        path = os.path.join("data", "out_L", "MisionMineral.csv")
        generador = cargar_materiales_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 3472, 5943, -1])
        *misiones_mineral_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 7973)

        # Revisar posiciones aleatorias
        misiones_mineral_esperadas = [
            MisionMineral(
                id_mision=1674,
                id_mineral=1,
                cantidad=2418.79
            ),
            MisionMineral(
                id_mision=3074,
                id_mineral=887,
                cantidad=2673.56
            ),
            MisionMineral(
                id_mision=2405,
                id_mineral=1498,
                cantidad=980.691
            ),
            MisionMineral(
                id_mision=1668,
                id_mineral=1999,
                cantidad=2911.377
            )
        ]

        self.assertCountEqual(misiones_mineral_cargadas, misiones_mineral_esperadas)

import os
import unittest
from collections.abc import Generator
from tests_publicos.utils import indexes_of
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

from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
from utilidades import (
    Astronauta, Nave, Mineral, Mision, MisionMineral, Planeta, PlanetaMineral, Tripulacion)

N_SECOND = FLEXIBILIDAD_ADICIONAL*0.04

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
        path = os.path.join("data_new", "out_new_S", "Astronauta.csv")
        generador = cargar_astronautas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 55, 97, -1])
        *astronautas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 120)

        # Revisar posiciones aleatorias
        astronautas_esperados = [
            Astronauta(
                id_astronauta=1,
                nombre="Adam Bryan",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=56,
                nombre="Adam Wilson",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=98,
                nombre="Elizabeth Mitchell",
                estado="Vacaciones"
            ),
            Astronauta(
                id_astronauta=120,
                nombre="Sierra Flores",
                estado="Vacaciones"
            ),
        ]

        self.assertCountEqual(astronautas_cargados, astronautas_esperados)

    @timeout(N_SECOND)
    def test_m_astronautas(self):
        """
        Verifica que los datos carguen bien con un dataset M de Astronauta.
        """
        path = os.path.join("data_new", "out_new_M", "Astronauta.csv")
        generador = cargar_astronautas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 392, 486, -1])
        *astronautas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 600)

        # Revisar posiciones aleatorias
        astronautas_esperados = [
            Astronauta(
                id_astronauta=1,
                nombre="Cody Williams",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=393,
                nombre="Mary Perez",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=487,
                nombre="Alejandra Riley",
                estado="Jubilado"
            ),
            Astronauta(
                id_astronauta=600,
                nombre="Robert Brown",
                estado="Activo"
            ),
        ]

        self.assertCountEqual(astronautas_cargados, astronautas_esperados)

    @timeout(N_SECOND)
    def test_l_astronautas(self):
        """
        Verifica que los datos carguen bien con un dataset L de Astronauta.
        """
        path = os.path.join("data_new", "out_new_L", "Astronauta.csv")
        generador = cargar_astronautas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 722, 1978, -1])
        *astronautas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 2500)

        # Revisar posiciones aleatorias
        astronautas_esperados = [
            Astronauta(
                id_astronauta=1,
                nombre="Maria Bush",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=723,
                nombre="Joseph Rodgers",
                estado="Jubilado"
            ),
            Astronauta(
                id_astronauta=1979,
                nombre="Matthew Morgan",
                estado="Activo"
            ),
            Astronauta(
                id_astronauta=2500,
                nombre="Tammy Grimes",
                estado="Jubilado"
            ),
        ]

        self.assertCountEqual(astronautas_cargados, astronautas_esperados)

    @timeout(N_SECOND)
    def test_s_naves(self):
        """
        Verifica que los datos carguen bien con un dataset S de Naves.
        """
        path = os.path.join("data_new", "out_new_S", "Nave.csv")
        generador = cargar_naves(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 19, 24, -1])
        *naves_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 30)

        # Revisar posiciones aleatorias
        naves_esperadas = [
            Nave(
                patente="N-001",
                material="Acero Inoxidable",
                tamano="S",
                capacidad_astronautas=6,
                capacidad_minerales=1724.76,
                autonomia=233.63
            ),
            Nave(
                patente="N-020",
                material="Grafeno",
                tamano="S",
                capacidad_astronautas=10,
                capacidad_minerales=1421.87,
                autonomia=45.17
            ),
            Nave(
                patente="N-025",
                material="Titanio",
                tamano="S",
                capacidad_astronautas=9,
                capacidad_minerales=1512.77,
                autonomia=160.75
            ),
            Nave(
                patente="N-030",
                material="Titanio",
                tamano="L",
                capacidad_astronautas=9,
                capacidad_minerales=1403.21,
                autonomia=106.43
            ),
        ]

        self.assertCountEqual(naves_cargadas, naves_esperadas)

    @timeout(N_SECOND)
    def test_m_naves(self):
        """
        Verifica que los datos carguen bien con un dataset M de Naves.
        """
        path = os.path.join("data_new", "out_new_M", "Nave.csv")
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
                material="Acero Inoxidable",
                tamano="S",
                capacidad_astronautas=9,
                capacidad_minerales=1860.53,
                autonomia=122.08
            ),
            Nave(
                patente="N-034",
                material="Titanio",
                tamano="XL",
                capacidad_astronautas=8,
                capacidad_minerales=1702.66,
                autonomia=205.6
            ),
            Nave(
                patente="N-077",
                material="Aluminio",
                tamano="L",
                capacidad_astronautas=6,
                capacidad_minerales=457.33,
                autonomia=137.77
            ),
            Nave(
                patente="N-100",
                material="Aluminio",
                tamano="L",
                capacidad_astronautas=4,
                capacidad_minerales=987.4,
                autonomia=154.61
            ),
        ]

        self.assertCountEqual(naves_cargadas, naves_esperadas)

    @timeout(N_SECOND)
    def test_l_naves(self):
        """
        Verifica que los datos carguen bien con un dataset L de Naves.
        """
        path = os.path.join("data_new", "out_new_L", "Nave.csv")
        generador = cargar_naves(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 476, 891, -1])
        *naves_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 1000)

        # Revisar posiciones aleatorias
        naves_esperadas = [
            Nave(
                patente="N-001",
                material="Titanio",
                tamano="S",
                capacidad_astronautas=3,
                capacidad_minerales=605.35,
                autonomia=77.06
            ),
            Nave(
                patente="N-476",
                material="Acero Inoxidable",
                tamano="L",
                capacidad_astronautas=6,
                capacidad_minerales=934.49,
                autonomia=43.82
            ),
            Nave(
                patente="N-891",
                material="Grafeno",
                tamano="S",
                capacidad_astronautas=3,
                capacidad_minerales=888.28,
                autonomia=78.73
            ),
            Nave(
                patente="N-999",
                material="Compósito",
                tamano="L",
                capacidad_astronautas=10,
                capacidad_minerales=1251.68,
                autonomia=142.33
            ),
        ]

        self.assertCountEqual(naves_cargadas, naves_esperadas)

    @timeout(N_SECOND)
    def test_s_tripulacion(self):
        """
        Verifica que los datos carguen bien con un dataset S de Naves.
        """
        path = os.path.join("data_new", "out_new_S", "Tripulacion.csv")
        generador = cargar_tripulaciones(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 36, 103, -1])
        *tripulaciones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 120)

        # Revisar posiciones aleatorias
        tripulaciones_esperadas = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-001",
                id_astronauta=33,
                rango=5
            ),
            Tripulacion(
                id_equipo=11,
                patente_nave="N-011",
                id_astronauta=9,
                rango=2
            ),
            Tripulacion(
                id_equipo=26,
                patente_nave="N-026",
                id_astronauta=116,
                rango=2
            ),
            Tripulacion(
                id_equipo=30,
                patente_nave="N-030",
                id_astronauta=55,
                rango=2
            )
        ]

        self.assertCountEqual(tripulaciones_cargadas, tripulaciones_esperadas)

    @timeout(N_SECOND)
    def test_m_tripulacion(self):
        """
        Verifica que los datos carguen bien con un dataset M de Naves.
        """
        path = os.path.join("data_new", "out_new_M", "Tripulacion.csv")
        generador = cargar_tripulaciones(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 122, 463, -1])
        *tripulaciones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 600)

        # Revisar posiciones aleatorias
        tripulaciones_esperadas = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-001",
                id_astronauta=124,
                rango=3
            ),
            Tripulacion(
                id_equipo=23,
                patente_nave="N-023",
                id_astronauta=266,
                rango=1
            ),
            Tripulacion(
                id_equipo=79,
                patente_nave="N-079",
                id_astronauta=192,
                rango=2
            ),
            Tripulacion(
                id_equipo=100,
                patente_nave="N-100",
                id_astronauta=303,
                rango=5
            )
        ]

        self.assertCountEqual(tripulaciones_cargadas, tripulaciones_esperadas)

    @timeout(N_SECOND)
    def test_l_tripulacion(self):
        """
        Verifica que los datos carguen bien con un dataset L de Tripulaciones.
        """
        path = os.path.join("data_new", "out_new_L", "Tripulacion.csv")
        generador = cargar_tripulaciones(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 892, 1467, -1])
        *tripulaciones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 2500)

        # Revisar posiciones aleatorias
        tripulaciones_esperadas = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-001",
                id_astronauta=537,
                rango=5
            ),
            Tripulacion(
                id_equipo=371,
                patente_nave="N-371",
                id_astronauta=428,
                rango=4
            ),
            Tripulacion(
                id_equipo=600,
                patente_nave="N-600",
                id_astronauta=1305,
                rango=2
            ),
            Tripulacion(
                id_equipo=999,
                patente_nave="N-999",
                id_astronauta=1752,
                rango=1
            )
        ]

        self.assertCountEqual(tripulaciones_cargadas, tripulaciones_esperadas)

    @timeout(N_SECOND)
    def test_s_planetas(self):
        """
        Verifica que los datos carguen bien con un dataset S de Planetas.
        """
        path = os.path.join("data_new", "out_new_S", "Planeta.csv")
        generador = cargar_planetas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 24, 55, -1])
        *planetas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 60)

        # Revisar posiciones aleatorias
        planetas_esperados = [
            Planeta(
                id_planeta=1,
                nombre="P-501",
                coordenada_x=-957152.06,
                coordenada_y=-757877.386,
                tamano="XL",
                tipo="Plasma"
            ),
            Planeta(
                id_planeta=25,
                nombre="P-528",
                coordenada_x=-29225.826,
                coordenada_y=-789718.189,
                tamano="XL",
                tipo="Líquido"
            ),
            Planeta(
                id_planeta=56,
                nombre="P-328",
                coordenada_x=372257.542,
                coordenada_y=-515244.874,
                tamano="L",
                tipo="Plasma"
            ),
            Planeta(
                id_planeta=60,
                nombre="P-699",
                coordenada_x=704498.226,
                coordenada_y=-999608.216,
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
        path = os.path.join("data_new", "out_new_M", "Planeta.csv")
        generador = cargar_planetas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 123, 200, -1])
        *planetas_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 250)

        # Revisar posiciones aleatorias
        planetas_esperados = [
            Planeta(
                id_planeta=1,
                nombre="P-418",
                coordenada_x=356898.635,
                coordenada_y=-802300.624,
                tamano="M",
                tipo="Gas"
            ),
            Planeta(
                id_planeta=124,
                nombre="P-991",
                coordenada_x=20591.982,
                coordenada_y=-694517.066,
                tamano="S",
                tipo="Sólido"
            ),
            Planeta(
                id_planeta=201,
                nombre="P-127",
                coordenada_x=-626312.781,
                coordenada_y=-326322.451,
                tamano="S",
                tipo="Gas"
            ),
            Planeta(
                id_planeta=250,
                nombre="P-857",
                coordenada_x=-326625.272,
                coordenada_y=561326.526,
                tamano="M",
                tipo="Plasma"
            )
        ]

        self.assertCountEqual(planetas_cargados, planetas_esperados)

    @timeout(N_SECOND)
    def test_l_planetas(self):
        """
        Verifica que los datos carguen bien con un dataset L de Planetaes.
        """
        path = os.path.join("data_new", "out_new_L", "Planeta.csv")
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
                nombre="P-824",
                coordenada_x=566960.859,
                coordenada_y=326000.337,
                tamano="XL",
                tipo="Gas"
            ),
            Planeta(
                id_planeta=656,
                nombre="P-846",
                coordenada_x=510929.818,
                coordenada_y=757449.771,
                tamano="M",
                tipo="Sólido"
            ),
            Planeta(
                id_planeta=720,
                nombre="P-936",
                coordenada_x=76594.609,
                coordenada_y=-952841.616,
                tamano="XL",
                tipo="Líquido"
            ),
            Planeta(
                id_planeta=1200,
                nombre="P-477",
                coordenada_x=-660998.401,
                coordenada_y=-594175.34,
                tamano="XL",
                tipo="Sólido"
            )
        ]

        self.assertCountEqual(planetas_cargados, planetas_esperados)

    @timeout(N_SECOND)
    def test_s_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset S de minerales.
        """
        path = os.path.join("data_new", "out_new_S", "Mineral.csv")
        generador = cargar_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 44, 54, -1])
        *minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 100)

        # Revisar posiciones aleatorias
        minerales_esperados = [
            Mineral(
                id_mineral=1,
                nombre="Min-MQU",
                simbolo_quimico="G",
                numero_atomico=87,
                masa_atomica=201.926
            ),
            Mineral(
                id_mineral=45,
                nombre="Min-GND",
                simbolo_quimico="N",
                numero_atomico=97,
                masa_atomica=235.639
            ),
            Mineral(
                id_mineral=55,
                nombre="Min-PCF",
                simbolo_quimico="Tg",
                numero_atomico=112,
                masa_atomica=257.251
            ),
            Mineral(
                id_mineral=100,
                nombre="Min-HUY",
                simbolo_quimico="Z",
                numero_atomico=86,
                masa_atomica=189.642
            )
        ]

        self.assertCountEqual(minerales_cargados, minerales_esperados)

    @timeout(N_SECOND)
    def test_m_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset M de minerales.
        """
        path = os.path.join("data_new", "out_new_M", "Mineral.csv")
        generador = cargar_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 100, 189, -1])
        *minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 250)

        # Revisar posiciones aleatorias
        minerales_esperados = [
            Mineral(
                id_mineral=1,
                nombre="Min-ZZU",
                simbolo_quimico="X",
                numero_atomico=113,
                masa_atomica=251.179
            ),
            Mineral(
                id_mineral=101,
                nombre="Min-ILE",
                simbolo_quimico="Vm",
                numero_atomico=26,
                masa_atomica=56.426
            ),
            Mineral(
                id_mineral=190,
                nombre="Min-TAT",
                simbolo_quimico="Al",
                numero_atomico=56,
                masa_atomica=105.879
            ),
            Mineral(
                id_mineral=250,
                nombre="Min-RBZ",
                simbolo_quimico="T",
                numero_atomico=105,
                masa_atomica=209.691
            )
        ]

        self.assertCountEqual(minerales_cargados, minerales_esperados)

    @timeout(N_SECOND)
    def test_l_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset L de Minerales.
        """
        path = os.path.join("data_new", "out_new_L", "Mineral.csv")
        generador = cargar_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 544, 1340, -1])
        *minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 2000)

        # Revisar posiciones aleatorias
        minerales_esperados = [
            Mineral(
                id_mineral=1,
                nombre="Min-DEF",
                simbolo_quimico="Nf",
                numero_atomico=66,
                masa_atomica=133.616
            ),
            Mineral(
                id_mineral=545,
                nombre="Min-HUQ",
                simbolo_quimico="J",
                numero_atomico=17,
                masa_atomica=35.814
            ),
            Mineral(
                id_mineral=1341,
                nombre="Min-RUP",
                simbolo_quimico="Hm",
                numero_atomico=14,
                masa_atomica=31.76
            ),
            Mineral(
                id_mineral=2000,
                nombre="Min-HYS",
                simbolo_quimico="Cfx",
                numero_atomico=107,
                masa_atomica=198.833
            )
        ]

        self.assertCountEqual(minerales_cargados, minerales_esperados)

    @timeout(N_SECOND)
    def test_s_planeta_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset S de PlanetaMineral.
        """
        path = os.path.join("data_new", "out_new_S", "PlanetaMineral.csv")
        generador = cargar_planeta_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 75, 139, -1])
        *planeta_minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 189)

        # Revisar posiciones aleatorias
        planeta_minerales_esperados = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=54,
                cantidad_disponible=630994.228,
                pureza=0.41
            ),
            PlanetaMineral(
                id_planeta=23,
                id_mineral=41,
                cantidad_disponible=968898.757,
                pureza=0.589
            ),
            PlanetaMineral(
                id_planeta=45,
                id_mineral=64,
                cantidad_disponible=678275.401,
                pureza=0.475
            ),
            PlanetaMineral(
                id_planeta=60,
                id_mineral=9,
                cantidad_disponible=332204.033,
                pureza=0.905
            )
        ]

        self.assertCountEqual(planeta_minerales_cargados, planeta_minerales_esperados)

    @timeout(N_SECOND)
    def test_m_planeta_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset M de PlanetaMineral.
        """
        path = os.path.join("data_new", "out_new_M", "PlanetaMineral.csv")
        generador = cargar_planeta_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 158, 755, -1])
        *planeta_minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 853)

        # Revisar posiciones aleatorias
        planeta_minerales_esperados = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=213,
                cantidad_disponible=346239.004,
                pureza=0.52
            ),
            PlanetaMineral(
                id_planeta=47,
                id_mineral=58,
                cantidad_disponible=777342.287,
                pureza=0.494
            ),
            PlanetaMineral(
                id_planeta=221,
                id_mineral=127,
                cantidad_disponible=83194.37,
                pureza=0.174
            ),
            PlanetaMineral(
                id_planeta=250,
                id_mineral=185,
                cantidad_disponible=184838.729,
                pureza=0.87
            )
        ]

        self.assertCountEqual(planeta_minerales_cargados, planeta_minerales_esperados)

    @timeout(N_SECOND)
    def test_l_planeta_minerales(self):
        """
        Verifica que los datos carguen bien con un dataset L de PlanetaMineral.
        """
        path = os.path.join("data_new", "out_new_L", "PlanetaMineral.csv")
        generador = cargar_planeta_minerales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 1385, 3793, -1])
        *planeta_minerales_cargados, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 4169)

        # Revisar posiciones aleatorias
        planeta_minerales_esperados = [
            PlanetaMineral(
                id_planeta=1,
                id_mineral=1903,
                cantidad_disponible=515397.437,
                pureza=0.626
            ),
            PlanetaMineral(
                id_planeta=404,
                id_mineral=9,
                cantidad_disponible=257559.594,
                pureza=0.102
            ),
            PlanetaMineral(
                id_planeta=1095,
                id_mineral=1564,
                cantidad_disponible=856785.104,
                pureza=0.606
            ),
            PlanetaMineral(
                id_planeta=1200,
                id_mineral=222,
                cantidad_disponible=563487.246,
                pureza=0.353
            )
        ]

        self.assertCountEqual(planeta_minerales_cargados, planeta_minerales_esperados)

    @timeout(N_SECOND)
    def test_s_misiones(self):
        """
        Verifica que los datos carguen bien con un dataset S de misiones.
        """
        path = os.path.join("data_new", "out_new_S", "Mision.csv")
        generador = cargar_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 5, 60, -1])
        *misiones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 150)

        # Revisar posiciones aleatorias
        misiones_esperadas = [
            Mision(
                id_mision=1,
                fecha="2023-11-02",
                hora="12:52",
                id_equipo=26,
                id_planeta=12,
                lograda=False
            ),
            Mision(
                id_mision=6,
                fecha="2022-10-27",
                hora="16:48",
                id_equipo=15,
                id_planeta=55,
                lograda=True
            ),
            Mision(
                id_mision=61,
                fecha="2024-06-23",
                hora="00:40",
                id_equipo=18,
                id_planeta=51,
                lograda=True
            ),
            Mision(
                id_mision=150,
                fecha="2024-01-22",
                hora="21:00",
                id_equipo=27,
                id_planeta=19,
                lograda=True
            )
        ]

        self.assertCountEqual(misiones_cargadas, misiones_esperadas)

    @timeout(N_SECOND)
    def test_m_misiones(self):
        """
        Verifica que los datos carguen bien con un dataset M de misiones.
        """
        path = os.path.join("data_new", "out_new_M", "Mision.csv")
        generador = cargar_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 538, 764, -1])
        *misiones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 800)

        # Revisar posiciones aleatorias
        misiones_esperadas = [
            Mision(
                id_mision=1,
                fecha="2024-09-02",
                hora="12:11",
                id_equipo=28,
                id_planeta=15,
                lograda=True
            ),
            Mision(
                id_mision=539,
                fecha="2024-03-17",
                hora="02:00",
                id_equipo=68,
                id_planeta=143,
                lograda=True
            ),
            Mision(
                id_mision=765,
                fecha="2026-02-16",
                hora="23:26",
                id_equipo=78,
                id_planeta=143,
                lograda=None
            ),
            Mision(
                id_mision=800,
                fecha="2024-09-10",
                hora="10:19",
                id_equipo=15,
                id_planeta=185,
                lograda=False
            )
        ]

        self.assertCountEqual(misiones_cargadas, misiones_esperadas)

    @timeout(N_SECOND)
    def test_l_misiones(self):
        """
        Verifica que los datos carguen bien con un dataset L de misiones.
        """
        path = os.path.join("data_new", "out_new_L", "Mision.csv")
        generador = cargar_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 9, 3998, -1])
        *misiones_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 4000)

        # Revisar posiciones aleatorias
        misiones_esperadas = [
            Mision(
                id_mision=1,
                fecha="2025-05-17",
                hora="12:18",
                id_equipo=995,
                id_planeta=6,
                lograda=False
            ),
            Mision(
                id_mision=10,
                fecha="2025-07-02",
                hora="21:05",
                id_equipo=40,
                id_planeta=567,
                lograda=True
            ),
            Mision(
                id_mision=3999,
                fecha="2025-10-02",
                hora="08:28",
                id_equipo=446,
                id_planeta=301,
                lograda=True
            ),
            Mision(
                id_mision=4000,
                fecha="2026-02-05",
                hora="11:38",
                id_equipo=90,
                id_planeta=898,
                lograda=None
            )
        ]

        self.assertCountEqual(misiones_cargadas, misiones_esperadas)

    @timeout(N_SECOND)
    def test_s_misiones_mineral(self):
        """
        Verifica que los datos carguen bien con un dataset S de misiones_mineral.
        """
        path = os.path.join("data_new", "out_new_S", "MisionMineral.csv")
        generador = cargar_materiales_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 69, 225, -1])
        *misiones_mineral_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 293)

        # Revisar posiciones aleatorias
        misiones_mineral_esperadas = [
            MisionMineral(
                id_mision=82,
                id_mineral=1,
                cantidad=2858.807
            ),
            MisionMineral(
                id_mision=137,
                id_mineral=24,
                cantidad=4628.776
            ),
            MisionMineral(
                id_mision=64,
                id_mineral=78,
                cantidad=3201.398
            ),
            MisionMineral(
                id_mision=53,
                id_mineral=100,
                cantidad=421.102
            )
        ]

        self.assertCountEqual(misiones_mineral_cargadas, misiones_mineral_esperadas)

    @timeout(N_SECOND)
    def test_m_misiones_mineral(self):
        """
        Verifica que los datos carguen bien con un dataset M de misiones_mineral.
        """
        path = os.path.join("data_new", "out_new_M", "MisionMineral.csv")
        generador = cargar_materiales_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 224, 599, -1])
        *misiones_mineral_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 1586)

        # Revisar posiciones aleatorias
        misiones_mineral_esperadas = [
            MisionMineral(
                id_mision=399,
                id_mineral=1,
                cantidad=4494.111
            ),
            MisionMineral(
                id_mision=746,
                id_mineral=36,
                cantidad=3001.287
            ),
            MisionMineral(
                id_mision=678,
                id_mineral=89,
                cantidad=4063.586
            ),
            MisionMineral(
                id_mision=710,
                id_mineral=250,
                cantidad=4549.063
            )
        ]

        self.assertCountEqual(misiones_mineral_cargadas, misiones_mineral_esperadas)

    @timeout(N_SECOND)
    def test_l_misiones_mineral(self):
        """
        Verifica que los datos carguen bien con un dataset L de misiones_mineral.
        """
        path = os.path.join("data_new", "out_new_L", "MisionMineral.csv")
        generador = cargar_materiales_mision(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Generator)

        generador_data = indexes_of(generador, [0, 5000, 7486, -1])
        *misiones_mineral_cargadas, largo = generador_data

        # Revisar largo
        self.assertEqual(largo, 7965)

        # Revisar posiciones aleatorias
        misiones_mineral_esperadas = [
            MisionMineral(
                id_mision=1026,
                id_mineral=1,
                cantidad=1489.568
            ),
            MisionMineral(
                id_mision=2685,
                id_mineral=1251,
                cantidad=3555.6
            ),
            MisionMineral(
                id_mision=3746,
                id_mineral=1875,
                cantidad=4424.355
            ),
            MisionMineral(
                id_mision=2664,
                id_mineral=2000,
                cantidad=2199.786
            )
        ]

        self.assertCountEqual(misiones_mineral_cargadas, misiones_mineral_esperadas)

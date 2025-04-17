import unittest
import os
import sys
from dccortaramas import Bonsai, DCCortaRamas
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 20

dccortaramas = DCCortaRamas()


class TestEsSimetrico(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_asimetrico_simple(self):
        """
        Bonsai de simple asimetrico
        """
        estructura_inicial = [
            ["1", True, False, ["0", "2"]],
            ["2", False, False, ["4", "5"]],
            ["3", False, False, ["0", "0"]],
            ["5", False, False, ["3", "0"]],
            ["4", False, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["0", "2"]],
            ["2", False, False, ["4", "5"]],
            ["3", False, False, ["0", "0"]],
            ["5", False, False, ["3", "0"]],
            ["4", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Aromo", 20, 25, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_simetrico_simple(self):
        """
        Bonsai de simple que cumple la simetría
        """
        estructura_inicial = [
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["4", "5"]],
            ["3", False, False, ["6", "7"]],
            ["5", False, False, ["0", "0"]],
            ["4", False, False, ["0", "0"]],
            ["6", False, False, ["0", "0"]],
            ["7", False, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["4", "5"]],
            ["3", False, False, ["6", "7"]],
            ["5", False, False, ["0", "0"]],
            ["4", False, False, ["0", "0"]],
            ["6", False, False, ["0", "0"]],
            ["7", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Quillay yalliuQ", 20, 25, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = True

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_asimetrico_medio(self):
        """
        Bonsai de 7 nodos asimetrico
        """

        estructura_inicial = [
            ["1", True, False, ["0", "2"]],
            ["2", False, False, ["0", "3"]],
            ["3", False, False, ["4", "5"]],
            ["5", False, False, ["0", "7"]],
            ["4", False, False, ["6", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", False, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["0", "2"]],
            ["2", False, False, ["0", "3"]],
            ["3", False, False, ["4", "5"]],
            ["5", False, False, ["0", "7"]],
            ["4", False, False, ["6", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Liquidambar", 20, 50, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_03_bonsai_asimetrico_medio(self):
        """
        Bonsai de 16 nodos asimetrico por flores y nodos
        """
        estructura_inicial = [
            ["1", True, False, ["2", "16"]],
            ["2", True, True, ["0", "4"]],
            ["3", True, True, ["9", "10"]],
            ["4", False, False, ["0", "0"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, False, ["7", "8"]],
            ["7", True, True, ["0", "0"]],
            ["8", False, False, ["13", "14"]],
            ["9", False, True, ["12", "11"]],
            ["10", True, False, ["0", "0"]],
            ["11", True, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "15"]],
            ["14", True, False, ["0", "0"]],
            ["15", True, True, ["0", "0"]],
            ["16", False, True, ["5", "6"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "16"]],
            ["2", True, True, ["0", "4"]],
            ["3", True, True, ["9", "10"]],
            ["4", False, False, ["0", "0"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, False, ["7", "8"]],
            ["7", True, True, ["0", "0"]],
            ["8", False, False, ["13", "14"]],
            ["9", False, True, ["12", "11"]],
            ["10", True, False, ["0", "0"]],
            ["11", True, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "15"]],
            ["14", True, False, ["0", "0"]],
            ["15", True, True, ["0", "0"]],
            ["16", False, True, ["5", "6"]]
        ]

        bonsai = Bonsai("Maiten", 4, 52, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_asimetrico_medio(self):
        """
        Bonsai de 15 nodos asimetrico
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", False, False, ["0", "10"]],
            ["5", False, True, ["9", "0"]],
            ["6", True, False, ["8", "0"]],
            ["7", True, True, ["0", "11"]],
            ["8", False, False, ["14", "15"]],
            ["9", False, True, ["12", "13"]],
            ["10", True, False, ["0", "0"]],
            ["11", True, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "0"]],
            ["14", True, False, ["0", "0"]],
            ["15", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", False, False, ["0", "10"]],
            ["5", False, True, ["9", "0"]],
            ["6", True, False, ["8", "0"]],
            ["7", True, True, ["0", "11"]],
            ["8", False, False, ["14", "15"]],
            ["9", False, True, ["12", "13"]],
            ["10", True, False, ["0", "0"]],
            ["11", True, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "0"]],
            ["14", True, False, ["0", "0"]],
            ["15", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Alerce", 43, 1, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_05_bonsai_simetrico_medio(self):
        """
        Bonsai mediano simetrico
        """

        estructura_inicial = [
            ["1", False, True, ["2", "3"]],
            ["2", True, False, ["0", "4"]],
            ["3", True, False, ["5", "0"]],
            ["4", False, True, ["6", "0"]],
            ["5", False, True, ["0", "7"]],
            ["6", False, True, ["8", "9"]],
            ["7", False, False, ["10", "11"]],
            ["8", True, True, ["12", "13"]],
            ["9", True, True, ["14", "15"]],
            ["10", True, True, ["16", "17"]],
            ["11", True, True, ["18", "19"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "0"]],
            ["14", False, False, ["0", "0"]],
            ["15", True, False, ["0", "0"]],
            ["16", True, True, ["0", "0"]],
            ["17", False, True, ["0", "0"]],
            ["18", True, False, ["0", "0"]],
            ["19", False, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", False, True, ["2", "3"]],
            ["2", True, False, ["0", "4"]],
            ["3", True, False, ["5", "0"]],
            ["4", False, True, ["6", "0"]],
            ["5", False, True, ["0", "7"]],
            ["6", False, True, ["8", "9"]],
            ["7", False, False, ["10", "11"]],
            ["8", True, True, ["12", "13"]],
            ["9", True, True, ["14", "15"]],
            ["10", True, True, ["16", "17"]],
            ["11", True, True, ["18", "19"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "0"]],
            ["14", False, False, ["0", "0"]],
            ["15", True, False, ["0", "0"]],
            ["16", True, True, ["0", "0"]],
            ["17", False, True, ["0", "0"]],
            ["18", True, False, ["0", "0"]],
            ["19", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("ABBA", 101, 101, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = True

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_06_bonsai_simetrico_grande(self):
        """
        Bonsai grande simetrico
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["0", "8"]],
            ["5", True, True, ["9", "0"]],
            ["6", True, True, ["0", "10"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, False, ["0", "0"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, False, ["26", "27"]],
            ["12", True, False, ["14", "15"]],
            ["13", True, False, ["16", "17"]],
            ["14", True, True, ["18", "19"]],
            ["15", True, False, ["20", "21"]],
            ["16", False, False, ["22", "23"]],
            ["17", False, True, ["24", "25"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]],
            ["25", False, True, ["0", "40"]],
            ["26", True, True, ["28", "29"]],
            ["27", True, False, ["30", "31"]],
            ["28", False, False, ["32", "33"]],
            ["29", False, True, ["34", "35"]],
            ["30", True, True, ["36", "37"]],
            ["31", True, False, ["38", "39"]],
            ["32", False, True, ["41", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", True, False, ["0", "0"]],
            ["35", True, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", True, False, ["0", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["42", "43"]],
            ["41", True, True, ["44", "45"]],
            ["42", True, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["0", "8"]],
            ["5", True, True, ["9", "0"]],
            ["6", True, True, ["0", "10"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, False, ["0", "0"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, False, ["26", "27"]],
            ["12", True, False, ["14", "15"]],
            ["13", True, False, ["16", "17"]],
            ["14", True, True, ["18", "19"]],
            ["15", True, False, ["20", "21"]],
            ["16", False, False, ["22", "23"]],
            ["17", False, True, ["24", "25"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]],
            ["25", False, True, ["0", "40"]],
            ["26", True, True, ["28", "29"]],
            ["27", True, False, ["30", "31"]],
            ["28", False, False, ["32", "33"]],
            ["29", False, True, ["34", "35"]],
            ["30", True, True, ["36", "37"]],
            ["31", True, False, ["38", "39"]],
            ["32", False, True, ["41", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", True, False, ["0", "0"]],
            ["35", True, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", True, False, ["0", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["42", "43"]],
            ["41", True, True, ["44", "45"]],
            ["42", True, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Tangananica", 238, 57, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = True

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_asimetrico_grande(self):
        """
        Bonsai de 49 nodos asimetrico por una flor
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["0", "8"]],
            ["5", True, True, ["9", "0"]],
            ["6", True, True, ["0", "10"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, False, ["0", "0"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, False, ["26", "27"]],
            ["12", True, False, ["14", "15"]],
            ["13", True, False, ["16", "17"]],
            ["14", True, True, ["18", "19"]],
            ["15", True, False, ["20", "21"]],
            ["16", False, False, ["22", "23"]],
            ["17", False, True, ["24", "25"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", False, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]],
            ["25", False, True, ["0", "40"]],
            ["26", True, True, ["28", "29"]],
            ["27", True, False, ["30", "31"]],
            ["28", False, False, ["32", "33"]],
            ["29", False, True, ["34", "35"]],
            ["30", True, True, ["36", "37"]],
            ["31", True, False, ["38", "39"]],
            ["32", False, True, ["41", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", True, False, ["0", "0"]],
            ["35", True, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", True, False, ["0", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["42", "43"]],
            ["41", True, True, ["44", "45"]],
            ["42", True, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["0", "8"]],
            ["5", True, True, ["9", "0"]],
            ["6", True, True, ["0", "10"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, False, ["0", "0"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, False, ["26", "27"]],
            ["12", True, False, ["14", "15"]],
            ["13", True, False, ["16", "17"]],
            ["14", True, True, ["18", "19"]],
            ["15", True, False, ["20", "21"]],
            ["16", False, False, ["22", "23"]],
            ["17", False, True, ["24", "25"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", False, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]],
            ["25", False, True, ["0", "40"]],
            ["26", True, True, ["28", "29"]],
            ["27", True, False, ["30", "31"]],
            ["28", False, False, ["32", "33"]],
            ["29", False, True, ["34", "35"]],
            ["30", True, True, ["36", "37"]],
            ["31", True, False, ["38", "39"]],
            ["32", False, True, ["41", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", True, False, ["0", "0"]],
            ["35", True, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", True, False, ["0", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["42", "43"]],
            ["41", True, True, ["44", "45"]],
            ["42", True, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Otto", 69, 69, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_08_bonsai_asimetrico_grande_2(self):
        """
        Bonsai de 49 nodos asimetrico aleatorio
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["52", "4"]],
            ["3", True, False, ["29", "55"]],
            ["4", True, False, ["5", "6"]],
            ["5", False, True, ["7", "0"]],
            ["6", True, True, ["0", "0"]],
            ["7", False, True, ["8", "10"]],
            ["8", True, False, ["0", "9"]],
            ["9", False, False, ["0", "0"]],
            ["10", True, True, ["11", "12"]],
            ["11", False, False, ["0", "0"]],
            ["12", True, False, ["13", "14"]],
            ["13", True, False, ["0", "0"]],
            ["14", False, True, ["15", "16"]],
            ["15", True, False, ["17", "18"]],
            ["16", True, False, ["19", "20"]],
            ["17", False, True, ["21", "22"]],
            ["18", False, True, ["23", "24"]],
            ["19", True, False, ["25", "26"]],
            ["20", True, False, ["27", "28"]],
            ["21", False, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", False, True, ["0", "0"]],
            ["24", True, False, ["0", "0"]],
            ["25", False, True, ["0", "0"]],
            ["26", True, True, ["0", "0"]],
            ["27", False, False, ["0", "0"]],
            ["28", True, False, ["0", "0"]],
            ["29", True, True, ["30", "0"]],
            ["30", False, True, ["0", "31"]],
            ["31", True, False, ["32", "0"]],
            ["32", False, True, ["0", "33"]],
            ["33", False, True, ["34", "35"]],
            ["34", True, False, ["36", "37"]],
            ["35", True, True, ["38", "39"]],
            ["36", True, False, ["40", "41"]],
            ["37", False, True, ["42", "43"]],
            ["38", True, False, ["44", "45"]],
            ["39", True, False, ["46", "47"]],
            ["40", True, False, ["0", "0"]],
            ["41", False, True, ["0", "0"]],
            ["42", True, True, ["0", "0"]],
            ["43", False, False, ["0", "48"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", False, False, ["0", "49"]],
            ["49", True, False, ["51", "50"]],
            ["50", False, True, ["0", "0"]],
            ["51", True, False, ["0", "0"]],
            ["52", False, False, ["54", "53"]],
            ["53", False, False, ["0", "48"]],
            ["54", True, False, ["0", "0"]],
            ["55", True, True, ["0", "56"]],
            ["56", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["52", "4"]],
            ["3", True, False, ["29", "55"]],
            ["4", True, False, ["5", "6"]],
            ["5", False, True, ["7", "0"]],
            ["6", True, True, ["0", "0"]],
            ["7", False, True, ["8", "10"]],
            ["8", True, False, ["0", "9"]],
            ["9", False, False, ["0", "0"]],
            ["10", True, True, ["11", "12"]],
            ["11", False, False, ["0", "0"]],
            ["12", True, False, ["13", "14"]],
            ["13", True, False, ["0", "0"]],
            ["14", False, True, ["15", "16"]],
            ["15", True, False, ["17", "18"]],
            ["16", True, False, ["19", "20"]],
            ["17", False, True, ["21", "22"]],
            ["18", False, True, ["23", "24"]],
            ["19", True, False, ["25", "26"]],
            ["20", True, False, ["27", "28"]],
            ["21", False, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", False, True, ["0", "0"]],
            ["24", True, False, ["0", "0"]],
            ["25", False, True, ["0", "0"]],
            ["26", True, True, ["0", "0"]],
            ["27", False, False, ["0", "0"]],
            ["28", True, False, ["0", "0"]],
            ["29", True, True, ["30", "0"]],
            ["30", False, True, ["0", "31"]],
            ["31", True, False, ["32", "0"]],
            ["32", False, True, ["0", "33"]],
            ["33", False, True, ["34", "35"]],
            ["34", True, False, ["36", "37"]],
            ["35", True, True, ["38", "39"]],
            ["36", True, False, ["40", "41"]],
            ["37", False, True, ["42", "43"]],
            ["38", True, False, ["44", "45"]],
            ["39", True, False, ["46", "47"]],
            ["40", True, False, ["0", "0"]],
            ["41", False, True, ["0", "0"]],
            ["42", True, True, ["0", "0"]],
            ["43", False, False, ["0", "48"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", False, False, ["0", "49"]],
            ["49", True, False, ["51", "50"]],
            ["50", False, True, ["0", "0"]],
            ["51", True, False, ["0", "0"]],
            ["52", False, False, ["54", "53"]],
            ["53", False, False, ["0", "48"]],
            ["54", True, False, ["0", "0"]],
            ["55", True, True, ["0", "56"]],
            ["56", False, True, ["0", "0"]]
        ]

        bonsai = Bonsai(":(", 34, 65, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_09_asimetrico_grande(self):
        """
        Bonsai casi simetrico, con un nodo de mas y una flor menos
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["0", "8"]],
            ["5", True, True, ["9", "0"]],
            ["6", True, True, ["0", "10"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, False, ["0", "0"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, False, ["26", "27"]],
            ["12", True, False, ["14", "15"]],
            ["13", True, False, ["16", "17"]],
            ["14", True, True, ["18", "19"]],
            ["15", True, False, ["20", "21"]],
            ["16", False, False, ["22", "23"]],
            ["17", False, True, ["24", "25"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]],
            ["25", False, True, ["0", "40"]],
            ["26", True, True, ["28", "29"]],
            ["27", True, False, ["30", "31"]],
            ["28", False, False, ["32", "33"]],
            ["29", False, True, ["34", "35"]],
            ["30", True, True, ["36", "37"]],
            ["31", True, False, ["38", "39"]],
            ["32", False, True, ["41", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", True, False, ["0", "0"]],
            ["35", True, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", True, False, ["50", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["42", "43"]],
            ["41", True, True, ["44", "45"]],
            ["42", True, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", False, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["0", "0"]],
            ["50", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["0", "8"]],
            ["5", True, True, ["9", "0"]],
            ["6", True, True, ["0", "10"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, False, ["0", "0"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, False, ["26", "27"]],
            ["12", True, False, ["14", "15"]],
            ["13", True, False, ["16", "17"]],
            ["14", True, True, ["18", "19"]],
            ["15", True, False, ["20", "21"]],
            ["16", False, False, ["22", "23"]],
            ["17", False, True, ["24", "25"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]],
            ["25", False, True, ["0", "40"]],
            ["26", True, True, ["28", "29"]],
            ["27", True, False, ["30", "31"]],
            ["28", False, False, ["32", "33"]],
            ["29", False, True, ["34", "35"]],
            ["30", True, True, ["36", "37"]],
            ["31", True, False, ["38", "39"]],
            ["32", False, True, ["41", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", True, False, ["0", "0"]],
            ["35", True, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", True, False, ["50", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["42", "43"]],
            ["41", True, True, ["44", "45"]],
            ["42", True, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", False, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["0", "0"]],
            ["50", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Mateo", 20, 14, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

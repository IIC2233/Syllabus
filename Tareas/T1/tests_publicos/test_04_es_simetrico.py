import unittest
import os
import sys
from dccortaramas import Bonsai, DCCortaRamas
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 20

dccortaramas = DCCortaRamas()


class TestEsSimetrico(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_simetrico_unico(self):
        """
        Bonsai de simple que cumple la simetría
        """
        estructura_inicial = [
            ["1", True, False, ["0", "0"]],
        ]

        estructura_final = [
            ["1", True, False, ["0", "0"]],
        ]

        bonsai = Bonsai("Ana", 20, 25, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = True

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_simetrico_simple(self):
        """
        Bonsai de simple que cumple la simetría
        """
        estructura_inicial = [
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["0", "0"]],
            ["3", False, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["0", "0"]],
            ["3", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Ana", 20, 25, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = True

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_asimetrico_simple(self):
        """
        Bonsai de 3 nodos que no es simétrico
        """

        estructura_inicial = [
            ["1", True, False, ["2", "0"]],
            ["2", False, False, ["0", "3"]],
            ["3", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "0"]],
            ["2", False, False, ["0", "3"]],
            ["3", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Adam", 20, 50, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_03_bonsai_simetrico_medio(self):
        """
        Bonsai de 9 nodos simetrico
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["0", "4"]],
            ["3", True, True, ["5", "0"]],
            ["4", False, False, ["6", "0"]],
            ["5", False, True, ["0", "7"]],
            ["6", True, False, ["0", "8"]],
            ["7", True, True, ["9", "0"]],
            ["8", False, False, ["0", "0"]],
            ["9", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["0", "4"]],
            ["3", True, True, ["5", "0"]],
            ["4", False, False, ["6", "0"]],
            ["5", False, True, ["0", "7"]],
            ["6", True, False, ["0", "8"]],
            ["7", True, True, ["9", "0"]],
            ["8", False, False, ["0", "0"]],
            ["9", False, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Bob", 25, 52, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = True

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_simetrico_medio_2(self):
        """
        Bonsai de 17 nodos simetrico
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["0", "4"]],
            ["3", True, True, ["5", "0"]],
            ["4", False, False, ["6", "0"]],
            ["5", False, True, ["0", "7"]],
            ["6", True, False, ["0", "8"]],
            ["7", True, True, ["9", "0"]],
            ["8", False, False, ["10", "11"]],
            ["9", False, True, ["12", "13"]],
            ["10", True, False, ["14", "0"]],
            ["11", True, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "15"]],
            ["14", True, False, ["16", "0"]],
            ["15", True, True, ["0", "17"]],
            ["16", False, False, ["0", "0"]],
            ["17", False, True, ["0", "0"]],
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["0", "4"]],
            ["3", True, True, ["5", "0"]],
            ["4", False, False, ["6", "0"]],
            ["5", False, True, ["0", "7"]],
            ["6", True, False, ["0", "8"]],
            ["7", True, True, ["9", "0"]],
            ["8", False, False, ["10", "11"]],
            ["9", False, True, ["12", "13"]],
            ["10", True, False, ["14", "0"]],
            ["11", True, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "15"]],
            ["14", True, False, ["16", "0"]],
            ["15", True, True, ["0", "17"]],
            ["16", False, False, ["0", "0"]],
            ["17", False, True, ["0", "0"]],
        ]

        bonsai = Bonsai("Hannah", 1010, 1, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = True

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_05_bonsai_asimetrico_medio(self):
        """
        Bonsai de 9 nodos asimetrico
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["0", "4"]],
            ["3", False, True, ["0", "6"]],
            ["4", False, False, ["0", "5"]],
            ["5", False, True, ["0", "7"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, True, ["9", "8"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["0", "4"]],
            ["3", False, True, ["0", "6"]],
            ["4", False, False, ["0", "5"]],
            ["5", False, True, ["0", "7"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, True, ["9", "8"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Martina", 8, 17, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_06_bonsai_asimetrico_medio_2(self):
        """
        Bonsai de 19 nodos asimetrico
        """

        estructura_inicial = [
            ["1", False, True, ["2", "3"]],
            ["2", False, False, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, True, ["0", "8"]],
            ["5", False, True, ["0", "9"]],
            ["6", False, True, ["10", "0"]],
            ["7", False, False, ["11", "0"]],
            ["8", True, True, ["12", "13"]],
            ["9", False, True, ["14", "15"]],
            ["10", False, True, ["16", "0"]],
            ["11", True, True, ["0", "0"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "0"]],
            ["14", False, False, ["0", "0"]],
            ["15", True, False, ["0", "0"]],
            ["16", False, True, ["0", "17"]],
            ["17", False, True, ["18", "19"]],
            ["18", False, False, ["0", "0"]],
            ["19", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", False, True, ["2", "3"]],
            ["2", False, False, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, True, ["0", "8"]],
            ["5", False, True, ["0", "9"]],
            ["6", False, True, ["10", "0"]],
            ["7", False, False, ["11", "0"]],
            ["8", True, True, ["12", "13"]],
            ["9", False, True, ["14", "15"]],
            ["10", False, True, ["16", "0"]],
            ["11", True, True, ["0", "0"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "0"]],
            ["14", False, False, ["0", "0"]],
            ["15", True, False, ["0", "0"]],
            ["16", False, True, ["0", "17"]],
            ["17", False, True, ["18", "19"]],
            ["18", False, False, ["0", "0"]],
            ["19", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Emilia", 238, 57, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_simetrico_grande(self):
        """
        Bonsai de 49 nodos simetrico tipo diamante
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "0"]],
            ["3", True, False, ["0", "5"]],
            ["4", True, False, ["6", "0"]],
            ["5", True, True, ["0", "7"]],
            ["6", True, True, ["8", "0"]],
            ["7", True, True, ["0", "9"]],
            ["8", True, False, ["10", "0"]],
            ["9", True, False, ["0", "11"]],
            ["10", True, True, ["12", "0"]],
            ["11", True, False, ["0", "13"]],
            ["12", True, False, ["14", "0"]],
            ["13", True, False, ["0", "15"]],
            ["14", True, True, ["16", "0"]],
            ["15", True, False, ["0", "17"]],
            ["16", True, False, ["18", "0"]],
            ["17", True, True, ["0", "19"]],
            ["18", True, True, ["20", "0"]],
            ["19", True, False, ["0", "21"]],
            ["20", True, False, ["22", "0"]],
            ["21", True, False, ["0", "23"]],
            ["22", True, False, ["24", "0"]],
            ["23", True, True, ["0", "25"]],
            ["24", False, False, ["0", "26"]],
            ["25", False, True, ["27", "0"]],
            ["26", True, True, ["0", "28"]],
            ["27", True, False, ["29", "0"]],
            ["28", True, False, ["0", "30"]],
            ["29", True, True, ["31", "0"]],
            ["30", True, True, ["0", "32"]],
            ["31", True, False, ["33", "0"]],
            ["32", True, True, ["0", "34"]],
            ["33", True, True, ["35", "0"]],
            ["34", True, False, ["0", "36"]],
            ["35", True, True, ["37", "0"]],
            ["36", True, False, ["0", "38"]],
            ["37", True, True, ["39", "0"]],
            ["38", True, False, ["0", "40"]],
            ["39", True, False, ["41", "0"]],
            ["40", True, False, ["0", "42"]],
            ["41", True, True, ["43", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", True, False, ["45", "0"]],
            ["44", True, False, ["0", "46"]],
            ["45", True, True, ["47", "0"]],
            ["46", True, True, ["0", "48"]],
            ["47", True, False, ["49", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "0"]],
            ["3", True, False, ["0", "5"]],
            ["4", True, False, ["6", "0"]],
            ["5", True, True, ["0", "7"]],
            ["6", True, True, ["8", "0"]],
            ["7", True, True, ["0", "9"]],
            ["8", True, False, ["10", "0"]],
            ["9", True, False, ["0", "11"]],
            ["10", True, True, ["12", "0"]],
            ["11", True, False, ["0", "13"]],
            ["12", True, False, ["14", "0"]],
            ["13", True, False, ["0", "15"]],
            ["14", True, True, ["16", "0"]],
            ["15", True, False, ["0", "17"]],
            ["16", True, False, ["18", "0"]],
            ["17", True, True, ["0", "19"]],
            ["18", True, True, ["20", "0"]],
            ["19", True, False, ["0", "21"]],
            ["20", True, False, ["22", "0"]],
            ["21", True, False, ["0", "23"]],
            ["22", True, False, ["24", "0"]],
            ["23", True, True, ["0", "25"]],
            ["24", False, False, ["0", "26"]],
            ["25", False, True, ["27", "0"]],
            ["26", True, True, ["0", "28"]],
            ["27", True, False, ["29", "0"]],
            ["28", True, False, ["0", "30"]],
            ["29", True, True, ["31", "0"]],
            ["30", True, True, ["0", "32"]],
            ["31", True, False, ["33", "0"]],
            ["32", True, True, ["0", "34"]],
            ["33", True, True, ["35", "0"]],
            ["34", True, False, ["0", "36"]],
            ["35", True, True, ["37", "0"]],
            ["36", True, False, ["0", "38"]],
            ["37", True, True, ["39", "0"]],
            ["38", True, False, ["0", "40"]],
            ["39", True, False, ["41", "0"]],
            ["40", True, False, ["0", "42"]],
            ["41", True, True, ["43", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", True, False, ["45", "0"]],
            ["44", True, False, ["0", "46"]],
            ["45", True, True, ["47", "0"]],
            ["46", True, True, ["0", "48"]],
            ["47", True, False, ["49", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Otto", 69, 69, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = True

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_08_bonsai_simetrico_grande_2(self):
        """
        Bonsai de 45 nodos simetrico
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "5"]],
            ["3", False, False, ["6", "7"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, True, ["10", "11"]],
            ["6", True, True, ["12", "13"]],
            ["7", True, True, ["14", "15"]],
            ["8", True, False, ["16", "17"]],
            ["9", True, False, ["18", "19"]],
            ["10", False, True, ["20", "21"]],
            ["11", True, False, ["22", "23"]],
            ["12", True, False, ["24", "25"]],
            ["13", False, False, ["26", "27"]],
            ["14", True, True, ["28", "29"]],
            ["15", True, False, ["30", "31"]],
            ["16", True, False, ["32", "33"]],
            ["17", False, True, ["34", "35"]],
            ["18", False, True, ["36", "37"]],
            ["19", False, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", False, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", True, False, ["0", "0"]],
            ["25", False, True, ["0", "0"]],
            ["26", True, True, ["0", "0"]],
            ["27", False, False, ["0", "0"]],
            ["28", False, False, ["0", "0"]],
            ["29", False, True, ["38", "39"]],
            ["30", False, True, ["40", "41"]],
            ["31", True, False, ["42", "43"]],
            ["32", True, True, ["0", "0"]],
            ["33", True, True, ["0", "45"]],
            ["34", True, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", False, False, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", False, False, ["0", "0"]],
            ["39", False, False, ["0", "0"]],
            ["40", False, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["44", "0"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "5"]],
            ["3", False, False, ["6", "7"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, True, ["10", "11"]],
            ["6", True, True, ["12", "13"]],
            ["7", True, True, ["14", "15"]],
            ["8", True, False, ["16", "17"]],
            ["9", True, False, ["18", "19"]],
            ["10", False, True, ["20", "21"]],
            ["11", True, False, ["22", "23"]],
            ["12", True, False, ["24", "25"]],
            ["13", False, False, ["26", "27"]],
            ["14", True, True, ["28", "29"]],
            ["15", True, False, ["30", "31"]],
            ["16", True, False, ["32", "33"]],
            ["17", False, True, ["34", "35"]],
            ["18", False, True, ["36", "37"]],
            ["19", False, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", False, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", True, False, ["0", "0"]],
            ["25", False, True, ["0", "0"]],
            ["26", True, True, ["0", "0"]],
            ["27", False, False, ["0", "0"]],
            ["28", False, False, ["0", "0"]],
            ["29", False, True, ["38", "39"]],
            ["30", False, True, ["40", "41"]],
            ["31", True, False, ["42", "43"]],
            ["32", True, True, ["0", "0"]],
            ["33", True, True, ["0", "45"]],
            ["34", True, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", False, False, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", False, False, ["0", "0"]],
            ["39", False, False, ["0", "0"]],
            ["40", False, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["44", "0"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
        ]

        bonsai = Bonsai("Pip", 69, 69, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = True

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_09_asimetrico_grande(self):
        """
        Bonsai de 57 nodos asimétrico por flores
        """
        estructura_inicial = [
            ["1", True, False, ["3", "2"]],
            ["2", False, True, ["0", "5"]],
            ["3", False, False, ["4", "0"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, True, ["6", "7"]],
            ["6", True, True, ["14", "15"]],
            ["7", False, True, ["10", "0"]],
            ["8", False, False, ["0", "11"]],
            ["9", True, False, ["16", "17"]],
            ["10", False, True, ["20", "21"]],
            ["11", False, False, ["12", "13"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "25"]],
            ["14", True, True, ["18", "19"]],
            ["15", False, False, ["22", "23"]],
            ["16", False, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", True, False, ["0", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", True, False, ["24", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["28", "29"]],
            ["25", False, True, ["26", "27"]],
            ["26", False, True, ["30", "31"]],
            ["27", True, False, ["36", "37"]],
            ["28", False, False, ["38", "39"]],
            ["29", False, True, ["40", "41"]],
            ["30", True, True, ["0", "0"]],
            ["31", True, False, ["0", "0"]],
            ["32", False, True, ["0", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", False, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", True, True, ["0", "42"]],
            ["38", True, False, ["43", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", True, False, ["45", "0"]],
            ["44", False, False, ["0", "0"]],
            ["45", False, True, ["0", "0"]],
        ]

        estructura_final = [
            ["1", True, False, ["3", "2"]],
            ["2", False, True, ["0", "5"]],
            ["3", False, False, ["4", "0"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, True, ["6", "7"]],
            ["6", True, True, ["14", "15"]],
            ["7", False, True, ["10", "0"]],
            ["8", False, False, ["0", "11"]],
            ["9", True, False, ["16", "17"]],
            ["10", False, True, ["20", "21"]],
            ["11", False, False, ["12", "13"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "25"]],
            ["14", True, True, ["18", "19"]],
            ["15", False, False, ["22", "23"]],
            ["16", False, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", True, False, ["0", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", True, False, ["24", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["28", "29"]],
            ["25", False, True, ["26", "27"]],
            ["26", False, True, ["30", "31"]],
            ["27", True, False, ["36", "37"]],
            ["28", False, False, ["38", "39"]],
            ["29", False, True, ["40", "41"]],
            ["30", True, True, ["0", "0"]],
            ["31", True, False, ["0", "0"]],
            ["32", False, True, ["0", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", False, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", True, True, ["0", "42"]],
            ["38", True, False, ["43", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", True, False, ["45", "0"]],
            ["44", False, False, ["0", "0"]],
            ["45", False, True, ["0", "0"]],
        ]

        bonsai = Bonsai("Andrés", 20, 14, estructura_inicial)
        respuesta_estudiante = dccortaramas.es_simetrico(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = False

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

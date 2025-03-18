import os
import sys
import unittest
from dccortaramas import Bonsai
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 10


class TestCargarBonsaiDeArchivo(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_3_nodos(self):
        """
        Bonsai de 3 nodos, se verifica que se haya creado de manera correcta la estructura segun
        lo pedido por enunciado
        """

        bonsai = Bonsai("pequeno_1.txt", 1, 1, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="pequeno", archivo="pequeno_1.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["2", "3"]],
            ["2", False, False, ["0", "0"]],
            ["3", True, False, ["0", "0"]]
        ]

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_5_nodos(self):
        """
        Bonsai de 5 nodos, con ramas de la izquierda a la izquierda y viceversa
        """

        bonsai = Bonsai("pequeno_2.txt", 1, 1, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="pequeno", archivo="pequeno_2.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, True, ["2", "3"]],
            ["2", True, True, ["4", "0"]],
            ["3", False, True, ["0", "5"]],
            ["4", False, True, ["0", "0"]],
            ["5", True, False, ["0", "0"]]
        ]

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_5_nodos(self):
        """
        Bonsai de 5 nodos, con ramas de la izquierda a la derecha y viceversa, ramas modificables
        alteradas
        """
        bonsai = Bonsai("pequeno_3.txt", 1, 1, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="pequeno", archivo="pequeno_3.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["0", "4"]],
            ["3", False, True, ["5", "0"]],
            ["4", False, False, ["0", "0"]],
            ["5", True, True, ["0", "0"]]
        ]

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_03_bonsai_3_nodos_ramas_modificables_flores(self):
        """
        Bonsai de 3 nodos lineal, donde todas las ramas se pueden modificar
        """
        bonsai = Bonsai("pequeno_4.txt", 1, 1, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="pequeno", archivo="pequeno_4.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, True, ["2", "0"]],
            ["2", True, True, ["3", "0"]],
            ["3", True, True, ["0", "0"]]
        ]

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_13_nodos(self):
        """
        Bonsai mediano de 13 nodos simétrico
        """
        bonsai = Bonsai("mediano_1.txt", 1, 1, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="mediano", archivo="mediano_1.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["10", "0"]],
            ["6", True, False, ["11", "12"]],
            ["7", True, True, ["0", "13"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, True, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, False, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]]
        ]

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_05_bonsai_13_nodos(self):
        """
        Bonsai mediano de 13 nodos simétrico con cambios en ramas modificables
        """
        bonsai = Bonsai("mediano_2.txt", 1, 1, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="mediano", archivo="mediano_2.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["10", "0"]],
            ["6", True, False, ["11", "12"]],
            ["7", True, True, ["0", "13"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, True, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]]
        ]

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_06_bonsai_19_nodos(self):
        """
        Bonsai de 19 nodos simétrico
        """
        bonsai = Bonsai("mediano_3.txt", 1, 1, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="mediano", archivo="mediano_3.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
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

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_45_nodos(self):
        """
        Bonsai de 45 nodos semi aleatorio
        """
        bonsai = Bonsai("grande_1.txt", 20, 25, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="grande", archivo="grande_1.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", True, False, ["0", "0"]],
            ["6", True, False, ["10", "11"]],
            ["7", True, True, ["0", "12"]],
            ["8", False, False, ["13", "14"]],
            ["9", True, False, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", False, True, ["15", "16"]],
            ["14", True, True, ["0", "0"]],
            ["15", False, True, ["0", "0"]],
            ["16", True, False, ["0", "17"]],
            ["17", True, False, ["18", "19"]],
            ["18", True, True, ["20", "21"]],
            ["19", False, True, ["22", "23"]],
            ["20", False, False, ["24", "25"]],
            ["21", False, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, True, ["26", "27"]],
            ["25", True, True, ["0", "0"]],
            ["26", False, False, ["0", "28"]],
            ["27", True, False, ["29", "0"]],
            ["28", False, False, ["0", "30"]],
            ["29", True, True, ["31", "32"]],
            ["30", True, True, ["33", "34"]],
            ["31", False, False, ["35", "36"]],
            ["32", True, False, ["37", "0"]],
            ["33", False, True, ["0", "38"]],
            ["34", True, False, ["0", "0"]],
            ["35", False, False, ["0", "0"]],
            ["36", True, True, ["0", "0"]],
            ["37", False, False, ["0", "39"]],
            ["38", False, True, ["0", "40"]],
            ["39", True, True, ["0", "0"]],
            ["40", False, False, ["41", "0"]],
            ["41", True, True, ["42", "43"]],
            ["42", False, False, ["44", "45"]],
            ["43", True, False, ["0", "0"]],
            ["44", False, False, ["0", "0"]],
            ["45", True, False, ["0", "0"]]
        ]

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_08_bonsai_50_nodos(self):
        """
        Bonsai de 50 nodos semi aleatorio
        """

        bonsai = Bonsai("grande_1.txt", 20, 25, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="grande", archivo="grande_2.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["3", "2"]],
            ["2", False, True, ["4", "5"]],
            ["3", True, False, ["0", "0"]],
            ["4", True, False, ["8", "9"]],
            ["5", False, True, ["6", "7"]],
            ["6", True, True, ["0", "0"]],
            ["7", False, True, ["10", "0"]],
            ["8", True, False, ["0", "11"]],
            ["9", False, False, ["16", "17"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, False, ["12", "13"]],
            ["12", True, False, ["0", "14"]],
            ["13", True, False, ["0", "15"]],
            ["14", False, True, ["28", "29"]],
            ["15", True, False, ["18", "19"]],
            ["16", True, False, ["32", "33"]],
            ["17", False, True, ["34", "35"]],
            ["18", False, True, ["36", "37"]],
            ["19", True, False, ["20", "21"]],
            ["20", True, False, ["22", "23"]],
            ["21", False, False, ["24", "25"]],
            ["22", True, False, ["0", "0"]],
            ["23", False, True, ["0", "0"]],
            ["24", True, False, ["0", "0"]],
            ["25", False, True, ["26", "27"]],
            ["26", True, True, ["0", "0"]],
            ["27", False, False, ["0", "0"]],
            ["28", True, False, ["0", "0"]],
            ["29", True, True, ["30", "31"]],
            ["30", False, True, ["0", "0"]],
            ["31", True, False, ["0", "0"]],
            ["32", False, True, ["0", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", True, False, ["0", "0"]],
            ["35", True, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", False, True, ["38", "39"]],
            ["38", True, False, ["40", "41"]],
            ["39", True, False, ["42", "44"]],
            ["40", True, False, ["43", "0"]],
            ["41", False, True, ["0", "0"]],
            ["42", True, True, ["0", "0"]],
            ["43", False, False, ["0", "0"]],
            ["44", True, False, ["45", "46"]],
            ["45", True, True, ["48", "47"]],
            ["46", False, True, ["0", "49"]],
            ["47", True, False, ["0", "0"]],
            ["48", False, False, ["0", "0"]],
            ["49", True, False, ["0", "50"]],
            ["50", False, True, ["0", "0"]]
        ]

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_09_bonsai_49_nodos(self):
        """
        Bonsai de 49 nodos semi diamante
        """

        bonsai = Bonsai("grande_1.txt", 20, 25, [])
        f_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="grande", archivo="grande_3.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
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

        self.assertIsNone(f_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

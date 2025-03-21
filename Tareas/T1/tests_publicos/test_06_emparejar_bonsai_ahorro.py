import unittest
import os
import sys
from dccortaramas import Bonsai, DCCortaRamas
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 20

dccortaramas = DCCortaRamas()


class TestEmparejarBonsaiAhorro(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_una_sola_posibilidad(self):
        """
        Bonsai de simple que tiene una sola opción
        """

        estructura_inicial = [
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["0", "4"]],
            ["3", False, False, ["0", "0"]],
            ["4", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["0", "4"]],
            ["3", False, False, ["0", "0"]],
            ["4", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("IIC2233", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [True, 22, [["Quitar Nodo", "4"]]]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_dos_posibilidades_pequeño(self):
        """
        Bonsai de simple que tiene una sola opción
        """

        estructura_inicial = [
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["0", "4"]],
            ["3", False, False, ["5", "0"]],
            ["4", True, False, ["6", "0"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["0", "4"]],
            ["3", False, False, ["5", "0"]],
            ["4", True, False, ["6", "0"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Isi Salas", 28, 13, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [
            [True, 41, [["Quitar Nodo", "6"], ["Modificar Flor", "5"]]],
            [True, 41, [["Modificar Flor", "5"], ["Quitar Nodo", "6"]]]
        ]

        self.assertIn(respuesta_estudiante, respuesta_esperada)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_sin_posibilidades(self):
        """
        Bonsai de simple no se puede arreglar
        """

        estructura_inicial = [
            ["5", False, True, ["0", "0"]],
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["0", "4"]],
            ["3", False, False, ["5", "0"]],
            ["4", True, True, ["6", "0"]],
            ["6", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["5", False, True, ["0", "0"]],
            ["1", True, False, ["3", "2"]],
            ["2", False, False, ["0", "4"]],
            ["3", False, False, ["5", "0"]],
            ["4", True, True, ["6", "0"]],
            ["6", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("MIP", 28, 13, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [False, []]

        self.assertEqual(respuesta_estudiante, respuesta_esperada)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_03_bonsai_mediano(self):
        """
        Bonsai mediano de varias opciones
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["0", "4"]],
            ["3", False, True, ["6", "0"]],
            ["4", False, True, ["5", "0"]],
            ["5", False, True, ["7", "0"]],
            ["6", True, False, ["0", "8"]],
            ["7", True, False, ["0", "0"]],
            ["8", False, True, ["0", "9"]],
            ["9", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["0", "4"]],
            ["3", False, True, ["6", "0"]],
            ["4", False, True, ["5", "0"]],
            ["5", False, True, ["7", "0"]],
            ["6", True, False, ["0", "8"]],
            ["7", True, False, ["0", "0"]],
            ["8", False, True, ["0", "9"]],
            ["9", False, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Angelina", 4, 3, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuestas = [
            [True, 9, [["Modificar Flor", "3"], [
                "Modificar Flor", "4"],  ["Modificar Flor", "9"]]],
            [True, 9, [["Modificar Flor", "4"], [
                "Modificar Flor", "9"],  ["Modificar Flor", "3"]]],
            [True, 9, [["Modificar Flor", "9"], [
                "Modificar Flor", "3"],  ["Modificar Flor", "4"]]],
            [True, 9, [["Modificar Flor", "4"], [
                "Modificar Flor", "9"],  ["Modificar Flor", "3"]]],
            [True, 9, [["Modificar Flor", "3"], [
                "Modificar Flor", "9"],  ["Modificar Flor", "4"]]],
            [True, 9, [["Modificar Flor", "9"], [
                "Modificar Flor", "4"],  ["Modificar Flor", "3"]]]
        ]

        self.assertIn(respuesta_estudiante, respuestas)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_mediano_2(self):
        """
        Bonsai mediano de varias opciones
        """

        estructura_inicial = [
            ["1", True, True, ["2", "3"]],
            ["2", True, False, ["0", "4"]],
            ["3", True, True, ["0", "6"]],
            ["4", False, True, ["0", "5"]],
            ["5", False, True, ["0", "7"]],
            ["6", True, True, ["0", "0"]],
            ["7", True, True, ["9", "8"]],
            ["8", False, True, ["0", "0"]],
            ["9", False, True, ["0", "10"]],
            ["10", True, True, ["11", "12"]],
            ["11", False, True, ["0", "0"]],
            ["12", False, True, ["13", "0"]],
            ["13", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, True, ["2", "3"]],
            ["2", True, False, ["0", "4"]],
            ["3", True, True, ["0", "6"]],
            ["4", False, True, ["0", "5"]],
            ["5", False, True, ["0", "7"]],
            ["6", True, True, ["0", "0"]],
            ["7", True, True, ["9", "8"]],
            ["8", False, True, ["0", "0"]],
            ["9", False, True, ["0", "10"]],
            ["10", True, True, ["11", "12"]],
            ["11", False, True, ["0", "0"]],
            ["12", False, True, ["13", "0"]],
            ["13", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Jolene", 40, 21, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuestas = [
            [True, 80, [["Quitar Nodo", "4"], ["Quitar Nodo", "6"]]],
            [True, 80, [["Quitar Nodo", "6"], ["Quitar Nodo", "4"]]]
        ]

        self.assertIn(respuesta_estudiante, respuestas)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_05_bonsai_mediano_sin_posibilidad(self):
        """
        Bonsai mediano de varias opciones
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["4", "5"]],
            ["3", False, False, ["6", "7"]],
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

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["4", "5"]],
            ["3", False, False, ["6", "7"]],
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

        bonsai = Bonsai("NoSePudu", 40, 21, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuestas = [False, []]

        self.assertEqual(respuesta_estudiante, respuestas)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_06_bonsai_grande(self):
        """
        Bonsai grande de varias opciones
        """

        estructura_inicial = [
            ["1", True, True, ["3", "2"]],
            ["2", False, False, ["0", "5"]],
            ["3", False, False, ["4", "0"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, False, ["6", "7"]],
            ["6", True, False, ["14", "15"]],
            ["7", False, False, ["10", "0"]],
            ["8", False, False, ["0", "11"]],
            ["9", True, False, ["16", "17"]],
            ["10", False, False, ["20", "21"]],
            ["11", False, False, ["12", "13"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "25"]],
            ["14", True, False, ["18", "19"]],
            ["15", False, False, ["22", "23"]],
            ["16", False, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", True, False, ["0", "0"]],
            ["21", False, False, ["0", "24"]],
            ["22", True, True, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, True, ["28", "29"]],
            ["25", False, True, ["26", "27"]],
            ["26", False, True, ["30", "31"]],
            ["27", True, True, ["36", "37"]],
            ["28", False, True, ["38", "39"]],
            ["29", False, True, ["40", "41"]],
            ["30", True, True, ["0", "0"]],
            ["31", True, True, ["0", "0"]],
            ["32", True, True, ["0", "0"]],
            ["33", True, True, ["0", "0"]],
            ["34", True, True, ["0", "0"]],
            ["35", True, True, ["0", "0"]],
            ["36", True, True, ["0", "0"]],
            ["37", True, True, ["0", "42"]],
            ["38", True, True, ["43", "0"]],
            ["39", True, True, ["0", "0"]],
            ["40", True, True, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", True, True, ["45", "0"]],
            ["44", False, True, ["0", "0"]],
            ["45", False, True, ["0", "0"]],
        ]

        estructura_final = [
            ["1", True, True, ["3", "2"]],
            ["2", False, False, ["0", "5"]],
            ["3", False, False, ["4", "0"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, False, ["6", "7"]],
            ["6", True, False, ["14", "15"]],
            ["7", False, False, ["10", "0"]],
            ["8", False, False, ["0", "11"]],
            ["9", True, False, ["16", "17"]],
            ["10", False, False, ["20", "21"]],
            ["11", False, False, ["12", "13"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "25"]],
            ["14", True, False, ["18", "19"]],
            ["15", False, False, ["22", "23"]],
            ["16", False, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", True, False, ["0", "0"]],
            ["21", False, False, ["0", "24"]],
            ["22", True, True, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, True, ["28", "29"]],
            ["25", False, True, ["26", "27"]],
            ["26", False, True, ["30", "31"]],
            ["27", True, True, ["36", "37"]],
            ["28", False, True, ["38", "39"]],
            ["29", False, True, ["40", "41"]],
            ["30", True, True, ["0", "0"]],
            ["31", True, True, ["0", "0"]],
            ["32", True, True, ["0", "0"]],
            ["33", True, True, ["0", "0"]],
            ["34", True, True, ["0", "0"]],
            ["35", True, True, ["0", "0"]],
            ["36", True, True, ["0", "0"]],
            ["37", True, True, ["0", "42"]],
            ["38", True, True, ["43", "0"]],
            ["39", True, True, ["0", "0"]],
            ["40", True, True, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", True, True, ["45", "0"]],
            ["44", False, True, ["0", "0"]],
            ["45", False, True, ["0", "0"]],
        ]

        bonsai = Bonsai("Tuto", 25, 14, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuestas = [
            [True, 50, [["Quitar Nodo", "25"], ["Quitar Nodo", "24"]]],
            [True, 50, [["Quitar Nodo", "24"], ["Quitar Nodo", "25"]]]
        ]

        self.assertIn(respuesta_estudiante, respuestas)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_grande_2(self):
        """
        Bonsai grande de varias opciones
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
            ["12", False, True, ["24", "25"]],
            ["13", False, True, ["26", "27"]],
            ["14", True, True, ["28", "29"]],
            ["15", True, False, ["30", "31"]],
            ["16", True, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", False, True, ["36", "37"]],
            ["19", False, False, ["0", "0"]],
            ["20", True, True, ["0", "0"]],
            ["21", True, True, ["0", "0"]],
            ["22", False, True, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", True, True, ["0", "0"]],
            ["25", False, True, ["0", "0"]],
            ["26", True, True, ["0", "0"]],
            ["27", False, False, ["0", "0"]],
            ["28", False, True, ["0", "0"]],
            ["29", False, True, ["38", "39"]],
            ["30", True, True, ["40", "41"]],
            ["31", True, True, ["42", "43"]],
            ["32", True, True, ["0", "0"]],
            ["33", True, True, ["0", "45"]],
            ["34", True, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", False, True, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", False, True, ["0", "0"]],
            ["39", False, True, ["0", "0"]],
            ["40", False, True, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["44", "0"]],
            ["43", True, True, ["0", "0"]],
            ["44", True, True, ["0", "0"]],
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
            ["12", False, True, ["24", "25"]],
            ["13", False, True, ["26", "27"]],
            ["14", True, True, ["28", "29"]],
            ["15", True, False, ["30", "31"]],
            ["16", True, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", False, True, ["36", "37"]],
            ["19", False, False, ["0", "0"]],
            ["20", True, True, ["0", "0"]],
            ["21", True, True, ["0", "0"]],
            ["22", False, True, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", True, True, ["0", "0"]],
            ["25", False, True, ["0", "0"]],
            ["26", True, True, ["0", "0"]],
            ["27", False, False, ["0", "0"]],
            ["28", False, True, ["0", "0"]],
            ["29", False, True, ["38", "39"]],
            ["30", True, True, ["40", "41"]],
            ["31", True, True, ["42", "43"]],
            ["32", True, True, ["0", "0"]],
            ["33", True, True, ["0", "45"]],
            ["34", True, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", False, True, ["0", "0"]],
            ["37", False, True, ["0", "0"]],
            ["38", False, True, ["0", "0"]],
            ["39", False, True, ["0", "0"]],
            ["40", False, True, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["44", "0"]],
            ["43", True, True, ["0", "0"]],
            ["44", True, True, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
        ]

        bonsai = Bonsai("Frida", 27, 14, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuestas = [
            [True, 28, [['Modificar Flor', '20'], ['Modificar Flor', '12']]],
            [True, 28, [['Modificar Flor', '12'], ['Modificar Flor', '20']]]
        ]

        self.assertIn(respuesta_estudiante, respuestas)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_08_bonsai_grande_sin_opciones(self):
        """
        Bonsai grande de varias opciones
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "5"]],
            ["3", False, False, ["6", "7"]],
            ["4", True, False, ["8", "9"]],
            ["5", False, False, ["10", "11"]],
            ["6", True, True, ["12", "13"]],
            ["7", True, True, ["14", "15"]],
            ["8", True, False, ["16", "17"]],
            ["9", True, False, ["18", "19"]],
            ["10", False, True, ["20", "21"]],
            ["11", True, True, ["22", "23"]],
            ["12", False, True, ["24", "25"]],
            ["13", False, True, ["26", "27"]],
            ["14", True, True, ["28", "29"]],
            ["15", True, False, ["30", "31"]],
            ["16", True, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", False, True, ["36", "37"]],
            ["19", False, False, ["0", "0"]],
            ["20", True, True, ["0", "0"]],
            ["21", True, True, ["0", "0"]],
            ["22", False, True, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", True, True, ["0", "0"]],
            ["25", False, True, ["0", "0"]],
            ["26", True, True, ["0", "0"]],
            ["27", False, True, ["0", "0"]],
            ["28", False, False, ["0", "0"]],
            ["29", False, True, ["38", "39"]],
            ["30", True, True, ["40", "41"]],
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
            ["45", True, True, ["0", "46"]],
            ["46", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "5"]],
            ["3", False, False, ["6", "7"]],
            ["4", True, False, ["8", "9"]],
            ["5", False, False, ["10", "11"]],
            ["6", True, True, ["12", "13"]],
            ["7", True, True, ["14", "15"]],
            ["8", True, False, ["16", "17"]],
            ["9", True, False, ["18", "19"]],
            ["10", False, True, ["20", "21"]],
            ["11", True, True, ["22", "23"]],
            ["12", False, True, ["24", "25"]],
            ["13", False, True, ["26", "27"]],
            ["14", True, True, ["28", "29"]],
            ["15", True, False, ["30", "31"]],
            ["16", True, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", False, True, ["36", "37"]],
            ["19", False, False, ["0", "0"]],
            ["20", True, True, ["0", "0"]],
            ["21", True, True, ["0", "0"]],
            ["22", False, True, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", True, True, ["0", "0"]],
            ["25", False, True, ["0", "0"]],
            ["26", True, True, ["0", "0"]],
            ["27", False, True, ["0", "0"]],
            ["28", False, False, ["0", "0"]],
            ["29", False, True, ["38", "39"]],
            ["30", True, True, ["40", "41"]],
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
            ["45", True, True, ["0", "46"]],
            ["46", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Liquidambar", 27, 14, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuestas = [False, []]

        self.assertEqual(respuesta_estudiante, respuestas)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_09_bonsai_simetrico(self):
        """
        Bonsai grande que ya es simétrico
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

        bonsai = Bonsai("Treeston", 27, 14, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuestas = [True, 0, []]

        self.assertEqual(respuesta_estudiante, respuestas)
        self.assertCountEqual(estructura_final, estructura_estudiante)

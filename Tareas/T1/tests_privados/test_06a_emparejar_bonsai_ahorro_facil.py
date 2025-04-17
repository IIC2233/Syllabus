import unittest
import os
import sys
from dccortaramas import Bonsai, DCCortaRamas
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 20

dccortaramas = DCCortaRamas()


class TestEmparejarBonsaiAhorroFacil(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_una_sola_posibilidad(self):
        """
        Bonsai de simple que tiene una sola opción
        """

        estructura_inicial = [
            ["1", True, False, ["0", "2"]],
            ["2", False, True, ["0", "3"]],
            ["3", False, True, ["4", "0"]],
            ["4", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["0", "2"]],
            ["2", False, True, ["0", "3"]],
            ["3", False, True, ["4", "0"]],
            ["4", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("IIC2233", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [True, 22, [["Quitar Nodo", "2"]]]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_una_sola_posibilidad(self):
        """
        Bonsai de simple que tiene una sola opción con dos pasos
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["4", "0"]],
            ["3", False, True, ["0", "5"]],
            ["4", True, True, ["6", "0"]],
            ["5", True, False, ["0", "0"]],
            ["6", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["4", "0"]],
            ["3", False, True, ["0", "5"]],
            ["4", True, True, ["6", "0"]],
            ["5", True, False, ["0", "0"]],
            ["6", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("IIC1113", 11, 13, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)

        estructura_estudiante = bonsai.estructura
        lista_esperada = [
            [True, 24, [["Quitar Nodo", "6"], ["Modificar Flor", "3"]]],
            [True, 24, [["Modificar Flor", "3"], ["Quitar Nodo", "6"]]]
        ]

        self.assertIn(respuesta_estudiante, lista_esperada)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_una_sola_posibilidad(self):
        """
        Bonsai de simple que tiene una sola opción con un paso
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["4", "0"]],
            ["3", False, True, ["0", "5"]],
            ["4", True, True, ["0", "0"]],
            ["5", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["4", "0"]],
            ["3", False, True, ["0", "5"]],
            ["4", True, True, ["0", "0"]],
            ["5", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("2.0", 1, 11, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)

        estructura_estudiante = bonsai.estructura
        lista_esperada = [True, 11, [["Modificar Flor", "3"]]]

        self.assertEqual(lista_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_03_bonsai_dos_posibilidades(self):
        """
        Bonsai de simple con dos opciones
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["0", "0"]],
            ["3", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["0", "0"]],
            ["3", False, True, ["0", "0"]]
        ]

        bonsai = Bonsai("IIC1113", 11, 13, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)

        estructura_estudiante = bonsai.estructura
        lista_posibles = [
            [True, 13, [["Modificar Flor", "3"]]],
            [True, 13, [["Modificar Flor", "2"]]]
            ]

        self.assertIn(respuesta_estudiante, lista_posibles)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_tres_acciones(self):
        """
        Bonsai de simple con tres acciones
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", False, True, ["0", "0"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", False, True, ["0", "0"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Araucaria", 7, 4, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura

        lista_posibles = [
            [True, 12, [["Modificar Flor", "4"], ["Modificar Flor", "2"], ["Modificar Flor", "5"]]],
            [True, 12, [["Modificar Flor", "4"], ["Modificar Flor", "5"], ["Modificar Flor", "2"]]],
            [True, 12, [["Modificar Flor", "5"], ["Modificar Flor", "2"], ["Modificar Flor", "4"]]],
            [True, 12, [["Modificar Flor", "5"], ["Modificar Flor", "4"], ["Modificar Flor", "2"]]],
            [True, 12, [["Modificar Flor", "2"], ["Modificar Flor", "5"], ["Modificar Flor", "4"]]],
            [True, 12, [["Modificar Flor", "2"], ["Modificar Flor", "4"], ["Modificar Flor", "5"]]]
                        ]

        self.assertIn(respuesta_estudiante, lista_posibles)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_05_bonsai_una_accion_mediano(self):
        """
        Bonsai de mediano con una pocion
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["8", "9"]],
            ["5", False, True, ["0", "0"]],
            ["6", False, True, ["0", "0"]],
            ["7", True, False, ["10", "11"]],
            ["8", False, True, ["12", "0"]],
            ["9", True, False, ["13", "0"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["8", "9"]],
            ["5", False, True, ["0", "0"]],
            ["6", False, True, ["0", "0"]],
            ["7", True, False, ["10", "11"]],
            ["8", False, True, ["12", "0"]],
            ["9", True, False, ["13", "0"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", True, True, ["0", "0"]]
        ]
        bonsai = Bonsai("Araucaria", 7, 15, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)

        estructura_estudiante = bonsai.estructura
        lista_esperada = [
            [True, 14, [["Quitar Nodo", "13"], ["Quitar Nodo", "12"]]],
            [True, 14, [["Quitar Nodo", "12"], ["Quitar Nodo", "13"]]]
        ]

        self.assertIn(respuesta_estudiante, lista_esperada)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_06_bonsai_una_accion_mediano(self):
        """
        Bonsai de mediano con una pocion
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", True, False, ["0", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", False, True, ["11", "12"]],
            ["8", False, False, ["10", "0"]],
            ["9", False, True, ["0", "0"]],
            ["10", True, True, ["0", "14"]],
            ["11", False, False, ["0", "0"]],
            ["12", False, True, ["0", "13"]],
            ["13", False, True, ["15", "0"]],
            ["14", True, False, ["0", "0"]],
            ["15", True, False, ["0", "0"]],
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", True, False, ["0", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", False, True, ["11", "12"]],
            ["8", False, False, ["10", "0"]],
            ["9", False, True, ["0", "0"]],
            ["10", True, True, ["0", "14"]],
            ["11", False, False, ["0", "0"]],
            ["12", False, True, ["0", "13"]],
            ["13", False, True, ["15", "0"]],
            ["14", True, False, ["0", "0"]],
            ["15", True, False, ["0", "0"]],
        ]

        bonsai = Bonsai("Bonsai", 7, 15, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)

        estructura_estudiante = bonsai.estructura
        lista_esperada = [
            [True, 15, [["Modificar Flor", "10"]]],
            [True, 15, [["Modificar Flor", "13"]]]
        ]

        self.assertIn(respuesta_estudiante, lista_esperada)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_tres_acciones(self):
        """
        Bonsai de mediano tres acciones
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", False, False, ["0", "9"]],
            ["5", True, False, ["0", "18"]],
            ["6", True, False, ["0", "0"]],
            ["7", False, True, ["8", "0"]],
            ["8", True, True, ["12", "13"]],
            ["9", False, True, ["10", "11"]],
            ["10", True, True, ["15", "14"]],
            ["11", False, True, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", False, True, ["16", "17"]],
            ["14", True, True, ["0", "0"]],
            ["15", True, True, ["0", "0"]],
            ["16", False, True, ["0", "0"]],
            ["17", False, True, ["0", "0"]],
            ["18", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", False, False, ["0", "9"]],
            ["5", True, False, ["0", "18"]],
            ["6", True, False, ["0", "0"]],
            ["7", False, True, ["8", "0"]],
            ["8", True, True, ["12", "13"]],
            ["9", False, True, ["10", "11"]],
            ["10", True, True, ["15", "14"]],
            ["11", False, True, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", False, True, ["16", "17"]],
            ["14", True, True, ["0", "0"]],
            ["15", True, True, ["0", "0"]],
            ["16", False, True, ["0", "0"]],
            ["17", False, True, ["0", "0"]],
            ["18", False, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Jazmin", 4, 3, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura

        lista = [
            [True, 12, [["Quitar Nodo", "18"], ["Quitar Nodo", "9"], ["Quitar Nodo", "8"]]],
            [True, 12, [["Quitar Nodo", "18"], ["Quitar Nodo", "8"], ["Quitar Nodo", "9"]]],
            [True, 12, [["Quitar Nodo", "9"], ["Quitar Nodo", "8"], ["Quitar Nodo", "18"]]],
            [True, 12, [["Quitar Nodo", "9"], ["Quitar Nodo", "18"], ["Quitar Nodo", "8"]]],
            [True, 12, [["Quitar Nodo", "8"], ["Quitar Nodo", "9"], ["Quitar Nodo", "18"]]],
            [True, 12, [["Quitar Nodo", "8"], ["Quitar Nodo", "18"], ["Quitar Nodo", "9"]]]
            ]

        self.assertIn(respuesta_estudiante, lista)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_08_bonsai_grande(self):
        """
        Bonsai de grande con una opcion
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
            ["46", True, True, ["0", "0"]],
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
            ["46", True, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Boldo", 7, 3, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [True, 3, [["Modificar Flor", "46"]]]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

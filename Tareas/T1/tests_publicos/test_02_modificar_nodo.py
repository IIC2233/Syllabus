import unittest
import os
import sys
from dccortaramas import Bonsai, DCCortaRamas
from tests_publicos.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 10

dccortaramas = DCCortaRamas()


class TestModificarNodo(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_ineditable_simple(self):
        """
        Bonsai de 3 nodos, con un nodo que no se puede editar
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", False, False, ["0", "0"]],
            ["3", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", False, False, ["0", "0"]],
            ["3", True, False, ["0", "0"]]
        ]
        arbol = Bonsai("Liam", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="2")
        cambio_esperado = "No permitido"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_editable_agregar(self):
        """
        Bonsai de 3 nodos, que sí se puede editar y que agrega flor
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["0", "0"]],
            ["3", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["0", "0"]],
            ["3", True, False, ["0", "0"]]
        ]

        arbol = Bonsai("Zayn", 1, 1, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="2")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_editable_quitar(self):
        """
        Bonsai de 3 nodos, que sí se puede editar y que elimina flor
        """
        estructura_inicial = [
            ["1", True, True, ["2", "3"]],
            ["2", True, True, ["0", "0"]],
            ["3", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", False, True, ["2", "3"]],
            ["2", True, True, ["0", "0"]],
            ["3", True, False, ["0", "0"]]
        ]

        arbol = Bonsai("Harry", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="1")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_03_bonsai_pequeno_no_encontrado(self):
        """
        Bonsai de 3 nodos, que no encuentra el nodo
        """
        estructura_inicial = [
            ["1", False, False, ["2", "3"]],
            ["2", False, True, ["0", "0"]],
            ["3", True, False, ["4", "0"]],
            ["4", False, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", False, False, ["2", "3"]],
            ["2", False, True, ["0", "0"]],
            ["3", True, False, ["4", "0"]],
            ["4", False, False, ["0", "0"]]
        ]

        arbol = Bonsai("Louis", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="1D")
        cambio_esperado = "No encontrado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_mediano_ineditable(self):
        """
        Bonsai de 9 nodos, que no se puede editar
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, True, ["0", "0"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, True, ["0", "0"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, False, ["0", "0"]]
        ]

        arbol = Bonsai("Niall", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="8")
        cambio_esperado = "No permitido"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_05_bonsai_mediano_editable_agregar(self):
        """
        Bonsai de 13 nodos, que si se puede editar y agrega una flor
        """

        estructura_inicial = [
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

        estructura_final = [
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
            ["12", True, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]]
        ]

        arbol = Bonsai("dodie", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="12")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_06_bonsai_mediano_no_encontrado(self):
        """
        Bonsai de 13 nodos, que no tiene el nodo pedido
        """
        estructura_inicial = [
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

        estructura_final = [
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

        arbol = Bonsai("Lizzy McAlpine", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="Older")
        cambio_esperado = "No encontrado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_mediano_editable_agregar(self):
        """
        Bonsai de 15 nodos, que agrega una flor
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, False, ["0", "0"]],
            ["6", True, False, ["11", "12"]],
            ["7", True, True, ["0", "13"]],
            ["8", False, False, ["10", "0"]],
            ["9", False, True, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", False, True, ["14", "15"]],
            ["14", True, True, ["0", "0"]],
            ["15", False, True, ["0", "0"]],
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, False, ["0", "0"]],
            ["6", True, False, ["11", "12"]],
            ["7", True, True, ["0", "13"]],
            ["8", False, False, ["10", "0"]],
            ["9", True, True, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", False, True, ["14", "15"]],
            ["14", True, True, ["0", "0"]],
            ["15", False, True, ["0", "0"]],
        ]

        arbol = Bonsai("Dr. Simi", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="9")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_08_bonsai_grande_agregar(self):
        """
        Bonsai de 65 nodos, que agrega una flor
        """

        estructura_inicial = [
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
            ["30", False, True, ["33", "34"]],
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

        estructura_final = [
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

        arbol = Bonsai("Groot", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="30")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    def test_09_bonsai_vacio(self):
        """
        Bonsai vacío por lo que no se encuentra el identificador
        """

        arbol = Bonsai("Planti", 22, 33, [])
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="30")
        cambio_esperado = "No encontrado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual([], resultado_estudiante)

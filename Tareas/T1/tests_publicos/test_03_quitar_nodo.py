from tests_publicos.timeout_function import timeout
from dccortaramas import Bonsai, DCCortaRamas
import unittest
import os
import sys
sys.stdout = open(os.devnull, 'w')

N_SECOND = 10

dccortaramas = DCCortaRamas()


class TestQuitarNodo(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_nodo_no_existente(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, True, ["2", "3"]], [
                        "2", True, False, ["0", "0"]], ["3", False, True, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "4")

        self.assertEqual(resultado_estudiante, "No encontrado")
        self.assertCountEqual(bonsai.estructura, [["1", True, True, ["2", "3"]], [
                         "2", True, False, ["0", "0"]], ["3", False, True, ["0", "0"]]])

    @timeout(N_SECOND)
    def test_01_permitido_raiz(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, True, ["2", "3"]], [
                        "2", False, True, ["0", "0"]], ["3", False, True, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "1")

        self.assertEqual(resultado_estudiante, "Realizado")
        self.assertCountEqual(bonsai.estructura, [])

    @timeout(N_SECOND)
    def test_02_permitido_hoja(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], [
                        "2", False, True, ["0", "0"]], ["3", False, True, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "2")

        self.assertEqual(resultado_estudiante, "Realizado")
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["0", "3"]], [
                         "3", False, True, ["0", "0"]]])

    @timeout(N_SECOND)
    def test_03_permitido_hoja_lejana(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", False, True, ["2", "0"]], ["2", False, True, ["3", "0"]], ["3", False, True, ["4", "0"]], ["4", False, True, [
                        "5", "0"]], ["5", False, True, ["6", "0"]], ["6", False, True, ["7", "0"]], ["7", False, True, ["8", "0"]], ["8", True, True, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "8")

        self.assertEqual(resultado_estudiante, "Realizado")
        self.assertCountEqual(bonsai.estructura, [["1", False, True, ["2", "0"]], ["2", False, True, ["3", "0"]], ["3", False, True, ["4", "0"]], [
                         "4", False, True, ["5", "0"]], ["5", False, True, ["6", "0"]], ["6", False, True, ["7", "0"]], ["7", False, True, ["0", "0"]]])

    @timeout(N_SECOND)
    def test_04_permitido_rama(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, True, ["2", "3"]], ["2", True, True, ["4", "5"]], ["3", False, True, ["6", "7"]], [
                        "4", True, True, ["0", "0"]], ["5", True, True, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, True, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "2")

        self.assertEqual(resultado_estudiante, "Realizado")
        self.assertCountEqual(bonsai.estructura, [["1", True, True, ["0", "3"]], ["3", False, True, [
                         "6", "7"]], ["6", False, True, ["0", "0"]], ["7", False, True, ["0", "0"]]])

    @timeout(N_SECOND)
    def test_05_no_permitido_raiz_directo(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", False, False, ["2", "3"]], [
                        "2", True, True, ["0", "0"]], ["3", True, True, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "1")

        self.assertEqual(resultado_estudiante, "No permitido")
        self.assertCountEqual(bonsai.estructura, [["1", False, False, ["2", "3"]], [
                         "2", True, True, ["0", "0"]], ["3", True, True, ["0", "0"]]])

    @timeout(N_SECOND)
    def test_06_no_permitido_raiz_indirecto(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, True, ["2", "3"]], ["2", True, True, ["4", "5"]], ["3", True, True, ["6", "7"]], [
                        "4", True, True, ["0", "0"]], ["5", True, True, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, False, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "1")

        self.assertEqual(resultado_estudiante, "No permitido")
        self.assertCountEqual(bonsai.estructura, [["1", True, True, ["2", "3"]], ["2", True, True, ["4", "5"]], ["3", True, True, ["6", "7"]], [
                         "4", True, True, ["0", "0"]], ["5", True, True, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, False, ["0", "0"]]])

    @timeout(N_SECOND)
    def test_07_no_permitido_hoja(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, True, ["2", "3"]], [
                        "2", True, False, ["0", "0"]], ["3", False, True, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "2")

        self.assertEqual(resultado_estudiante, "No permitido")
        self.assertCountEqual(bonsai.estructura, [["1", True, True, ["2", "3"]], [
                         "2", True, False, ["0", "0"]], ["3", False, True, ["0", "0"]]])

    @timeout(N_SECOND)
    def test_08_no_permitido_rama_directo(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, True, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", False, True, ["6", "7"]], [
                        "4", True, True, ["0", "0"]], ["5", True, True, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, True, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "2")

        self.assertEqual(resultado_estudiante, "No permitido")
        self.assertCountEqual(bonsai.estructura, [["1", True, True, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", False, True, ["6", "7"]], [
                         "4", True, True, ["0", "0"]], ["5", True, True, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, True, ["0", "0"]]])

    @timeout(N_SECOND)
    def test_09_no_permitido_rama_indirecto(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, True, ["2", "3"]], ["2", True, True, ["4", "5"]], ["3", True, True, ["6", "7"]], [
                        "4", True, True, ["0", "0"]], ["5", True, True, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, False, ["0", "0"]]])
        resultado_estudiante = dccortaramas.quitar_nodo(bonsai, "3")

        self.assertEqual(resultado_estudiante, "No permitido")
        self.assertCountEqual(bonsai.estructura, [["1", True, True, ["2", "3"]], ["2", True, True, ["4", "5"]], ["3", True, True, ["6", "7"]], [
                         "4", True, True, ["0", "0"]], ["5", True, True, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, False, ["0", "0"]]])

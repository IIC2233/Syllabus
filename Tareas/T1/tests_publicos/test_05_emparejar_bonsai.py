from tests_publicos.timeout_function import timeout
from dccortaramas import Bonsai, DCCortaRamas
import unittest
import os
import sys
sys.stdout = open(os.devnull, 'w')

N_SECOND = 20

dccortaramas = DCCortaRamas()


class TestEmparejarBonsai(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_ya_emparejado(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", True, False, ["6", "7"]], [
            "4", False, False, ["0", "0"]], ["5", False, False, ["0", "0"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", True, False, ["6", "7"]], [
            "4", False, False, ["0", "0"]], ["5", False, False, ["0", "0"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [True, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_01_emparejable_flores(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", True, False, ["0", "0"]], ["5", True, False, ["0", "0"]], ["6", True, False, ["0", "0"]], ["7", False, True, ["0", "0"]]]

        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", True, False, ["0", "0"]], ["5", True, False, ["0", "0"]], ["6", True, False, ["0", "0"]], ["7", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [
                         True, [["Modificar Flor", "7"]]])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_02_emparejable_cortes(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "0"]], [
            "3", False, False, ["0", "0"]], ["4", False, True, ["0", "0"]]]

        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "0"]], [
            "3", False, False, ["0", "0"]], ["4", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [True, [["Quitar Nodo", "4"]]])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_03_emparejable_cortes_flores(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, True, ["4", "0"]], [
            "3", False, False, ["0", "0"]], ["4", False, True, ["0", "0"]]]

        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, True, ["4", "0"]], [
            "3", False, False, ["0", "0"]], ["4", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        orden_1 = [True, [["Modificar Flor", "2"], ["Quitar Nodo", "4"]]]
        orden_2 = [True, [["Quitar Nodo", "4"], ["Modificar Flor", "2"]]]
        soluciones = [orden_1, orden_2]

        self.assertIn(resultado_estudiante, soluciones)
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_04_emparejable_cortes_grandes(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "0"]], [
            "3", False, True, ["0", "0"]], ["4", False, True, ["5", "0"]], ["5", False, True, ["0", "0"]]]

        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "0"]], [
            "3", False, True, ["0", "0"]], ["4", False, True, ["5", "0"]], ["5", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        solucion_1 = [True, [["Quitar Nodo", "5"], ["Quitar Nodo", "4"]]]
        solucion_2 = [True, [["Quitar Nodo", "4"]]]
        soluciones = [solucion_1, solucion_2]

        self.assertIn(resultado_estudiante, soluciones)
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_05_emparejable_solo_raiz(self):
        estructura_inicial = [["1", True, False, ["2", "0"]], ["2", False, True, ["3", "0"]], [
            "3", False, True, ["4", "0"]], ["4", False, True, ["0", "0"]]]

        estructura_final = [["1", True, False, ["2", "0"]], ["2", False, True, ["3", "0"]], [
            "3", False, True, ["4", "0"]], ["4", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        posibilidad_1 = [True, [["Quitar Nodo", "4"], [
            "Quitar Nodo", "3"], ["Quitar Nodo", "2"]]]
        posibilidad_2 = [True, [["Quitar Nodo", "3"], ["Quitar Nodo", "2"]]]
        posibilidad_3 = [True, [["Quitar Nodo", "2"]]]
        soluciones = [posibilidad_1, posibilidad_2, posibilidad_3]

        self.assertIn(resultado_estudiante, soluciones)
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_06_no_emparejable_flores(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], [
            "2", True, False, ["0", "0"]], ["3", False, False, ["0", "0"]]]

        estructura_final = [["1", True, False, ["2", "3"]], [
            "2", True, False, ["0", "0"]], ["3", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_07_no_emparejable_cortes(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["0", "0"]], [
            "3", False, False, ["4", "0"]], ["4", False, False, ["0", "0"]]]

        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["0", "0"]], [
            "3", False, False, ["4", "0"]], ["4", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_08_no_emparejable_corte_lejano(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, True, ["4", "0"]], [
            "3", False, True, ["0", "0"]], ["4", False, True, ["5", "0"]], ["5", False, False, ["0", "0"]]]

        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, True, ["4", "0"]], [
            "3", False, True, ["0", "0"]], ["4", False, True, ["5", "0"]], ["5", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)

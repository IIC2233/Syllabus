from tests_publicos.timeout_function import timeout
from dccortaramas import Bonsai, DCCortaRamas
import unittest
import os
import sys
sys.stdout = open(os.devnull, 'w')

N_SECOND = 20

dccortaramas = DCCortaRamas()


class TestComprobarSolucion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_corte_invalido(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, True, ["2", "3"]], ["2", False, True, [
                        "5", "0"]], ["3", False, True, ["0", "0"]], ["5", False, False, ["0", "0"]]])
        instrucciones = [["Quitar Nodo", "5"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)

        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, [["1", True, True, ["2", "3"]], ["2", False, True, [
            "5", "0"]], ["3", False, True, ["0", "0"]], ["5", False, False, ["0", "0"]]])

    @timeout(N_SECOND)
    def test_01_flor_invalido(self):
        estructura_inicial = [["1", True, True, ["2", "3"]], ["2", False, True, ["4", "5"]], ["3", False, True, ["6", "7"]], [
            "4", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]], ["6", True, True, ["0", "0"]], ["7", True, False, ["0", "0"]]]
        estructura_final = [["1", True, True, ["2", "3"]], ["2", False, True, ["4", "5"]], ["3", False, True, ["6", "7"]], [
            "4", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]], ["6", True, True, ["0", "0"]], ["7", True, False, ["0", "0"]]]

        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        instrucciones = [["Modificar Flor", "6"], ["Modificar Flor", "7"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_02_nodo_invalido(self):
        estructura_inicial = [["1", True, True, ["2", "3"]], ["2", False, True, ["5", "0"]], [
            "3", False, True, ["0", "0"]], ["5", False, False, ["0", "0"]]]
        estructura_final = [["1", True, True, ["2", "3"]], ["2", False, True, ["5", "0"]], [
            "3", False, True, ["0", "0"]], ["5", False, False, ["0", "0"]]]

        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        instrucciones = [["Quitar Nodo", "4"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)

        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_03_flor_luego_de_corte_invalido(self):
        estructura_inicial = [["1", True, True, ["2", "0"]], [
            "2", False, True, ["3", "0"]], ["3", False, True, ["0", "0"]]]
        estructura_final = [["1", True, True, ["2", "0"]], [
            "2", False, True, ["3", "0"]], ["3", False, True, ["0", "0"]]]

        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        instrucciones = [["Quitar Nodo", "3"], ["Modificar Flor", "3"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)

        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_04_corte_luego_de_corte_invalido(self):
        estructura_inicial = [["1", True, True, ["2", "0"]], ["2", False, True, ["3", "0"]], [
            "3", False, True, ["4", "0"]], ["4", False, True, ["0", "0"]]]
        estructura_final = [["1", True, True, ["2", "0"]], ["2", False, True, ["3", "0"]], [
            "3", False, True, ["4", "0"]], ["4", False, True, ["0", "0"]]]

        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        instrucciones = [["Quitar Nodo", "3"], ["Quitar Nodo", "4"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)

        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_05_valido_no_solucion(self):
        estructura_inicial = [["1", True, True, ["2", "0"]], ["2", False, True, ["3", "0"]], [
            "3", False, True, ["4", "0"]], ["4", False, True, ["0", "0"]]]
        estructura_final = [["1", True, True, ["2", "0"]], ["2", False, True, ["3", "0"]], [
            "3", False, True, ["4", "0"]], ["4", False, True, ["0", "0"]]]

        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        instrucciones = [["Quitar Nodo", "4"], ["Quitar Nodo", "3"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)

        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_06_valido_solucion_flores(self):
        estructura_inicial = [["1", True, True, ["2", "3"]], ["2", False, True, ["4", "5"]], ["3", False, True, ["6", "7"]], [
            "4", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]], ["6", True, True, ["0", "0"]], ["7", True, True, ["0", "0"]]]
        estructura_final = [["1", True, True, ["2", "3"]], ["2", False, True, ["4", "5"]], ["3", False, True, ["6", "7"]], [
            "4", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]], ["6", True, True, ["0", "0"]], ["7", True, True, ["0", "0"]]]

        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        instrucciones = [["Modificar Flor", "6"], ["Modificar Flor", "7"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)

        self.assertEqual(resultado_estudiante, [True, 40])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_07_valido_solucion_cortes(self):
        estructura_inicial = [["1", True, True, ["2", "3"]], ["2", False, True, ["5", "0"]], [
            "3", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]]]
        estructura_final = [["1", True, True, ["2", "3"]], ["2", False, True, ["5", "0"]], [
            "3", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]]]

        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        instrucciones = [["Quitar Nodo", "5"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)

        self.assertEqual(resultado_estudiante, [True, 10])
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_08_valido_solucion_cortes_flores(self):
        estructura_inicial = [["1", True, True, ["2", "3"]], ["2", False, True, ["5", "0"]], [
            "3", True, True, ["0", "0"]], ["5", False, True, ["0", "0"]]]
        estructura_final = [["1", True, True, ["2", "3"]], ["2", False, True, ["5", "0"]], [
            "3", True, True, ["0", "0"]], ["5", False, True, ["0", "0"]]]

        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        instrucciones = [["Quitar Nodo", "5"], ["Modificar Flor", "3"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)

        self.assertEqual(resultado_estudiante, [True, 30])
        self.assertCountEqual(bonsai.estructura, estructura_final)

from tests_privados.timeout_function import timeout
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
    def test_00_instrucciones_vacias_simetrico(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", False, False, ["0", "0"]]])
        instrucciones = []
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [True, 0])
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", False, False, ["0", "0"]]])


    @timeout(N_SECOND)
    def test_01_instrucciones_vacías_no_simetrico(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", True, False, ["0", "0"]]])
        instrucciones = []
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", True, False, ["0", "0"]]])


    @timeout(N_SECOND)
    def test_02_instruccion_invalida_corte(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", True, False, ["0", "0"]]])
        instrucciones = [["Quitar Nodo", "3"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", True, False, ["0", "0"]]])
        

    @timeout(N_SECOND)
    def test_03_instruccion_invalida_flor(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", True, False, ["0", "0"]]])
        instrucciones = [["Modificar Flor", "3"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", True, False, ["0", "0"]]])        


    @timeout(N_SECOND)
    def test_04_instruccion_invalida_nodo(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", True, False, ["0", "0"]]])
        instrucciones = [["Quitar Nodo", "4"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["2", "3"]], ["2", False, False, [
                        "0", "0"]], ["3", True, False, ["0", "0"]]])


    @timeout(N_SECOND)
    def test_05_instruccion_invalida_cortar_hijo_cortado(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", False, True, [
                        "4", "5"]], ["3", True, False, ["0", "0"]], ["4", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]]])
        instrucciones = [["Quitar Nodo", "2"], ["Quitar Nodo", "4"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["2", "3"]], ["2", False, True, [
                        "4", "5"]], ["3", True, False, ["0", "0"]], ["4", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]]])


    @timeout(N_SECOND)
    def test_06_instrucciones_validas_no_simetrico(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", False, True, [
                        "4", "5"]], ["3", True, False, ["0", "0"]], ["4", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]]])
        instrucciones = [["Quitar Nodo", "5"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["2", "3"]], ["2", False, True, [
                        "4", "5"]], ["3", True, False, ["0", "0"]], ["4", False, True, ["0", "0"]], ["5", False, True, ["0", "0"]]])


    @timeout(N_SECOND)
    def test_07_instrucciones_validas_flores_simetrico(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", False, True, [
                        "4", "5"]], ["3", True, False, ["6", "7"]], ["4", False, True, ["8", "9"]], ["5", False, True, ["10", "11"]],
                        ["6", False, True, ["12", "13"]], ["7", False, True, ["14", "15"]], ["8", True, True, ["0", "0"]], ["9", True, True, ["0", "0"]],
                        ["10", True, True, ["0", "0"]], ["11", True, True, ["0", "0"]], ["12", False, True, ["0", "0"]], ["13", False, True, ["0", "0"]],
                        ["14", False, True, ["0", "0"]], ["15", False, True, ["0", "0"]]])
        instrucciones = [["Modificar Flor", "2"], ["Modificar Flor", "8"], ["Modificar Flor", "9"], ["Modificar Flor", "10"], ["Modificar Flor", "11"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [True, 100])
        self.assertCountEqual(bonsai.estructura,[["1", True, False, ["2", "3"]], ["2", False, True, [
                        "4", "5"]], ["3", True, False, ["6", "7"]], ["4", False, True, ["8", "9"]], ["5", False, True, ["10", "11"]],
                        ["6", False, True, ["12", "13"]], ["7", False, True, ["14", "15"]], ["8", True, True, ["0", "0"]], ["9", True, True, ["0", "0"]],
                        ["10", True, True, ["0", "0"]], ["11", True, True, ["0", "0"]], ["12", False, True, ["0", "0"]], ["13", False, True, ["0", "0"]],
                        ["14", False, True, ["0", "0"]], ["15", False, True, ["0", "0"]]])


    @timeout(N_SECOND)
    def test_08_instrucciones_validas_corte_simetrico(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", True, True, [
                        "4", "5"]], ["3", True, False, ["6", "7"]], ["4", False, True, ["8", "9"]], ["5", False, True, ["10", "11"]],
                        ["6", False, True, ["0", "0"]], ["7", False, True, ["0", "0"]], ["8", True, True, ["0", "0"]], ["9", True, True, ["0", "0"]],
                        ["10", True, True, ["0", "0"]], ["11", True, True, ["0", "0"]]])
        instrucciones = [["Quitar Nodo", "8"], ["Quitar Nodo", "9"], ["Quitar Nodo", "10"], ["Quitar Nodo", "11"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [True, 40])
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["2", "3"]], ["2", True, True, [
                        "4", "5"]], ["3", True, False, ["6", "7"]], ["4", False, True, ["8", "9"]], ["5", False, True, ["10", "11"]],
                        ["6", False, True, ["0", "0"]], ["7", False, True, ["0", "0"]], ["8", True, True, ["0", "0"]], ["9", True, True, ["0", "0"]],
                        ["10", True, True, ["0", "0"]], ["11", True, True, ["0", "0"]]])
        
    
    @timeout(N_SECOND)
    def test_09_instrucciones_validas_corte_no_simetrico(self):
        bonsai = Bonsai("Arbolito", 10, 20, [["1", True, False, ["2", "3"]], ["2", True, True, [
                        "4", "5"]], ["3", True, False, ["6", "7"]], ["4", False, True, ["8", "9"]], ["5", False, True, ["10", "11"]],
                        ["6", False, True, ["0", "0"]], ["7", False, True, ["0", "0"]], ["8", True, True, ["0", "0"]], ["9", True, True, ["0", "0"]],
                        ["10", True, True, ["0", "0"]], ["11", True, True, ["0", "0"]]])
        instrucciones = [["Quitar Nodo", "6"], ["Quitar Nodo", "7"]]
        resultado_estudiante = dccortaramas.comprobar_solucion(
            bonsai, instrucciones)
        
        self.assertEqual(resultado_estudiante, [False, 0])
        self.assertCountEqual(bonsai.estructura, [["1", True, False, ["2", "3"]], ["2", True, True, [
                        "4", "5"]], ["3", True, False, ["6", "7"]], ["4", False, True, ["8", "9"]], ["5", False, True, ["10", "11"]],
                        ["6", False, True, ["0", "0"]], ["7", False, True, ["0", "0"]], ["8", True, True, ["0", "0"]], ["9", True, True, ["0", "0"]],
                        ["10", True, True, ["0", "0"]], ["11", True, True, ["0", "0"]]])
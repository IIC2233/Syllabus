from tests_privados.timeout_function import timeout
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
    def test_00_emparejado_raiz(self):
        estructura_inicial = [["1", True, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [True, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_01_emparejado_nivel_2(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, False, ["0", "0"]], ["3", True, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, False, ["0", "0"]], ["3", True, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [True, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_02_emparejado_nivel_4(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", True, False, ["6", "7"]], [
            "4", True, False, ["8", "0"]], ["5", True, False, ["0", "0"]], ["6", True, False, ["0", "0"]], ["7", True, False, ["0", "9"]], ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", True, False, ["6", "7"]], [
            "4", True, False, ["8", "0"]], ["5", True, False, ["0", "0"]], ["6", True, False, ["0", "0"]], ["7", True, False, ["0", "9"]], ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [True, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_03_flores_izquierda_nivel_2(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, True, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", True, True, ["0", "0"]], ["5", False, True, ["0", "0"]], ["6", True, False, ["0", "0"]], ["7", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, True, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", True, True, ["0", "0"]], ["5", False, True, ["0", "0"]], ["6", True, False, ["0", "0"]], ["7", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        posibilidad_1 = [True, [["Modificar Flor", "2"], ["Modificar Flor", "4"], ["Modificar Flor", "5"]]]
        posibilidad_2 = [True, [["Modificar Flor", "2"], ["Modificar Flor", "5"], ["Modificar Flor", "4"]]]
        posibilidad_3 = [True, [["Modificar Flor", "4"], ["Modificar Flor", "2"], ["Modificar Flor", "5"]]]
        posibilidad_4 = [True, [["Modificar Flor", "4"], ["Modificar Flor", "5"], ["Modificar Flor", "2"]]]
        posibilidad_5 = [True, [["Modificar Flor", "5"], ["Modificar Flor", "2"], ["Modificar Flor", "4"]]]
        posibilidad_6 = [True, [["Modificar Flor", "5"], ["Modificar Flor", "4"], ["Modificar Flor", "2"]]]
        posibilidades = [posibilidad_1, posibilidad_2, posibilidad_3, posibilidad_4, posibilidad_5, posibilidad_6]

        self.assertIn(resultado_estudiante, posibilidades)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    
    @timeout(N_SECOND)
    def test_04_flores_derecha_nivel_3(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", False, True, ["6", "7"]], [
            "4", True, False, ["8", "9"]], ["5", True, False, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, True, ["10", "11"]], ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]], ["10", False, True, ["0", "0"]], ["11", False, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", False, True, ["6", "7"]], [
            "4", True, False, ["8", "9"]], ["5", True, False, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, True, ["10", "11"]], ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]], ["10", False, True, ["0", "0"]], ["11", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Modificar Flor", "3"], ["Modificar Flor", "6"],["Modificar Flor", "7"], ["Modificar Flor", "10"], ["Modificar Flor", "11"]]
        
        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_05_flores_izquierda_derecha_nivel_3(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, True, ["4", "5"]], ["3", True, False, ["6", "7"]], [
            "4", True, False, ["8", "9"]], ["5", True, False, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, True, ["10", "11"]], ["8", False, True, ["0", "0"]], ["9", False, True, ["0", "0"]], ["10", True, False, ["0", "0"]], ["11", True, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, True, ["4", "5"]], ["3", True, False, ["6", "7"]], [
            "4", True, False, ["8", "9"]], ["5", True, False, ["0", "0"]], ["6", False, True, ["0", "0"]], ["7", False, True, ["10", "11"]], ["8", False, True, ["0", "0"]], ["9", False, True, ["0", "0"]], ["10", True, False, ["0", "0"]], ["11", True, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Modificar Flor", "2"], ["Modificar Flor", "6"],["Modificar Flor", "7"], ["Modificar Flor", "8"], ["Modificar Flor", "9"]]

        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)

    @timeout(N_SECOND)
    def test_06_cortes_izquierda_largo_1(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", True, False, ["6", "7"]],
                              ["4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]], ["8", False, True, ["0", "0"]], ["9", False, True, ["0", "0"]], ["10", False, True, ["0", "0"]], ["11", False, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", True, False, ["6", "7"]],
                              ["4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]], ["8", False, True, ["0", "0"]], ["9", False, True, ["0", "0"]], ["10", False, True, ["0", "0"]], ["11", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "8"], ["Quitar Nodo", "9"], ["Quitar Nodo", "10"], ["Quitar Nodo", "11"]]

        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_07_cortes_izquierda_largo_1_flores_ramas(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, True, ["4", "5"]], ["3", True, False, ["6", "7"]],
                              ["4", True, True, ["8", "9"]], ["5", True, True, ["10", "11"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]], ["8", False, True, ["0", "0"]], ["9", False, True, ["0", "0"]], ["10", False, True, ["0", "0"]], ["11", False, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, True, ["4", "5"]], ["3", True, False, ["6", "7"]],
                              ["4", True, True, ["8", "9"]], ["5", True, True, ["10", "11"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]], ["8", False, True, ["0", "0"]], ["9", False, True, ["0", "0"]], ["10", False, True, ["0", "0"]], ["11", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "8"], ["Quitar Nodo", "9"], ["Quitar Nodo", "10"], ["Quitar Nodo", "11"], ["Modificar Flor", "2"], ["Modificar Flor", "4"], ["Modificar Flor", "5"]]

        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_08_cortar_rama_de_raiz(self):
        estructura_inicial = [["1", True, False, ["2", "0"]], ["2", False, True, ["3", "0"]], ["3", False, True, ["4", "0"]], ["4", False, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "0"]], ["2", False, True, ["3", "0"]], ["3", False, True, ["4", "0"]], ["4", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        posibilidad_1 = [True, [["Quitar Nodo", "4"], ["Quitar Nodo", "3"], ["Quitar Nodo", "2"]]]
        posibilidad_2 = [True, [["Quitar Nodo", "3"], ["Quitar Nodo", "2"]]]
        posibilidad_3 = [True, [["Quitar Nodo", "2"]]]
        soluciones = [posibilidad_1, posibilidad_2, posibilidad_3]

        self.assertIn(resultado_estudiante, soluciones)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_09_repetido_cortes(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "0"]], ["3", True, False, ["6", "0"]],[ "4", False, True, ["5", "0"]], ["5", False, True, ["0", "0"]], ["6", False, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "0"]], ["3", True, False, ["6", "0"]],[ "4", False, True, ["5", "0"]], ["5", False, True, ["0", "0"]], ["6", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        posibilidad_1 = [True, [["Quitar Nodo", "5"], ["Quitar Nodo", "4"], ["Quitar Nodo", "6"]]]
        posibilidad_2 = [True, [["Quitar Nodo", "4"], ["Quitar Nodo", "6"]]]
        posibilidad_3 = [True, [["Quitar Nodo", "6"], ["Quitar Nodo", "4"]]]
        posibilidad_4 = [True, [["Quitar Nodo", "6"], ["Quitar Nodo", "5"]], ["Quitar Nodo", "4"]]
        posibilidades = [posibilidad_1, posibilidad_2, posibilidad_3, posibilidad_4]

        self.assertIn(resultado_estudiante, posibilidades)
        self.assertCountEqual(bonsai.estructura, estructura_final)
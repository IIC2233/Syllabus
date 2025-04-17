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
    def test_00_nivel_4_izquierda(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "0"]], ["6", False, False, ["0", "11"]], ["7", False, False, ["12", "13"]],
            ["8", False, False, ["14", "15"]], ["9", False, False, ["16", "0"]], ["10", False, False, ["17", "18"]], ["11", False, False, ["19", "20"]],
            ["12", False, False, ["0", "0"]], ["13", False, False, ["0", "0"]], ["14", False, True, ["0", "0"]], ["15", False, True, ["0", "0"]],
            ["16", False, True, ["0", "0"]], ["17", False, True, ["0", "0"]], ["18", False, True, ["0", "0"]], ["19", True, False, ["0", "0"]],
            ["20", True, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "0"]], ["6", False, False, ["0", "11"]], ["7", False, False, ["12", "13"]],
            ["8", False, False, ["14", "15"]], ["9", False, False, ["16", "0"]], ["10", False, False, ["17", "18"]], ["11", False, False, ["19", "20"]],
            ["12", False, False, ["0", "0"]], ["13", False, False, ["0", "0"]], ["14", False, True, ["0", "0"]], ["15", False, True, ["0", "0"]],
            ["16", False, True, ["0", "0"]], ["17", False, True, ["0", "0"]], ["18", False, True, ["0", "0"]], ["19", True, False, ["0", "0"]],
            ["20", True, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "14"], ["Quitar Nodo", "15"], ["Quitar Nodo", "16"], ["Modificar Flor", "17"], ["Modificar Flor", "18"]]

        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_01_nivel_4_dos_lados(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, True, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", True, True, ["8", "9"]], ["5", True, True, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["0", "0"]], ["10", False, False, ["18", "19"]], ["11", False, False, ["20", "21"]],
            ["12", False, False, ["22", "23"]], ["13", False, False, ["24", "25"]], ["14", False, False, ["26", "27"]], ["15", False, False, ["0", "0"]],
            ["16", False, True, ["0", "0"]], ["17", False, True, ["0", "0"]], ["18", False, False, ["0", "0"]], ["19", False, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", True, True, ["0", "0"]], ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]], ["25", False, False, ["0", "0"]], ["26", False, True, ["0", "0"]], ["27", False, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, True, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", True, True, ["8", "9"]], ["5", True, True, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["0", "0"]], ["10", False, False, ["18", "19"]], ["11", False, False, ["20", "21"]],
            ["12", False, False, ["22", "23"]], ["13", False, False, ["24", "25"]], ["14", False, False, ["26", "27"]], ["15", False, False, ["0", "0"]],
            ["16", False, True, ["0", "0"]], ["17", False, True, ["0", "0"]], ["18", False, False, ["0", "0"]], ["19", False, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", True, True, ["0", "0"]], ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]], ["25", False, False, ["0", "0"]], ["26", False, True, ["0", "0"]], ["27", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "16"], ["Quitar Nodo", "17"], ["Quitar Nodo", "26"], ["Quitar Nodo", "27"], ["Modificar Flor", "2"], ["Modificar Flor", "4"], ["Modificar Flor", "5"], ["Modificar Flor", "22"], ["Modificar Flor", "23"]]

        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_02_solo_flores(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", True, True, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", True, True, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["0", "0"]], ["10", False, False, ["18", "19"]], ["11", False, False, ["0", "0"]],
            ["12", False, False, ["0", "0"]], ["13", False, False, ["20", "21"]], ["14", False, False, ["0", "0"]], ["15", False, False, ["22", "23"]],
            ["16", True, True, ["0", "0"]], ["17", False, False, ["0", "0"]], ["18", True, True, ["0", "0"]], ["19", False, False, ["0", "0"]],
            ["20", True, True, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", True, True, ["0", "0"]], ["23", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", True, True, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", True, True, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["0", "0"]], ["10", False, False, ["18", "19"]], ["11", False, False, ["0", "0"]],
            ["12", False, False, ["0", "0"]], ["13", False, False, ["20", "21"]], ["14", False, False, ["0", "0"]], ["15", False, False, ["22", "23"]],
            ["16", True, True, ["0", "0"]], ["17", False, False, ["0", "0"]], ["18", True, True, ["0", "0"]], ["19", False, False, ["0", "0"]],
            ["20", True, True, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", True, True, ["0", "0"]], ["23", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Modificar Flor", "4"], ["Modificar Flor", "6"], ["Modificar Flor", "16"], ["Modificar Flor", "18"], ["Modificar Flor", "20"], ["Modificar Flor", "22"]]

        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_03_cortar_hasta_3_nivel_5(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["0", "10"]], ["6", False, False, ["11", "0"]], ["7", False, False, ["12", "13"]],
            ["8", False, False, ["14", "0"]], ["9", False, False, ["0", "16"]], ["10", False, False, ["18", "0"]], ["11", False, False, ["19", "0"]],
            ["12", False, False, ["0", "20"]], ["13", False, False, ["21", "0"]], ["14", False, True, ["15", "0"]], ["15", False, True, ["0", "0"]],
            ["16", False, True, ["0", "17"]], ["17", False, True, ["0", "0"]], ["18", False, True, ["0", "0"]], ["19", False, True, ["0", "0"]],
            ["20", False, True, ["0", "0"]], ["21", False, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["0", "10"]], ["6", False, False, ["11", "0"]], ["7", False, False, ["12", "13"]],
            ["8", False, False, ["14", "0"]], ["9", False, False, ["0", "16"]], ["10", False, False, ["18", "0"]], ["11", False, False, ["19", "0"]],
            ["12", False, False, ["0", "20"]], ["13", False, False, ["21", "0"]], ["14", False, True, ["15", "0"]], ["15", False, True, ["0", "0"]],
            ["16", False, True, ["0", "17"]], ["17", False, True, ["0", "0"]], ["18", False, True, ["0", "0"]], ["19", False, True, ["0", "0"]],
            ["20", False, True, ["0", "0"]], ["21", False, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        posibilidad_1 = [["Quitar Nodo", "14"], ["Quitar Nodo", "16"], ["Quitar Nodo", "18"], ["Quitar Nodo", "19"], ["Quitar Nodo", "20"], ["Quitar Nodo", "21"]]
        posibilidad_2 = [["Quitar Nodo", "15"], ["Quitar Nodo", "14"], ["Quitar Nodo", "16"], ["Quitar Nodo", "18"], ["Quitar Nodo", "19"], ["Quitar Nodo", "20"], ["Quitar Nodo", "21"]]
        posibilidad_3 = [["Quitar Nodo", "15"], ["Quitar Nodo", "14"], ["Quitar Nodo", "17"], ["Quitar Nodo", "16"], ["Quitar Nodo", "18"], ["Quitar Nodo", "19"], ["Quitar Nodo", "20"], ["Quitar Nodo", "21"]]
        posibilidad_4 = [ ["Quitar Nodo", "14"], ["Quitar Nodo", "17"], ["Quitar Nodo", "16"], ["Quitar Nodo", "18"], ["Quitar Nodo", "19"], ["Quitar Nodo", "20"], ["Quitar Nodo", "21"]]
        soluciones = [posibilidad_1, posibilidad_2, posibilidad_3, posibilidad_4]

        self.assertEqual(resultado_estudiante[0], True)
        # Esto permite revisar si cualquiera de los anteriores se cumple, sin importar el orden, lo que es más fácil que pensar en todos los ordenes posibles
        self.assertTrue(any(
            self.assertCountEqual(resultado_estudiante[1], solucion) is None  
            for solucion in soluciones
        ))
        self.assertCountEqual(bonsai.estructura, estructura_final)



    @timeout(N_SECOND)
    def test_04_nivel_5_casi_parejo(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "49"]], ["25", False, False, ["50", "51"]], ["26", False, False, ["52", "53"]], ["27", False, False, ["54", "55"]],
            ["28", False, False, ["56", "57"]], ["29", False, False, ["58", "59"]], ["30", False, False, ["60", "61"]], ["31", False, False, ["62", "0"]],
            ["32", False, True, ["0", "0"]], ["33", False, False, ["0", "0"]], ["34", False, False, ["0", "0"]], ["35", False, False, ["0", "0"]],
            ["36", False, False, ["0", "0"]], ["37", False, False, ["0", "0"]], ["38", False, False, ["0", "0"]], ["39", False, False, ["0", "0"]],
            ["40", False, False, ["0", "0"]], ["41", False, False, ["0", "0"]], ["42", False, False, ["0", "0"]], ["43", False, False, ["0", "0"]],
            ["44", False, False, ["0", "0"]], ["45", False, False, ["0", "0"]], ["46", False, False, ["0", "0"]], ["47", False, False, ["0", "0"]],
            ["48", False, False, ["0", "0"]], ["49", False, False, ["0", "0"]], ["50", False, False, ["0", "0"]], ["51", False, False, ["0", "0"]],
            ["52", False, False, ["0", "0"]], ["53", False, False, ["0", "0"]], ["54", False, False, ["0", "0"]], ["55", False, False, ["0", "0"]],
            ["56", False, False, ["0", "0"]], ["57", False, False, ["0", "0"]], ["58", False, False, ["0", "0"]], ["59", False, False, ["0", "0"]],
            ["60", False, False, ["0", "0"]], ["61", False, False, ["0", "0"]], ["62", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "49"]], ["25", False, False, ["50", "51"]], ["26", False, False, ["52", "53"]], ["27", False, False, ["54", "55"]],
            ["28", False, False, ["56", "57"]], ["29", False, False, ["58", "59"]], ["30", False, False, ["60", "61"]], ["31", False, False, ["62", "0"]],
            ["32", False, True, ["0", "0"]], ["33", False, False, ["0", "0"]], ["34", False, False, ["0", "0"]], ["35", False, False, ["0", "0"]],
            ["36", False, False, ["0", "0"]], ["37", False, False, ["0", "0"]], ["38", False, False, ["0", "0"]], ["39", False, False, ["0", "0"]],
            ["40", False, False, ["0", "0"]], ["41", False, False, ["0", "0"]], ["42", False, False, ["0", "0"]], ["43", False, False, ["0", "0"]],
            ["44", False, False, ["0", "0"]], ["45", False, False, ["0", "0"]], ["46", False, False, ["0", "0"]], ["47", False, False, ["0", "0"]],
            ["48", False, False, ["0", "0"]], ["49", False, False, ["0", "0"]], ["50", False, False, ["0", "0"]], ["51", False, False, ["0", "0"]],
            ["52", False, False, ["0", "0"]], ["53", False, False, ["0", "0"]], ["54", False, False, ["0", "0"]], ["55", False, False, ["0", "0"]],
            ["56", False, False, ["0", "0"]], ["57", False, False, ["0", "0"]], ["58", False, False, ["0", "0"]], ["59", False, False, ["0", "0"]],
            ["60", False, False, ["0", "0"]], ["61", False, False, ["0", "0"]], ["62", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "32"]]

        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_05_nivel_5_izquierda(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "0"]], ["25", False, False, ["50", "0"]], ["26", False, False, ["52", "0"]], ["27", False, False, ["54", "0"]],
            ["28", False, False, ["56", "0"]], ["29", False, False, ["58", "0"]], ["30", False, False, ["60", "0"]], ["31", False, False, ["62", "0"]],
            ["32", False, True, ["0", "0"]], ["33", False, False, ["0", "0"]], ["34", False, True, ["0", "0"]], ["35", False, False, ["0", "0"]],
            ["36", False, True, ["0", "0"]], ["37", False, False, ["0", "0"]], ["38", False, True, ["0", "0"]], ["39", False, False, ["0", "0"]],
            ["40", False, True, ["0", "0"]], ["41", False, False, ["0", "0"]], ["42", False, True, ["0", "0"]], ["43", False, False, ["0", "0"]],
            ["44", False, True, ["0", "0"]], ["45", False, False, ["0", "0"]], ["46", False, True, ["0", "0"]], ["47", False, False, ["0", "0"]],
            ["48", False, False, ["0", "0"]], ["50", False, False, ["0", "0"]], ["52", False, False, ["0", "0"]],  ["54", False, False, ["0", "0"]],
            ["56", False, False, ["0", "0"]], ["58", False, False, ["0", "0"]], ["60", False, False, ["0", "0"]], ["62", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "0"]], ["25", False, False, ["50", "0"]], ["26", False, False, ["52", "0"]], ["27", False, False, ["54", "0"]],
            ["28", False, False, ["56", "0"]], ["29", False, False, ["58", "0"]], ["30", False, False, ["60", "0"]], ["31", False, False, ["62", "0"]],
            ["32", False, True, ["0", "0"]], ["33", False, False, ["0", "0"]], ["34", False, True, ["0", "0"]], ["35", False, False, ["0", "0"]],
            ["36", False, True, ["0", "0"]], ["37", False, False, ["0", "0"]], ["38", False, True, ["0", "0"]], ["39", False, False, ["0", "0"]],
            ["40", False, True, ["0", "0"]], ["41", False, False, ["0", "0"]], ["42", False, True, ["0", "0"]], ["43", False, False, ["0", "0"]],
            ["44", False, True, ["0", "0"]], ["45", False, False, ["0", "0"]], ["46", False, True, ["0", "0"]], ["47", False, False, ["0", "0"]],
            ["48", False, False, ["0", "0"]], ["50", False, False, ["0", "0"]], ["52", False, False, ["0", "0"]],  ["54", False, False, ["0", "0"]],
            ["56", False, False, ["0", "0"]], ["58", False, False, ["0", "0"]], ["60", False, False, ["0", "0"]], ["62", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "32"], ["Quitar Nodo", "34"], ["Quitar Nodo", "36"], ["Quitar Nodo", "38"], ["Quitar Nodo", "40"], ["Quitar Nodo", "42"], ["Quitar Nodo", "44"], ["Quitar Nodo", "46"]]
        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)



    @timeout(N_SECOND)
    def test_06_nivel_5_dos_lados(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "0"]], ["25", False, False, ["50", "0"]], ["26", False, False, ["52", "0"]], ["27", False, False, ["54", "0"]],
            ["28", False, False, ["56", "0"]], ["29", False, False, ["58", "0"]], ["30", False, False, ["60", "0"]], ["31", False, False, ["62", "0"]],
            ["32", False, True, ["0", "0"]], ["33", False, False, ["0", "0"]], ["34", False, True, ["0", "0"]], ["35", False, False, ["0", "0"]],
            ["36", False, True, ["0", "0"]], ["37", False, False, ["0", "0"]], ["38", False, True, ["0", "0"]], ["39", False, False, ["0", "0"]],
            ["40", False, True, ["0", "0"]], ["41", False, False, ["0", "0"]], ["42", False, True, ["0", "0"]], ["43", False, False, ["0", "0"]],
            ["44", False, True, ["0", "0"]], ["45", False, False, ["0", "0"]], ["46", False, True, ["0", "0"]], ["47", False, False, ["0", "0"]],
            ["48", True, True, ["0", "0"]], ["50", True, True, ["0", "0"]], ["52", True, True, ["0", "0"]],  ["54", True, True, ["0", "0"]],
            ["56", True, True, ["0", "0"]], ["58", True, True, ["0", "0"]], ["60", True, True, ["0", "0"]], ["62", True, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "0"]], ["25", False, False, ["50", "0"]], ["26", False, False, ["52", "0"]], ["27", False, False, ["54", "0"]],
            ["28", False, False, ["56", "0"]], ["29", False, False, ["58", "0"]], ["30", False, False, ["60", "0"]], ["31", False, False, ["62", "0"]],
            ["32", False, True, ["0", "0"]], ["33", False, False, ["0", "0"]], ["34", False, True, ["0", "0"]], ["35", False, False, ["0", "0"]],
            ["36", False, True, ["0", "0"]], ["37", False, False, ["0", "0"]], ["38", False, True, ["0", "0"]], ["39", False, False, ["0", "0"]],
            ["40", False, True, ["0", "0"]], ["41", False, False, ["0", "0"]], ["42", False, True, ["0", "0"]], ["43", False, False, ["0", "0"]],
            ["44", False, True, ["0", "0"]], ["45", False, False, ["0", "0"]], ["46", False, True, ["0", "0"]], ["47", False, False, ["0", "0"]],
            ["48", True, True, ["0", "0"]], ["50", True, True, ["0", "0"]], ["52", True, True, ["0", "0"]],  ["54", True, True, ["0", "0"]],
            ["56", True, True, ["0", "0"]], ["58", True, True, ["0", "0"]], ["60", True, True, ["0", "0"]], ["62", True, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "32"], ["Quitar Nodo", "34"], ["Quitar Nodo", "36"], ["Quitar Nodo", "38"], ["Quitar Nodo", "40"], ["Quitar Nodo", "42"], ["Quitar Nodo", "44"], ["Quitar Nodo", "46"], ["Modificar Flor", "48"], ["Modificar Flor", "50"], ["Modificar Flor", "52"], ["Modificar Flor", "54"], ["Modificar Flor", "56"], ["Modificar Flor", "58"], ["Modificar Flor", "60"], ["Modificar Flor", "62"]]
        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_07_nivel_6_casi_parejo(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "49"]], ["25", False, False, ["50", "51"]], ["26", False, False, ["52", "53"]], ["27", False, False, ["54", "55"]],
            ["28", False, False, ["56", "57"]], ["29", False, False, ["58", "59"]], ["30", False, False, ["60", "61"]], ["31", False, False, ["62", "63"]],
            ["32", False, False, ["64", "65"]], ["33", False, False, ["66", "67"]], ["34", False, False, ["68", "69"]], ["35", False, False, ["70", "71"]],
            ["36", False, False, ["72", "73"]], ["37", False, False, ["74", "75"]], ["38", False, False, ["76", "77"]], ["39", False, False, ["78", "79"]],
            ["40", False, False, ["80", "81"]], ["41", False, False, ["82", "83"]], ["42", False, False, ["84", "85"]], ["43", False, False, ["86", "87"]],
            ["44", False, False, ["88", "89"]], ["45", False, False, ["90", "91"]], ["46", False, False, ["92", "93"]], ["47", False, False, ["94", "95"]],
            ["48", False, False, ["96", "97"]], ["49", False, False, ["98", "99"]], ["50", False, False, ["100", "101"]], ["51", False, False, ["102", "103"]],
            ["52", False, False, ["104", "105"]], ["53", False, False, ["106", "107"]], ["54", False, False, ["108", "109"]], ["55", False, False, ["110", "111"]],
            ["56", False, False, ["112", "113"]], ["57", False, False, ["114", "115"]], ["58", False, False, ["116", "117"]], ["59", False, False, ["118", "119"]],
            ["60", False, False, ["120", "121"]], ["61", False, False, ["122", "123"]], ["62", False, False, ["124", "125"]], ["63", False, False, ["126", "0"]],
            ["64", False, True, ["0", "0"]], ["65", False, False, ["0", "0"]], ["66", False, False, ["0", "0"]], ["67", False, False, ["0", "0"]],
            ["68", False, False, ["0", "0"]], ["69", False, False, ["0", "0"]], ["70", False, False, ["0", "0"]], ["71", False, False, ["0", "0"]],
            ["72", False, False, ["0", "0"]], ["73", False, False, ["0", "0"]], ["74", False, False, ["0", "0"]], ["75", False, False, ["0", "0"]],
            ["76", False, False, ["0", "0"]], ["77", False, False, ["0", "0"]], ["78", False, False, ["0", "0"]], ["79", False, False, ["0", "0"]],
            ["80", False, False, ["0", "0"]], ["81", False, False, ["0", "0"]], ["82", False, False, ["0", "0"]], ["83", False, False, ["0", "0"]],
            ["84", False, False, ["0", "0"]], ["85", False, False, ["0", "0"]], ["86", False, False, ["0", "0"]], ["87", False, False, ["0", "0"]],
            ["88", False, False, ["0", "0"]], ["89", False, False, ["0", "0"]], ["90", False, False, ["0", "0"]], ["91", False, False, ["0", "0"]],
            ["92", False, False, ["0", "0"]], ["93", False, False, ["0", "0"]], ["94", False, False, ["0", "0"]], ["95", False, False, ["0", "0"]],
            ["96", False, False, ["0", "0"]], ["97", False, False, ["0", "0"]], ["98", False, False, ["0", "0"]], ["99", False, False, ["0", "0"]],
            ["100", False, False, ["0", "0"]], ["101", False, False, ["0", "0"]], ["102", False, False, ["0", "0"]], ["103", False, False, ["0", "0"]],
            ["104", False, False, ["0", "0"]], ["105", False, False, ["0", "0"]], ["106", False, False, ["0", "0"]], ["107", False, False, ["0", "0"]],
            ["108", False, False, ["0", "0"]], ["109", False, False, ["0", "0"]], ["110", False, False, ["0", "0"]], ["111", False, False, ["0", "0"]],
            ["112", False, False, ["0", "0"]], ["113", False, False, ["0", "0"]], ["114", False, False, ["0", "0"]], ["115", False, False, ["0", "0"]],
            ["116", False, False, ["0", "0"]], ["117", False, False, ["0", "0"]], ["118", False, False, ["0", "0"]], ["119", False, False, ["0", "0"]],
            ["120", False, False, ["0", "0"]], ["121", False, False, ["0", "0"]], ["122", False, False, ["0", "0"]], ["123", False, False, ["0", "0"]],
            ["124", False, False, ["0", "0"]], ["125", False, False, ["0", "0"]], ["126", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "49"]], ["25", False, False, ["50", "51"]], ["26", False, False, ["52", "53"]], ["27", False, False, ["54", "55"]],
            ["28", False, False, ["56", "57"]], ["29", False, False, ["58", "59"]], ["30", False, False, ["60", "61"]], ["31", False, False, ["62", "63"]],
            ["32", False, False, ["64", "65"]], ["33", False, False, ["66", "67"]], ["34", False, False, ["68", "69"]], ["35", False, False, ["70", "71"]],
            ["36", False, False, ["72", "73"]], ["37", False, False, ["74", "75"]], ["38", False, False, ["76", "77"]], ["39", False, False, ["78", "79"]],
            ["40", False, False, ["80", "81"]], ["41", False, False, ["82", "83"]], ["42", False, False, ["84", "85"]], ["43", False, False, ["86", "87"]],
            ["44", False, False, ["88", "89"]], ["45", False, False, ["90", "91"]], ["46", False, False, ["92", "93"]], ["47", False, False, ["94", "95"]],
            ["48", False, False, ["96", "97"]], ["49", False, False, ["98", "99"]], ["50", False, False, ["100", "101"]], ["51", False, False, ["102", "103"]],
            ["52", False, False, ["104", "105"]], ["53", False, False, ["106", "107"]], ["54", False, False, ["108", "109"]], ["55", False, False, ["110", "111"]],
            ["56", False, False, ["112", "113"]], ["57", False, False, ["114", "115"]], ["58", False, False, ["116", "117"]], ["59", False, False, ["118", "119"]],
            ["60", False, False, ["120", "121"]], ["61", False, False, ["122", "123"]], ["62", False, False, ["124", "125"]], ["63", False, False, ["126", "0"]],
            ["64", False, True, ["0", "0"]], ["65", False, False, ["0", "0"]], ["66", False, False, ["0", "0"]], ["67", False, False, ["0", "0"]],
            ["68", False, False, ["0", "0"]], ["69", False, False, ["0", "0"]], ["70", False, False, ["0", "0"]], ["71", False, False, ["0", "0"]],
            ["72", False, False, ["0", "0"]], ["73", False, False, ["0", "0"]], ["74", False, False, ["0", "0"]], ["75", False, False, ["0", "0"]],
            ["76", False, False, ["0", "0"]], ["77", False, False, ["0", "0"]], ["78", False, False, ["0", "0"]], ["79", False, False, ["0", "0"]],
            ["80", False, False, ["0", "0"]], ["81", False, False, ["0", "0"]], ["82", False, False, ["0", "0"]], ["83", False, False, ["0", "0"]],
            ["84", False, False, ["0", "0"]], ["85", False, False, ["0", "0"]], ["86", False, False, ["0", "0"]], ["87", False, False, ["0", "0"]],
            ["88", False, False, ["0", "0"]], ["89", False, False, ["0", "0"]], ["90", False, False, ["0", "0"]], ["91", False, False, ["0", "0"]],
            ["92", False, False, ["0", "0"]], ["93", False, False, ["0", "0"]], ["94", False, False, ["0", "0"]], ["95", False, False, ["0", "0"]],
            ["96", False, False, ["0", "0"]], ["97", False, False, ["0", "0"]], ["98", False, False, ["0", "0"]], ["99", False, False, ["0", "0"]],
            ["100", False, False, ["0", "0"]], ["101", False, False, ["0", "0"]], ["102", False, False, ["0", "0"]], ["103", False, False, ["0", "0"]],
            ["104", False, False, ["0", "0"]], ["105", False, False, ["0", "0"]], ["106", False, False, ["0", "0"]], ["107", False, False, ["0", "0"]],
            ["108", False, False, ["0", "0"]], ["109", False, False, ["0", "0"]], ["110", False, False, ["0", "0"]], ["111", False, False, ["0", "0"]],
            ["112", False, False, ["0", "0"]], ["113", False, False, ["0", "0"]], ["114", False, False, ["0", "0"]], ["115", False, False, ["0", "0"]],
            ["116", False, False, ["0", "0"]], ["117", False, False, ["0", "0"]], ["118", False, False, ["0", "0"]], ["119", False, False, ["0", "0"]],
            ["120", False, False, ["0", "0"]], ["121", False, False, ["0", "0"]], ["122", False, False, ["0", "0"]], ["123", False, False, ["0", "0"]],
            ["124", False, False, ["0", "0"]], ["125", False, False, ["0", "0"]], ["126", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "64"]]
        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)



    @timeout(N_SECOND)
    def test_08_nivel_6_izquierda(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "49"]], ["25", False, False, ["50", "51"]], ["26", False, False, ["52", "53"]], ["27", False, False, ["54", "55"]],
            ["28", False, False, ["56", "57"]], ["29", False, False, ["58", "59"]], ["30", False, False, ["60", "61"]], ["31", False, False, ["62", "63"]],
            ["32", False, False, ["64", "65"]], ["33", False, False, ["66", "67"]], ["34", False, False, ["68", "69"]], ["35", False, False, ["70", "71"]],
            ["36", False, False, ["72", "73"]], ["37", False, False, ["74", "75"]], ["38", False, False, ["76", "77"]], ["39", False, False, ["78", "79"]],
            ["40", False, False, ["80", "81"]], ["41", False, False, ["82", "83"]], ["42", False, False, ["84", "85"]], ["43", False, False, ["86", "87"]],
            ["44", False, False, ["88", "89"]], ["45", False, False, ["90", "91"]], ["46", False, False, ["92", "93"]], ["47", False, False, ["94", "95"]],
            ["48", False, False, ["96", "0"]], ["49", False, False, ["98", "0"]], ["50", False, False, ["100", "0"]], ["51", False, False, ["102", "0"]],
            ["52", False, False, ["104", "0"]], ["53", False, False, ["106", "0"]], ["54", False, False, ["108", "0"]], ["55", False, False, ["110", "0"]],
            ["56", False, False, ["112", "0"]], ["57", False, False, ["114", "0"]], ["58", False, False, ["116", "0"]], ["59", False, False, ["118", "0"]],
            ["60", False, False, ["120", "0"]], ["61", False, False, ["122", "0"]], ["62", False, False, ["124", "0"]], ["63", False, False, ["126", "0"]],
            ["64", False, True, ["0", "0"]], ["65", False, False, ["0", "0"]], ["66", False, True, ["0", "0"]], ["67", False, False, ["0", "0"]],
            ["68", False, True, ["0", "0"]], ["69", False, False, ["0", "0"]], ["70", False, True, ["0", "0"]], ["71", False, False, ["0", "0"]],
            ["72", False, True, ["0", "0"]], ["73", False, False, ["0", "0"]], ["74", False, True, ["0", "0"]], ["75", False, False, ["0", "0"]],
            ["76", False, True, ["0", "0"]], ["77", False, False, ["0", "0"]], ["78", False, True, ["0", "0"]], ["79", False, False, ["0", "0"]],
            ["80", False, True, ["0", "0"]], ["81", False, False, ["0", "0"]], ["82", False, True, ["0", "0"]], ["83", False, False, ["0", "0"]],
            ["84", False, True, ["0", "0"]], ["85", False, False, ["0", "0"]], ["86", False, True, ["0", "0"]], ["87", False, False, ["0", "0"]],
            ["88", False, True, ["0", "0"]], ["89", False, False, ["0", "0"]], ["90", False, True, ["0", "0"]], ["91", False, False, ["0", "0"]],
            ["92", False, True, ["0", "0"]], ["93", False, False, ["0", "0"]], ["94", False, True, ["0", "0"]], ["95", False, False, ["0", "0"]],
            ["96", False, False, ["0", "0"]], ["98", False, False, ["0", "0"]], ["100", False, False, ["0", "0"]], ["102", False, False, ["0", "0"]], 
            ["104", False, False, ["0", "0"]], ["106", False, False, ["0", "0"]], ["108", False, False, ["0", "0"]], ["110", False, False, ["0", "0"]],
            ["112", False, False, ["0", "0"]], ["114", False, False, ["0", "0"]], ["116", False, False, ["0", "0"]], ["118", False, False, ["0", "0"]],
            ["120", False, False, ["0", "0"]], ["122", False, False, ["0", "0"]], ["124", False, False, ["0", "0"]], ["126", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "49"]], ["25", False, False, ["50", "51"]], ["26", False, False, ["52", "53"]], ["27", False, False, ["54", "55"]],
            ["28", False, False, ["56", "57"]], ["29", False, False, ["58", "59"]], ["30", False, False, ["60", "61"]], ["31", False, False, ["62", "63"]],
            ["32", False, False, ["64", "65"]], ["33", False, False, ["66", "67"]], ["34", False, False, ["68", "69"]], ["35", False, False, ["70", "71"]],
            ["36", False, False, ["72", "73"]], ["37", False, False, ["74", "75"]], ["38", False, False, ["76", "77"]], ["39", False, False, ["78", "79"]],
            ["40", False, False, ["80", "81"]], ["41", False, False, ["82", "83"]], ["42", False, False, ["84", "85"]], ["43", False, False, ["86", "87"]],
            ["44", False, False, ["88", "89"]], ["45", False, False, ["90", "91"]], ["46", False, False, ["92", "93"]], ["47", False, False, ["94", "95"]],
            ["48", False, False, ["96", "0"]], ["49", False, False, ["98", "0"]], ["50", False, False, ["100", "0"]], ["51", False, False, ["102", "0"]],
            ["52", False, False, ["104", "0"]], ["53", False, False, ["106", "0"]], ["54", False, False, ["108", "0"]], ["55", False, False, ["110", "0"]],
            ["56", False, False, ["112", "0"]], ["57", False, False, ["114", "0"]], ["58", False, False, ["116", "0"]], ["59", False, False, ["118", "0"]],
            ["60", False, False, ["120", "0"]], ["61", False, False, ["122", "0"]], ["62", False, False, ["124", "0"]], ["63", False, False, ["126", "0"]],
            ["64", False, True, ["0", "0"]], ["65", False, False, ["0", "0"]], ["66", False, True, ["0", "0"]], ["67", False, False, ["0", "0"]],
            ["68", False, True, ["0", "0"]], ["69", False, False, ["0", "0"]], ["70", False, True, ["0", "0"]], ["71", False, False, ["0", "0"]],
            ["72", False, True, ["0", "0"]], ["73", False, False, ["0", "0"]], ["74", False, True, ["0", "0"]], ["75", False, False, ["0", "0"]],
            ["76", False, True, ["0", "0"]], ["77", False, False, ["0", "0"]], ["78", False, True, ["0", "0"]], ["79", False, False, ["0", "0"]],
            ["80", False, True, ["0", "0"]], ["81", False, False, ["0", "0"]], ["82", False, True, ["0", "0"]], ["83", False, False, ["0", "0"]],
            ["84", False, True, ["0", "0"]], ["85", False, False, ["0", "0"]], ["86", False, True, ["0", "0"]], ["87", False, False, ["0", "0"]],
            ["88", False, True, ["0", "0"]], ["89", False, False, ["0", "0"]], ["90", False, True, ["0", "0"]], ["91", False, False, ["0", "0"]],
            ["92", False, True, ["0", "0"]], ["93", False, False, ["0", "0"]], ["94", False, True, ["0", "0"]], ["95", False, False, ["0", "0"]],
            ["96", False, False, ["0", "0"]], ["98", False, False, ["0", "0"]], ["100", False, False, ["0", "0"]], ["102", False, False, ["0", "0"]], 
            ["104", False, False, ["0", "0"]], ["106", False, False, ["0", "0"]], ["108", False, False, ["0", "0"]], ["110", False, False, ["0", "0"]],
            ["112", False, False, ["0", "0"]], ["114", False, False, ["0", "0"]], ["116", False, False, ["0", "0"]], ["118", False, False, ["0", "0"]],
            ["120", False, False, ["0", "0"]], ["122", False, False, ["0", "0"]], ["124", False, False, ["0", "0"]], ["126", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "64"], ["Quitar Nodo", "66"], ["Quitar Nodo", "68"], ["Quitar Nodo", "70"], ["Quitar Nodo", "72"], ["Quitar Nodo", "74"], ["Quitar Nodo", "76"], ["Quitar Nodo", "78"], ["Quitar Nodo", "80"], ["Quitar Nodo", "82"], ["Quitar Nodo", "84"], ["Quitar Nodo", "86"], ["Quitar Nodo", "88"], ["Quitar Nodo", "90"], ["Quitar Nodo", "92"], ["Quitar Nodo", "94"]]
        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_09_nivel_6_dos_lados(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "49"]], ["25", False, False, ["50", "51"]], ["26", False, False, ["52", "53"]], ["27", False, False, ["54", "55"]],
            ["28", False, False, ["56", "57"]], ["29", False, False, ["58", "59"]], ["30", False, False, ["60", "61"]], ["31", False, False, ["62", "63"]],
            ["32", False, False, ["64", "65"]], ["33", False, False, ["66", "67"]], ["34", False, False, ["68", "69"]], ["35", False, False, ["70", "71"]],
            ["36", False, False, ["72", "73"]], ["37", False, False, ["74", "75"]], ["38", False, False, ["76", "77"]], ["39", False, False, ["78", "79"]],
            ["40", False, False, ["80", "81"]], ["41", False, False, ["82", "83"]], ["42", False, False, ["84", "85"]], ["43", False, False, ["86", "87"]],
            ["44", False, False, ["88", "89"]], ["45", False, False, ["90", "91"]], ["46", False, False, ["92", "93"]], ["47", False, False, ["94", "95"]],
            ["48", False, False, ["96", "0"]], ["49", False, False, ["98", "0"]], ["50", False, False, ["100", "0"]], ["51", False, False, ["102", "0"]],
            ["52", False, False, ["104", "0"]], ["53", False, False, ["106", "0"]], ["54", False, False, ["108", "0"]], ["55", False, False, ["110", "0"]],
            ["56", False, False, ["112", "0"]], ["57", False, False, ["114", "0"]], ["58", False, False, ["116", "0"]], ["59", False, False, ["118", "0"]],
            ["60", False, False, ["120", "0"]], ["61", False, False, ["122", "0"]], ["62", False, False, ["124", "0"]], ["63", False, False, ["126", "0"]],
            ["64", False, True, ["0", "0"]], ["65", False, False, ["0", "0"]], ["66", False, True, ["0", "0"]], ["67", False, False, ["0", "0"]],
            ["68", False, True, ["0", "0"]], ["69", False, False, ["0", "0"]], ["70", False, True, ["0", "0"]], ["71", False, False, ["0", "0"]],
            ["72", False, True, ["0", "0"]], ["73", False, False, ["0", "0"]], ["74", False, True, ["0", "0"]], ["75", False, False, ["0", "0"]],
            ["76", False, True, ["0", "0"]], ["77", False, False, ["0", "0"]], ["78", False, True, ["0", "0"]], ["79", False, False, ["0", "0"]],
            ["80", False, True, ["0", "0"]], ["81", False, False, ["0", "0"]], ["82", False, True, ["0", "0"]], ["83", False, False, ["0", "0"]],
            ["84", False, True, ["0", "0"]], ["85", False, False, ["0", "0"]], ["86", False, True, ["0", "0"]], ["87", False, False, ["0", "0"]],
            ["88", False, True, ["0", "0"]], ["89", False, False, ["0", "0"]], ["90", False, True, ["0", "0"]], ["91", False, False, ["0", "0"]],
            ["92", False, True, ["0", "0"]], ["93", False, False, ["0", "0"]], ["94", False, True, ["0", "0"]], ["95", False, False, ["0", "0"]],
            ["96", True, True, ["0", "0"]], ["98", True, True, ["0", "0"]], ["100", True, True, ["0", "0"]], ["102", True, True, ["0", "0"]], 
            ["104", True, True, ["0", "0"]], ["106", True, True, ["0", "0"]], ["108", True, True, ["0", "0"]], ["110", True, True, ["0", "0"]],
            ["112", True, True, ["0", "0"]], ["114", True, True, ["0", "0"]], ["116", True, True, ["0", "0"]], ["118", True, True, ["0", "0"]],
            ["120", True, True, ["0", "0"]], ["122", True, True, ["0", "0"]], ["124", True, True, ["0", "0"]], ["126", True, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]], [
            "4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
            ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
            ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
            ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
            ["20", False, False, ["40", "41"]], ["21", False, False, ["42", "43"]], ["22", False, False, ["44", "45"]], ["23", False, False, ["46", "47"]],
            ["24", False, False, ["48", "49"]], ["25", False, False, ["50", "51"]], ["26", False, False, ["52", "53"]], ["27", False, False, ["54", "55"]],
            ["28", False, False, ["56", "57"]], ["29", False, False, ["58", "59"]], ["30", False, False, ["60", "61"]], ["31", False, False, ["62", "63"]],
            ["32", False, False, ["64", "65"]], ["33", False, False, ["66", "67"]], ["34", False, False, ["68", "69"]], ["35", False, False, ["70", "71"]],
            ["36", False, False, ["72", "73"]], ["37", False, False, ["74", "75"]], ["38", False, False, ["76", "77"]], ["39", False, False, ["78", "79"]],
            ["40", False, False, ["80", "81"]], ["41", False, False, ["82", "83"]], ["42", False, False, ["84", "85"]], ["43", False, False, ["86", "87"]],
            ["44", False, False, ["88", "89"]], ["45", False, False, ["90", "91"]], ["46", False, False, ["92", "93"]], ["47", False, False, ["94", "95"]],
            ["48", False, False, ["96", "0"]], ["49", False, False, ["98", "0"]], ["50", False, False, ["100", "0"]], ["51", False, False, ["102", "0"]],
            ["52", False, False, ["104", "0"]], ["53", False, False, ["106", "0"]], ["54", False, False, ["108", "0"]], ["55", False, False, ["110", "0"]],
            ["56", False, False, ["112", "0"]], ["57", False, False, ["114", "0"]], ["58", False, False, ["116", "0"]], ["59", False, False, ["118", "0"]],
            ["60", False, False, ["120", "0"]], ["61", False, False, ["122", "0"]], ["62", False, False, ["124", "0"]], ["63", False, False, ["126", "0"]],
            ["64", False, True, ["0", "0"]], ["65", False, False, ["0", "0"]], ["66", False, True, ["0", "0"]], ["67", False, False, ["0", "0"]],
            ["68", False, True, ["0", "0"]], ["69", False, False, ["0", "0"]], ["70", False, True, ["0", "0"]], ["71", False, False, ["0", "0"]],
            ["72", False, True, ["0", "0"]], ["73", False, False, ["0", "0"]], ["74", False, True, ["0", "0"]], ["75", False, False, ["0", "0"]],
            ["76", False, True, ["0", "0"]], ["77", False, False, ["0", "0"]], ["78", False, True, ["0", "0"]], ["79", False, False, ["0", "0"]],
            ["80", False, True, ["0", "0"]], ["81", False, False, ["0", "0"]], ["82", False, True, ["0", "0"]], ["83", False, False, ["0", "0"]],
            ["84", False, True, ["0", "0"]], ["85", False, False, ["0", "0"]], ["86", False, True, ["0", "0"]], ["87", False, False, ["0", "0"]],
            ["88", False, True, ["0", "0"]], ["89", False, False, ["0", "0"]], ["90", False, True, ["0", "0"]], ["91", False, False, ["0", "0"]],
            ["92", False, True, ["0", "0"]], ["93", False, False, ["0", "0"]], ["94", False, True, ["0", "0"]], ["95", False, False, ["0", "0"]],
            ["96", True, True, ["0", "0"]], ["98", True, True, ["0", "0"]], ["100", True, True, ["0", "0"]], ["102", True, True, ["0", "0"]], 
            ["104", True, True, ["0", "0"]], ["106", True, True, ["0", "0"]], ["108", True, True, ["0", "0"]], ["110", True, True, ["0", "0"]],
            ["112", True, True, ["0", "0"]], ["114", True, True, ["0", "0"]], ["116", True, True, ["0", "0"]], ["118", True, True, ["0", "0"]],
            ["120", True, True, ["0", "0"]], ["122", True, True, ["0", "0"]], ["124", True, True, ["0", "0"]], ["126", True, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        instrucciones_sin_orden = [["Quitar Nodo", "64"], ["Quitar Nodo", "66"], ["Quitar Nodo", "68"], ["Quitar Nodo", "70"], ["Quitar Nodo", "72"], ["Quitar Nodo", "74"], ["Quitar Nodo", "76"], ["Quitar Nodo", "78"], ["Quitar Nodo", "80"], ["Quitar Nodo", "82"], ["Quitar Nodo", "84"], ["Quitar Nodo", "86"], ["Quitar Nodo", "88"], ["Quitar Nodo", "90"], ["Quitar Nodo", "92"], ["Quitar Nodo", "94"],
                                   ["Modificar Flor", "96"], ["Modificar Flor", "98"], ["Modificar Flor", "100"], ["Modificar Flor", "102"], ["Modificar Flor", "104"], ["Modificar Flor", "106"], ["Modificar Flor", "108"], ["Modificar Flor", "110"], ["Modificar Flor", "112"], ["Modificar Flor", "114"], ["Modificar Flor", "116"], ["Modificar Flor", "118"], ["Modificar Flor", "120"], ["Modificar Flor", "122"], ["Modificar Flor", "124"], ["Modificar Flor", "126"]]
        self.assertEqual(resultado_estudiante[0], True)
        self.assertCountEqual(resultado_estudiante[1], instrucciones_sin_orden)
        self.assertCountEqual(bonsai.estructura, estructura_final)
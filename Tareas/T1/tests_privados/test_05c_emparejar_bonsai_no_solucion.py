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
    def test_00_no_emparejable_flores_chico(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "0"]], ["3", True, False, ["0", "5"]], 
        ["4", True, False, ["0", "0"]], ["5", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "0"]], ["3", True, False, ["0", "5"]],
        ["4", True, False, ["0", "0"]], ["5", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_01_no_emparejable_cortes_chico(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "0"]], ["3", True, False, ["5", "0"]], 
        ["4", False, True, ["6", "0"]], ["5", False, False, ["7", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "0"]], ["3", True, False, ["5", "0"]],
        ["4", False, True, ["6", "0"]], ["5", False, False, ["7", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_02_no_emparejable_flores_grande(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", True, True, ["8", "9"]], ["5", True, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
        ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]], ["10", True, True, ["0", "0"]], ["11", True, False, ["0", "0"]],
        ["12", False, False, ["0", "0"]], ["13", False, False, ["0", "0"]], ["14", True, False, ["0", "0"]], ["15", True, True, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", True, True, ["8", "9"]], ["5", True, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
        ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]], ["10", True, True, ["0", "0"]], ["11", True, False, ["0", "0"]],
        ["12", False, False, ["0", "0"]], ["13", False, False, ["0", "0"]], ["14", True, False, ["0", "0"]], ["15", True, True, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_03_no_emparejable_cortes_grande(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", False, True, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
        ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
        ["12", False, False, ["0", "0"]], ["13", False, False, ["0", "0"]], ["14", False, False, ["0", "0"]], ["15", False, False, ["0", "0"]],
        ["16", False, False, ["0", "0"]], ["17", False, False, ["0", "0"]], ["18", False, False, ["0", "0"]], ["19", False, False, ["0", "0"]],
        ["20", False, False, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", False, False, ["0", "0"]], ["23", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", False, True, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
        ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
        ["12", False, False, ["0", "0"]], ["13", False, False, ["0", "0"]], ["14", False, False, ["0", "0"]], ["15", False, False, ["0", "0"]],
        ["16", False, False, ["0", "0"]], ["17", False, False, ["0", "0"]], ["18", False, False, ["0", "0"]], ["19", False, False, ["0", "0"]],
        ["20", False, False, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", False, False, ["0", "0"]], ["23", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_04_no_emparejable_falta__raiz(self):
        estructura_inicial = [["1", True, False, ["2", "0"]], ["2", False, False, ["3", "4"]], ["3", False, False, ["5", "6"]],
        ["4", False, False, ["7", "8"]], ["5", False, False, ["0", "0"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]],
        ["8", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "0"]], ["2", False, False, ["3", "4"]], ["3", False, False, ["5", "6"]],
        ["4", False, False, ["7", "8"]], ["5", False, False, ["0", "0"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]],
        ["8", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_05_no_emparejable_hoja_no_cortable_nivel_3(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", True, False, ["8", "9"]], ["5", True, False, ["10", "0"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]],
        ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]], ["10", True, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", True, False, ["8", "9"]], ["5", True, False, ["10", "0"]], ["6", False, False, ["0", "0"]], ["7", False, False, ["0", "0"]],
        ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]], ["10", True, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_06_no_emparejable_hoja_no_cortable_nivel_5(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
        ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
        ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
        ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
        ["20", False, False, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", False, False, ["0", "0"]], ["23", False, False, ["0", "0"]],
        ["24", False, False, ["40", "41"]], ["25", False, False, ["42", "43"]], ["26", False, False, ["44", "45"]], ["27", False, False, ["46", "47"]],
        ["28", False, False, ["0", "0"]], ["29", False, False, ["0", "0"]], ["30", False, False, ["0", "0"]], ["31", False, False, ["0", "0"]],
        ["32", False, False, ["0", "0"]], ["33", False, False, ["0", "0"]], ["34", False, False, ["0", "0"]], ["35", False, False, ["0", "0"]],
        ["36", False, False, ["0", "0"]], ["37", False, False, ["0", "0"]], ["38", False, False, ["0", "0"]], ["39", False, False, ["0", "0"]],
        ["40", False, False, ["0", "0"]], ["41", False, False, ["0", "0"]], ["42", False, False, ["0", "0"]], ["43", False, False, ["0", "0"]],
        ["44", False, False, ["0", "0"]], ["45", False, False, ["0", "0"]], ["46", False, False, ["0", "0"]], ["47", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
        ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
        ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
        ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
        ["20", False, False, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", False, False, ["0", "0"]], ["23", False, False, ["0", "0"]],
        ["24", False, False, ["40", "41"]], ["25", False, False, ["42", "43"]], ["26", False, False, ["44", "45"]], ["27", False, False, ["46", "47"]],
        ["28", False, False, ["0", "0"]], ["29", False, False, ["0", "0"]], ["30", False, False, ["0", "0"]], ["31", False, False, ["0", "0"]],
        ["32", False, False, ["0", "0"]], ["33", False, False, ["0", "0"]], ["34", False, False, ["0", "0"]], ["35", False, False, ["0", "0"]],
        ["36", False, False, ["0", "0"]], ["37", False, False, ["0", "0"]], ["38", False, False, ["0", "0"]], ["39", False, False, ["0", "0"]],
        ["40", False, False, ["0", "0"]], ["41", False, False, ["0", "0"]], ["42", False, False, ["0", "0"]], ["43", False, False, ["0", "0"]],
        ["44", False, False, ["0", "0"]], ["45", False, False, ["0", "0"]], ["46", False, False, ["0", "0"]], ["47", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_07_no_emparejable_dos_lados(self):
        estructura_inicial = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", True, False, ["6", "7"]],
        ["4", True, False, ["8", "9"]], ["5", True, False, ["10", "11"]], ["6", True, False, ["0", "0"]], ["7", True, False, ["0", "0"]],
        ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]], ["10", True, False, ["0", "0"]], ["11", True, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", True, False, ["6", "7"]],
        ["4", True, False, ["8", "9"]], ["5", True, False, ["10", "11"]], ["6", True, False, ["0", "0"]], ["7", True, False, ["0", "0"]],
        ["8", True, False, ["0", "0"]], ["9", True, False, ["0", "0"]], ["10", True, False, ["0", "0"]], ["11", True, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_08_no_emparejable_dos_lados_nivel_6(self):
        estructura_inicial =  [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
        ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
        ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
        ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
        ["20", False, False, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", False, False, ["0", "0"]], ["23", False, False, ["0", "0"]],
        ["24", False, False, ["40", "41"]], ["25", False, False, ["42", "43"]], ["26", False, False, ["44", "45"]], ["27", False, False, ["46", "47"]],
        ["28", False, False, ["0", "0"]], ["29", False, False, ["0", "0"]], ["30", False, False, ["0", "0"]], ["31", False, False, ["0", "0"]],
        ["32", False, False, ["48", "0"]], ["33", False, False, ["0", "49"]], ["34", False, False, ["50", "0"]], ["35", False, False, ["0", "51"]],
        ["36", False, False, ["52", "0"]], ["37", False, False, ["53", "0"]], ["38", False, False, ["54", "0"]], ["39", False, False, ["0", "55"]],
        ["40", False, False, ["0", "56"]], ["41", False, False, ["0", "57"]], ["42", False, False, ["0", "58"]], ["43", False, False, ["59", "0"]],
        ["44", False, False, ["0", "60"]], ["45", False, False, ["0", "61"]], ["46", False, False, ["62", "0"]], ["47", False, False, ["0", "63"]],
        ["48", False, False, ["0", "0"]], ["49", False, False, ["0", "0"]], ["50", False, False, ["0", "0"]], ["51", False, False, ["0", "0"]],
        ["52", False, False, ["0", "0"]], ["53", False, False, ["0", "0"]], ["54", False, False, ["0", "0"]], ["55", False, False, ["0", "0"]],
        ["56", False, False, ["0", "0"]], ["57", False, False, ["0", "0"]], ["58", False, False, ["0", "0"]], ["59", False, False, ["0", "0"]],
        ["60", False, False, ["0", "0"]], ["61", False, False, ["0", "0"]], ["62", False, False, ["0", "0"]], ["63", False, False, ["0", "0"]]]
        estructura_final = [["1", True, False, ["2", "3"]], ["2", False, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
        ["4", False, False, ["8", "9"]], ["5", False, False, ["10", "11"]], ["6", False, False, ["12", "13"]], ["7", False, False, ["14", "15"]],
        ["8", False, False, ["16", "17"]], ["9", False, False, ["18", "19"]], ["10", False, False, ["20", "21"]], ["11", False, False, ["22", "23"]],
        ["12", False, False, ["24", "25"]], ["13", False, False, ["26", "27"]], ["14", False, False, ["28", "29"]], ["15", False, False, ["30", "31"]],
        ["16", False, False, ["32", "33"]], ["17", False, False, ["34", "35"]], ["18", False, False, ["36", "37"]], ["19", False, False, ["38", "39"]],
        ["20", False, False, ["0", "0"]], ["21", False, False, ["0", "0"]], ["22", False, False, ["0", "0"]], ["23", False, False, ["0", "0"]],
        ["24", False, False, ["40", "41"]], ["25", False, False, ["42", "43"]], ["26", False, False, ["44", "45"]], ["27", False, False, ["46", "47"]],
        ["28", False, False, ["0", "0"]], ["29", False, False, ["0", "0"]], ["30", False, False, ["0", "0"]], ["31", False, False, ["0", "0"]],
        ["32", False, False, ["48", "0"]], ["33", False, False, ["0", "49"]], ["34", False, False, ["50", "0"]], ["35", False, False, ["0", "51"]],
        ["36", False, False, ["52", "0"]], ["37", False, False, ["53", "0"]], ["38", False, False, ["54", "0"]], ["39", False, False, ["0", "55"]],
        ["40", False, False, ["0", "56"]], ["41", False, False, ["0", "57"]], ["42", False, False, ["0", "58"]], ["43", False, False, ["59", "0"]],
        ["44", False, False, ["0", "60"]], ["45", False, False, ["0", "61"]], ["46", False, False, ["62", "0"]], ["47", False, False, ["0", "63"]],
        ["48", False, False, ["0", "0"]], ["49", False, False, ["0", "0"]], ["50", False, False, ["0", "0"]], ["51", False, False, ["0", "0"]],
        ["52", False, False, ["0", "0"]], ["53", False, False, ["0", "0"]], ["54", False, False, ["0", "0"]], ["55", False, False, ["0", "0"]],
        ["56", False, False, ["0", "0"]], ["57", False, False, ["0", "0"]], ["58", False, False, ["0", "0"]], ["59", False, False, ["0", "0"]],
        ["60", False, False, ["0", "0"]], ["61", False, False, ["0", "0"]], ["62", False, False, ["0", "0"]], ["63", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)


    @timeout(N_SECOND)
    def test_09_no_emparejable_nada_editable(self):
        estructura_inicial = [["1", False, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
                              ["4", True, False, ["0", "0"]], ["5", False, False, ["0", "0"]], ["6", True, False, ["0", "0"]], ["7", False, False, ["0", "0"]]]
        estructura_final = [["1", False, False, ["2", "3"]], ["2", True, False, ["4", "5"]], ["3", False, False, ["6", "7"]],
                            ["4", True, False, ["0", "0"]], ["5", False, False, ["0", "0"]], ["6", True, False, ["0", "0"]], ["7", False, False, ["0", "0"]]]
        bonsai = Bonsai("Arbolito", 10, 20, estructura_inicial)
        resultado_estudiante = dccortaramas.emparejar_bonsai(bonsai)

        self.assertEqual(resultado_estudiante, [False, []])
        self.assertCountEqual(bonsai.estructura, estructura_final)
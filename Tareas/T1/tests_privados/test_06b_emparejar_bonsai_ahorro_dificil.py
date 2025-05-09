import unittest
import os
import sys
from dccortaramas import Bonsai, DCCortaRamas
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 20

dccortaramas = DCCortaRamas()


class TestEmparejarBonsaiAhorroDificil(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_dos_v(self):
        """
        Bonsai de mediano misma cantidad de acciones, mas barato cortar
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", True, False, ["0", "10"]],
            ["5", False, True, ["9", "0"]],
            ["6", False, False, ["0", "8"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, True, ["14", "15"]],
            ["9", False, True, ["12", "13"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "0"]],
            ["14", False, True, ["0", "0"]],
            ["15", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", True, False, ["0", "10"]],
            ["5", False, True, ["9", "0"]],
            ["6", False, False, ["0", "8"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, True, ["14", "15"]],
            ["9", False, True, ["12", "13"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "0"]],
            ["14", False, True, ["0", "0"]],
            ["15", False, True, ["0", "0"]]
        ]

        bonsai = Bonsai("MJ", 5, 6, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        lista_esperada = [
            [True, 16, [["Quitar Nodo", "9"], [
                "Quitar Nodo", "8"], ["Modificar Flor", "11"]]],
            [True, 16, [["Quitar Nodo", "8"], [
                "Quitar Nodo", "9"], ["Modificar Flor", "11"]]],
            [True, 16, [["Quitar Nodo", "8"], [
                "Modificar Flor", "11"], ["Quitar Nodo", "9"]]],
            [True, 16, [["Quitar Nodo", "9"], [
                "Modificar Flor", "11"], ["Quitar Nodo", "8"]]],
            [True, 16, [["Modificar Flor", "11"], [
                "Quitar Nodo", "9"], ["Quitar Nodo", "8"]]],
            [True, 16, [["Modificar Flor", "11"], [
                "Quitar Nodo", "8"], ["Quitar Nodo", "9"]]]
        ]

        self.assertIn(respuesta_estudiante, lista_esperada)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_cinco_ves(self):
        """
        Bonsai de mediano misma cantidad de acciones y mismo valor cortar o flor
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", True, False, ["0", "10"]],
            ["5", False, True, ["9", "0"]],
            ["6", False, False, ["0", "8"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, True, ["14", "15"]],
            ["9", False, True, ["12", "13"]],
            ["10", False, False, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]],
            ["14", True, True, ["0", "0"]],
            ["15", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", True, False, ["0", "10"]],
            ["5", False, True, ["9", "0"]],
            ["6", False, False, ["0", "8"]],
            ["7", True, True, ["11", "0"]],
            ["8", False, True, ["14", "15"]],
            ["9", False, True, ["12", "13"]],
            ["10", False, False, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]],
            ["14", True, True, ["0", "0"]],
            ["15", False, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Roble", 6, 6, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura

        v_1 = [True, 12, [["Modificar Flor", "14"], ["Modificar Flor", "12"]]]
        v_2 = [True, 12, [["Modificar Flor", "14"], ["Modificar Flor", "15"]]]
        v_3 = [True, 12, [["Modificar Flor", "15"], ["Modificar Flor", "14"]]]
        v_4 = [True, 12, [["Modificar Flor", "15"], ["Modificar Flor", "13"]]]
        v_6 = [True, 12, [["Modificar Flor", "13"], ["Modificar Flor", "15"]]]
        v_7 = [True, 12, [["Modificar Flor", "13"], ["Modificar Flor", "12"]]]
        v_8 = [True, 12, [["Modificar Flor", "12"], ["Modificar Flor", "13"]]]
        v_9 = [True, 12, [["Modificar Flor", "12"], ["Modificar Flor", "14"]]]
        v_10 = [True, 12, [["Quitar Nodo", "9"], ["Quitar Nodo", "8"]]]
        v_5 = [True, 12, [["Quitar Nodo", "8"], ["Quitar Nodo", "9"]]]
        soluciones = [v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10]

        self.assertIn(respuesta_estudiante, soluciones)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_3_flores_baratas(self):
        """
        Bonsai grande misma cantidad de acciones y mismo valor cortar o flor
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
            ["42", False, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", False, True, ["0", "0"]],
            ["48", True, True, ["0", "0"]],
            ["49", True, True, ["0", "0"]]
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
            ["42", False, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", False, True, ["0", "0"]],
            ["48", True, True, ["0", "0"]],
            ["49", True, True, ["0", "0"]]
        ]


        bonsai = Bonsai("Nogal", 11, 7, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)

        valor_estudiante = respuesta_estudiante[0]
        precio_estudiante = respuesta_estudiante[1]
        lista_estudiante = respuesta_estudiante[2]

        estructura_estudiante = bonsai.estructura
        valor_esperado = True
        precio_esperado = 21

        
        v_1 = [
            ["Modificar Flor", "46"],
            ["Modificar Flor", "47"],
            ["Modificar Flor", "45"]]
        v_2 = [
            ["Modificar Flor", "46"],
            ["Modificar Flor", "47"],
            ["Modificar Flor", "42"]]
        v_3 = [
            ["Modificar Flor", "46"],
            ["Modificar Flor", "48"],
            ["Modificar Flor", "45"]]
        v_4 = [
            ["Modificar Flor", "46"],
            ["Modificar Flor", "48"],
            ["Modificar Flor", "42"]]
        v_5 = [
            ["Modificar Flor", "49"],
            ["Modificar Flor", "47"],
            ["Modificar Flor", "45"]]
        v_6 = [
            ["Modificar Flor", "49"],
            ["Modificar Flor", "47"],
            ["Modificar Flor", "42"]]
        v_7 = [
            ["Modificar Flor", "49"],
            ["Modificar Flor", "48"],
            ["Modificar Flor", "45"]]
        v_8 = [
            ["Modificar Flor", "49"],
            ["Modificar Flor", "48"],
            ["Modificar Flor", "42"]]

        sols = [v_1, v_2, v_3, v_4, v_5, v_7, v_6, v_8]

        
        lista_estudiante_set = set(map(tuple, lista_estudiante))
        sols_sets = [set(map(tuple, solucion)) for solucion in sols]

        self.assertEqual(valor_estudiante, valor_esperado)
        self.assertTrue(any(lista_estudiante_set ==
                        solucion_set for solucion_set in sols_sets))
        self.assertCountEqual(estructura_estudiante, estructura_final)
        self.assertEqual(precio_esperado, precio_estudiante)



    @timeout(N_SECOND)
    def test_03_bonsai_cortes_baratos(self):
        """
        Bonsai grande misma cantidad de acciones y mismo valor cortar o flor
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
            ["42", False, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", False, True, ["0", "0"]],
            ["48", True, True, ["0", "0"]],
            ["49", True, True, ["0", "0"]]
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
            ["42", False, True, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", True, True, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", False, True, ["0", "0"]],
            ["48", True, True, ["0", "0"]],
            ["49", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Nogal", 10, 7, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        v_1 = [True, 20, [["Quitar Nodo", "42"], ["Quitar Nodo", "45"]]]
        v_2 = [True, 20, [["Quitar Nodo", "45"], ["Quitar Nodo", "42"]]]

        sols = [v_1, v_2]

        self.assertIn(respuesta_estudiante, sols)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_8_flores(self):
        """
        Bonsai grande misma cantidad de acciones y mismo valor cortar o flor
        """

        estructura_inicial = [
            ["1", True, False, ["3", "2"]],
            ["2", False, True, ["0", "5"]],
            ["3", False, False, ["4", "0"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, True, ["6", "7"]],
            ["6", True, True, ["14", "15"]],
            ["7", False, True, ["10", "0"]],
            ["8", False, False, ["0", "11"]],
            ["9", True, False, ["16", "17"]],
            ["10", False, True, ["20", "21"]],
            ["11", False, False, ["12", "13"]],
            ["12", False, True, ["0", "0"]],
            ["13", True, False, ["0", "25"]],
            ["14", True, True, ["18", "19"]],
            ["15", False, False, ["22", "23"]],
            ["16", False, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, True, ["0", "0"]],
            ["20", True, False, ["24", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["28", "29"]],
            ["25", False, True, ["26", "27"]],
            ["26", False, True, ["30", "31"]],
            ["27", True, True, ["36", "37"]],
            ["28", False, False, ["38", "39"]],
            ["29", False, True, ["40", "41"]],
            ["30", True, True, ["0", "0"]],
            ["31", True, False, ["0", "0"]],
            ["32", False, True, ["0", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", False, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", True, True, ["0", "42"]],
            ["38", True, False, ["43", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", False, False, ["45", "0"]],
            ["44", False, False, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
        ]

        estructura_final = [
            ["1", True, False, ["3", "2"]],
            ["2", False, True, ["0", "5"]],
            ["3", False, False, ["4", "0"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, True, ["6", "7"]],
            ["6", True, True, ["14", "15"]],
            ["7", False, True, ["10", "0"]],
            ["8", False, False, ["0", "11"]],
            ["9", True, False, ["16", "17"]],
            ["10", False, True, ["20", "21"]],
            ["11", False, False, ["12", "13"]],
            ["12", False, True, ["0", "0"]],
            ["13", True, False, ["0", "25"]],
            ["14", True, True, ["18", "19"]],
            ["15", False, False, ["22", "23"]],
            ["16", False, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, True, ["0", "0"]],
            ["20", True, False, ["24", "0"]],
            ["21", True, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["28", "29"]],
            ["25", False, True, ["26", "27"]],
            ["26", False, True, ["30", "31"]],
            ["27", True, True, ["36", "37"]],
            ["28", False, False, ["38", "39"]],
            ["29", False, True, ["40", "41"]],
            ["30", True, True, ["0", "0"]],
            ["31", True, False, ["0", "0"]],
            ["32", False, True, ["0", "0"]],
            ["33", False, True, ["0", "0"]],
            ["34", False, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", True, True, ["0", "42"]],
            ["38", True, False, ["43", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", False, False, ["45", "0"]],
            ["44", False, False, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
        ]

        bonsai = Bonsai("Manzano", 11, 7, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)

        valor_estudiante = respuesta_estudiante[0]
        precio_estudiante = respuesta_estudiante[1]
        lista_estudiante = respuesta_estudiante[2]

        estructura_estudiante = bonsai.estructura
        valor_esperado = True
        precio_esperado = 56

        v_1 = [
            ["Modificar Flor", "27"], ["Modificar Flor", "12"], [
                "Modificar Flor", "45"],
            ["Modificar Flor", "42"], ["Modificar Flor", "19"], [
                "Modificar Flor", "18"],
            ["Modificar Flor", "33"], ["Modificar Flor", "32"]]

        v_2 = [
            ["Modificar Flor", "27"], ["Modificar Flor", "12"], [
                "Modificar Flor", "45"],
            ["Modificar Flor", "42"], ["Modificar Flor", "19"], [
                "Modificar Flor", "35"],
            ["Modificar Flor", "33"], ["Modificar Flor", "32"]]

        v_3 = [
            ["Modificar Flor", "27"], ["Modificar Flor", "12"], [
                "Modificar Flor", "45"],
            ["Modificar Flor", "42"], ["Modificar Flor", "19"], [
                "Modificar Flor", "18"],
            ["Modificar Flor", "33"], ["Modificar Flor", "23"]]

        v_4 = [
            ["Modificar Flor", "27"], ["Modificar Flor", "12"], [
                "Modificar Flor", "45"],
            ["Modificar Flor", "42"], ["Modificar Flor", "19"], [
                "Modificar Flor", "35"],
            ["Modificar Flor", "33"], ["Modificar Flor", "23"]]

        sols = [v_1, v_2, v_3, v_4]
        lista_estudiante_set = set(map(tuple, lista_estudiante))
        sols_sets = [set(map(tuple, solucion)) for solucion in sols]

        self.assertEqual(valor_estudiante, valor_esperado)
        self.assertEqual(precio_esperado, precio_estudiante)
        self.assertTrue(any(lista_estudiante_set ==
                        solucion_set for solucion_set in sols_sets))
        self.assertCountEqual(estructura_estudiante, estructura_final)

    @timeout(N_SECOND)
    def test_05_bonsai_flores_nodos(self):
        """
        Bonsai grande cortar o modificar mismo valor
        """

        estructura_inicial = [
            ["1", True, False, ["3", "2"]],
            ["2", False, True, ["0", "5"]],
            ["3", False, False, ["4", "0"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, True, ["6", "7"]],
            ["6", True, True, ["14", "15"]],
            ["7", False, True, ["10", "0"]],
            ["8", False, False, ["0", "11"]],
            ["9", True, False, ["16", "17"]],
            ["10", False, True, ["20", "21"]],
            ["11", False, False, ["12", "13"]],
            ["12", False, True, ["0", "0"]],
            ["13", True, False, ["0", "25"]],
            ["14", True, True, ["18", "19"]],
            ["15", False, False, ["22", "23"]],
            ["16", False, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", False, True, ["0", "0"]],
            ["19", False, True, ["0", "0"]],
            ["20", True, False, ["24", "0"]],
            ["21", False, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["28", "29"]],
            ["25", False, True, ["26", "27"]],
            ["26", False, True, ["30", "31"]],
            ["27", True, True, ["36", "37"]],
            ["28", True, False, ["38", "39"]],
            ["29", False, True, ["40", "41"]],
            ["30", True, True, ["0", "0"]],
            ["31", True, False, ["0", "0"]],
            ["32", True, True, ["0", "0"]],
            ["33", True, True, ["0", "0"]],
            ["34", False, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", True, True, ["0", "42"]],
            ["38", True, False, ["43", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", False, True, ["45", "0"]],
            ["44", False, True, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
        ]

        estructura_final = [
            ["1", True, False, ["3", "2"]],
            ["2", False, True, ["0", "5"]],
            ["3", False, False, ["4", "0"]],
            ["4", True, False, ["8", "9"]],
            ["5", True, True, ["6", "7"]],
            ["6", True, True, ["14", "15"]],
            ["7", False, True, ["10", "0"]],
            ["8", False, False, ["0", "11"]],
            ["9", True, False, ["16", "17"]],
            ["10", False, True, ["20", "21"]],
            ["11", False, False, ["12", "13"]],
            ["12", False, True, ["0", "0"]],
            ["13", True, False, ["0", "25"]],
            ["14", True, True, ["18", "19"]],
            ["15", False, False, ["22", "23"]],
            ["16", False, False, ["32", "33"]],
            ["17", True, True, ["34", "35"]],
            ["18", False, True, ["0", "0"]],
            ["19", False, True, ["0", "0"]],
            ["20", True, False, ["24", "0"]],
            ["21", False, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["28", "29"]],
            ["25", False, True, ["26", "27"]],
            ["26", False, True, ["30", "31"]],
            ["27", True, True, ["36", "37"]],
            ["28", True, False, ["38", "39"]],
            ["29", False, True, ["40", "41"]],
            ["30", True, True, ["0", "0"]],
            ["31", True, False, ["0", "0"]],
            ["32", True, True, ["0", "0"]],
            ["33", True, True, ["0", "0"]],
            ["34", False, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", True, True, ["0", "42"]],
            ["38", True, False, ["43", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "44"]],
            ["43", False, True, ["45", "0"]],
            ["44", False, True, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
        ]

        bonsai = Bonsai("Tuberculo", 28, 28, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)

        valor_estudiante = respuesta_estudiante[0]
        precio_estudiante = respuesta_estudiante[1]
        lista_estudiante = respuesta_estudiante[2]

        estructura_estudiante = bonsai.estructura
        valor_esperado = True
        precio_esperado = 56

        v_1 = [["Modificar Flor", "42"], ["Modificar Flor", "44"]]
        v_2 = [["Modificar Flor", "42"], ["Modificar Flor", "45"]]
        v_3 = [["Modificar Flor", "43"], ["Modificar Flor", "44"]]
        v_4 = [["Modificar Flor", "43"], ["Modificar Flor", "45"]]
        v_5 = [["Quitar Nodo", "43"], ["Quitar Nodo", "42"]]

        sols = [v_1, v_2, v_3, v_4, v_5]
        lista_estudiante_set = set(map(tuple, lista_estudiante))
        sols_sets = [set(map(tuple, solucion)) for solucion in sols]

        self.assertEqual(valor_estudiante, valor_esperado)
        self.assertEqual(precio_esperado, precio_estudiante)
        self.assertTrue(any(lista_estudiante_set ==
                        solucion_set for solucion_set in sols_sets))
        self.assertCountEqual(estructura_estudiante, estructura_final)

    @timeout(N_SECOND)
    def test_06_bonsai_flores_nodos(self):
        """
        Bonsai grande con dos ves correctas
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
            ["13", False, True, ["16", "17"]],
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
            ["46", False, True, ["0", "0"]],
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
            ["13", False, True, ["16", "17"]],
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
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Tuberculo", 11, 7, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura

        v_1 = [True, 7, [["Modificar Flor", "13"]]]
        v_2 = [True, 7, [["Modificar Flor", "26"]]]
        sols = [v_1, v_2]

        self.assertIn(respuesta_estudiante, sols)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_5_acciones(self):
        """
        Bonsai grande cortar o modificar mismo valor
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "0"]],
            ["3", False, False, ["57", "5"]],
            ["4", True, False, ["6", "7"]],
            ["5", True, True, ["8", "9"]],
            ["6", True, True, ["12", "13"]],
            ["7", False, True, ["14", "0"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, False, ["11", "10"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, True, ["17", "0"]],
            ["12", False, True, ["15", "0"]],
            ["13", True, False, ["0", "16"]],
            ["14", True, True, ["46", "47"]],
            ["15", False, True, ["0", "0"]],
            ["16", True, False, ["0", "19"]],
            ["17", True, True, ["18", "0"]],
            ["18", True, True, ["20", "56"]],
            ["19", False, True, ["0", "23"]],
            ["20", True, False, ["21", "22"]],
            ["21", False, False, ["30", "31"]],
            ["22", True, False, ["32", "33"]],
            ["23", True, True, ["24", "25"]],
            ["24", True, False, ["26", "27"]],
            ["25", False, True, ["28", "29"]],
            ["26", True, True, ["34", "35"]],
            ["27", True, True, ["36", "37"]],
            ["28", True, False, ["38", "39"]],
            ["29", False, True, ["0", "0"]],
            ["30", False, True, ["0", "0"]],
            ["31", True, False, ["41", "40"]],
            ["32", True, True, ["42", "43"]],
            ["33", True, True, ["44", "45"]],
            ["34", False, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", True, True, ["0", "0"]],
            ["38", True, False, ["0", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "0"]],
            ["43", True, True, ["0", "0"]],
            ["44", False, True, ["0", "0"]],
            ["45", False, True, ["0", "0"]],
            ["46", True, True, ["48", "49"]],
            ["47", True, True, ["50", "51"]],
            ["48", True, True, ["0", "0"]],
            ["49", True, True, ["0", "0"]],
            ["50", False, True, ["52", "53"]],
            ["51", False, True, ["0", "0"]],
            ["52", True, True, ["54", "55"]],
            ["53", True, True, ["0", "0"]],
            ["54", True, True, ["0", "0"]],
            ["55", False, True, ["0", "0"]],
            ["56", False, True, ["0", "0"]],
            ["57", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "0"]],
            ["3", False, False, ["57", "5"]],
            ["4", True, False, ["6", "7"]],
            ["5", True, True, ["8", "9"]],
            ["6", True, True, ["12", "13"]],
            ["7", False, True, ["14", "0"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, False, ["11", "10"]],
            ["10", True, True, ["0", "0"]],
            ["11", False, True, ["17", "0"]],
            ["12", False, True, ["15", "0"]],
            ["13", True, False, ["0", "16"]],
            ["14", True, True, ["46", "47"]],
            ["15", False, True, ["0", "0"]],
            ["16", True, False, ["0", "19"]],
            ["17", True, True, ["18", "0"]],
            ["18", True, True, ["20", "56"]],
            ["19", False, True, ["0", "23"]],
            ["20", True, False, ["21", "22"]],
            ["21", False, False, ["30", "31"]],
            ["22", True, False, ["32", "33"]],
            ["23", True, True, ["24", "25"]],
            ["24", True, False, ["26", "27"]],
            ["25", False, True, ["28", "29"]],
            ["26", True, True, ["34", "35"]],
            ["27", True, True, ["36", "37"]],
            ["28", True, False, ["38", "39"]],
            ["29", False, True, ["0", "0"]],
            ["30", False, True, ["0", "0"]],
            ["31", True, False, ["41", "40"]],
            ["32", True, True, ["42", "43"]],
            ["33", True, True, ["44", "45"]],
            ["34", False, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, False, ["0", "0"]],
            ["37", True, True, ["0", "0"]],
            ["38", True, False, ["0", "0"]],
            ["39", True, False, ["0", "0"]],
            ["40", True, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["42", True, True, ["0", "0"]],
            ["43", True, True, ["0", "0"]],
            ["44", False, True, ["0", "0"]],
            ["45", False, True, ["0", "0"]],
            ["46", True, True, ["48", "49"]],
            ["47", True, True, ["50", "51"]],
            ["48", True, True, ["0", "0"]],
            ["49", True, True, ["0", "0"]],
            ["50", False, True, ["52", "53"]],
            ["51", False, True, ["0", "0"]],
            ["52", True, True, ["54", "55"]],
            ["53", True, True, ["0", "0"]],
            ["54", True, True, ["0", "0"]],
            ["55", False, True, ["0", "0"]],
            ["56", False, True, ["0", "0"]],
            ["57", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Yuca", 4, 5, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        valor_estudiante = respuesta_estudiante[0]
        precio_estudiante = respuesta_estudiante[1]
        lista_estudiante = respuesta_estudiante[2]

        estructura_estudiante = bonsai.estructura
        valor_esperado = True
        precio_esperado = 30

        v_1 = [['Quitar Nodo', '12'], ['Quitar Nodo', '10'], ['Modificar Flor', '11'],
                ['Modificar Flor', '19'], ['Quitar Nodo', '56'], ['Quitar Nodo', '14'], 
                ['Quitar Nodo', '57']]
        
        sols = [v_1]
        lista_estudiante_set = set(map(tuple, lista_estudiante))
        sols_sets = [set(map(tuple, solucion)) for solucion in sols]

        self.assertEqual(valor_estudiante, valor_esperado)
        self.assertEqual(precio_esperado, precio_estudiante)
        self.assertTrue(any(lista_estudiante_set ==
                        solucion_set for solucion_set in sols_sets))
        self.assertCountEqual(estructura_estudiante, estructura_final)

    @timeout(N_SECOND)
    def test_08_bonsai_5_acciones_4_ves(self):
        """
        Bonsai grande cortar o modificar mismo valor
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "0"]],
            ["3", False, False, ["0", "5"]],
            ["4", True, False, ["6", "0"]],
            ["5", True, True, ["0", "7"]],
            ["6", True, True, ["8", "9"]],
            ["7", True, True, ["10", "11"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, False, ["14", "15"]],
            ["10", True, True, ["16", "17"]],
            ["11", False, False, ["18", "19"]],
            ["12", False, True, ["20", "0"]],
            ["13", True, False, ["0", "0"]],
            ["14", True, True, ["0", "0"]],
            ["15", True, True, ["0", "0"]],
            ["16", True, False, ["0", "0"]],
            ["17", True, True, ["0", "0"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, True, ["0", "21"]],
            ["20", False, False, ["22", "23"]],
            ["21", False, False, ["24", "25"]],
            ["22", False, False, ["26", "27"]],
            ["23", True, True, ["30", "0"]],
            ["24", True, False, ["0", "0"]],
            ["25", False, True, ["28", "29"]],
            ["26", True, True, ["31", "32"]],
            ["27", True, True, ["0", "0"]],
            ["28", False, True, ["0", "0"]],
            ["29", True, True, ["33", "34"]],
            ["30", False, True, ["0", "0"]],
            ["31", True, False, ["36", "0"]],
            ["32", True, True, ["35", "0"]],
            ["33", True, True, ["0", "0"]],
            ["34", True, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", False, True, ["4", "0"]],
            ["3", False, False, ["0", "5"]],
            ["4", True, False, ["6", "0"]],
            ["5", True, True, ["0", "7"]],
            ["6", True, True, ["8", "9"]],
            ["7", True, True, ["10", "11"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, False, ["14", "15"]],
            ["10", True, True, ["16", "17"]],
            ["11", False, False, ["18", "19"]],
            ["12", False, True, ["20", "0"]],
            ["13", True, False, ["0", "0"]],
            ["14", True, True, ["0", "0"]],
            ["15", True, True, ["0", "0"]],
            ["16", True, False, ["0", "0"]],
            ["17", True, True, ["0", "0"]],
            ["18", True, True, ["0", "0"]],
            ["19", True, True, ["0", "21"]],
            ["20", False, False, ["22", "23"]],
            ["21", False, False, ["24", "25"]],
            ["22", False, False, ["26", "27"]],
            ["23", True, True, ["30", "0"]],
            ["24", True, False, ["0", "0"]],
            ["25", False, True, ["28", "29"]],
            ["26", True, True, ["31", "32"]],
            ["27", True, True, ["0", "0"]],
            ["28", False, True, ["0", "0"]],
            ["29", True, True, ["33", "34"]],
            ["30", False, True, ["0", "0"]],
            ["31", True, False, ["36", "0"]],
            ["32", True, True, ["35", "0"]],
            ["33", True, True, ["0", "0"]],
            ["34", True, False, ["0", "0"]],
            ["35", False, True, ["0", "0"]],
            ["36", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Leech", 4, 5, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        valor_estudiante = respuesta_estudiante[0]
        precio_estudiante = respuesta_estudiante[1]
        lista_estudiante = respuesta_estudiante[2]

        estructura_estudiante = bonsai.estructura
        valor_esperado = True
        precio_esperado = 22

        v_1 = [
            ["Quitar Nodo", "36"], ["Quitar Nodo", "35"], ["Quitar Nodo", "30"],
            ["Modificar Flor", "12"], ["Modificar Flor", "28"]]

        v_2 = [
            ["Quitar Nodo", "36"], ["Quitar Nodo", "35"], ["Quitar Nodo", "30"],
            ["Modificar Flor", "12"], ["Modificar Flor", "27"]]

        v_3 = [
            ["Quitar Nodo", "36"], ["Quitar Nodo", "35"], ["Quitar Nodo", "30"],
            ["Modificar Flor", "19"], ["Modificar Flor", "28"]]

        v_4 = [
            ["Quitar Nodo", "36"], ["Quitar Nodo", "35"], ["Quitar Nodo", "30"],
            ["Modificar Flor", "19"], ["Modificar Flor", "27"]]

        sols = [v_1, v_2, v_3, v_4]
        lista_estudiante_set = set(map(tuple, lista_estudiante))
        sols_sets = [set(map(tuple, solucion)) for solucion in sols]

        self.assertEqual(valor_estudiante, valor_esperado)
        self.assertEqual(precio_esperado, precio_estudiante)
        self.assertTrue(any(lista_estudiante_set ==
                        solucion_set for solucion_set in sols_sets))
        self.assertCountEqual(estructura_estudiante, estructura_final)

    @timeout(N_SECOND)
    def test_09_bonsai_8_acciones_2_ves(self):
        """
        Bonsai grande cortar o modificar mismo valor
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "0"]],
            ["3", False, True, ["0", "5"]],
            ["4", True, False, ["6", "0"]],
            ["5", True, True, ["0", "7"]],
            ["6", True, True, ["8", "0"]],
            ["7", True, True, ["51", "9"]],
            ["8", True, False, ["10", "0"]],
            ["9", True, False, ["0", "11"]],
            ["10", True, True, ["12", "0"]],
            ["11", True, False, ["0", "13"]],
            ["12", True, False, ["14", "0"]],
            ["13", True, False, ["50", "15"]],
            ["14", True, True, ["16", "0"]],
            ["15", True, False, ["0", "17"]],
            ["16", True, False, ["18", "0"]],
            ["17", True, True, ["0", "19"]],
            ["18", False, True, ["20", "0"]],
            ["19", True, False, ["0", "21"]],
            ["20", True, False, ["22", "0"]],
            ["21", True, False, ["0", "23"]],
            ["22", True, False, ["24", "0"]],
            ["23", True, True, ["54", "25"]],
            ["24", False, False, ["0", "26"]],
            ["25", False, True, ["27", "0"]],
            ["26", True, True, ["0", "28"]],
            ["27", True, False, ["29", "0"]],
            ["28", True, False, ["0", "30"]],
            ["29", True, True, ["31", "0"]],
            ["30", True, True, ["0", "32"]],
            ["31", True, False, ["33", "0"]],
            ["32", True, True, ["0", "34"]],
            ["33", True, True, ["35", "0"]],
            ["34", True, False, ["0", "36"]],
            ["35", True, True, ["37", "0"]],
            ["36", True, False, ["0", "38"]],
            ["37", True, True, ["39", "0"]],
            ["38", False, True, ["0", "40"]],
            ["39", True, False, ["41", "0"]],
            ["40", True, False, ["0", "42"]],
            ["41", True, True, ["43", "0"]],
            ["42", False, True, ["0", "44"]],
            ["43", True, False, ["45", "0"]],
            ["44", True, False, ["0", "46"]],
            ["45", True, True, ["47", "0"]],
            ["46", False, True, ["0", "48"]],
            ["47", True, False, ["49", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", True, False, ["0", "0"]],
            ["50", True, True, ["0", "0"]],
            ["51", True, True, ["52", "53"]],
            ["52", True, True, ["0", "0"]],
            ["53", True, True, ["0", "0"]],
            ["54", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "0"]],
            ["3", False, True, ["0", "5"]],
            ["4", True, False, ["6", "0"]],
            ["5", True, True, ["0", "7"]],
            ["6", True, True, ["8", "0"]],
            ["7", True, True, ["51", "9"]],
            ["8", True, False, ["10", "0"]],
            ["9", True, False, ["0", "11"]],
            ["10", True, True, ["12", "0"]],
            ["11", True, False, ["0", "13"]],
            ["12", True, False, ["14", "0"]],
            ["13", True, False, ["50", "15"]],
            ["14", True, True, ["16", "0"]],
            ["15", True, False, ["0", "17"]],
            ["16", True, False, ["18", "0"]],
            ["17", True, True, ["0", "19"]],
            ["18", False, True, ["20", "0"]],
            ["19", True, False, ["0", "21"]],
            ["20", True, False, ["22", "0"]],
            ["21", True, False, ["0", "23"]],
            ["22", True, False, ["24", "0"]],
            ["23", True, True, ["54", "25"]],
            ["24", False, False, ["0", "26"]],
            ["25", False, True, ["27", "0"]],
            ["26", True, True, ["0", "28"]],
            ["27", True, False, ["29", "0"]],
            ["28", True, False, ["0", "30"]],
            ["29", True, True, ["31", "0"]],
            ["30", True, True, ["0", "32"]],
            ["31", True, False, ["33", "0"]],
            ["32", True, True, ["0", "34"]],
            ["33", True, True, ["35", "0"]],
            ["34", True, False, ["0", "36"]],
            ["35", True, True, ["37", "0"]],
            ["36", True, False, ["0", "38"]],
            ["37", True, True, ["39", "0"]],
            ["38", False, True, ["0", "40"]],
            ["39", True, False, ["41", "0"]],
            ["40", True, False, ["0", "42"]],
            ["41", True, True, ["43", "0"]],
            ["42", False, True, ["0", "44"]],
            ["43", True, False, ["45", "0"]],
            ["44", True, False, ["0", "46"]],
            ["45", True, True, ["47", "0"]],
            ["46", False, True, ["0", "48"]],
            ["47", True, False, ["49", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", True, False, ["0", "0"]],
            ["50", True, True, ["0", "0"]],
            ["51", True, True, ["52", "53"]],
            ["52", True, True, ["0", "0"]],
            ["53", True, True, ["0", "0"]],
            ["54", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Sicomoro", 56, 2, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)

        valor_estudiante = respuesta_estudiante[0]
        precio_estudiante = respuesta_estudiante[1]
        lista_estudiante = respuesta_estudiante[2]

        estructura_estudiante = bonsai.estructura
        valor_esperado = True
        precio_esperado = 178

        v_1 = [
            ["Quitar Nodo", "50"], ["Quitar Nodo", "51"], ["Quitar Nodo", "54"],
            ["Modificar Flor", "18"], ["Modificar Flor", "38"], [
                "Modificar Flor", "42"],
            ["Modificar Flor", "46"], ["Modificar Flor", "2"]]

        v_2 = [
            ["Quitar Nodo", "50"], ["Quitar Nodo", "51"], ["Quitar Nodo", "54"],
            ["Modificar Flor", "18"], ["Modificar Flor", "38"], [
                "Modificar Flor", "42"],
            ["Modificar Flor", "46"], ["Modificar Flor", "3"]]

        sols = [v_1, v_2]
        lista_estudiante_set = set(map(tuple, lista_estudiante))
        sols_sets = [set(map(tuple, solucion)) for solucion in sols]

        self.assertEqual(valor_estudiante, valor_esperado)
        self.assertTrue(any(lista_estudiante_set ==
                        solucion_set for solucion_set in sols_sets))
        self.assertCountEqual(estructura_estudiante, estructura_final)
        self.assertEqual(precio_esperado, precio_estudiante)

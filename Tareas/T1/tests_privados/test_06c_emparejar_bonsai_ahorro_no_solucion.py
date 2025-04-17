import unittest
import os
import sys
from dccortaramas import Bonsai, DCCortaRamas
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 20

dccortaramas = DCCortaRamas()


class TestEmparejarBonsaiAhorroSinSolucion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_una_sola_posibilidad(self):
        """
        Bonsai simple sin solucion
        """

        estructura_inicial = [
            ["1", True, False, ["0", "2"]],
            ["2", False, True, ["0", "3"]],
            ["3", False, True, ["4", "0"]],
            ["4", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["0", "2"]],
            ["2", False, True, ["0", "3"]],
            ["3", False, True, ["4", "0"]],
            ["4", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("IIC2233", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [False, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_pequeno_1(self):
        """
        Bonsai de simple sin solucion
        """

        estructura_inicial = [
            ["1", True, False, ["0", "2"]],
            ["2", False, True, ["0", "3"]],
            ["3", False, True, ["4", "0"]],
            ["4", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["0", "2"]],
            ["2", False, True, ["0", "3"]],
            ["3", False, True, ["4", "0"]],
            ["4", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("IIC2233", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [False, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_pequeno_2(self):
        """
        Bonsai de simple sin solucion
        """

        estructura_inicial = [
            ["1", True, False, ["3", "2"]],
            ["2", False, True, ["0", "5"]],
            ["3", True, True, ["4", "0"]],
            ["4", True, False, ["0", "6"]],
            ["5", True, False, ["0", "0"]],
            ["6", True, False, ["7", "0"]],
            ["7", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["3", "2"]],
            ["2", False, True, ["0", "5"]],
            ["3", True, True, ["4", "0"]],
            ["4", True, False, ["0", "6"]],
            ["5", True, False, ["0", "0"]],
            ["6", True, False, ["7", "0"]],
            ["7", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("IIC2233", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [False, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_03_bonsai_mediano_1(self):
        """
        Bonsai de simple sin solucion
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", False, False, ["0", "10"]],
            ["5", False, False, ["9", "0"]],
            ["6", True, False, ["8", "0"]],
            ["7", True, True, ["0", "11"]],
            ["8", False, False, ["14", "15"]],
            ["9", False, True, ["12", "13"]],
            ["10", True, False, ["0", "0"]],
            ["11", True, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "0"]],
            ["14", True, False, ["0", "0"]],
            ["15", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, True, ["6", "7"]],
            ["4", False, False, ["0", "10"]],
            ["5", False, False, ["9", "0"]],
            ["6", True, False, ["8", "0"]],
            ["7", True, True, ["0", "11"]],
            ["8", False, False, ["14", "15"]],
            ["9", False, True, ["12", "13"]],
            ["10", True, False, ["0", "0"]],
            ["11", True, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["13", True, True, ["0", "0"]],
            ["14", True, False, ["0", "0"]],
            ["15", True, True, ["0", "0"]]
        ]

        bonsai = Bonsai("Nein", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [False, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_mediano_2(self):
        """
        Bonsai de simple ya simetrico
        """

        estructura_inicial = [
            ["1", False, True, ["2", "3"]],
            ["2", True, False, ["0", "4"]],
            ["3", True, False, ["5", "0"]],
            ["4", False, True, ["6", "0"]],
            ["5", False, True, ["0", "7"]],
            ["6", False, True, ["8", "9"]],
            ["7", False, False, ["10", "11"]],
            ["8", True, True, ["12", "13"]],
            ["9", True, True, ["14", "15"]],
            ["10", True, True, ["16", "17"]],
            ["11", True, True, ["18", "19"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "0"]],
            ["14", False, False, ["0", "0"]],
            ["15", True, False, ["0", "0"]],
            ["16", True, True, ["0", "0"]],
            ["17", False, True, ["0", "0"]],
            ["18", True, False, ["0", "0"]],
            ["19", False, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", False, True, ["2", "3"]],
            ["2", True, False, ["0", "4"]],
            ["3", True, False, ["5", "0"]],
            ["4", False, True, ["6", "0"]],
            ["5", False, True, ["0", "7"]],
            ["6", False, True, ["8", "9"]],
            ["7", False, False, ["10", "11"]],
            ["8", True, True, ["12", "13"]],
            ["9", True, True, ["14", "15"]],
            ["10", True, True, ["16", "17"]],
            ["11", True, True, ["18", "19"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "0"]],
            ["14", False, False, ["0", "0"]],
            ["15", True, False, ["0", "0"]],
            ["16", True, True, ["0", "0"]],
            ["17", False, True, ["0", "0"]],
            ["18", True, False, ["0", "0"]],
            ["19", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Jaa", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [True, 0, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_05_bonsai_grande_1(self):
        """
        Bonsai de simple ya simetrico
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
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Jaa", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [True, 0, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_06_bonsai_grande_2(self):
        """
        Bonsai grande sin solucion
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["0", "8"]],
            ["5", True, True, ["9", "0"]],
            ["6", True, False, ["0", "10"]],
            ["7", True, False, ["11", "0"]],
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
            ["25", False, False, ["0", "40"]],
            ["26", True, False, ["28", "29"]],
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
            ["41", True, False, ["44", "45"]],
            ["42", True, False, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", False, False, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["50", "51"]],
            ["50", True, False, ["0", "0"]],
            ["51", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", True, False, ["6", "7"]],
            ["4", True, False, ["0", "8"]],
            ["5", True, True, ["9", "0"]],
            ["6", True, False, ["0", "10"]],
            ["7", True, False, ["11", "0"]],
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
            ["25", False, False, ["0", "40"]],
            ["26", True, False, ["28", "29"]],
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
            ["41", True, False, ["44", "45"]],
            ["42", True, False, ["46", "47"]],
            ["43", True, False, ["0", "0"]],
            ["44", True, False, ["0", "0"]],
            ["45", False, False, ["48", "49"]],
            ["46", False, True, ["0", "0"]],
            ["47", True, False, ["0", "0"]],
            ["48", True, False, ["0", "0"]],
            ["49", False, False, ["50", "51"]],
            ["50", True, False, ["0", "0"]],
            ["51", True, False, ["0", "0"]]
        ]

        bonsai = Bonsai("Oops", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [False, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_grande_2(self):
        """
        Bonsai grande sin solucion
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
            ["18", False, False, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", False, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]],
            ["25", False, True, ["0", "40"]],
            ["26", True, False, ["28", "29"]],
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
            ["13", True, False, ["16", "17"]],
            ["14", True, True, ["18", "19"]],
            ["15", True, False, ["20", "21"]],
            ["16", False, False, ["22", "23"]],
            ["17", False, True, ["24", "25"]],
            ["18", False, False, ["0", "0"]],
            ["19", True, False, ["0", "0"]],
            ["20", False, False, ["0", "0"]],
            ["21", False, False, ["0", "0"]],
            ["22", True, False, ["0", "0"]],
            ["23", True, True, ["0", "0"]],
            ["24", False, False, ["0", "0"]],
            ["25", False, True, ["0", "40"]],
            ["26", True, False, ["28", "29"]],
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

        bonsai = Bonsai("Almost", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [False, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_08_bonsai_grande_2(self):
        """
        Bonsai grande simetrico
        """

        estructura_inicial = [
                ["1", True, False, ["2", "3"]],
                ["2", False, True, ["4", "5"]],
                ["3", False, False, ["6", "7"]],
                ["4", True, False, ["8", "9"]],
                ["5", True, True, ["10", "11"]],
                ["6", True, True, ["12", "13"]],
                ["7", True, True, ["14", "15"]],
                ["8", True, False, ["16", "17"]],
                ["9", True, False, ["18", "19"]],
                ["10", False, True, ["20", "21"]],
                ["11", True, False, ["22", "23"]],
                ["12", True, False, ["24", "25"]],
                ["13", False, False, ["26", "27"]],
                ["14", True, True, ["28", "29"]],
                ["15", True, False, ["30", "31"]],
                ["16", True, False, ["32", "33"]],
                ["17", False, True, ["34", "35"]],
                ["18", False, True, ["36", "37"]],
                ["19", False, False, ["0", "0"]],
                ["20", False, False, ["0", "0"]],
                ["21", True, False, ["0", "0"]],
                ["22", False, False, ["0", "0"]],
                ["23", True, True, ["0", "0"]],
                ["24", True, False, ["0", "0"]],
                ["25", False, True, ["0", "0"]],
                ["26", True, True, ["0", "0"]],
                ["27", False, False, ["0", "0"]],
                ["28", False, False, ["0", "0"]],
                ["29", False, True, ["38", "39"]],
                ["30", False, True, ["40", "41"]],
                ["31", True, False, ["42", "43"]],
                ["32", True, True, ["0", "0"]],
                ["33", True, True, ["0", "45"]],
                ["34", True, False, ["0", "0"]],
                ["35", False, True, ["0", "0"]],
                ["36", False, False, ["0", "0"]],
                ["37", False, True, ["0", "0"]],
                ["38", False, False, ["0", "0"]],
                ["39", False, False, ["0", "0"]],
                ["40", False, False, ["0", "0"]],
                ["41", True, True, ["0", "0"]],
                ["42", True, True, ["44", "0"]],
                ["43", True, False, ["0", "0"]],
                ["44", True, False, ["0", "0"]],
                ["45", True, True, ["0", "0"]],
            ]

        estructura_final = [
                ["1", True, False, ["2", "3"]],
                ["2", False, True, ["4", "5"]],
                ["3", False, False, ["6", "7"]],
                ["4", True, False, ["8", "9"]],
                ["5", True, True, ["10", "11"]],
                ["6", True, True, ["12", "13"]],
                ["7", True, True, ["14", "15"]],
                ["8", True, False, ["16", "17"]],
                ["9", True, False, ["18", "19"]],
                ["10", False, True, ["20", "21"]],
                ["11", True, False, ["22", "23"]],
                ["12", True, False, ["24", "25"]],
                ["13", False, False, ["26", "27"]],
                ["14", True, True, ["28", "29"]],
                ["15", True, False, ["30", "31"]],
                ["16", True, False, ["32", "33"]],
                ["17", False, True, ["34", "35"]],
                ["18", False, True, ["36", "37"]],
                ["19", False, False, ["0", "0"]],
                ["20", False, False, ["0", "0"]],
                ["21", True, False, ["0", "0"]],
                ["22", False, False, ["0", "0"]],
                ["23", True, True, ["0", "0"]],
                ["24", True, False, ["0", "0"]],
                ["25", False, True, ["0", "0"]],
                ["26", True, True, ["0", "0"]],
                ["27", False, False, ["0", "0"]],
                ["28", False, False, ["0", "0"]],
                ["29", False, True, ["38", "39"]],
                ["30", False, True, ["40", "41"]],
                ["31", True, False, ["42", "43"]],
                ["32", True, True, ["0", "0"]],
                ["33", True, True, ["0", "45"]],
                ["34", True, False, ["0", "0"]],
                ["35", False, True, ["0", "0"]],
                ["36", False, False, ["0", "0"]],
                ["37", False, True, ["0", "0"]],
                ["38", False, False, ["0", "0"]],
                ["39", False, False, ["0", "0"]],
                ["40", False, False, ["0", "0"]],
                ["41", True, True, ["0", "0"]],
                ["42", True, True, ["44", "0"]],
                ["43", True, False, ["0", "0"]],
                ["44", True, False, ["0", "0"]],
                ["45", True, True, ["0", "0"]],
            ]

        bonsai = Bonsai("MirrorrroriM", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [True, 0, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

    @timeout(N_SECOND)
    def test_09_bonsai_grande_3(self):
        """
        Bonsai grande sin solucion
        """

        estructura_inicial = [
                ["1", True, False, ["2", "5"]],
                ["2", False, True, ["3", "4"]],
                ["3", False, False, ["0", "0"]],
                ["4", True, False, ["11", "13"]],
                ["5", True, True, ["7", "6"]],
                ["6", True, True, ["0", "8"]],
                ["7", True, True, ["14", "34"]],
                ["8", True, False, ["0", "9"]],
                ["9", True, False, ["0", "10"]],
                ["10", False, True, ["0", "15"]],
                ["11", True, False, ["12", "0"]],
                ["12", True, False, ["0", "0"]],
                ["13", False, False, ["0", "0"]],
                ["14", True, True, ["0", "0"]],
                ["15", True, False, ["16", "17"]],
                ["16", True, False, ["18", "19"]],
                ["17", False, True, ["20", "21"]],
                ["18", False, True, ["22", "23"]],
                ["19", False, False, ["24", "25"]],
                ["20", False, False, ["26", "27"]],
                ["21", True, False, ["28", "29"]],
                ["22", False, False, ["0", "0"]],
                ["23", True, True, ["0", "30"]],
                ["24", True, False, ["0", "0"]],
                ["25", False, True, ["0", "0"]],
                ["26", True, True, ["31", "32"]],
                ["27", False, False, ["0", "0"]],
                ["28", False, False, ["0", "0"]],
                ["29", False, True, ["0", "0"]],
                ["30", False, True, ["0", "0"]],
                ["31", True, False, ["3", "0"]],
                ["32", True, True, ["0", "0"]],
                ["33", True, True, ["0", "0"]],
                ["34", True, False, ["35", "0"]],
                ["35", False, True, ["36", "0"]],
                ["36", False, False, ["37", "0"]],
                ["37", False, True, ["38", "39"]],
                ["38", False, False, ["40", "0"]],
                ["39", False, False, ["41", "0"]],
                ["40", False, False, ["42", "43"]],
                ["41", True, True, ["0", "0"]],
                ["42", True, True, ["44", "0"]],
                ["43", True, False, ["0", "0"]],
                ["44", True, False, ["45", "0"]],
                ["45", True, True, ["0", "0"]],
            ]

        estructura_final = [
                ["1", True, False, ["2", "5"]],
                ["2", False, True, ["3", "4"]],
                ["3", False, False, ["0", "0"]],
                ["4", True, False, ["11", "13"]],
                ["5", True, True, ["7", "6"]],
                ["6", True, True, ["0", "8"]],
                ["7", True, True, ["14", "34"]],
                ["8", True, False, ["0", "9"]],
                ["9", True, False, ["0", "10"]],
                ["10", False, True, ["0", "15"]],
                ["11", True, False, ["12", "0"]],
                ["12", True, False, ["0", "0"]],
                ["13", False, False, ["0", "0"]],
                ["14", True, True, ["0", "0"]],
                ["15", True, False, ["16", "17"]],
                ["16", True, False, ["18", "19"]],
                ["17", False, True, ["20", "21"]],
                ["18", False, True, ["22", "23"]],
                ["19", False, False, ["24", "25"]],
                ["20", False, False, ["26", "27"]],
                ["21", True, False, ["28", "29"]],
                ["22", False, False, ["0", "0"]],
                ["23", True, True, ["0", "30"]],
                ["24", True, False, ["0", "0"]],
                ["25", False, True, ["0", "0"]],
                ["26", True, True, ["31", "32"]],
                ["27", False, False, ["0", "0"]],
                ["28", False, False, ["0", "0"]],
                ["29", False, True, ["0", "0"]],
                ["30", False, True, ["0", "0"]],
                ["31", True, False, ["3", "0"]],
                ["32", True, True, ["0", "0"]],
                ["33", True, True, ["0", "0"]],
                ["34", True, False, ["35", "0"]],
                ["35", False, True, ["36", "0"]],
                ["36", False, False, ["37", "0"]],
                ["37", False, True, ["38", "39"]],
                ["38", False, False, ["40", "0"]],
                ["39", False, False, ["41", "0"]],
                ["40", False, False, ["42", "43"]],
                ["41", True, True, ["0", "0"]],
                ["42", True, True, ["44", "0"]],
                ["43", True, False, ["0", "0"]],
                ["44", True, False, ["45", "0"]],
                ["45", True, True, ["0", "0"]],
            ]

        bonsai = Bonsai("Pipipi", 22, 33, estructura_inicial)
        respuesta_estudiante = dccortaramas.emparejar_bonsai_ahorro(bonsai)
        estructura_estudiante = bonsai.estructura
        respuesta_esperada = [False, []]

        self.assertEqual(respuesta_esperada, respuesta_estudiante)
        self.assertCountEqual(estructura_final, estructura_estudiante)

import os
import sys
import unittest
from dccortaramas import Bonsai
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 10


class TestCargarBonsaiDeArchivo(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_5_nodos(self):
        """
        Bonsai de palabras especiales
        """

        bonsai = Bonsai("pequeno_1.txt", 1, 1, [])
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="pequeno_privado", archivo="pequeno_1.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["True", "False"]],
            ["True", False, True, ["T", "0"]],
            ["False", True, False, ["0", "F"]],
            ["F", False, False, ["0", "0"]],
            ["T", True, True, ["0", "0"]]
        ]

        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_3_nodos_nombres(self):
        """
        Bonsai de 3 nodos con identificadores strings
        """

        bonsai = Bonsai("pequeno_2.txt", 1, 1, [])
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="pequeno_privado", archivo="pequeno_2.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["Hijo", "Hija"]],
            ["Hija", False, False, ["0", "0"]],
            ["Hijo", True, False, ["0", "0"]]
        ]

        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_5_nodos(self):
        """
        Bonsai de 5 nodos desordenado
        """

        bonsai = Bonsai("pequeno_3.txt", 1, 1, [])
        # cambiar nombre/archivo
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="pequeno_privado", archivo="pequeno_3.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, True, ["2", "5"]],
            ["5", True, False, ["0", "3"]],
            ["3", False, True, ["0", "0"]],
            ["4", False, True, ["0", "0"]],
            ["2", True, True, ["4", "0"]]
        ]

        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_03_bonsai_7_nodos_mezcla(self):
        """
        Bonsai mediano de 7 nodos con strings y en desorden
        """
        bonsai = Bonsai("pequeno_4.txt", 1, 1, [])
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="pequeno_privado", archivo="pequeno_4.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["5", True, True, ["0", "Seis"]],
            ["Mama", True, False, ["0", "4"]],
            ["1", True, False, ["Mama", "Papa"]],
            ["4", False, False, ["0", "0"]],
            ["Papa", False, True, ["5", "0"]],
            ["7", False, False, ["0", "0"]],
            ["Seis", True, False, ["7", "0"]]
        ]

        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_mediano_mezclado(self):
        """
        Bonsai mediano de 13 nodos dados en desorden en archivo
        """
        bonsai = Bonsai("mediano_1.txt", 1, 1, [])
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="mediano_privado", archivo="mediano_1.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["9", True, False, ["0", "0"]],
            ["2", True, True, ["4", "5"]],
            ["6", True, False, ["10", "11"]],
            ["7", True, True, ["0", "12"]],
            ["1", True, False, ["2", "3"]],
            ["4", False, False, ["8", "9"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, False, ["0", "0"]],
            ["12", True, True, ["0", "0"]],
            ["8", False, False, ["13", "14"]],
            ["5", True, False, ["0", "0"]],
            ["13", False, True, ["0", "0"]],
            ["3", False, True, ["6", "7"]],
            ["14", True, True, ["0", "0"]]
        ]
        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_05_bonsai_13_nodos(self):
        """
        Bonsai mediano de 13 nodos con identificadores palabras
        """
        bonsai = Bonsai("mediano_2.txt", 1, 1, [])
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="mediano_privado", archivo="mediano_2.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["Abuela", "TioAbuelo"]],
            ["Abuela", True, True, ["Hijo", "Hija"]],
            ["TioAbuelo", False, True, ["Primo", "Prima"]],
            ["Hijo", False, False, ["Nieta", "Nieto"]],
            ["Hija", False, True, ["Nieta_2", "Nieto_2"]],
            ["Primo", True, False, ["0", "0"]],
            ["Prima", True, True, ["0", "0"]],
            ["Nieta", False, False, ["BisNieto", "BisNieta"]],
            ["Nieto", True, True, ["0", "0"]],
            ["Nieto_2", True, False, ["0", "0"]],
            ["Nieta_2", False, False, ["0", "0"]],
            ["BisNieto", False, True, ["0", "0"]],
            ["BisNieta", False, True, ["0", "0"]]
        ]

        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_06_bonsai_13_nodos(self):
        """
        Bonsai mediano de 13 nodos, identificadores palabras y numeros
        """
        bonsai = Bonsai("mediano_3.txt", 1, 1, [])
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="mediano_privado", archivo="mediano_3.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["Dos", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["Seis", "7"]],
            ["4", False, False, ["8", "Nueve"]],
            ["5", False, True, ["10", "0"]],
            ["Seis", True, False, ["Once", "Doce"]],
            ["7", True, True, ["0", "Trece"]],
            ["8", False, False, ["0", "0"]],
            ["Nueve", True, True, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["Once", False, True, ["0", "0"]],
            ["Doce", False, True, ["0", "0"]],
            ["Trece", False, True, ["0", "0"]]
        ]

        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_19_nodos(self):
        """
        Bonsai de 19 nodos normal
        """
        bonsai = Bonsai("mediano_4.txt", 1, 1, [])
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="mediano_privado", archivo="mediano_4.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", False, True, ["2", "3"]],
            ["2", False, False, ["4", "5"]],
            ["3", True, False, ["0", "7"]],
            ["4", True, True, ["6", "8"]],
            ["5", False, True, ["0", "9"]],
            ["6", False, True, ["0", "0"]],
            ["7", False, False, ["11", "10"]],
            ["8", True, True, ["12", "13"]],
            ["9", False, True, ["14", "15"]],
            ["10", False, True, ["16", "0"]],
            ["11", True, True, ["0", "0"]],
            ["12", False, False, ["0", "0"]],
            ["13", True, False, ["0", "0"]],
            ["14", False, False, ["0", "0"]],
            ["15", True, False, ["17", "0"]],
            ["16", False, True, ["0", "18"]],
            ["17", False, True, ["0", "19"]],
            ["18", False, False, ["0", "0"]],
            ["19", True, False, ["0", "0"]]
        ]

        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_08_bonsai_13_nodos_ceros(self):
        """
        Bonsai mediano de 13 nodos, identificadores palabras y numeros
        """
        bonsai = Bonsai("mediano_5.txt", 1, 1, [])
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="mediano_privado", archivo="mediano_5.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["1", True, False, ["00", "000"]],
            ["00", True, True, ["0000", "00000"]],
            ["000", False, True, ["000000", "0000000"]],
            ["0000", False, False, ["00000000", "00000000"]],
            ["00000", False, True, ["0000000000", "0"]],
            ["000000", True, False, ["00000000000", "000000000000"]],
            ["0000000", True, True, ["0", "0000000000000"]],
            ["00000000", False, False, ["0", "0"]],
            ["000000000", True, True, ["0", "0"]],
            ["0000000000", True, False, ["0", "0"]],
            ["00000000000", False, True, ["0", "0"]],
            ["000000000000", False, True, ["0", "0"]],
            ["0000000000000", False, True, ["0", "0"]]
        ]

        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

    @timeout(N_SECOND)
    def test_09_bonsai_37_nodos_aleatorio(self):
        """
        Bonsai de 36 nodos numeros aleatorios
        """
        bonsai = Bonsai("grande_1.txt", 20, 25, [])
        respuesta_estudiante = bonsai.cargar_bonsai_de_archivo(
            carpeta="grande_privado", archivo="grande_1.txt")
        estructura_estudiante = bonsai.estructura
        estructura_esperada = [
            ["2", True, True, ["4", "00"]],
            ["7", True, True, ["0", "12"]],
            ["32", True, False, ["37", "0"]],
            ["53", False, True, ["32", "7"]],
            ["00", True, True, ["11", "111"]],
            ["4", False, False, ["256", "562"]],
            ["11", False, False, ["0", "121"]],
            ["121", True, True, ["3", "5"]],
            ["256", False, True, ["26", "13"]],
            ["13", False, True, ["15", "16"]],
            ["12", True, True, ["0", "0"]],
            ["15", False, True, ["75", "57"]],
            ["16", True, False, ["0", "17"]],
            ["562", False, True, ["8", "40"]],
            ["40", False, False, ["41", "0"]],
            ["26", False, False, ["0", "0"]],
            ["41", True, True, ["0", "0"]],
            ["5", True, True, ["33", "34"]],
            ["111", True, False, ["01", "001"]],
            ["01", True, False, ["0", "0"]],
            ["001", True, True, ["0", "0"]],
            ["3", False, False, ["0", "28"]],
            ["28", True, False, ["29", "0"]],
            ["29", True, False, ["0", "0"]],
            ["37", True, False, ["0", "81"]],
            ["75", True, True, ["0", "0"]],
            ["57", False, False, ["0", "1024"]],
            ["1024", False, False, ["0", "0"]],
            ["17", True, False, ["0", "0"]],
            ["81", True, True, ["0", "0"]],
            ["33", True, True, ["42", "0"]],
            ["44", False, False, ["0", "0"]],
            ["45", True, True, ["0", "0"]],
            ["1", True, False, ["2", "53"]],
            ["42", False, False, ["44", "45"]],
            ["8", True, False, ["0", "0"]],
            ["34", False, False, ["0", "0"]]
        ]

        self.assertIsNone(respuesta_estudiante)
        self.assertCountEqual(estructura_esperada, estructura_estudiante)

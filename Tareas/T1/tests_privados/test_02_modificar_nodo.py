import unittest
import os
import sys
from dccortaramas import Bonsai, DCCortaRamas
from tests_privados.timeout_function import timeout

sys.stdout = open(os.devnull, 'w')

N_SECOND = 10

dccortaramas = DCCortaRamas()


class TestModificarNodo(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_flor_simple_nombres(self):
        """
        Bonsai de 3 nodos, eliminar flor por nombre
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["0", "0"]],
            ["3", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["0", "0"]],
            ["3", False, True, ["0", "0"]]
        ]

        arbol = Bonsai("Cipres de la cordillera", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="3")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_01_bonsai_flor_simple_nombre_equivocado(self):
        """
        Bonsai de 3 nodos, identificador con mayusculas
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["0", "0"]],
            ["3", True, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, False, ["0", "0"]],
            ["3", True, True, ["0", "0"]]
        ]

        arbol = Bonsai("Girasol", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="HIJA")
        cambio_esperado = "No encontrado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_02_bonsai_editable_agregar_00(self):
        """
        Bonsai de 3 nodos, que agrega flor a nodo "00"
        """
        estructura_inicial = [
            ["1", True, False, ["00", "3"]],
            ["00", False, True, ["0", "0"]],
            ["3", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["00", "3"]],
            ["00", True, True, ["0", "0"]],
            ["3", True, False, ["0", "0"]]
        ]

        arbol = Bonsai("Platano Oriental", 1, 1, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="00")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_03_bonsai_editable_quitar_numero(self):
        """
        Bonsai de 6 nodos, que elimina flor por numero, numeros aleatorios
        """
        estructura_inicial = [
            ["1", True, True, ["7", "4"]],
            ["5", False, True, ["9", "3"]],
            ["3", True, False, ["0", "0"]],
            ["7", False, True, ["0", "5"]],
            ["4", True, True, ["0", "0"]],
            ["9", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", False, True, ["7", "4"]],
            ["5", False, True, ["9", "3"]],
            ["3", True, False, ["0", "0"]],
            ["7", False, True, ["0", "5"]],
            ["4", True, True, ["0", "0"]],
            ["9", False, True, ["0", "0"]]
        ]

        arbol = Bonsai("Random", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="1")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_04_bonsai_mediano_no_encontrado_nombre(self):
        """
        Bonsai de 13 nodos, que no encuentra el nodo por nombre
        """
        estructura_inicial = [
            ["1", True, False, ["4", "5"]],
            ["4", True, True, ["2", "3"]],
            ["5", False, True, ["6", "7"]],
            ["2", False, False, ["8", "9"]],
            ["3", False, True, ["10", "11"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, True, ["0", "0"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, True, ["0", "0"]],
            ["11", True, False, ["0", "0"]],
            ["10", False, False, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["4", "5"]],
            ["4", True, True, ["2", "3"]],
            ["5", False, True, ["6", "7"]],
            ["2", False, False, ["8", "9"]],
            ["3", False, True, ["10", "11"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, True, ["0", "0"]],
            ["8", False, False, ["12", "13"]],
            ["9", True, True, ["0", "0"]],
            ["11", True, False, ["0", "0"]],
            ["10", False, False, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]]
        ]

        arbol = Bonsai("Familiar", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="Pariente")
        cambio_esperado = "No encontrado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_05_bonsai_mediano_inexistente(self):
        """
        Bonsai de 9 nodos, que no se encuentra
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, True, ["0", "0"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["0", "0"]],
            ["6", True, False, ["0", "0"]],
            ["7", True, True, ["0", "0"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, False, ["0", "0"]]
        ]

        arbol = Bonsai("Numeros", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="270")
        cambio_esperado = "No encontrado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_06_bonsai_mediano_editable_agregar(self):
        """
        Bonsai de 13 nodos, agrega una flor de las de abajo
        """

        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["10", "0"]],
            ["6", True, False, ["11", "12"]],
            ["7", True, True, ["0", "13"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, True, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["10", "0"]],
            ["6", True, False, ["11", "12"]],
            ["7", True, True, ["0", "13"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, True, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", True, True, ["0", "0"]]
        ]

        arbol = Bonsai("Num3r0s", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="13")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_07_bonsai_mediano_inalterable(self):
        """
        Bonsai de 13 nodos, que no tiene el nodo pedido
        """
        estructura_inicial = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["10", "0"]],
            ["6", True, False, ["11", "12"]],
            ["7", True, True, ["0", "13"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, True, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["2", "3"]],
            ["2", True, True, ["4", "5"]],
            ["3", False, True, ["6", "7"]],
            ["4", False, False, ["8", "9"]],
            ["5", False, True, ["10", "0"]],
            ["6", True, False, ["11", "12"]],
            ["7", True, True, ["0", "13"]],
            ["8", False, False, ["0", "0"]],
            ["9", True, True, ["0", "0"]],
            ["10", True, False, ["0", "0"]],
            ["11", False, True, ["0", "0"]],
            ["12", False, True, ["0", "0"]],
            ["13", False, True, ["0", "0"]]
        ]

        arbol = Bonsai("Timothy Green", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="Seis")
        cambio_esperado = "No encontrado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_08_bonsai_grande_inalterable(self):
        """
        Bonsai de 37 nodos, que no se puede alterar
        """

        estructura_inicial = [
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

        estructura_final = [
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

        arbol = Bonsai("Pino", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="42")
        cambio_esperado = "No permitido"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

    @timeout(N_SECOND)
    def test_09_bonsai_grande_agregar(self):
        """
        Bonsai de 45 nodos con letras, que agrega una flor
        """

        estructura_inicial = [
            ["1", True, False, ["A", "B"]],
            ["A", True, True, ["C", "D"]],
            ["B", False, True, ["E", "F"]],
            ["C", False, False, ["G", "H"]],
            ["D", True, False, ["0", "0"]],
            ["E", True, False, ["I", "J"]],
            ["F", True, True, ["0", "K"]],
            ["G", False, False, ["L", "M"]],
            ["H", True, False, ["0", "0"]],
            ["I", True, False, ["0", "0"]],
            ["J", False, False, ["0", "0"]],
            ["K", True, True, ["0", "0"]],
            ["L", False, True, ["N", "O"]],
            ["M", True, True, ["0", "0"]],
            ["N", False, True, ["0", "0"]],
            ["O", True, False, ["0", "P"]],
            ["P", True, False, ["R", "Q"]],
            ["Q", True, True, ["T", "S"]],
            ["R", False, True, ["V", "U"]],
            ["S", False, False, ["X", "W"]],
            ["T", False, False, ["0", "0"]],
            ["U", True, False, ["0", "0"]],
            ["V", True, True, ["0", "0"]],
            ["W", False, True, ["Z", "Y"]],
            ["X", True, True, ["0", "0"]],
            ["Y", False, False, ["0", "AA"]],
            ["Z", True, False, ["BB", "0"]],
            ["AA", False, False, ["0", "CC"]],
            ["BB", True, True, ["EE", "DD"]],
            ["CC", False, True, ["GG", "FF"]],
            ["DD", False, False, ["II", "HH"]],
            ["EE", True, False, ["JJ", "0"]],
            ["FF", False, True, ["0", "KK"]],
            ["GG", True, False, ["0", "0"]],
            ["HH", False, False, ["0", "0"]],
            ["II", True, True, ["0", "0"]],
            ["JJ", False, True, ["0", "LL"]],
            ["KK", False, True, ["0", "MM"]],
            ["LL", True, True, ["0", "0"]],
            ["MM", False, False, ["NN", "0"]],
            ["NN", True, True, ["OO", "PP"]],
            ["OO", False, False, ["RR", "QQ"]],
            ["PP", True, False, ["0", "0"]],
            ["QQ", False, False, ["0", "0"]],
            ["RR", True, False, ["0", "0"]]
        ]

        estructura_final = [
            ["1", True, False, ["A", "B"]],
            ["A", True, True, ["C", "D"]],
            ["B", False, True, ["E", "F"]],
            ["C", False, False, ["G", "H"]],
            ["D", True, False, ["0", "0"]],
            ["E", True, False, ["I", "J"]],
            ["F", True, True, ["0", "K"]],
            ["G", False, False, ["L", "M"]],
            ["H", True, False, ["0", "0"]],
            ["I", True, False, ["0", "0"]],
            ["J", False, False, ["0", "0"]],
            ["K", True, True, ["0", "0"]],
            ["L", False, True, ["N", "O"]],
            ["M", True, True, ["0", "0"]],
            ["N", False, True, ["0", "0"]],
            ["O", True, False, ["0", "P"]],
            ["P", True, False, ["R", "Q"]],
            ["Q", True, True, ["T", "S"]],
            ["R", False, True, ["V", "U"]],
            ["S", False, False, ["X", "W"]],
            ["T", False, False, ["0", "0"]],
            ["U", True, False, ["0", "0"]],
            ["V", True, True, ["0", "0"]],
            ["W", False, True, ["Z", "Y"]],
            ["X", True, True, ["0", "0"]],
            ["Y", False, False, ["0", "AA"]],
            ["Z", True, False, ["BB", "0"]],
            ["AA", False, False, ["0", "CC"]],
            ["BB", True, True, ["EE", "DD"]],
            ["CC", False, True, ["GG", "FF"]],
            ["DD", False, False, ["II", "HH"]],
            ["EE", True, False, ["JJ", "0"]],
            ["FF", False, True, ["0", "KK"]],
            ["GG", True, False, ["0", "0"]],
            ["HH", False, False, ["0", "0"]],
            ["II", True, True, ["0", "0"]],
            ["JJ", True, True, ["0", "LL"]],
            ["KK", False, True, ["0", "MM"]],
            ["LL", True, True, ["0", "0"]],
            ["MM", False, False, ["NN", "0"]],
            ["NN", True, True, ["OO", "PP"]],
            ["OO", False, False, ["RR", "QQ"]],
            ["PP", True, False, ["0", "0"]],
            ["QQ", False, False, ["0", "0"]],
            ["RR", True, False, ["0", "0"]]
        ]

        arbol = Bonsai("Groot", 22, 33, estructura_inicial)
        cambio_estudiante = dccortaramas.modificar_nodo(
            bonsai=arbol, identificador="JJ")
        cambio_esperado = "Realizado"
        resultado_estudiante = arbol.estructura

        self.assertEqual(cambio_esperado, cambio_estudiante)
        self.assertCountEqual(estructura_final, resultado_estudiante)

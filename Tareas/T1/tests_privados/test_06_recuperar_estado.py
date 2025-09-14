# Test numero: 6
import sys, os
import unittest

from os import path

from tests_privados.timeout_function import timeout

from dccasillas import DCCasillas

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestRecuperarEstado(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    

    @timeout(N_SECOND)
    def test_00_recuperar_estado_True_1(self):
        """
        Evalua parametros de un tablero simple.
        Retorna True.
        """

        config = "config08.txt"
        user = "cristobalross29"
        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.recuperar_estado()
        tableros = dccasillas_estudiante.tableros

        tablero_esperado = [
            ["2", "3", ".", ".", "1", "6"],
            [".", "4", ".", "1", ".", "5"],
            ["1", ".", "2", "3", ".", "6"],
            [".", ".", "1", "2", ".", "3"],
            ["3", "1", ".", ".", "2", "6"],
            ["6", "8", "3", "6", "3", "."]
        ]

        resultado_esperado = [tablero_esperado, 4, True]
        resultado_estudiante_more = [tableros[0].tablero, tableros[0].movimientos, tableros[0].estado]

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)
        self.assertListEqual(resultado_esperado, resultado_estudiante_more)

    @timeout(N_SECOND)
    def test_01_recuperar_estado_True_2(self):
        """
        Evalua parametros de 2 tableros simples con esatdo variado.
        Retorna True.
        """

        config = "config09.txt"
        user = "piton"
        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.recuperar_estado()
        tableros = dccasillas_estudiante.tableros

        tablero_esperado = [[[".", ".", ".", ".", "0"],
                            [".", ".", ".", ".", "10"],
                            [".", ".", ".", ".", "24"],
                            [".", ".", ".", ".", "7"],
                            [".", ".", ".", ".", "1"],
                            ["1", "5", "8", "8", "."]],

                            [[".", "2", "2"],
                             ["3", "6", "."],
                             ["3", "8", "."]]
                            
                            ]

        resultado_esperado = [tablero_esperado, [0, 3], [False, True]]
        resultado_estudiante_more = [[a.tablero for a in tableros], [a.movimientos for a in tableros], [a.estado for a in tableros]]

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)
        self.assertListEqual(resultado_esperado, resultado_estudiante_more)


    @timeout(N_SECOND)
    def test_02_recuperar_estado_True_3(self):
        """
        Evalua parametros de 2 tableros simples con igual estado.
        Retorna True.
        """

        config = "configuracion3.txt"
        user = "usuario_3"
        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.recuperar_estado()
        tableros = dccasillas_estudiante.tableros


        tablero_esperado = [[
            ["X2", ".", "1", ".", "X4", "."],
            ["3", ".", "2", ".", "1", "."],
            ["4", "2", "X3", "2", "2", "10"],
            ["7", ".", "3", ".", "3", "."]
        ], [
            ["6", ".", "4", "1", "10", "."],
            ["6", "3", ".", "5", "9", "."],
            ["10", "X3", "13", "7", "10", "."],
            ["X4", ".", "3", "7", "X16", "10"],
            ["5", "3", ".", "X7", "X5", "8"],
            [".", "6", ".", ".", ".", "."]
        ]]

        resultado_esperado = [tablero_esperado, [8,5], [True, True]]
        resultado_estudiante_more = [[a.tablero for a in tableros], [a.movimientos for a in tableros], [a.estado for a in tableros]]

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)
        self.assertListEqual(resultado_esperado, resultado_estudiante_more)

    @timeout(N_SECOND)
    def test_03_recuperar_estado_True_4(self):
        """
        Evalua parametros de un tablero grande.
        Retorna True.
        """

        config = "config10.txt"
        user = "lele"
        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.recuperar_estado()
        tableros = dccasillas_estudiante.tableros

        tablero_esperado = [[
            ["1", "8", ".", "4", "4", "8", "7", "2", "24"],
            ["1", "1", ".", ".", "5", "3", "3", "6", "15"],
            ["3", "2", "7", "4", "1", ".", "3", "5", "14"],
            ["9", "6", "2", "4", "2", "1", "3", "9", "12"],
            [".", "4", "1", "0", "9", "9", ".", "3", "14"],
            ["9", "3", ".", "2", "8", "9", "7", "9", "17"],
            ["3", "8", "2", "2", "1", "5", "6", "4", "14"],
            ["8", "4", "7", ".", "4", ".", "7", "6", "18"],
            ["1", "20", "12", "12", "21", "26", "25", "11", "."]
        ]]

        resultado_esperado = [tablero_esperado, [10], [False]]
        resultado_estudiante_more = [[a.tablero for a in tableros], [a.movimientos for a in tableros], [a.estado for a in tableros]]

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)
        self.assertListEqual(resultado_esperado, resultado_estudiante_more)


    @timeout(N_SECOND)
    def test_04_recuperar_estado_True_5(self):
        """
        Evalua parametros de 3 tableros medianos con estado variado.
        Retorna True.
        """

        config = "configuracion6.txt"
        user = "usuario"
        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.recuperar_estado()
        tableros = dccasillas_estudiante.tableros

        tablero_esperado = [[
            [".", ".",  "13",  "1",     "X8", ".",    "X16", "14"],
            ["X8", "4", "X11",  "X12",   "3",   "12", "7", "."],
            ["7", "3",  "X2",  ".",    ".",    "X14", "9", "19"],
            ["3", "2",  "X7",   "1",   "X17",   "X9", ".", "6"],
            [".", "4",  "2",  ".",     "X15",   "X5", "2", "8"],
            ["3", "X2",  ".",  ".",    "7",     ".", "X6", "10"],
            ["1", "X15", ".",  "6",   "X13",    "X17", ".", "7"],
            [".", "13", ".",    ".",   ".",       ".", "18", "."]
        ],[
            ["X2", ".", "1", ".", "X4", "."],
            ["3", ".", "2", ".", "1", "."],
            ["4", "2", "X3", "2", "2", "10"],
            ["7", ".", "3", ".", "3", "."]
        ],[
            ["13", ".", "14", "7", ".", "X4", "8"],
            ["1", "11", "11", ".", "15", ".", "6"],
            ["X9", "6", "13", ".", "6", "1", "15"],
            ["5", "4", "11", "X5", ".", ".", "."],
            ["6", ".", "2", "15", "11", "X10", "7"],
            [".", ".", ".", "14", ".", "16", "."]
        ]]

        resultado_esperado = [tablero_esperado, [19, 7, 4], [True, True, False]]
        resultado_estudiante_more = [[a.tablero for a in tableros], [a.movimientos for a in tableros], [a.estado for a in tableros]]

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(resultado_estudiante)
        self.assertListEqual(resultado_esperado, resultado_estudiante_more)



    @timeout(N_SECOND)
    def test_05_recuperar_estado_False_1(self):
        """
        Evalua con archivo de un usuario inexistente.
        Retorna False.
        """

        config = "config05.txt"
        user = "MereQuetenge"
        dccasillas_estudiante = DCCasillas(user, config)

        ruta = path.join("data", user+"txt")
        if path.exists(ruta):
            os.remove(ruta)

        resultado_estudiante = dccasillas_estudiante.recuperar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)

    @timeout(N_SECOND)
    def test_06_recuperar_estado_False_2(self):
        """
        Evalua formato incorrecto del archivo al recuperar.
        Retorna False.
        """

        config = "config07.txt"
        user = "usuario_8"
        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.recuperar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)

    @timeout(N_SECOND)
    def test_07_recuperar_estado_False_3(self):
        """
        Evalua coordenadas negativas al recuperar.
        Retorna False.
        """

        config = "configuracion1.txt"
        user = "usuario_6"
        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.recuperar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)
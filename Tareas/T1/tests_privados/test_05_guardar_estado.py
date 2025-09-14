# Test numero: 5
import sys, os
import unittest

from os import path

from tests_privados.timeout_function import timeout

from dccasillas import DCCasillas

sys.stdout = open(os.devnull, "w")

N_SECOND = 10


class TestGuardarEstado(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    

    archivos = []
    
    
    @timeout(N_SECOND)
    def test_00_guardar_estado_True_1(self):
        """
        Evalua formato correcto.
        Retorna True.
        """

        config = "config03.txt"
        user = "Frandeus"
        archivo = user + ".txt"
        self.archivos.append(archivo)

        ruta_esperada = path.join("data", archivo)

        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(path.exists(ruta_esperada))
        self.assertTrue(resultado_estudiante)

        with open(ruta_esperada, "r", encoding="utf-8") as f, open(path.join("data",user+"_expected.txt"), "r", encoding="utf-8") as g:
            contenido_1 = f.read()
            contenido_2 = g.read()
        
        self.assertEqual(contenido_1, contenido_2)


    @timeout(N_SECOND)
    def test_01_guardar_estado_True_2(self):
        """
        Evalua formato correcto.
        Retorna True.
        """

        config = "config04.txt"
        user = "Agusrush21"
        archivo = user + ".txt"
        self.archivos.append(archivo)

        ruta_esperada = path.join("data", archivo)

        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(path.exists(ruta_esperada))
        self.assertTrue(resultado_estudiante)

        with open(ruta_esperada, "r", encoding="utf-8") as f, open(path.join("data",user+"_expected.txt"), "r", encoding="utf-8") as g:
            contenido_1 = f.read()
            contenido_2 = g.read()
        
        self.assertEqual(contenido_1, contenido_2)


    @timeout(N_SECOND)
    def test_02_guardar_estado_True_3(self):
        """
        Evalua formato correcto.
        implementa movimientos.
        Retorna True.
        """

        config = "config05.txt"
        user = "consomedejaiba"
        archivo = user + ".txt"
        self.archivos.append(archivo)

        ruta_esperada = path.join("data", archivo)

        dccasillas_estudiante = DCCasillas(user, config)

        movimientos = [54, 21, 5, 7]
        for a in range(len(dccasillas_estudiante.tableros)):
            dccasillas_estudiante.tableros[a].movimientos = movimientos[a]


        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(path.exists(ruta_esperada))
        self.assertTrue(resultado_estudiante)

        with open(ruta_esperada, "r", encoding="utf-8") as f, open(path.join("data",user+"_expected.txt"), "r", encoding="utf-8") as g:
            contenido_1 = f.read()
            contenido_2 = g.read()
        
        self.assertEqual(contenido_1, contenido_2)


    @timeout(N_SECOND)
    def test_03_guardar_estado_True_4(self):
        """
        Evalua formato correcto.
        Evalua movimientos despues de modificar casillas.
        Retorna True.
        """

        config = "config06.txt"
        user = "pepegrillo"
        archivo = user + ".txt"
        self.archivos.append(archivo)

        ruta_esperada = path.join("data", archivo)

        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(path.exists(ruta_esperada))
        self.assertTrue(resultado_estudiante)

        
        indice = 2

        dccasillas_estudiante.tableros[indice].tablero[0][0] = "X" + dccasillas_estudiante.tableros[indice].tablero[0][0]
        dccasillas_estudiante.tableros[indice].tablero[1][4] = "X" + dccasillas_estudiante.tableros[indice].tablero[1][4]
        dccasillas_estudiante.tableros[indice].tablero[2][2] = "X" + dccasillas_estudiante.tableros[indice].tablero[2][2]

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(path.exists(ruta_esperada))
        self.assertTrue(resultado_estudiante)

        with open(ruta_esperada, "r", encoding="utf-8") as f, open(path.join("data",user+"_expected.txt"), "r", encoding="utf-8") as g:
            contenido_1 = f.read()
            contenido_2 = g.read()
        
        self.assertEqual(contenido_1, contenido_2)


    @timeout(N_SECOND)
    def test_04_guardar_estado_True_5(self):
        """
        Evalua formato correcto.
        Evalua movimientos despues de modificar casillas (varias veces).
        Retorna True.
        """

        config = "config07.txt"
        user = "cobreloa"
        archivo = user + ".txt"
        self.archivos.append(archivo)

        ruta_esperada = path.join("data", archivo)

        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        indice_1 = 0
        indice_2 = 1

        dccasillas_estudiante.tableros[indice_1].movimientos = 10
        dccasillas_estudiante.tableros[indice_2].movimientos = 30

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(path.exists(ruta_esperada))
        self.assertTrue(resultado_estudiante)


        dccasillas_estudiante.tableros[indice_1].tablero[6][7] = "X" + dccasillas_estudiante.tableros[indice_1].tablero[6][7]
        dccasillas_estudiante.tableros[indice_1].tablero[0][11] = "X" + dccasillas_estudiante.tableros[indice_1].tablero[0][11]
        dccasillas_estudiante.tableros[indice_1].tablero[4][6] = "X" + dccasillas_estudiante.tableros[indice_1].tablero[4][6]

        dccasillas_estudiante.tableros[indice_2].tablero[0][3] = "X" + dccasillas_estudiante.tableros[indice_2].tablero[0][3]
        dccasillas_estudiante.tableros[indice_2].tablero[1][3] = "X" + dccasillas_estudiante.tableros[indice_2].tablero[1][3]

        dccasillas_estudiante.tableros[indice_1].movimientos += 3
        dccasillas_estudiante.tableros[indice_2].movimientos += 2

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(path.exists(ruta_esperada))
        self.assertTrue(resultado_estudiante)


        dccasillas_estudiante.tableros[indice_1].tablero[0][11] = dccasillas_estudiante.tableros[indice_1].tablero[0][11].replace("X","")
        dccasillas_estudiante.tableros[indice_1].tablero[4][6] = dccasillas_estudiante.tableros[indice_1].tablero[4][6].replace("X","")

        dccasillas_estudiante.tableros[indice_2].tablero[1][3] = dccasillas_estudiante.tableros[indice_2].tablero[1][3].replace("X","")

        dccasillas_estudiante.tableros[indice_1].movimientos += 2
        dccasillas_estudiante.tableros[indice_2].movimientos += 1

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertTrue(path.exists(ruta_esperada))
        self.assertTrue(resultado_estudiante)

        with open(ruta_esperada, "r", encoding="utf-8") as f, open(path.join("data",user+"_expected.txt"), "r", encoding="utf-8") as g:
            contenido_1 = f.read()
            contenido_2 = g.read()
        
        self.assertEqual(contenido_1, contenido_2)


    @timeout(N_SECOND)
    def test_05_guardar_estado_False_1(self):
        """
        Usuario invalido. Retorna False
        """

        config = "config.txt"
        user = ""
        archivo = user + ".txt"
        self.archivos.append(archivo)

        dccasillas_estudiante = DCCasillas(user, config)

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)

    @timeout(N_SECOND)
    def test_06_guardar_estado_False_2(self):
        """
        No hay tableros que guardar. Retorna False
        """

        config = "config07.txt"
        user = "IefGO"
        archivo = user + ".txt"
        self.archivos.append(archivo)

        dccasillas_estudiante = DCCasillas(user, config)
        dccasillas_estudiante.tableros = []

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertIsNotNone(resultado_estudiante)
        self.assertFalse(resultado_estudiante)

    @classmethod
    def tearDownClass(cls):
        directorio = "data"
        for archivo in os.listdir(directorio):
            if archivo.endswith(".txt"):
                ruta_completa = path.join(directorio, archivo)
                if path.isfile(ruta_completa) and archivo in cls.archivos:
                    os.remove(ruta_completa)
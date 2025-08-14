import unittest, os
from os import path

from dccasillas import DCCasillas

from tests_publicos.timeout_function import timeout

N_SECOND = 5

class TestGuardarEstado(unittest.TestCase):
    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    @timeout(N_SECOND)
    def test_00_guardar_estado_True_1(self):
        """
        Verifica que se guarde correctamente el archivo, devuelva True.
        """

        config = "config01.txt"
        user = "Agusrush21"
        archivo = user + ".txt"
        
        ruta_esperada = path.join("data", archivo)
        
        dccasillas_estudiante = DCCasillas(usuario=user, config=config)
        dccasillas_estudiante.tablero_actual = 0

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertTrue(path.exists(ruta_esperada), "No existe el archivo")
        self.assertTrue(resultado_estudiante, "Debe retornar True")

    @timeout(N_SECOND)
    def test_01_guardar_estado_True_2(self):
        """
        Verifica que se guarde correctamente el archivo, devuelva True.
        """
        config = "config01.txt"
        user = "cruz"
        archivo = user + ".txt"
        
        ruta_esperada = path.join("data", archivo)
        
        dccasillas_estudiante = DCCasillas(usuario=user, config=config)
        dccasillas_estudiante.tablero_actual = 2

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertTrue(path.exists(ruta_esperada), "No existe el archivo")
        self.assertTrue(resultado_estudiante, "Debe retornar True")


    @timeout(N_SECOND)
    def test_02_guardar_estado_True_3(self):
        """
        Verifica que se guarde correctamente el archivo, devuelva True.
        Ademas evalua el puntaje y movimientos.
        """
        config = "config01.txt"
        user = "R3Y3X"
        archivo = user + ".txt"
        
        ruta_esperada = path.join("data", archivo)
        
        dccasillas_estudiante = DCCasillas(usuario=user, config=config)
        dccasillas_estudiante.tablero_actual = 1
        dccasillas_estudiante.puntaje = 20
        dccasillas_estudiante.tableros[1].movimientos = 4

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertTrue(path.exists(ruta_esperada), "No existe el archivo")
        self.assertTrue(resultado_estudiante, "Debe retornar True")

    
    @timeout(N_SECOND)
    def test_03_guardar_estado_True_4(self):
        """
        Verifica que se guarde correctamente el archivo, devuelva True.
        Ademas evalua el puntaje y movimientos.
        """
        config = "config01.txt"
        user = "trinicamposl"
        archivo = user + ".txt"
        
        ruta_esperada = path.join("data", archivo)
        
        dccasillas_estudiante = DCCasillas(usuario=user, config=config)
        dccasillas_estudiante.tablero_actual = 3
        dccasillas_estudiante.puntaje = 10
        dccasillas_estudiante.tableros[3].movimientos = 8

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertTrue(path.exists(ruta_esperada), "No existe el archivo")
        self.assertTrue(resultado_estudiante, "Debe retornar True")


    @timeout(N_SECOND)
    def test_04_guardar_estado_True_5(self):
        """
        Verifica que se guarde correctamente el archivo, devuelva True.
        Ademas evalua el puntaje y movimientos.
        Evalua distintos cambios en las casillas.
        """
        config = "config01.txt"
        user = "pepe"
        archivo = user + ".txt"
    
        ruta_esperada = path.join("data", archivo)
        
        dccasillas_estudiante = DCCasillas(usuario=user, config=config)
        dccasillas_estudiante.tablero_actual = 4
        dccasillas_estudiante.puntaje = 60
        dccasillas_estudiante.tableros[4].movimientos = 23

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertTrue(path.exists(ruta_esperada), "No existe el archivo")
        self.assertTrue(resultado_estudiante, "Debe retornar True")

        dccasillas_estudiante.tableros[4].tablero[0][0] = "." + dccasillas_estudiante.tableros[4].tablero[0][0]
        dccasillas_estudiante.tableros[4].tablero[2][0] = "." + dccasillas_estudiante.tableros[4].tablero[0][0]
        dccasillas_estudiante.tableros[4].tablero[3][1] = "." + dccasillas_estudiante.tableros[4].tablero[0][0]
        dccasillas_estudiante.tableros[4].tablero[7][0] = "." + dccasillas_estudiante.tableros[4].tablero[0][0]

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertTrue(path.exists(ruta_esperada), "No existe el archivo")
        self.assertTrue(resultado_estudiante, "Debe retornar True")


    @timeout(N_SECOND)
    def test_05_guardar_estado_True_6(self):
        """
        Verifica que se guarde correctamente el archivo, devuelva True.
        Ademas evalua el puntaje y movimientos.
        Evalua distintos cambios en las casillas
        """
        config = "config01.txt"
        user = "maria"
        archivo = user + ".txt"
    
        ruta_esperada = path.join("data", archivo)
        
        dccasillas_estudiante = DCCasillas(usuario=user, config=config)
        dccasillas_estudiante.tablero_actual = 2
        dccasillas_estudiante.puntaje = 30
        dccasillas_estudiante.tableros[2].movimientos = 50

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertTrue(path.exists(ruta_esperada), "No existe el archivo")
        self.assertTrue(resultado_estudiante, "Debe retornar True")

        dccasillas_estudiante.tableros[2].tablero[0][3] = "." + dccasillas_estudiante.tableros[4].tablero[0][0]
        dccasillas_estudiante.tableros[2].tablero[1][2] = "." + dccasillas_estudiante.tableros[4].tablero[0][0]
        dccasillas_estudiante.tableros[2].tablero[2][1] = "." + dccasillas_estudiante.tableros[4].tablero[0][0]
        dccasillas_estudiante.tableros[2].tablero[0][0] = "." + dccasillas_estudiante.tableros[4].tablero[0][0]

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        dccasillas_estudiante.tableros[2].tablero[0][3] = dccasillas_estudiante.tableros[4].tablero[0][0].replace(".","")
        dccasillas_estudiante.tableros[2].tablero[1][2] = "." + dccasillas_estudiante.tableros[4].tablero[0][0].replace(".","")
        dccasillas_estudiante.tableros[2].tablero[2][1] = "." + dccasillas_estudiante.tableros[4].tablero[0][0].replace(".","")

        resultado_estudiante = dccasillas_estudiante.guardar_estado()

        self.assertTrue(path.exists(ruta_esperada), "No existe el archivo")
        self.assertTrue(resultado_estudiante, "Debe retornar True")
    
    
    @classmethod
    def tearDownClass(cls):
        directorio = "data"
        for archivo in os.listdir(directorio):
            if archivo.endswith(".txt"):
                ruta_completa = path.join(directorio, archivo)
                if path.isfile(ruta_completa):
                    os.remove(ruta_completa)
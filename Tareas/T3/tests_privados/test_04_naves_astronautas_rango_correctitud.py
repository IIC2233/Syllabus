import os
import sys
import unittest
from collections.abc import Generator
from backend.consultas import naves_astronautas_rango
from utilidades import Tripulacion
from tests_privados.timeout_function import timeout
from tests_privados.utils import FLEXIBILIDAD_ADICIONAL
sys.stdout = open(os.devnull, 'w')


# ver tema generador con tuplas y considerar mayores rangos

# Constante para timeout en tests
N_SECOND = FLEXIBILIDAD_ADICIONAL*0.08
tipos_adicionales_permitidos = (
    map, filter, enumerate, zip
)


class TestNavesAstronautasRango(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne una sola patente.
        """

        lista_tripulaciones = [
            Tripulacion(
                id_equipo=5,
                patente_nave="Nave",
                id_astronauta=1,
                rango=3),
            Tripulacion(
                id_equipo=5,
                patente_nave="Nave",
                id_astronauta=2,
                rango=3),
            Tripulacion(
                id_equipo=5,
                patente_nave="Nave",
                id_astronauta=3,
                rango=3)
        ]

        generador_tripulacion = (tripulacion for tripulacion in lista_tripulaciones)

        resultado_estudiante = naves_astronautas_rango(
            generador_tripulacion, rango=3, minimo_astronautas=3)

        self.assertTrue(isinstance(resultado_estudiante, Generator)
                        or type(resultado_estudiante) in tipos_adicionales_permitidos,
                        'Revisa que la función sea generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(any(isinstance(item, Generator) or type(item) in tipos_adicionales_permitidos 
                            for _, item in lista_resultado), 
                            'Revisa que las ids astronauta se entregen como generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = [("Nave", (1, 2, 3))]

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que la función no retornen todos los del rango cuando es un numero negativo.
        """

        lista_tripulaciones = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=0,
                rango=2),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=2,
                rango=4),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=4),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=4,
                rango=4),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=5,
                rango=4)
        ]

        generador_tripulacion = (tripulacion for tripulacion in lista_tripulaciones)

        resultado_estudiante = naves_astronautas_rango(
            generador_tripulacion, rango=4, minimo_astronautas=-2)

        self.assertTrue(isinstance(resultado_estudiante, Generator) 
                        or type(resultado_estudiante) in tipos_adicionales_permitidos,
                        'Revisa que la función sea generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = [("N-1", (2, 3)), ("N-2", (4, 5))]

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retornen las dos naves que cumplen solo las naves que llegan a quorum,
        considerndo rangos mayores como utiles
        """

        lista_tripulaciones = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=2,
                rango=2),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-1",
                id_astronauta=3,
                rango=3),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=4,
                rango=3),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=5,
                rango=2),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=6,
                rango=4),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-3",
                id_astronauta=7,
                rango=2)
        ]

        generador_tripulacion = (tripulacion for tripulacion in lista_tripulaciones)

        resultado_estudiante = naves_astronautas_rango(
            generador_tripulacion, rango=3, minimo_astronautas=2)

        self.assertTrue(isinstance(resultado_estudiante, Generator)
                        or type(resultado_estudiante) in tipos_adicionales_permitidos,
                        'Revisa que la función sea generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(any(isinstance(item, Generator) or type(item) in tipos_adicionales_permitidos 
                            for _, item in lista_resultado), 
                            'Revisa que las ids astronauta se entregen como generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = [("N-1", (1, 3)), ("N-2", (4, 6))]

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorna todo el generador.
        """

        lista_tripulaciones = [
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=4,
                rango=4),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=5,
                rango=2),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-2",
                id_astronauta=6,
                rango=2),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-3",
                id_astronauta=7,
                rango=2),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-3",
                id_astronauta=8,
                rango=2)
        ]

        generador_tripulacion = (tripulacion for tripulacion in lista_tripulaciones)

        resultado_estudiante = naves_astronautas_rango(
            generador_tripulacion, rango=1, minimo_astronautas=1)

        self.assertTrue(isinstance(resultado_estudiante, Generator) 
                        or type(resultado_estudiante) in tipos_adicionales_permitidos,
                        'Revisa que la función sea generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = [("N-2", (4, 5, 6)), ("N-3", (7, 8))]

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que cuando hay más del mínimo retorne todos, incluidos lo de mayor rango.
        """

        lista_tripulaciones = [
            Tripulacion(
                id_equipo=1,
                patente_nave="N-2233",
                id_astronauta=1,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-2233",
                id_astronauta=2,
                rango=4),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-2233",
                id_astronauta=3,
                rango=5),
            Tripulacion(
                id_equipo=1,
                patente_nave="N-2233",
                id_astronauta=4,
                rango=5)
        ]

        generador_tripulacion = (tripulacion for tripulacion in lista_tripulaciones)

        resultado_estudiante = naves_astronautas_rango(
            generador_tripulacion, rango=4, minimo_astronautas=2)

        self.assertTrue(isinstance(resultado_estudiante, Generator) 
                        or type(resultado_estudiante) in tipos_adicionales_permitidos,
                        'Revisa que la función sea generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(any(isinstance(item, Generator) or type(item) in tipos_adicionales_permitidos 
                            for _, item in lista_resultado), 
                            'Revisa que las ids astronauta se entregen como generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = [("N-2233", (1, 2, 3, 4))]

        self.assertCountEqual(lista_resultado, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retornen cargos más altos, que igual cumplen, se filtre por cantidad y no 
        se retornen las que no cumplen
        """

        lista_tripulaciones = [
            Tripulacion(
                id_equipo=3,
                patente_nave="N-3",
                id_astronauta=7,
                rango=1),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-3",
                id_astronauta=8,
                rango=1),
            Tripulacion(
                id_equipo=2,
                patente_nave="N-3",
                id_astronauta=9,
                rango=3),
            Tripulacion(
                id_equipo=3,
                patente_nave="N-3",
                id_astronauta=10,
                rango=3),
            Tripulacion(
                id_equipo=4,
                patente_nave="N-4",
                id_astronauta=11,
                rango=3),
            Tripulacion(
                id_equipo=4,
                patente_nave="N-4",
                id_astronauta=12,
                rango=1),
            Tripulacion(
                id_equipo=5,
                patente_nave="N-5",
                id_astronauta=13,
                rango=1)
        ]

        generador_tripulacion = (tripulacion for tripulacion in lista_tripulaciones)

        resultado_estudiante = naves_astronautas_rango(
            generador_tripulacion, rango=1, minimo_astronautas=2)

        self.assertTrue(isinstance(resultado_estudiante, Generator) 
                        or type(resultado_estudiante) in tipos_adicionales_permitidos,
                        'Revisa que la función sea generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = list(resultado_estudiante)
        self.assertTrue(all(isinstance(item, tuple) for item in lista_resultado), 'Revisa que el primer generador sea de tuples')
        self.assertTrue(any(isinstance(item, Generator) or type(item) in tipos_adicionales_permitidos 
                            for _, item in lista_resultado), 
                            'Revisa que las ids astronauta se entregen como generador, o uno entre '+', '.join(
                            str(item) for item in tipos_adicionales_permitidos
                        ))

        lista_resultado = [(k, tuple(v)) for k, v in lista_resultado]
        lista_esperada = [("N-3", (7, 8, 9, 10)), ("N-4", (11, 12))]

        self.assertCountEqual(lista_resultado, lista_esperada)

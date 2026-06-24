import os
from tests_privados.test_tools import IICTest, timeout, indexes_of
from backend.consultas import juguetes_producen, cargar_juguete_recurso

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestJuguetesProducenCargaDatosPrivado(IICTest):
    """
    Verifica juguetes_producen cargando juguete_recurso desde datasets privados S, M, L y XL.
    Comprueba lista completa de productores en orden ascendente y caso sin productores.
    """

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        Dataset S, id_recurso=1: tres juguetes lo producen; verifica lista completa
        en orden ascendente.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        resultado = list(juguetes_producen(gen, 1))
        self.assertEqual(resultado, [11, 29, 44])

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        Dataset S, id_recurso=5: seis juguetes lo producen; verifica lista completa
        en orden ascendente.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        resultado = list(juguetes_producen(gen, 5))
        self.assertEqual(resultado, [2, 28, 35, 38, 41, 45])

    @timeout(N_SECOND)
    def test_S_2(self):
        """
        Dataset S, id_recurso=99: ningun juguete lo produce; retorna generador vacio.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        *items, largo = indexes_of(juguetes_producen(gen, 99), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        Dataset M, id_recurso=10: cinco juguetes lo producen; verifica lista completa
        en orden ascendente.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        resultado = list(juguetes_producen(gen, 10))
        self.assertEqual(resultado, [4, 33, 112, 123, 146])

    @timeout(N_SECOND)
    def test_M_1(self):
        """
        Dataset M, id_recurso=50: tres juguetes lo producen; verifica lista completa
        en orden ascendente.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        resultado = list(juguetes_producen(gen, 50))
        self.assertEqual(resultado, [66, 97, 142])

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        Dataset L, id_recurso=1: cuatro juguetes lo producen; verifica lista completa
        en orden ascendente.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        resultado = list(juguetes_producen(gen, 1))
        self.assertEqual(resultado, [11, 62, 101, 232])

    @timeout(N_SECOND)
    def test_L_1(self):
        """
        Dataset L, id_recurso=100: ningun juguete lo produce; retorna generador vacio.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        *items, largo = indexes_of(juguetes_producen(gen, 100), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_XL_0(self):
        """
        Dataset XL, id_recurso=6: cuatro juguetes dispersos lo producen; verifica
        filtrado correcto y orden ascendente sobre un archivo grande.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_XL, "juguete_recurso.csv"))
        resultado = list(juguetes_producen(gen, 6))
        self.assertEqual(resultado, [3, 66, 73, 383])

import os
from tests_privados.test_tools import IICTest, timeout, indexes_of
from backend.consultas import juguetes_productivos, cargar_juguete_recurso

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestJuguetesProductivosCargaDatosPrivado(IICTest):
    """
    Verifica juguetes_productivos cargando juguete_recurso desde datasets privados S, M, L
    y XL. Comprueba productividad maxima con empate, umbral estricto y caso sin resultados.
    """

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        Dataset S, minimo=None: cuatro juguetes empatan la productividad maxima; retorna
        todos en orden ascendente.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        resultado = list(juguetes_productivos(gen, None))
        self.assertEqual(resultado, [1, 4, 8, 9])

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        Dataset S, minimo=1.0: ninguna productividad supera el umbral estrictamente;
        retorna generador vacio.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        *items, largo = indexes_of(juguetes_productivos(gen, 1.0), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        Dataset M, minimo=None: dos juguetes empatan la productividad maxima; retorna
        ambos en orden ascendente.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        resultado = list(juguetes_productivos(gen, None))
        self.assertEqual(resultado, [56, 76])

    @timeout(N_SECOND)
    def test_M_1(self):
        """
        Dataset M, minimo=1.0: cinco juguetes superan estrictamente el umbral.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        resultado = list(juguetes_productivos(gen, 1.0))
        self.assertEqual(resultado, [30, 56, 63, 76, 82])

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        Dataset L, minimo=None: un unico juguete tiene la productividad maxima (J151).
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        resultado = list(juguetes_productivos(gen, None))
        self.assertEqual(resultado, [151])

    @timeout(N_SECOND)
    def test_L_1(self):
        """
        Dataset L, minimo=5.0: dos juguetes superan estrictamente el umbral.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        resultado = list(juguetes_productivos(gen, 5.0))
        self.assertEqual(resultado, [27, 151])

    @timeout(N_SECOND)
    def test_XL_0(self):
        """
        Dataset XL, minimo=None: un unico juguete tiene la productividad maxima (J707).
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_XL, "juguete_recurso.csv"))
        resultado = list(juguetes_productivos(gen, None))
        self.assertEqual(resultado, [707])

    @timeout(N_SECOND)
    def test_XL_1(self):
        """
        Dataset XL, minimo=2.0: seis juguetes superan estrictamente el umbral; los que
        tienen productividad exactamente 2.0 quedan excluidos.
        """
        gen = cargar_juguete_recurso(os.path.join(PATH_XL, "juguete_recurso.csv"))
        resultado = list(juguetes_productivos(gen, 2.0))
        self.assertEqual(resultado, [348, 350, 433, 511, 569, 707])

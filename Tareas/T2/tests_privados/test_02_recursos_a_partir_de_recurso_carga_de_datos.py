import os
from tests_privados.test_tools import IICTest, timeout, indexes_of
from backend.consultas import recursos_a_partir_de_recurso, cargar_recurso_recurso

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestRecursosAPartirDeRecursoCargaDatosPrivado(IICTest):
    """
    Verifica recursos_a_partir_de_recurso cargando recurso_recurso desde datasets privados
    S, M, L y XL. Comprueba largo, orden, afinidades acumuladas y cantidades totales.
    """

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        Dataset S, id_recurso=1 (recurso base): 19 recursos creables en total.
        Verifica el primero (pos 0), uno intermedio (pos 9) y el ultimo con sus afinidades
        y cantidades acumuladas correctas.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        resultado = recursos_a_partir_de_recurso(gen, 1)
        *items, largo = indexes_of(resultado, [0, 9, -1])
        self.assertEqual(largo, 19)
        self.assertEqual(items[0], (2, (1,), 1))
        self.assertEqual(items[1], (11, (1, 12), 3))
        self.assertEqual(items[2], (20, (3, 9, 11), 6))

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        Dataset S, id_recurso=6: resultado completo de 5 elementos verificado.
        Comprueba orden ascendente por id_recurso y estructura de cada tupla
        (id, afinidades, cantidad).
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        resultado = list(recursos_a_partir_de_recurso(gen, 6))
        self.assertEqual(resultado, [
            (7, (20,), 3),
            (8, (2, 20), 4),
            (12, (99,), 1),
            (13, (2, 20), 6),
            (17, (16, 99), 1),
        ])

    @timeout(N_SECOND)
    def test_S_2(self):
        """
        Dataset S, id_recurso=8: recurso hoja que no aparece como ingrediente en ninguna
        receta; retorna generador vacio.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        *items, largo = indexes_of(recursos_a_partir_de_recurso(gen, 8), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        Dataset M, id_recurso=20: exactamente dos recursos creables a partir de el.
        Verifica lista completa con afinidades y cantidades correctas.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_M, "recurso_recurso.csv"))
        resultado = list(recursos_a_partir_de_recurso(gen, 20))
        self.assertEqual(resultado, [
            (28, (33,), 1),
            (40, (12, 33), 3),
        ])

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        Dataset L, id_recurso=2: 7 recursos creables en total.
        Verifica el primero (id=6, afinidad simple) y el ultimo (id=486, afinidades
        multiples acumuladas a lo largo de la cadena).
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_L, "recurso_recurso.csv"))
        resultado = recursos_a_partir_de_recurso(gen, 2)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 7)
        self.assertEqual(items[0], (6, (1,), 1))
        self.assertEqual(items[1], (486, (1, 29, 99), 3))

    @timeout(N_SECOND)
    def test_XL_0(self):
        """
        Dataset XL, id_recurso=1: habilita 1499 recursos creables (toda la cadena).
        Verifica propagacion completa: el ultimo recurso acumula 34 afinidades distintas
        y una cantidad total de 206370 unidades.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_XL, "recurso_recurso.csv"))
        resultado = recursos_a_partir_de_recurso(gen, 1)
        *items, largo = indexes_of(resultado, [0, 749, -1])
        self.assertEqual(largo, 1499)
        self.assertEqual(items[0], (2, (1,), 1))
        self.assertEqual(items[1], (751, (1, 20), 3))
        self.assertEqual(items[2], (
            1500,
            (1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 99),
            206370,
        ))

    @timeout(N_SECOND)
    def test_XL_1(self):
        """
        Dataset XL, id_recurso=1500: recurso hoja (el de mayor id); no es ingrediente de
        ninguna receta, debe retornar vacio incluso procesando el archivo completo.
        """
        gen = cargar_recurso_recurso(os.path.join(PATH_XL, "recurso_recurso.csv"))
        *_, largo = indexes_of(recursos_a_partir_de_recurso(gen, 1500), [])
        self.assertEqual(largo, 0)

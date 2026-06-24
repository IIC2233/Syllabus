import os

from tests_privados.test_tools import IICTest, timeout, indexes_of
from backend.consultas import juguetes_a_aparecer, cargar_juguete_habitat, cargar_periodo_dia

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")

S_HABITAT_10_MOMENTO_0 = [
    (11, 1),
    (12, 1),
    (14, 25),
    (39, 86),
    (36, 119),
    (32, 208),
    (28, 265),
]
M_HABITAT_2_MOMENTO_0 = [(1, 3), (3, 24), (77, 24), (80, 112)]
L_HABITAT_1_MOMENTO_0 = [(1, 1), (2, 1), (315, 87), (176, 330)]


def cargar_resultado(path: str, id_habitat: int, momento_dia: int):
    gen_jh = cargar_juguete_habitat(os.path.join(path, "juguete_habitat.csv"))
    gen_pd = cargar_periodo_dia(os.path.join(path, "periodo_dia.csv"))
    return juguetes_a_aparecer(gen_jh, gen_pd, id_habitat, momento_dia)


class TestJuguetesAAparecerCargaDatosPrivado(IICTest):
    """
    Verifica juguetes_a_aparecer con datasets privados S, M, L y XL.
    Comprueba orden por tiempo de espera, calculo relativo al momento_dia y saltos
    al siguiente periodo valido.
    """

    @timeout(N_SECOND)
    def test_S_habitat_1_momento_0(self):
        """
        Dataset S, habitat=1, momento=0: 5 juguetes posibles; verifica el primero
        (J1, espera 1 min) y el ultimo (J33, espera 252 min).
        """
        resultado = cargar_resultado(PATH_S, 1, 0)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 5)
        self.assertEqual(items[0], (1, 1))
        self.assertEqual(items[1], (33, 252))

    @timeout(N_SECOND)
    def test_S_habitat_10_momento_0(self):
        """
        Dataset S, habitat=10, momento=0: verifica lista completa de 7 juguetes con
        sus tiempos de espera ordenados.
        """
        resultado = cargar_resultado(PATH_S, 10, 0)
        self.assertEqual(list(resultado), S_HABITAT_10_MOMENTO_0)

    @timeout(N_SECOND)
    def test_S_habitat_10_momento_30(self):
        """
        Dataset S, habitat=10, momento=30: mismo habitat que el test anterior pero
        desde minuto 30; cambia el orden y las esperas relativas al momento actual.
        """
        resultado = cargar_resultado(PATH_S, 10, 30)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 7)
        self.assertEqual(items[0], (11, 1))
        self.assertEqual(items[1], (28, 252))

    @timeout(N_SECOND)
    def test_M_habitat_2_momento_0(self):
        """
        Dataset M, habitat=2, momento=0: cuatro juguetes posibles; verifica lista
        completa con tiempos de espera ordenados.
        """
        resultado = cargar_resultado(PATH_M, 2, 0)
        self.assertEqual(list(resultado), M_HABITAT_2_MOMENTO_0)

    @timeout(N_SECOND)
    def test_M_habitat_50_momento_0(self):
        """
        Dataset M, habitat=50, momento=0: 5 juguetes posibles; verifica el primero
        (J7, espera 59 min) y el ultimo (J116, espera 320 min).
        """
        resultado = cargar_resultado(PATH_M, 50, 0)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 5)
        self.assertEqual(items[0], (7, 59))
        self.assertEqual(items[1], (116, 320))

    @timeout(N_SECOND)
    def test_L_habitat_1_momento_0(self):
        """
        Dataset L, habitat=1, momento=0: cuatro juguetes posibles; verifica lista
        completa con tiempos de espera ordenados.
        """
        resultado = cargar_resultado(PATH_L, 1, 0)
        self.assertEqual(list(resultado), L_HABITAT_1_MOMENTO_0)

    @timeout(N_SECOND)
    def test_L_habitat_10_momento_30(self):
        """
        Dataset L, habitat=10, momento=30: 7 juguetes posibles; verifica el primero
        (J11, espera 1 min) y el ultimo (J298, espera 662 min).
        """
        resultado = cargar_resultado(PATH_L, 10, 30)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 7)
        self.assertEqual(items[0], (11, 1))
        self.assertEqual(items[1], (298, 662))

    @timeout(N_SECOND)
    def test_XL_habitat_161_momento_0(self):
        """
        Dataset XL, habitat=161, momento=0: cinco juguetes con esperas largas que
        requieren saltar al siguiente periodo valido; verifica lista completa ordenada.
        """
        resultado = cargar_resultado(PATH_XL, 161, 0)
        self.assertEqual(list(resultado), [
            (219, 180),
            (66, 1101),
            (120, 1265),
            (133, 2015),
            (751, 2837),
        ])

    @timeout(N_SECOND)
    def test_XL_habitat_161_momento_alto(self):
        """
        Dataset XL, habitat=161, momento=1000: mismo habitat que el test anterior pero
        desde minuto 1000; cambia el orden de aparicion por las esperas relativas.
        """
        resultado = cargar_resultado(PATH_XL, 161, 1000)
        self.assertEqual(list(resultado), [
            (219, 175),
            (120, 265),
            (133, 1015),
            (66, 1766),
            (751, 1837),
        ])


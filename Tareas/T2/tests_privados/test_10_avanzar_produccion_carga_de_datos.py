import os

from tests_privados.test_tools import IICTest, timeout
from backend.consultas import (
    avanzar_produccion,
    cargar_juguete_objeto,
    cargar_juguete_recurso,
)
from backend.nodo_ligado import NodoLigado

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


def cadena_productores(pares):
    cabeza = None
    for id_juguete, tiempo_actual in sorted(pares):
        nodo = NodoLigado(id=id_juguete, tiempo_actual=tiempo_actual)
        cabeza = nodo if cabeza is None else cabeza.insertar(nodo)
    return cabeza


def tiempos_cadena(cabeza):
    tiempos = []
    while cabeza is not None:
        tiempos.append((cabeza.id, cabeza.tiempo_actual))
        cabeza = cabeza.siguiente
    return tiempos


def ejecutar(path, productores, objetos, minutos):
    gen_jr = cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv"))
    gen_jo = cargar_juguete_objeto(os.path.join(path, "juguete_objeto.csv"))
    cadena = cadena_productores(productores)
    resultado = list(avanzar_produccion(gen_jr, gen_jo, cadena, objetos, minutos=minutos))
    return resultado, tiempos_cadena(cadena)


class TestAvanzarProduccionCargaDatosPrivado(IICTest):
    """
    Verifica avanzar_produccion con datasets privados S, M, L y XL.
    Comprueba recursos generados, bonificacion por objetos presentes, eficiencia con
    minutos altos y mutacion de tiempo_actual en la cadena de productores.
    """

    def assertResultadoFloat(self, resultado, esperado):
        self.assertEqual(len(resultado), len(esperado))
        for (id_recurso, cantidad), (id_esperado, cantidad_esperada) in zip(resultado, esperado):
            self.assertEqual(id_recurso, id_esperado)
            self.assertAlmostEqual(cantidad, cantidad_esperada, places=10)

    @timeout(N_SECOND)
    def test_S_resultado_corto_y_mutacion(self):
        """
        Dataset S, avance=1 min, sin objetos.
          J1  (t_espera= 2, t_actual= 0):  0+1= 1 < 2    -> sin produccion, tiempo=1
          J12 (t_espera= 4, t_actual= 3):  3+1= 4 = 4    -> 1 ciclo, R12 cant=1.0, tiempo=0
          J33 (t_espera=193, t_actual=12): 12+1=13 < 193  -> sin produccion, tiempo=13
        Verifica que solo J12 produce y que todos los nodos mutan tiempo_actual.
        """
        resultado, tiempos = ejecutar(PATH_S, [(1, 0), (12, 3), (33, 12)], set(), 1)

        self.assertResultadoFloat(resultado, [(12, 1.0)])
        self.assertEqual(tiempos, [(1, 1), (12, 0), (33, 13)])

    @timeout(N_SECOND)
    def test_S_bonus_con_objetos_presentes(self):
        """
        Dataset S, avance=30 min, t_actual=0 para todos, objetos={1,2,3,4,5,10,20,30}.
        ciclos = 30 // t_espera. Cantidades con bonus (multiplicar por 1.1^favoritos):
          J1 (t_espera=2, R=7,  cant=2, fav {1,4} presentes): 15 ciclos * 2 * 1.1^2 = 36.3
          J2 (t_espera=3, R=5,  cant=1, fav {2}   presente ): 10 ciclos * 1 * 1.1   = 11.0
          J3 (t_espera=4, R=6,  cant=2, fav {3}   presente ):  7 ciclos * 2 * 1.1   = 15.4
          J4 (t_espera=1, R=10, cant=1, fav {7}   ausente  ): 30 ciclos * 1         = 30.0
          J5 (t_espera=5, R=2,  cant=4, fav {8}   ausente  ):  6 ciclos * 4         = 24.0
        """
        resultado, tiempos = ejecutar(
            PATH_S,
            [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)],
            {1, 2, 3, 4, 5, 10, 20, 30},
            30,
        )

        self.assertResultadoFloat(resultado, [
            (2, 24.0),
            (5, 11.0),
            (6, 15.400000000000002),
            (7, 36.300000000000004),
            (10, 30.0),
        ])
        self.assertEqual(tiempos, [(1, 0), (2, 0), (3, 2), (4, 0), (5, 0)])

    @timeout(N_SECOND)
    def test_M_varios_productores_dataset_real(self):
        """
        Dataset M, avance=12 min, sin objetos.
          J100 (t_espera=18,  t_actual= 6):  6+12=18 >= 18  -> 1 ciclo,  R4  cant=7.0, tiempo= 0
          J105 (t_espera=146, t_actual= 2):  2+12=14 < 146  -> sin produccion,          tiempo=14
          J120 (t_espera=24,  t_actual= 4):  4+12=16 < 24   -> sin produccion,          tiempo=16
          J130 (t_espera= 6,  t_actual= 0):  0+12=12 >= 6   -> 2 ciclos, R48 cant=4.0, tiempo= 0
          J147 (t_espera=24,  t_actual= 1):  1+12=13 < 24   -> sin produccion,          tiempo=13
        """
        resultado, tiempos = ejecutar(
            PATH_M,
            [(100, 6), (105, 2), (120, 4), (130, 0), (147, 1)],
            set(),
            12,
        )

        self.assertResultadoFloat(resultado, [(4, 7.0), (48, 4.0)])
        self.assertEqual(tiempos, [(100, 0), (105, 14), (120, 16), (130, 0), (147, 13)])

    @timeout(N_SECOND)
    def test_L_minutos_altos_eficiencia(self):
        """
        Dataset L, avance=400 min, sin objetos. Verifica calculo por division entera
        (no simulacion minuto a minuto). Ciclos completados por cada productor:
          J200 (t_espera= 50, t_actual=0): 400/50 =  8 ciclos, R599  * 2 =  16.0, tiempo= 0
          J210 (t_espera= 21, t_actual=1): 401/21 = 19 ciclos, R13   * 7 = 133.0, tiempo= 2
          J220 (t_espera= 39, t_actual=2): 402/39 = 10 ciclos, R410  * 2 =  20.0, tiempo=12
          J230 (t_espera= 28, t_actual=3): 403/28 = 14 ciclos, R393  * 7 =  98.0, tiempo=11
          J294 (t_espera= 54, t_actual=4): 404/54 =  7 ciclos, R299  *10 =  70.0, tiempo=26
          J380 (t_espera= 94, t_actual=0): 400/94 =  4 ciclos, R545  *11 =  44.0, tiempo=24
        """
        resultado, tiempos = ejecutar(
            PATH_L,
            [(200, 0), (210, 1), (220, 2), (230, 3), (294, 4), (380, 0)],
            set(),
            400,
        )

        self.assertResultadoFloat(resultado, [
            (13, 133.0),
            (299, 70.0),
            (393, 98.0),
            (410, 20.0),
            (545, 44.0),
            (599, 16.0),
        ])
        self.assertEqual(
            tiempos,
            [(200, 0), (210, 2), (220, 12), (230, 11), (294, 26), (380, 24)],
        )

    @timeout(N_SECOND)
    def test_XL_minutos_altos_eficiencia(self):
        """
        Dataset XL, avance=400 min, sin objetos. Productores dispersos en IDs bajos,
        medios y altos; exige ubicar cada JugueteRecurso sin recorrer el dataset completo:
          J14  (t_espera= 94, t_actual= 6): 406/ 94 =  4 ciclos, R306  * 10 =  40.0, tiempo= 30
          J200 (t_espera= 99, t_actual= 7): 407/ 99 =  4 ciclos, R214  * 12 =  48.0, tiempo= 11
          J500 (t_espera=183, t_actual= 0): 400/183 =  2 ciclos, R331  *  5 =  10.0, tiempo= 34
          J510 (t_espera= 54, t_actual= 1): 401/ 54 =  7 ciclos, R858  *  5 =  35.0, tiempo= 23
          J520 (t_espera= 24, t_actual= 2): 402/ 24 = 16 ciclos, R647  * 11 = 176.0, tiempo= 18
          J530 (t_espera=223, t_actual= 3): 403/223 =  1 ciclo,  R797  *  6 =   6.0, tiempo=180
          J600 (t_espera=110, t_actual= 8): 408/110 =  3 ciclos, R418  *  9 =  27.0, tiempo= 78
          J751 (t_espera=190, t_actual= 4): 404/190 =  2 ciclos, R1113 *  4 =   8.0, tiempo= 24
        """
        resultado, tiempos = ejecutar(
            PATH_XL,
            [(14, 6), (200, 7), (500, 0), (510, 1), (520, 2), (530, 3), (600, 8), (751, 4)],
            set(),
            400,
        )

        self.assertResultadoFloat(resultado, [
            (214, 48.0),
            (306, 40.0),
            (331, 10.0),
            (418, 27.0),
            (647, 176.0),
            (797, 6.0),
            (858, 35.0),
            (1113, 8.0),
        ])
        self.assertEqual(
            tiempos,
            [(14, 30), (200, 11), (500, 34), (510, 23), (520, 18), (530, 180), (600, 78), (751, 24)],
        )

import os

from tests_privados.test_tools import IICTest, timeout
from backend.consultas import (
    cargar_juguete,
    cargar_juguete_objeto,
    cargar_juguete_recurso,
    crear_recursos,
)

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


def cargar_generador(path):
    gen_jr = cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv"))
    gen_jo = cargar_juguete_objeto(os.path.join(path, "juguete_objeto.csv"))
    generador = crear_recursos(gen_jr, gen_jo)
    next(generador)
    return generador


def cargar_juguetes(path):
    return {
        juguete.id_juguete: juguete
        for juguete in cargar_juguete(os.path.join(path, "juguetes.csv"))
    }


def tuplas_cadena(cabeza):
    resultado = []
    while cabeza is not None:
        resultado.append((cabeza.id, cabeza.tiempo_actual))
        cabeza = cabeza.siguiente
    return resultado


class TestCrearRecursosCargaDatosPrivado(IICTest):
    """
    Verifica crear_recursos con datasets privados S, M, L y XL.
    Comprueba secuencias de send, estado final, objetos acumulados y eficiencia con
    minutos altos sobre datos reales.
    """

    def assertResultadoFloat(self, resultado, esperado):
        self.assertEqual(len(resultado), len(esperado))
        for (id_recurso, cantidad), (id_esperado, cantidad_esperada) in zip(resultado, esperado):
            self.assertEqual(id_recurso, id_esperado)
            self.assertAlmostEqual(cantidad, cantidad_esperada, places=10)

    @timeout(N_SECOND)
    def test_S_none_int_y_estado_final(self):
        """
        Dataset S: se agregan J1 y J2, se mezclan send(None) y send(int), y el
        estado final conserva el tiempo acumulado de ambos productores.
        """
        juguetes = cargar_juguetes(PATH_S)
        generador = cargar_generador(PATH_S)
        generador.send(juguetes[1])
        generador.send(juguetes[2])

        resultados = [
            generador.send(None),
            generador.send(None),
            generador.send(None),
            generador.send(2),
        ]
        cadena, objetos = generador.send("end")

        esperados = [
            tuple(),
            ((7, 2.0),),
            ((5, 1.0),),
            ((7, 2.0),),
        ]
        for resultado, esperado in zip(resultados, esperados):
            self.assertResultadoFloat(resultado, esperado)
        self.assertEqual(tuplas_cadena(cadena), [(1, 1), (2, 2)])
        self.assertEqual(objetos, set())

    @timeout(N_SECOND)
    def test_S_set_persistente_y_bonus(self):
        """
        Dataset S: el set interno acumula objetos entre envios, por lo que J1
        aumenta su bonus en la segunda produccion.
        """
        juguetes = cargar_juguetes(PATH_S)
        generador = cargar_generador(PATH_S)
        generador.send(juguetes[1])

        self.assertIsNone(generador.send({1}))
        primer_resultado = generador.send(10)
        self.assertIsNone(generador.send({4, 999}))
        segundo_resultado = generador.send(10)
        cadena, objetos = generador.send("end")

        self.assertResultadoFloat(primer_resultado, ((7, 11.0),))
        self.assertResultadoFloat(segundo_resultado, ((7, 12.100000000000001),))
        self.assertEqual(tuplas_cadena(cadena), [(1, 0)])
        self.assertEqual(objetos, {1, 4, 999})

    @timeout(N_SECOND)
    def test_M_varios_productores_reales(self):
        """
        Dataset M, avance=20 min, todos en t_actual=0:
          J100 (t_espera=18):  20/ 18= 1 ciclo,  R4  * 7 =  7.0, tiempo= 2
          J105 (t_espera=146): 20/146= 0 ciclos,                  tiempo=20
          J120 (t_espera=24):  20/ 24= 0 ciclos,                  tiempo=20
          J130 (t_espera= 6):  20/  6= 3 ciclos, R48 * 2 =  6.0, tiempo= 2
          J147 (t_espera=24):  20/ 24= 0 ciclos,                  tiempo=20
        """
        juguetes = cargar_juguetes(PATH_M)
        generador = cargar_generador(PATH_M)
        for id_juguete in (100, 105, 120, 130, 147):
            generador.send(juguetes[id_juguete])

        resultado = generador.send(20)
        cadena, objetos = generador.send("end")

        self.assertResultadoFloat(resultado, ((4, 7.0), (48, 6.0)))
        self.assertEqual(
            tuplas_cadena(cadena),
            [(100, 2), (105, 20), (120, 20), (130, 2), (147, 20)],
        )
        self.assertEqual(objetos, set())

    @timeout(N_SECOND)
    def test_L_minutos_altos_eficiencia(self):
        """
        Dataset L, avance=400 min, todos en t_actual=0. Verifica calculo por
        division entera (no simulacion minuto a minuto):
          J200 (t_espera= 50): 400/ 50=  8 ciclos, R599  * 2 =  16.0, tiempo= 0
          J210 (t_espera= 21): 400/ 21= 19 ciclos, R13   * 7 = 133.0, tiempo= 1
          J220 (t_espera= 39): 400/ 39= 10 ciclos, R410  * 2 =  20.0, tiempo=10
          J230 (t_espera= 28): 400/ 28= 14 ciclos, R393  * 7 =  98.0, tiempo= 8
          J294 (t_espera= 54): 400/ 54=  7 ciclos, R299  *10 =  70.0, tiempo=22
          J380 (t_espera= 94): 400/ 94=  4 ciclos, R545  *11 =  44.0, tiempo=24
        """
        juguetes = cargar_juguetes(PATH_L)
        generador = cargar_generador(PATH_L)
        for id_juguete in (200, 210, 220, 230, 294, 380):
            generador.send(juguetes[id_juguete])

        resultado = generador.send(400)
        cadena, objetos = generador.send("end")

        self.assertResultadoFloat(resultado, (
            (13, 133.0),
            (299, 70.0),
            (393, 98.0),
            (410, 20.0),
            (545, 44.0),
            (599, 16.0),
        ))
        self.assertEqual(
            tuplas_cadena(cadena),
            [(200, 0), (210, 1), (220, 10), (230, 8), (294, 22), (380, 24)],
        )
        self.assertEqual(objetos, set())

    @timeout(N_SECOND)
    def test_XL_minutos_altos_eficiencia(self):
        """
        Dataset XL, avance=400 min, todos en t_actual=0. Productores dispersos en
        IDs bajos, medios y altos; exige ubicar cada JugueteRecurso sin recorrer
        el dataset completo:
          J15  (t_espera=172): 400/172=  2 ciclos, R1114 * 9 =  18.0, tiempo= 56
          J100 (t_espera=216): 400/216=  1 ciclo,  R958  * 3 =   3.0, tiempo=184
          J300 (t_espera= 84): 400/ 84=  4 ciclos, R1496 * 9 =  36.0, tiempo= 64
          J500 (t_espera=183): 400/183=  2 ciclos, R331  * 5 =  10.0, tiempo= 34
          J503 (t_espera= 42): 400/ 42=  9 ciclos, R464  * 2 =  18.0, tiempo= 22
          J510 (t_espera= 54): 400/ 54=  7 ciclos, R858  * 5 =  35.0, tiempo= 22
          J520 (t_espera= 24): 400/ 24= 16 ciclos, R647  *11 = 176.0, tiempo= 16
          J530 (t_espera=223): 400/223=  1 ciclo,  R797  * 6 =   6.0, tiempo=177
          J650 (t_espera= 68): 400/ 68=  5 ciclos, R1288 * 6 =  30.0, tiempo= 60
          J751 (t_espera=190): 400/190=  2 ciclos, R1113 * 4 =   8.0, tiempo= 20
        """
        juguetes = cargar_juguetes(PATH_XL)
        generador = cargar_generador(PATH_XL)
        for id_juguete in (15, 100, 300, 500, 503, 510, 520, 530, 650, 751):
            generador.send(juguetes[id_juguete])

        resultado = generador.send(400)
        cadena, objetos = generador.send("end")

        self.assertResultadoFloat(resultado, (
            (331, 10.0),
            (464, 18.0),
            (647, 176.0),
            (797, 6.0),
            (858, 35.0),
            (958, 3.0),
            (1113, 8.0),
            (1114, 18.0),
            (1288, 30.0),
            (1496, 36.0),
        ))
        self.assertEqual(
            tuplas_cadena(cadena),
            [(15, 56), (100, 184), (300, 64), (500, 34), (503, 22),
             (510, 22), (520, 16), (530, 177), (650, 60), (751, 20)],
        )
        self.assertEqual(objetos, set())

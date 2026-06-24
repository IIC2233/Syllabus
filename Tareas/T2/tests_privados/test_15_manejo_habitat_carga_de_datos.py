import os

from tests_privados.test_tools import IICTest, timeout
from backend.consultas import (
    cargar_habitat_objeto,
    cargar_juguete,
    cargar_juguete_habitat,
    cargar_objeto_recurso,
    cargar_periodo_dia,
    cargar_recurso_recurso,
    manejo_habitat,
)

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


def crear_generador(path, tiempo_inicial=0):
    generador = manejo_habitat(
        cargar_juguete(os.path.join(path, "juguetes.csv")),
        cargar_juguete_habitat(os.path.join(path, "juguete_habitat.csv")),
        cargar_habitat_objeto(os.path.join(path, "habitat_objeto.csv")),
        cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv")),
        cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv")),
        cargar_periodo_dia(os.path.join(path, "periodo_dia.csv")),
        tiempo_inicial,
    )
    next(generador)
    return generador

def tuplas_cadena(cabeza, *attrs):
    resultado = []
    while cabeza is not None:
        resultado.append(tuple(getattr(cabeza, attr) for attr in attrs))
        cabeza = cabeza.siguiente
    return resultado


def report(generador):
    tiempo, juguetes, habitats, objetos, recursos = generador.send("report")
    return (
        tiempo,
        sorted(juguetes),
        tuplas_cadena(habitats, "id", "tiempo_presente"),
        tuplas_cadena(objetos, "id", "cantidad"),
        tuplas_cadena(recursos, "id", "cantidad"),
    )


class TestManejoHabitatCargaDatosPrivado(IICTest):
    """
    Verifica manejo_habitat con datasets privados S, M y L.
    Comprueba tiempo, creacion, apariciones tempranas y estado reportado.
    """

    @timeout(N_SECOND)
    def test_S_tiempo_inicial_y_send_none(self):
        """
        Dataset S: tiempo_inicial se respeta y send(None) avanza de a una unidad.
        """
        generador = crear_generador(PATH_S, tiempo_inicial=10)

        self.assertEqual(report(generador)[:2], (10, []))
        self.assertEqual(generador.send(None), tuple())
        self.assertEqual(generador.send(None), tuple())
        self.assertEqual(report(generador)[:2], (12, []))

    @timeout(N_SECOND)
    def test_S_crear_y_apariciones_tempranas(self):
        """
        Dataset S: con recursos suficientes se crean varios habitats, y al avanzar
        tres ticks aparecen los primeros juguetes esperados.
        """
        generador = crear_generador(PATH_S)
        self.assertIsNone(generador.send(tuple((i, 20) for i in range(1, 80))))

        objetos, habitats = generador.send("crear")
        self.assertEqual(objetos, set(range(1, 10)))
        self.assertEqual(len(habitats), 31)
        self.assertEqual(habitats[:10], tuple(range(1, 11)))
        self.assertEqual(habitats[-5:], (41, 45, 46, 48, 50))

        self.assertEqual(generador.send(None), tuple())
        self.assertEqual(generador.send(None), (1, 7, 11))
        self.assertEqual(generador.send(None), (9,))

        tiempo, juguetes, habitats_report, objetos_report, recursos_report = report(generador)
        self.assertEqual(tiempo, 3)
        self.assertEqual(juguetes, [1, 7, 9, 11])
        self.assertEqual(habitats_report[:5], [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3)])
        self.assertEqual(objetos_report[:5], [(1, 9), (2, 20), (3, 10), (4, 11), (5, 9)])
        self.assertEqual(recursos_report[:5], [(1, 1), (2, 20), (3, 20), (4, 20), (5, 9)])
        self.assertEqual(recursos_report[-5:], [(75, 20), (76, 20), (77, 20), (78, 20), (79, 20)])

    @timeout(N_SECOND)
    def test_M_crear_stock_generoso(self):
        """
        Dataset M: crear con stock generoso fabrica muchos objetos y habitats en
        orden, sin comparar una lista completa muy larga.
        """
        generador = crear_generador(PATH_M)
        self.assertIsNone(generador.send(tuple((i, 20) for i in range(1, 200))))

        objetos, habitats = generador.send("crear")

        self.assertEqual(sorted(objetos), [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 34, 35, 36, 37, 38, 40,
        ])
        self.assertEqual(habitats, (
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 22, 23,
            26, 28, 31, 34, 35, 39, 43, 44, 47, 48, 50, 51, 58, 63, 64, 78, 84, 91,
            94, 122, 123, 134, 136, 140, 141, 148, 173, 175, 200,
        ))

    @timeout(N_SECOND)
    def test_L_crear_stock_generoso_eficiencia(self):
        """
        Dataset L: caso grande con stock generoso para verificar eficiencia y
        estructura de la creacion.
        """
        generador = crear_generador(PATH_L)
        self.assertIsNone(generador.send(tuple((i, 20) for i in range(1, 700))))

        objetos, habitats = generador.send("crear")
        tiempo, juguetes, habitats_report, objetos_report, recursos_report = report(generador)

        obj = sorted(objetos)
        self.assertEqual(len(obj), 178)
        self.assertEqual(obj[:5], [1, 2, 3, 4, 5])        # inicio
        self.assertEqual(obj[len(obj) // 4], 51)           # primer cuarto
        self.assertEqual(obj[len(obj) // 2], 101)          # mitad
        self.assertEqual(obj[3 * len(obj) // 4], 154)      # tercer cuarto
        self.assertEqual(obj[-5:], [196, 197, 198, 199, 200])  # final

        self.assertEqual(len(habitats), 223)
        self.assertEqual(habitats[:5], (1, 2, 3, 4, 5))           # inicio
        self.assertEqual(habitats[len(habitats) // 4], 68)         # primer cuarto
        self.assertEqual(habitats[len(habitats) // 2], 183)        # mitad
        self.assertEqual(habitats[3 * len(habitats) // 4], 466)    # tercer cuarto
        self.assertEqual(habitats[-5:], (966, 968, 970, 977, 999)) # final
        self.assertEqual(tiempo, 0)
        self.assertEqual(juguetes, [])
        self.assertEqual(habitats_report[:5], [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
        self.assertEqual(len(objetos_report), 178)
        self.assertEqual(len(recursos_report), 653)

    @timeout(N_SECOND)
    def test_XL_crear_stock_parcial(self):
        """
        Dataset XL con stock R1-R200 (20 unidades cada uno). Verifica integracion
        completa sobre el dataset mas grande con un subconjunto de recursos real.
        """
        generador = crear_generador(PATH_XL)
        generador.send(tuple((i, 20) for i in range(1, 201)))

        objetos, habitats = generador.send("crear")

        self.assertEqual(sorted(objetos), [
            1, 2, 3, 4, 5, 6, 7, 8, 15, 37, 61, 68, 97, 102,
            112, 121, 146, 296, 333, 354, 360, 366, 379, 382, 423, 433, 439, 476, 486,
        ])
        self.assertEqual(len(habitats), 53)
        self.assertEqual(habitats[:5], (1, 2, 3, 4, 5))              # inicio
        self.assertEqual(habitats[len(habitats) // 4], 69)            # primer cuarto
        self.assertEqual(habitats[len(habitats) // 2], 777)           # mitad
        self.assertEqual(habitats[3 * len(habitats) // 4], 1787)      # tercer cuarto
        self.assertEqual(habitats[-5:], (2094, 2123, 2180, 2230, 2243, 2371, 2373, 2462)[-5:])

import os

from tests_privados.test_tools import IICTest, timeout
from backend.consultas import agregar_recursos, cargar_juguete_recurso
from backend.nodo_ligado import NodoLigado

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


def cadena_recursos(pares):
    cabeza = None
    for id_recurso, cantidad in sorted(pares):
        nodo = NodoLigado(id=id_recurso, cantidad=cantidad)
        cabeza = nodo if cabeza is None else cabeza.insertar(nodo)
    return cabeza


def tuplas_cadena(cabeza):
    resultado = []
    while cabeza is not None:
        resultado.append((cabeza.id, cabeza.cantidad))
        cabeza = cabeza.siguiente
    return resultado


def pares_juguete_recurso(path):
    generador = cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv"))
    return [(jr.id_recurso, jr.cantidad) for jr in generador]


def agregar_pares(pares):
    acumulados = {}
    for id_recurso, cantidad in pares:
        if id_recurso not in acumulados:
            acumulados[id_recurso] = 0
        acumulados[id_recurso] += cantidad
    return sorted(acumulados.items())


class TestAgregarRecursosCargaDatosPrivado(IICTest):
    """
    Verifica agregar_recursos con recursos obtenidos desde datasets privados.
    Comprueba orden completo en S y eficiencia con muchos recursos en L y XL.
    """

    @timeout(N_SECOND)
    def test_S_primeros_recursos_reales(self):
        """
        Dataset S. El CSV viene ordenado por id_juguete, no por id_recurso.
        Cadena inicial con pares[:4] ordenados por id: 5->6->7->10.
        pares[4:8] = (2,4),(8,1),(3,3),(9,2) son todos nuevos: se insertan en orden.
        Verifica la cadena completa resultante de 8 nodos.
        """
        pares = pares_juguete_recurso(PATH_S)
        cadena = cadena_recursos(pares[:4])

        resultado = agregar_recursos(cadena, tuple(pares[4:8]))

        self.assertEqual(
            tuplas_cadena(resultado),
            [(2, 4), (3, 3), (5, 1), (6, 2), (7, 2), (8, 1), (9, 2), (10, 1)],
        )

    @timeout(N_SECOND)
    def test_S_recurso_repetido_en_datos_reales(self):
        """
        Dataset S. Cadena inicial: (5,10),(7,20).
        nuevos_recursos: pares[0]=(7,2), pares[10]=(1,3), pares[20]=(14,4).
          (1, 3): nuevo, inserta al inicio
          (7, 2): existe, acumula: 20+2=22
          (14,4): nuevo, inserta al final
        Verifica que id=7 no se duplique.
        """
        pares = pares_juguete_recurso(PATH_S)
        cadena = cadena_recursos(((5, 10), (7, 20)))
        nuevos = (pares[0], pares[10], pares[20])

        resultado = agregar_recursos(cadena, nuevos)

        self.assertEqual(tuplas_cadena(resultado), [(1, 3), (5, 10), (7, 22), (14, 4)])

    @timeout(N_SECOND)
    def test_L_muchos_recursos_eficiencia_y_orden(self):
        """
        Dataset L. Cadena inicial con pares[:100] pre-agregados; se suman 300
        entradas mas (pares[100:400]). Se verifican puntos representativos:
          largo: 285 nodos, inicio: [(1,23),...], mitad: (312,11), final: [...(599,7)]
        """
        pares = pares_juguete_recurso(PATH_L)
        cadena = cadena_recursos(agregar_pares(pares[:100]))

        resultado = tuplas_cadena(agregar_recursos(cadena, tuple(pares[100:400])))

        self.assertEqual(len(resultado), 285)
        self.assertEqual(resultado[:5], [(1, 23), (2, 24), (3, 3), (4, 1), (5, 22)])
        self.assertEqual(resultado[len(resultado) // 2], (312, 11))
        self.assertEqual(
            resultado[-5:],
            [(590, 1), (594, 6), (595, 2), (598, 3), (599, 7)],
        )

    @timeout(N_SECOND)
    def test_XL_muchos_recursos_eficiencia(self):
        """
        Dataset XL. Cadena inicial con pares[:200] pre-agregados; se suman 600
        entradas mas (pares[200:800]), IDs hasta 1498. Puntos representativos:
          largo: 624 nodos, inicio: [(1,3),...], mitad: (765,8), final: [...(1498,8)]
        """
        pares = pares_juguete_recurso(PATH_XL)
        cadena = cadena_recursos(agregar_pares(pares[:200]))

        resultado = tuplas_cadena(agregar_recursos(cadena, tuple(pares[200:800])))

        self.assertEqual(len(resultado), 624)
        self.assertEqual(resultado[:5], [(1, 3), (2, 7), (3, 3), (4, 13), (5, 1)])
        self.assertEqual(resultado[len(resultado) // 2], (765, 8))
        self.assertEqual(
            resultado[-5:],
            [(1494, 12), (1495, 4), (1496, 9), (1497, 8), (1498, 8)],
        )

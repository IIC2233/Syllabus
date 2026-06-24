from tests_privados.test_tools import IICTest, timeout
from backend.consultas import agregar_recursos
from backend.nodo_ligado import NodoLigado

N_SECOND_BASE = 0.3


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


class TestAgregarRecursosPrivado(IICTest):
    """
    Pruebas de correctitud para agregar_recursos.
    Verifica cadena vacia, acumulacion, insercion en orden y ausencia de nodos
    duplicados recorriendo la cadena resultante.
    """

    @timeout(N_SECOND_BASE)
    def test_cadena_none_y_nuevos_vacios_retorna_none(self):
        """
        Si no hay cadena inicial ni recursos nuevos, el resultado debe ser None.
        """
        self.assertIsNone(agregar_recursos(None, tuple()))

    @timeout(N_SECOND_BASE)
    def test_cadena_none_crea_cadena_ordenada(self):
        """
        Si la cadena inicial es None, los recursos nuevos crean una cadena ordenada
        por id aunque vengan desordenados.
        """
        resultado = agregar_recursos(None, ((3, 5), (1, 2)))

        self.assertEqual(tuplas_cadena(resultado), [(1, 2), (3, 5)])

    @timeout(N_SECOND_BASE)
    def test_nuevos_vacios_no_modifica_cadena(self):
        """
        Si nuevos_recursos esta vacio, debe retornar la misma cabeza sin cambiar
        cantidades ni orden.
        """
        cadena = cadena_recursos(((2, 5), (4, 10)))

        resultado = agregar_recursos(cadena, tuple())

        self.assertIs(resultado, cadena)
        self.assertEqual(tuplas_cadena(resultado), [(2, 5), (4, 10)])

    @timeout(N_SECOND_BASE)
    def test_solo_acumula_existentes(self):
        """
        Cuando todos los recursos nuevos ya existen, solo se suman cantidades y no
        se insertan nodos nuevos.
        """
        cadena = cadena_recursos(((2, 5), (4, 10)))

        resultado = agregar_recursos(cadena, ((2, 3), (4, 1)))

        self.assertEqual(tuplas_cadena(resultado), [(2, 8), (4, 11)])

    @timeout(N_SECOND_BASE)
    def test_inserta_inicio_medio_final_y_acumula(self):
        """
        En una misma llamada puede insertar al inicio, al medio y al final, ademas
        de acumular un recurso existente.
        """
        cadena = cadena_recursos(((4, 10), (8, 1)))

        resultado = agregar_recursos(cadena, ((2, 5), (4, 3), (6, 7), (10, 2)))

        self.assertEqual(
            tuplas_cadena(resultado),
            [(2, 5), (4, 13), (6, 7), (8, 1), (10, 2)],
        )

    @timeout(N_SECOND_BASE)
    def test_repite_ids_en_nuevos_recursos(self):
        """
        Si nuevos_recursos repite ids, cada aparicion debe acumularse en el mismo
        nodo y la cadena debe mantenerse ordenada.
        """
        cadena = cadena_recursos(((5, 10),))

        resultado = agregar_recursos(cadena, ((5, 1), (3, 2), (3, 4), (5, 6)))

        self.assertEqual(tuplas_cadena(resultado), [(3, 6), (5, 17)])

    @timeout(N_SECOND_BASE)
    def test_no_duplica_nodos_existentes(self):
        """
        Acumular varias veces recursos existentes no debe crear nodos duplicados
        para el mismo id.
        """
        cadena = cadena_recursos(((1, 4), (2, 5), (3, 6)))

        resultado = agregar_recursos(cadena, ((2, 1), (2, 2), (3, 3), (1, 4)))
        ids = [id_recurso for id_recurso, _ in tuplas_cadena(resultado)]

        self.assertEqual(tuplas_cadena(resultado), [(1, 8), (2, 8), (3, 9)])
        self.assertEqual(len(ids), len(set(ids)))

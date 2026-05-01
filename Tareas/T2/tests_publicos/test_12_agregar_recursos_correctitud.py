import unittest
from tests_publicos.test_tools import IICTest, timeout
from backend.consultas import agregar_recursos
from backend.nodo_ligado import NodoLigado

N_SECOND = 0.3

def make_recurso_nodo(id_recurso, cantidad):
    return NodoLigado(id=id_recurso, cantidad=cantidad)

def cadena_a_dict(nodo):
    """Convierte cadena de NodoLigado de Recurso en dict {id: cantidad}."""
    resultado = {}
    while nodo is not None:
        resultado[nodo.id] = nodo.cantidad
        nodo = nodo.siguiente
    return resultado

def make_cadena_recursos(pares):
    """Construye cadena NodoLigado desde lista de (id, cantidad)."""
    cabeza = None
    for id_r, cant in sorted(pares, key=lambda x: x[0]):
        nodo = make_recurso_nodo(id_r, cant)
        if cabeza is None:
            cabeza = nodo
        else:
            cabeza = cabeza.insertar(nodo)
    return cabeza


class TestAgregarRecursosCorrectitud(IICTest):
    """
    Pruebas de correctitud para agregar_recursos(recursos: NodoLigado,
    nuevos_recursos: Tuple[Tuple[int, int]]) -> NodoLigado.
    """

    @timeout(N_SECOND)
    def test_nuevos_recursos_vacio_no_modifica_cadena(self):
        """
        Si nuevos_recursos es una tupla vacía, retorna el NodoLigado sin cambios.
        """
        cadena = make_cadena_recursos([(5, 10), (10, 3)])
        resultado = agregar_recursos(cadena, tuple())
        d = cadena_a_dict(resultado)
        self.assertEqual(d, {5: 10, 10: 3})

    @timeout(N_SECOND)
    def test_recurso_ya_existente_suma_cantidad(self):
        """
        Si el recurso ya existe en la cadena, se suma la cantidad
        (no se crea un nodo nuevo).
        """
        cadena = make_cadena_recursos([(5, 10)])
        nuevos = ((5, 7),)
        resultado = agregar_recursos(cadena, nuevos)
        d = cadena_a_dict(resultado)
        self.assertEqual(d[5], 17)
        # Solo un nodo con id=5
        ids = list(d.keys())
        self.assertEqual(ids.count(5), 1)

    @timeout(N_SECOND)
    def test_recurso_nuevo_se_crea_nodo(self):
        """
        Si el recurso no existe en la cadena, se crea un nuevo NodoLigado.
        """
        cadena = make_cadena_recursos([(5, 10)])
        nuevos = ((99, 4),)
        resultado = agregar_recursos(cadena, nuevos)
        d = cadena_a_dict(resultado)
        self.assertIn(99, d)
        self.assertEqual(d[99], 4)
        self.assertEqual(list(d.keys()), [5, 99])

    @timeout(N_SECOND)
    def test_cadena_inicial_none_crea_nuevos_nodos(self):
        """
        Si recursos es None (cadena vacía), se crean nodos para todos los nuevos.
        """
        nuevos = ((1, 5), (2, 3))
        resultado = agregar_recursos(None, nuevos)
        d = cadena_a_dict(resultado)
        self.assertEqual(d, {1: 5, 2: 3})

    @timeout(N_SECOND)
    def test_multiples_recursos_mixtos(self):
        """
        Algunos recursos existen (se suman) y otros son nuevos (se crean).
        """
        cadena = make_cadena_recursos([(1, 10), (3, 5)])
        nuevos = ((1, 2), (2, 8), (3, 1))
        resultado = agregar_recursos(cadena, nuevos)
        d = cadena_a_dict(resultado)
        self.assertEqual(d[1], 12)
        self.assertEqual(d[2], 8)
        self.assertEqual(d[3], 6)

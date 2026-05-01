import os

from tests_publicos.test_tools import IICTest, timeout
from backend.consultas import agregar_recursos, cargar_juguete_recurso
from backend.nodo_ligado import NodoLigado

N_SECOND = 0.3
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


def _tomar_todos_juguete_recurso(path):
    gen = cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv"))
    return list(gen)

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

class TestAgregarRecursosCargaDatos(IICTest):
    """
    Verifica agregar_recursos cargando todos los datos inicialmente,
    creando una cadena con parte de ellos, agregando el resto y verificando
    que el primero, último y uno del medio sean correctos.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_0_agregar_recursos_S(self):
        """
        S — Cargar todos los recursos, crear cadena con la mitad,
        agregar el resto y verificar que primero, último y uno del medio
        estén presentes en el resultado.
        """
        jrs = _tomar_todos_juguete_recurso(PATH_S)
        if len(jrs) < 2:
            self.skipTest("Datos insuficientes")

        mid = len(jrs) // 2
        initial = jrs[:mid]
        to_add = jrs[mid:]

        cadena = make_cadena_recursos([(jr.id_recurso, jr.cantidad) for jr in initial])

        nuevos = tuple((jr.id_recurso, jr.cantidad) for jr in to_add)
        resultado = agregar_recursos(cadena, nuevos)
        resultado_dict = cadena_a_dict(resultado)

        self.assertIn(initial[0].id_recurso, resultado_dict)
        self.assertGreater(resultado_dict[initial[0].id_recurso], 0)

        self.assertIn(jrs[-1].id_recurso, resultado_dict)
        self.assertGreater(resultado_dict[jrs[-1].id_recurso], 0)

        mid_item = jrs[len(jrs) // 2]
        self.assertIn(mid_item.id_recurso, resultado_dict)
        self.assertGreater(resultado_dict[mid_item.id_recurso], 0)

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_1_agregar_recursos_M(self):
        """
        M — Cargar todos los recursos, crear cadena con la mitad,
        agregar el resto y verificar que primero, último y uno del medio
        estén presentes en el resultado.
        """
        jrs = _tomar_todos_juguete_recurso(PATH_M)
        if len(jrs) < 2:
            self.skipTest("Datos insuficientes")

        mid = len(jrs) // 2
        initial = jrs[:mid]
        to_add = jrs[mid:]

        cadena = make_cadena_recursos([(jr.id_recurso, jr.cantidad) for jr in initial])
        nuevos = tuple((jr.id_recurso, jr.cantidad) for jr in to_add)
        resultado = agregar_recursos(cadena, nuevos)
        resultado_dict = cadena_a_dict(resultado)

        self.assertIn(initial[0].id_recurso, resultado_dict)
        self.assertGreater(resultado_dict[initial[0].id_recurso], 0)

        self.assertIn(jrs[-1].id_recurso, resultado_dict)
        self.assertGreater(resultado_dict[jrs[-1].id_recurso], 0)

        mid_item = jrs[len(jrs) // 2]
        self.assertIn(mid_item.id_recurso, resultado_dict)
        self.assertGreater(resultado_dict[mid_item.id_recurso], 0)

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_2_agregar_recursos_L(self):
        """
        L — Cargar todos los recursos de CSV grande, crear cadena con la mitad,
        agregar el resto y verificar que primero, último y uno del medio
        estén presentes en el resultado.
        """
        jrs = _tomar_todos_juguete_recurso(PATH_L)
        if len(jrs) < 2:
            self.skipTest("Datos insuficientes")

        mid = len(jrs) // 2
        initial = jrs[:mid]
        to_add = jrs[mid:]

        cadena = make_cadena_recursos([(jr.id_recurso, jr.cantidad) for jr in initial])
        nuevos = tuple((jr.id_recurso, jr.cantidad) for jr in to_add)
        resultado = agregar_recursos(cadena, nuevos)
        resultado_dict = cadena_a_dict(resultado)

        self.assertIn(initial[0].id_recurso, resultado_dict)
        self.assertGreater(resultado_dict[initial[0].id_recurso], 0)

        self.assertIn(jrs[-1].id_recurso, resultado_dict)
        self.assertGreater(resultado_dict[jrs[-1].id_recurso], 0)

        mid_item = jrs[len(jrs) // 2]
        self.assertIn(mid_item.id_recurso, resultado_dict)
        self.assertGreater(resultado_dict[mid_item.id_recurso], 0)

from tests_privados.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import habitat_creables
from backend.nodo_ligado import NodoLigado
from utils import Juguete, JugueteRecurso, RecursoRecurso, ObjetoRecurso, HabitatObjeto

N_SECOND_BASE = 0.3


def gen(iterable):
    yield from iterable


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


def ejecutar(juguetes, juguete_recurso, recurso_recurso, objeto_recurso, habitat_objeto, recurso):
    return list(habitat_creables(
        gen(juguetes),
        gen(juguete_recurso),
        gen(recurso_recurso),
        gen(objeto_recurso),
        gen(habitat_objeto),
        recurso,
    ))


class TestHabitatCreablesPrivado(IICTest):
    """
    Pruebas de correctitud para habitat_creables.
    Verifica stock actual, objetos requeridos, suma de recursos, sintesis con
    RecursoRecurso, afinidades y que el stock no se mute.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe retornar un generador.
        """
        assert_es_generador(self, habitat_creables)

    @timeout(N_SECOND_BASE)
    def test_sin_stock_actual_no_crea_habitat_eventual(self):
        """
        Aunque el habitat sea eventualmente fabricable por un juguete presente,
        no es creable ahora si no hay recursos en stock.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_recurso = (JugueteRecurso(1, 1, "00:01", 1),)
        objeto_recurso = (ObjetoRecurso(10, ((1, 2),)),)
        habitat_objeto = (HabitatObjeto(5, ((10, 1),)),)

        resultado = ejecutar(juguetes, juguete_recurso, (), objeto_recurso, habitat_objeto, None)

        self.assertEqual(resultado, [])

    @timeout(N_SECOND_BASE)
    def test_recurso_directo_suficiente(self):
        """
        Si el objeto requerido usa recursos directos disponibles en cantidad
        suficiente, el habitat es creable.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_recurso = (JugueteRecurso(1, 1, "00:01", 1),)
        objeto_recurso = (ObjetoRecurso(10, ((1, 2),)),)
        habitat_objeto = (HabitatObjeto(5, ((10, 1),)),)
        recurso = cadena_recursos(((1, 2),))

        resultado = ejecutar(juguetes, juguete_recurso, (), objeto_recurso, habitat_objeto, recurso)

        self.assertEqual(resultado, [5])

    @timeout(N_SECOND_BASE)
    def test_recurso_directo_insuficiente(self):
        """
        Si falta cantidad del recurso directo requerido por el objeto, el habitat
        no es creable.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_recurso = (JugueteRecurso(1, 1, "00:01", 1),)
        objeto_recurso = (ObjetoRecurso(10, ((1, 2),)),)
        habitat_objeto = (HabitatObjeto(5, ((10, 1),)),)
        recurso = cadena_recursos(((1, 1),))

        resultado = ejecutar(juguetes, juguete_recurso, (), objeto_recurso, habitat_objeto, recurso)

        self.assertEqual(resultado, [])

    @timeout(N_SECOND_BASE)
    def test_varios_objetos_suman_recursos(self):
        """
        Si un habitat requiere varios objetos que usan el mismo recurso, deben
        sumarse todas las cantidades requeridas.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_recurso = (JugueteRecurso(1, 1, "00:01", 1),)
        objeto_recurso = (
            ObjetoRecurso(10, ((1, 2),)),
            ObjetoRecurso(11, ((1, 3),)),
        )
        habitat_objeto = (HabitatObjeto(5, ((10, 1), (11, 1))),)
        recurso = cadena_recursos(((1, 5),))

        resultado = ejecutar(juguetes, juguete_recurso, (), objeto_recurso, habitat_objeto, recurso)

        self.assertEqual(resultado, [5])

    @timeout(N_SECOND_BASE)
    def test_varios_objetos_insuficientes_por_suma(self):
        """
        El stock puede alcanzar para cada objeto por separado, pero no para la suma
        total de recursos que requiere el habitat.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_recurso = (JugueteRecurso(1, 1, "00:01", 1),)
        objeto_recurso = (
            ObjetoRecurso(10, ((1, 2),)),
            ObjetoRecurso(11, ((1, 3),)),
        )
        habitat_objeto = (HabitatObjeto(5, ((10, 1), (11, 1))),)
        recurso = cadena_recursos(((1, 4),))

        resultado = ejecutar(juguetes, juguete_recurso, (), objeto_recurso, habitat_objeto, recurso)

        self.assertEqual(resultado, [])

    @timeout(N_SECOND_BASE)
    def test_recurso_indirecto_con_afinidad(self):
        """
        Un recurso requerido por un objeto puede fabricarse desde recursos del stock
        si existe la afinidad exigida por RecursoRecurso.
        """
        juguetes = (Juguete(1, "uno", (7,), "001"),)
        juguete_recurso = (JugueteRecurso(1, 3, "00:01", 1),)
        recurso_recurso = (RecursoRecurso(8, ((3, 2),), 7),)
        objeto_recurso = (ObjetoRecurso(4, ((8, 1),)),)
        habitat_objeto = (HabitatObjeto(40, ((4, 1),)),)
        recurso = cadena_recursos(((3, 2),))

        resultado = ejecutar(
            juguetes, juguete_recurso, recurso_recurso, objeto_recurso, habitat_objeto, recurso
        )

        self.assertEqual(resultado, [40])

    @timeout(N_SECOND_BASE)
    def test_recurso_indirecto_insuficiente(self):
        """
        El objeto requiere R8 sintetico (necesita 5 de R3 con afinidad 7).
        El stock tiene solo 2 de R3: recursos insuficientes aunque la afinidad este presente.
        """
        juguetes = (Juguete(1, "uno", (7,), "001"),)
        juguete_recurso = (JugueteRecurso(1, 3, "00:01", 1),)
        recurso_recurso = (RecursoRecurso(8, ((3, 5),), 7),)
        objeto_recurso = (ObjetoRecurso(4, ((8, 1),)),)
        habitat_objeto = (HabitatObjeto(40, ((4, 1),)),)
        recurso = cadena_recursos(((3, 2),))

        resultado = ejecutar(
            juguetes, juguete_recurso, recurso_recurso, objeto_recurso, habitat_objeto, recurso
        )

        self.assertEqual(resultado, [])

    @timeout(N_SECOND_BASE)
    def test_recurso_indirecto_sin_afinidad(self):
        """
        Si falta la afinidad requerida para sintetizar un recurso intermedio, el
        habitat no es creable aunque haya recursos base suficientes.
        """
        juguetes = (Juguete(1, "uno", (3,), "001"),)
        juguete_recurso = (JugueteRecurso(1, 3, "00:01", 1),)
        recurso_recurso = (RecursoRecurso(8, ((3, 2),), 7),)
        objeto_recurso = (ObjetoRecurso(4, ((8, 1),)),)
        habitat_objeto = (HabitatObjeto(40, ((4, 1),)),)
        recurso = cadena_recursos(((3, 2),))

        resultado = ejecutar(
            juguetes, juguete_recurso, recurso_recurso, objeto_recurso, habitat_objeto, recurso
        )

        self.assertEqual(resultado, [])

    @timeout(N_SECOND_BASE)
    def test_no_muta_stock_de_recursos(self):
        """
        La consulta solo decide que habitats son creables; no debe consumir ni
        modificar el stock recibido.
        """
        juguetes = (Juguete(1, "uno", (7,), "001"),)
        juguete_recurso = (JugueteRecurso(1, 3, "00:01", 1),)
        recurso_recurso = (RecursoRecurso(8, ((3, 2),), 7),)
        objeto_recurso = (ObjetoRecurso(4, ((8, 1),)),)
        habitat_objeto = (HabitatObjeto(40, ((4, 1),)),)
        recurso = cadena_recursos(((3, 2), (5, 9)))

        resultado = ejecutar(
            juguetes, juguete_recurso, recurso_recurso, objeto_recurso, habitat_objeto, recurso
        )

        self.assertEqual(resultado, [40])
        self.assertEqual(tuplas_cadena(recurso), [(3, 2), (5, 9)])

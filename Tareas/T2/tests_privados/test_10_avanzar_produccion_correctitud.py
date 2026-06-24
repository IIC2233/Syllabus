from tests_privados.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import avanzar_produccion
from backend.nodo_ligado import NodoLigado
from utils import JugueteObjeto, JugueteRecurso

N_SECOND_BASE = 0.3


def gen(iterable):
    yield from iterable


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


class TestAvanzarProduccionPrivado(IICTest):
    """
    Pruebas de correctitud para avanzar_produccion.
    Verifica avance sin produccion, ciclos multiples, agrupacion, orden, bonus por
    objetos favoritos presentes, juguetes ausentes y tiempos con horas.
    """

    def assertResultadoFloat(self, resultado, esperado):
        self.assertEqual(len(resultado), len(esperado))
        for (id_recurso, cantidad), (id_esperado, cantidad_esperada) in zip(resultado, esperado):
            self.assertEqual(id_recurso, id_esperado)
            self.assertAlmostEqual(cantidad, cantidad_esperada, places=10)

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe ser generadora.
        """
        assert_es_generador(self, avanzar_produccion)

    @timeout(N_SECOND_BASE)
    def test_juguete_productor_none_retorna_vacio(self):
        """
        Si la cadena de JugueteProductor es None no hay nadie que produzca.
        El generador debe estar vacio independiente de los datos de JugueteRecurso.
        """
        juguete_recurso = (JugueteRecurso(1, 10, "00:01", 5),)

        resultado = list(avanzar_produccion(
            gen(juguete_recurso), gen(()), None, set(), minutos=10
        ))

        self.assertEqual(resultado, [])

    @timeout(N_SECOND_BASE)
    def test_avanza_tiempo_sin_producir(self):
        """
        Si ningun productor completa su ciclo, no se generan recursos, pero el
        tiempo_actual de cada nodo debe avanzar.
        """
        juguete_recurso = (
            JugueteRecurso(1, 10, "00:05", 3),
            JugueteRecurso(2, 20, "00:07", 4),
        )
        productores = cadena_productores(((1, 1), (2, 3)))

        resultado = list(avanzar_produccion(
            gen(juguete_recurso), gen(()), productores, set(), minutos=2
        ))

        self.assertEqual(resultado, [])
        self.assertEqual(tiempos_cadena(productores), [(1, 3), (2, 5)])

    @timeout(N_SECOND_BASE)
    def test_completa_varios_ciclos_y_guarda_resto(self):
        """
        Un mismo productor puede completar mas de un ciclo en una llamada. La
        cantidad se multiplica por los ciclos completos y queda solo el resto.
        """
        juguete_recurso = (JugueteRecurso(7, 70, "00:04", 5),)
        productores = cadena_productores(((7, 3),))

        resultado = list(avanzar_produccion(
            gen(juguete_recurso), gen(()), productores, set(), minutos=10
        ))

        self.assertResultadoFloat(resultado, [(70, 15.0)])
        self.assertEqual(tiempos_cadena(productores), [(7, 1)])

    @timeout(N_SECOND_BASE)
    def test_agrupa_mismo_recurso_y_ordena_por_id(self):
        """
        Si varios juguetes producen recursos en el mismo avance, el resultado queda
        ordenado por id_recurso y junta en una sola tupla los recursos repetidos.
        """
        juguete_recurso = (
            JugueteRecurso(1, 30, "00:05", 4),
            JugueteRecurso(2, 10, "00:05", 6),
            JugueteRecurso(3, 30, "00:05", 2),
        )
        productores = cadena_productores(((1, 0), (2, 0), (3, 0)))

        resultado = list(avanzar_produccion(
            gen(juguete_recurso), gen(()), productores, set(), minutos=5
        ))

        self.assertResultadoFloat(resultado, [(10, 6.0), (30, 6.0)])

    @timeout(N_SECOND_BASE)
    def test_bonus_solo_con_favoritos_presentes(self):
        """
        El bonus usa solo objetos favoritos que estan en el set recibido. Objetos
        favoritos ausentes y objetos presentes no favoritos no deben bonificar.
        """
        juguete_recurso = (
            JugueteRecurso(1, 50, "00:05", 10),
            JugueteRecurso(2, 60, "00:05", 8),
        )
        juguete_objeto = (
            JugueteObjeto(1, 100),
            JugueteObjeto(1, 101),
            JugueteObjeto(2, 200),
        )
        productores = cadena_productores(((1, 4), (2, 4)))

        resultado = list(avanzar_produccion(
            gen(juguete_recurso), gen(juguete_objeto), productores, {100, 999}, minutos=1
        ))

        self.assertResultadoFloat(resultado, [(50, 11.0), (60, 8.0)])

    @timeout(N_SECOND_BASE)
    def test_no_produce_juguete_ausente_en_cadena(self):
        """
        Un JugueteRecurso cargado no debe producir si su id_juguete no esta en la
        cadena de JugueteProductor.
        """
        juguete_recurso = (
            JugueteRecurso(1, 10, "00:01", 2),
            JugueteRecurso(2, 20, "00:01", 99),
        )
        productores = cadena_productores(((1, 0),))

        resultado = list(avanzar_produccion(
            gen(juguete_recurso), gen(()), productores, set(), minutos=1
        ))

        self.assertResultadoFloat(resultado, [(10, 2.0)])

    @timeout(N_SECOND_BASE)
    def test_parsea_tiempo_con_horas(self):
        """
        El tiempo_espera puede incluir horas. Con 01:30 y 180 minutos avanzados se
        completan exactamente dos ciclos.
        """
        juguete_recurso = (JugueteRecurso(4, 40, "01:30", 7),)
        productores = cadena_productores(((4, 0),))

        resultado = list(avanzar_produccion(
            gen(juguete_recurso), gen(()), productores, set(), minutos=180
        ))

        self.assertResultadoFloat(resultado, [(40, 14.0)])
        self.assertEqual(tiempos_cadena(productores), [(4, 0)])

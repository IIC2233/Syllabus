from tests_privados.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import crear_recursos
from utils import Juguete, JugueteObjeto, JugueteRecurso

N_SECOND_BASE = 0.3


def gen(iterable):
    yield from iterable


def crear_generador(juguete_recurso, juguete_objeto=()):
    generador = crear_recursos(gen(juguete_recurso), gen(juguete_objeto))
    next(generador)
    return generador


def tuplas_cadena(cabeza):
    resultado = []
    while cabeza is not None:
        resultado.append((cabeza.id, cabeza.tiempo_actual))
        cabeza = cabeza.siguiente
    return resultado


class TestCrearRecursosPrivado(IICTest):
    """
    Pruebas de correctitud para crear_recursos.
    Verifica comportamiento de coroutine, estado interno, formato de retorno,
    bonus por objetos acumulados, comando end y generador cerrado.
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
        assert_es_generador(self, crear_recursos)

    @timeout(N_SECOND_BASE)
    def test_send_juguete_y_set_retornan_none(self):
        """
        Enviar un Juguete o un set actualiza el estado interno sin avanzar tiempo
        y retorna None.
        """
        juguete_recurso = (JugueteRecurso(1, 20, "00:03", 2),)
        generador = crear_generador(juguete_recurso)

        self.assertIsNone(generador.send(Juguete(1, "uno", (1,), "001")))
        self.assertIsNone(generador.send({5, 6}))

        cadena, objetos = generador.send("end")
        self.assertEqual(tuplas_cadena(cadena), [(1, 0)])
        self.assertEqual(objetos, {5, 6})

    @timeout(N_SECOND_BASE)
    def test_send_none_equivale_a_un_minuto(self):
        """
        send(None) debe actuar como send(1). Un juguete que produce cada minuto
        genera exactamente una vez.
        """
        juguete_recurso = (JugueteRecurso(1, 20, "00:01", 5),)
        generador = crear_generador(juguete_recurso)
        generador.send(Juguete(1, "uno", (1,), "001"))

        resultado = generador.send(None)
        generador.send("end")

        self.assertResultadoFloat(resultado, ((20, 5.0),))

    @timeout(N_SECOND_BASE)
    def test_un_recurso_mantiene_tupla_de_tuplas(self):
        """
        Si se produce un solo recurso, el resultado debe ser una tupla que contiene
        un par, no una tupla plana.
        """
        juguete_recurso = (JugueteRecurso(1, 20, "00:03", 2),)
        juguete_objeto = (JugueteObjeto(1, 5),)
        generador = crear_generador(juguete_recurso, juguete_objeto)
        generador.send(Juguete(1, "uno", (1,), "001"))
        generador.send({5})

        resultado = generador.send(3)
        cadena, objetos = generador.send("end")

        self.assertIsInstance(resultado, tuple)
        self.assertIsInstance(resultado[0], tuple)
        self.assertResultadoFloat(resultado, ((20, 2.2),))
        self.assertEqual(tuplas_cadena(cadena), [(1, 0)])
        self.assertEqual(objetos, {5})

    @timeout(N_SECOND_BASE)
    def test_sin_objetos_en_set_no_hay_bonus(self):
        """
        Aunque JugueteObjeto defina un favorito para el juguete, si el set interno
        esta vacio no hay bonificacion. La cantidad debe ser cant * 1.1^0 = cant.
        """
        juguete_recurso = (JugueteRecurso(1, 20, "00:03", 4),)
        juguete_objeto = (JugueteObjeto(1, 5),)
        generador = crear_generador(juguete_recurso, juguete_objeto)
        generador.send(Juguete(1, "uno", (1,), "001"))

        resultado = generador.send(3)
        generador.send("end")

        self.assertResultadoFloat(resultado, ((20, 4.0),))

    @timeout(N_SECOND_BASE)
    def test_estado_persistente_entre_sends(self):
        """
        El tiempo_actual se conserva entre envios. Un avance parcial no produce,
        pero permite que el siguiente avance complete ciclos.
        """
        juguete_recurso = (
            JugueteRecurso(1, 10, "00:05", 2),
            JugueteRecurso(2, 20, "00:03", 1),
        )
        generador = crear_generador(juguete_recurso)
        generador.send(Juguete(1, "uno", (1,), "001"))
        generador.send(Juguete(2, "dos", (2,), "002"))

        self.assertEqual(generador.send(2), tuple())
        resultado = generador.send(3)
        cadena, _ = generador.send("end")

        self.assertResultadoFloat(resultado, ((10, 2.0), (20, 1.0)))
        self.assertEqual(tuplas_cadena(cadena), [(1, 0), (2, 2)])

    @timeout(N_SECOND_BASE)
    def test_set_objetos_se_acumula_y_bonus_cambia(self):
        """
        Los objetos enviados por set se acumulan. Al agregar un segundo favorito,
        la produccion posterior debe usar un bonus mayor.
        """
        juguete_recurso = (JugueteRecurso(1, 7, "00:10", 10),)
        juguete_objeto = (
            JugueteObjeto(1, 100),
            JugueteObjeto(1, 101),
        )
        generador = crear_generador(juguete_recurso, juguete_objeto)
        generador.send(Juguete(1, "uno", (1,), "001"))

        generador.send({100})
        primer_resultado = generador.send(10)
        generador.send({101, 999})
        segundo_resultado = generador.send(10)
        cadena, objetos = generador.send("end")

        self.assertResultadoFloat(primer_resultado, ((7, 11.0),))
        self.assertResultadoFloat(segundo_resultado, ((7, 12.100000000000001),))
        self.assertEqual(tuplas_cadena(cadena), [(1, 0)])
        self.assertEqual(objetos, {100, 101, 999})

    @timeout(N_SECOND_BASE)
    def test_end_retorna_estado_y_cierra(self):
        """
        send("end") retorna la cadena interna ordenada por id y el set de objetos.
        Luego el generador queda agotado.
        """
        juguete_recurso = (
            JugueteRecurso(1, 10, "00:05", 2),
            JugueteRecurso(3, 30, "00:07", 4),
        )
        generador = crear_generador(juguete_recurso)
        generador.send(Juguete(3, "tres", (3,), "003"))
        generador.send(Juguete(1, "uno", (1,), "001"))
        generador.send({8})
        generador.send(2)

        cadena, objetos = generador.send("end")

        self.assertEqual(tuplas_cadena(cadena), [(1, 2), (3, 2)])
        self.assertEqual(objetos, {8})
        with self.assertRaises(StopIteration):
            next(generador)

    @timeout(N_SECOND_BASE)
    def test_sin_juguetes_no_produce(self):
        """
        Avanzar tiempo sin haber enviado juguetes productores retorna una tupla vacia.
        """
        juguete_recurso = (JugueteRecurso(1, 20, "00:01", 5),)
        generador = crear_generador(juguete_recurso)

        resultado = generador.send(100)
        cadena, objetos = generador.send("end")

        self.assertEqual(resultado, tuple())
        self.assertIsNone(cadena)
        self.assertEqual(objetos, set())

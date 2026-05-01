from tests_publicos.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import crear_recursos
from utils import JugueteRecurso, Juguete

N_SECOND = 0.3

JR_BASE = [
    JugueteRecurso(1, 10, "00:05", 2),
    JugueteRecurso(2, 20, "00:03", 1),
]

JO_BASE = []

JUGUETE_1 = Juguete(1, "Pikachu", (1,), "001")
JUGUETE_2 = Juguete(2, "Bulbasaur", (2,), "002")


class TestCrearRecursosCorrectitud(IICTest):
    """
    Pruebas de correctitud para crear_recursos(generador_juguete_recurso,
    generador_juguete_objeto).
    Es una función generadora que acepta valores enviados (send).
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        assert_es_generador(self, crear_recursos)

    @timeout(N_SECOND)
    def test_send_none_actua_como_1(self):
        """
        Enviar None avanza 1 unidad de tiempo (equivale a enviar 1).
        Verificamos que el generador no lanza excepción y retorna algo coherente.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)  # inicializar
        resultado = gen.send(None)
        # Debe ser una tupla de pares (id_recurso, cantidad) — puede ser vacía
        self.assertIsInstance(resultado, tuple)

    @timeout(N_SECOND)
    def test_send_int_avanza_tiempo(self):
        """
        Enviar un int avanza esa cantidad de tiempo y retorna tupla de pares.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        # Avanzar suficiente tiempo como para que J2 produzca (tiempo_espera=3)
        resultado = gen.send(JUGUETE_2)
        resultado = gen.send(3)
        self.assertIsInstance(resultado, tuple)
        # R20 debe estar en el resultado (J2 produce R20 cada 3 min)
        ids = [r[0] for r in resultado]
        self.assertIn(20, ids)

    @timeout(N_SECOND)
    def test_send_juguete_incluye_juguete(self):
        """
        Enviar un Juguete incluye ese juguete en la cadena de JugueteProductor.
        Tras agregar J1 y avanzar 5 min, debe producir R10.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        gen.send(JUGUETE_1)   # incluir J1
        resultado = gen.send(5)  # avanzar 5 minutos
        self.assertIsInstance(resultado, tuple)
        ids = [r[0] for r in resultado]
        self.assertIn(10, ids)

    @timeout(N_SECOND)
    def test_send_set_actualiza_objetos(self):
        """
        Enviar un set actualiza el set interno de objetos presentes.
        No debe lanzar excepción.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        # No debe fallar al recibir un set
        gen.send({101, 102})
        resultado = gen.send(1)
        self.assertIsInstance(resultado, tuple)

    @timeout(N_SECOND)
    def test_send_end_retorna_estado_final(self):
        """
        Enviar 'end' retorna tupla con (cadena JugueteProductor, set_objetos)
        y luego el generador se agota.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        gen.send(JUGUETE_1)
        resultado = gen.send("end")
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(len(resultado), 2)
        # Primer elemento es cadena NodoLigado o None, segundo es set
        _, set_objs = resultado
        self.assertIsInstance(set_objs, set)
        # El generador debe estar agotado
        with self.assertRaises(StopIteration):
            next(gen)


    @timeout(N_SECOND)
    def test_resultado_int_pares_ordenados_por_id_recurso(self):
        """
        Al enviar int, los pares retornados deben estar ordenados
        por id_recurso ascendentemente.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        gen.send(JUGUETE_1)
        gen.send(JUGUETE_2)
        resultado = gen.send(5)  # ambos juguetes deben producir
        ids = [r[0] for r in resultado]
        self.assertEqual(ids, sorted(ids))

    @timeout(N_SECOND)
    def test_send_muchas_veces_no_falla(self):
        """
        Enviar varias veces no debe lanzar excepción y debe retornar tuplas de pares.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        gen.send(JUGUETE_1)
        gen.send(JUGUETE_2)
        for time in range(10):
            resultado = gen.send(1)
            self.assertIsInstance(resultado, tuple)
            ids = [r[0] for r in resultado]
            # J1 produce R10 cada 5 min, J2 produce R20 cada 3 min
            if (time+1) % 5 == 0 and time != 0:
                self.assertIn(10, ids)
            if (time+1) % 3 == 0 and time != 0:
                self.assertIn(20, ids)
        final = gen.send("end")
        self.assertIsInstance(final, tuple)
        self.assertEqual(len(final), 2)
        _, set_objs = final
        self.assertIsInstance(set_objs, set)

    @timeout(N_SECOND)
    def test_end_genera_error_despues(self):
        """
        Después de enviar 'end', el generador debe estar agotado y lanzar StopIteration.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        resultado = gen.send("end")
        self.assertIsInstance(resultado, tuple)
        with self.assertRaises(StopIteration):
            next(gen)

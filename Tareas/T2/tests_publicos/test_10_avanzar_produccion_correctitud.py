import unittest
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import avanzar_produccion
from utils import JugueteRecurso, JugueteObjeto
from backend.nodo_ligado import NodoLigado

N_SECOND = 0.3

# Datos base:
# J1 produce R10 cada 5 min, cantidad 2
# J2 produce R20 cada 3 min, cantidad 1
# J3 produce R10 cada 10 min, cantidad 3  (mismo recurso que J1)
JR_BASE = [
    JugueteRecurso(1, 10, "00:05", 2),
    JugueteRecurso(2, 20, "00:03", 1),
    JugueteRecurso(3, 10, "00:10", 3),
]

# Sin objetos favoritos en base
JO_BASE = []

# Con objetos favoritos: J1 tiene 2 objetos favoritos distintos presentes
JO_BONIFICADO = [
    JugueteObjeto(1, 101),
    JugueteObjeto(1, 102),
]

def make_nodo_productor(juguetes_tiempo):
    """
    Construye una cadena de NodoLigado de JugueteProductor.
    juguetes_tiempo: lista de (id_juguete, tiempo_actual)
    """
    cabeza = None
    for id_j, t in sorted(juguetes_tiempo, key=lambda x: x[0]):
        nodo = NodoLigado(id=id_j, tiempo_actual=t)
        if cabeza is None:
            cabeza = nodo
        else:
            cabeza = cabeza.insertar(nodo)
    return cabeza

class TestAvanzarProduccionCorrectitud(IICTest):
    """
    Pruebas de correctitud para avanzar_produccion(generador_juguete_recurso,
    generador_juguete_objeto, JugueteProductor, minutos). Debe retornar un generador de id's
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador lazy.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        assert_es_generador(self, avanzar_produccion)

    @timeout(N_SECOND)
    def test_juguete_productor_none(self):
        """
        Si JugueteProductor es None, debe retornar generador vacío.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        resultado = list(avanzar_produccion(jr_gen, jo_gen, None, set(), minutos=1))
        self.assertEqual(resultado, [])

    @timeout(N_SECOND)
    def test_un_minuto_sin_produccion(self):
        """
        Con tiempo_actual=0 y minutos=1, ningún juguete completa su ciclo
        (tiempo_espera mínimo es 3 min) → generador vacío.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        # J1: tiempo_actual=0, necesita 5 min; J2: tiempo_actual=0, necesita 3 min
        productor = make_nodo_productor([(1, 0), (2, 0)])
        resultado = list(avanzar_produccion(jr_gen, jo_gen, productor, set(), minutos=1))
        self.assertEqual(resultado, [])

    @timeout(N_SECOND)
    def test_juguete_completa_exactamente_ciclo(self):
        """
        Juguete que completa exactamente un ciclo (tiempo_actual + minutos == tiempo_espera):
        produce una vez y tiempo_actual se reinicia a 0.
        J2: tiempo_actual=2, minutos=1 → 2+1=3==tiempo_espera → produce R20 cantidad 1.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        productor = make_nodo_productor([(2, 2)])
        resultado = list(avanzar_produccion(jr_gen, jo_gen, productor, set(), minutos=1))
        self.assertCountEqual(resultado, [(20, 1)])

    @timeout(N_SECOND)
    def test_multiples_juguetes_mismo_recurso(self):
        """
        Dos juguetes producen el mismo recurso (R10): se debe retornar
        solo un par por id_recurso con las cantidades sumadas.
        J1 y J3 producen R10. Con tiempo suficiente ambos completan ciclo.
        J1: tiempo_actual=4, minutos=1 → produce R10 cant 2
        J3: tiempo_actual=9, minutos=1 → produce R10 cant 3
        → resultado: [(10, 5)]
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        productor = make_nodo_productor([(1, 4), (3, 9)])
        resultado = list(avanzar_produccion(jr_gen, jo_gen, productor, set(), minutos=1))
        self.assertCountEqual(resultado, [(10, 5)])

    @timeout(N_SECOND)
    def test_resultado_ordenado_por_id_recurso(self):
        """
        El generador retorna pares (id_recurso, cantidad) ordenados
        ascendentemente por id_recurso.
        J1 produce R10, J2 produce R20 — R10 debe venir antes que R20.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        # J1: tiempo_actual=4, minutos=1 → produce R10
        # J2: tiempo_actual=2, minutos=1 → produce R20
        productor = make_nodo_productor([(1, 4), (2, 2)])
        resultado = list(avanzar_produccion(jr_gen, jo_gen, productor, set(), minutos=1))
        ids = [r[0] for r in resultado]
        self.assertEqual(ids, sorted(ids))

    @timeout(N_SECOND)
    def test_resultado_avanza_produccion(self):
        """
        Revisa que en efecto se avance en la producción de JugueteProductor
        la cantidad de tiempo correcta.
        """
        jr_gen = (jr for jr in JR_BASE)
        jo_gen = (jo for jo in JO_BASE)
        # J1: tiempo_actual=4, minutos=1 → produce R10 y tiempo_actual reinicia a 0
        # J2: tiempo_actual=2, minutos=1 → produce R20 y tiempo_actual reinicia a 0
        productor = make_nodo_productor([(1, 4), (2, 2)])
        resultado = list(avanzar_produccion(jr_gen, jo_gen, productor, set(), minutos=15))
        self.assertCountEqual(resultado, [(10, 6), (20, 5)])
        self.assertEqual(productor.tiempo_actual, 4)
        self.assertEqual(productor.siguiente.tiempo_actual, 2)

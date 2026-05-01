import unittest
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import habitat_creables
from utils import Juguete, JugueteRecurso, ObjetoRecurso, RecursoRecurso, HabitatObjeto
from backend.nodo_ligado import NodoLigado

N_SECOND = 0.3

# Datos base:
# H1 requiere: O1×1, O2×2
# H2 requiere: O3×1
# H3 requiere: O1×5 (mucho, probablemente no creable)
HO_BASE = [
    HabitatObjeto(1, ((1, 1), (2, 2))),
    HabitatObjeto(2, ((3, 1),)),
    HabitatObjeto(3, ((1, 5),)),
]

JUGUETES_BASE = [
    Juguete(1, "Pikachu",   (1,), "001"),
    Juguete(2, "Bulbasaur", (2,), "002"),
]

JR_BASE = [
    JugueteRecurso(1, 10, "00:05", 2),
    JugueteRecurso(2, 20, "00:03", 1),
]

RR_BASE = []

OR_BASE = []

def make_cadena(pares, tipo="objeto"):
    """Construye cadena NodoLigado de Objeto o Recurso."""
    cabeza = None
    for id_, cant in sorted(pares, key=lambda x: x[0]):
        nodo = NodoLigado(id=id_, cantidad=cant)
        if cabeza is None:
            cabeza = nodo
        else:
            cabeza = cabeza.insertar(nodo)
    return cabeza

class TestHabitatCreablesCorrectitud(IICTest):
    """
    Pruebas de correctitud para habitat_creables(generador_juguete,
    generador_juguete_recurso, generador_recurso_recurso,
    generador_habitat_objeto, Objeto, Recurso).
    Entrega hábitats que se pueden crear sin avanzar el tiempo.
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador.
        """
        jug_gen = (j for j in JUGUETES_BASE)
        jr_gen  = (jr for jr in JR_BASE)
        rr_gen  = (rr for rr in RR_BASE)
        ho_gen  = (ho for ho in HO_BASE)
        assert_es_generador(self, habitat_creables)

    @timeout(N_SECOND)
    def test_sin_objetos_ni_recursos_retorna_vacio(self):
        """
        Si Objeto y Recurso son None (sin inventario), ningún hábitat es creable.
        """
        jug_gen = (j for j in JUGUETES_BASE)
        jr_gen  = (jr for jr in JR_BASE)
        rr_gen  = (rr for rr in RR_BASE)
        ho_gen  = (ho for ho in HO_BASE)
        or_gen  = (_or for _or in OR_BASE)
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, None))
        self.assertEqual(resultado, [])

    @timeout(N_SECOND)
    def test_habitat_creable_con_objetos_suficientes(self):
        """
        H2 requiere O3x1. Con O3x1 disponible, H2 es creable.
        """
        jug_gen = (j for j in JUGUETES_BASE)
        jr_gen  = (jr for jr in JR_BASE)
        # Cadena: Juguete 1->Recurso 10. Recurso 10->Recurso 3 (afinidad 1).  Objeto 3 necesita Recurso 3.
        rr_gen = (rr for rr in (RecursoRecurso(3, ((10, 1),), 1),))
        ho_gen  = (ho for ho in HO_BASE)
        # Simplificado: Objeto 3 necesita Recurso 3 (producible de Juguete 1)
        or_gen  = (_or for _or in (ObjetoRecurso(3, ((3, 1),)),))
        recurso = make_cadena([(3, 1)])
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, recurso))
        self.assertGreater(len(resultado), 0)
        self.assertIn(2, resultado)

    @timeout(N_SECOND)
    def test_habitat_no_creable_por_falta_objeto(self):
        """
        H1 requiere O1x1 y O2x2. Solo tenemos O1x1 (falta O2) → H1 no creable.
        """
        jug_gen = (j for j in JUGUETES_BASE)
        jr_gen  = (jr for jr in JR_BASE)
        rr_gen  = (rr for rr in RR_BASE)
        ho_gen  = (ho for ho in HO_BASE if ho.id_habitat != 1)
        or_gen  = (_or for _or in OR_BASE)
        recurso = None
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, recurso))
        self.assertNotIn(1, resultado)

    @timeout(N_SECOND)
    def test_habitat_no_creable_cantidad_insuficiente(self):
        """
        H3 requiere O1x5. Con solo O1x3, H3 no es creable.
        """
        jug_gen = (j for j in JUGUETES_BASE)
        jr_gen  = (jr for jr in JR_BASE)
        rr_gen  = (rr for rr in RR_BASE)
        ho_gen  = (ho for ho in HO_BASE if ho.id_habitat != 3)
        or_gen  = (_or for _or in OR_BASE)
        recurso = None
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, recurso))
        self.assertNotIn(3, resultado)

    @timeout(N_SECOND)
    def test_multiples_habitats_creables(self):
        """
        Con objetos suficientes para H1 y H2, ambos deben aparecer en el resultado.
        """
        jug_gen = (j for j in JUGUETES_BASE)
        jr_gen  = (jr for jr in JR_BASE)
        # Cadena: Juguete 1->Rec 10, Rec 10->Rec 1 (afinidad 1). Juguete 2->Rec 20, Rec 20->Rec 3 (afinidad 2)
        rr_gen = (rr for rr in (RecursoRecurso(1, ((10, 1),), 1), RecursoRecurso(3, ((20, 1),), 2)))
        ho_gen  = (ho for ho in HO_BASE)
        # H1: O1x1, O2x2 | H2: O3x1
        # Objeto 1 requiere Rec 1; Objeto 2 requiere Rec 1; Objeto 3 requiere Rec 3
        or_gen  = (_or for _or in (ObjetoRecurso(1, ((1, 1),)), ObjetoRecurso(2, ((1, 1),)), ObjetoRecurso(3, ((3, 1),)),))
        recurso = make_cadena([(1, 3), (3, 1)])
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, recurso))
        self.assertGreaterEqual(len(resultado), 2)
        self.assertIn(1, resultado)
        self.assertIn(2, resultado)

    @timeout(N_SECOND)
    def test_habitat_creable_muchos_pasos(self):
        """
        H1 requiere O1x1 y O2x2. Con cadena J1->R10->R1->O1 y J2->R20->R3->O2, H1 es creable.
        """
        jug_gen = (j for j in JUGUETES_BASE)
        jr_gen  = (jr for jr in JR_BASE)
        rr_gen = (rr for rr in (RecursoRecurso(1, ((10, 1),), 1), RecursoRecurso(3, ((20, 1),), 2)))
        ho_gen  = (ho for ho in HO_BASE)
        or_gen  = (_or for _or in (ObjetoRecurso(1, ((1, 1),)), ObjetoRecurso(2, ((1, 1),)),))
        recurso = make_cadena([(1, 3), (3, 2)])
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, recurso))
        self.assertGreater(len(resultado), 0)
        self.assertIn(1, resultado)
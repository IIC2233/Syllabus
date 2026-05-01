import os
import unittest
from tests_publicos.test_tools import IICTest, timeout
from tests_publicos.solution.test_14 import (HAB_CREABLES_S_0, HAB_CREABLES_S_0_RECURSOS, 
                                             HAB_CREABLES_M_0, HAB_CREABLES_M_0_RECURSOS,
                                             HAB_CREABLES_L_0, HAB_CREABLES_L_0_RECURSOS)
from backend.consultas import (habitat_creables, cargar_juguete, cargar_juguete_recurso,
             cargar_recurso_recurso, cargar_habitat_objeto, cargar_objeto_recurso)
from backend.nodo_ligado import NodoLigado

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


def make_cadena(pares):
    cabeza = None
    for id_, cant in sorted(pares, key=lambda x: x[0]):
        nodo = NodoLigado(id=id_, cantidad=cant)
        if cabeza is None:
            cabeza = nodo
        else:
            cabeza = cabeza.insertar(nodo)
    return cabeza


class TestHabitatCreablesCargaDatos(IICTest):
    """
    Verifica habitat_creables cargando datos reales desde S, M y L.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_0(self):
        """
        S — Con objetos y recursos dados, verificar hábitats creables.
        """
        jug_gen = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        jr_gen  = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        rr_gen  = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        ho_gen  = cargar_habitat_objeto(os.path.join(PATH_S, "habitat_objeto.csv"))
        or_gen  = cargar_objeto_recurso(os.path.join(PATH_S, "objeto_recurso.csv"))
        recurso = make_cadena(HAB_CREABLES_S_0_RECURSOS) if HAB_CREABLES_S_0_RECURSOS else None
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, recurso))
        self.assertCountEqual(resultado, HAB_CREABLES_S_0)

    @timeout(N_SECOND)
    def test_1(self):
        """
        S — Sin inventario de objetos: ningún hábitat creable.
        """
        jug_gen = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        jr_gen  = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        rr_gen  = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        ho_gen  = cargar_habitat_objeto(os.path.join(PATH_S, "habitat_objeto.csv"))
        or_gen  = cargar_objeto_recurso(os.path.join(PATH_S, "objeto_recurso.csv"))
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, None))
        self.assertEqual(resultado, [])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_2(self):
        """
        M — Dataset mediano con inventario parcial de objetos.
        """
        jug_gen = cargar_juguete(os.path.join(PATH_M, "juguetes.csv"))
        jr_gen  = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        rr_gen  = cargar_recurso_recurso(os.path.join(PATH_M, "recurso_recurso.csv"))
        ho_gen  = cargar_habitat_objeto(os.path.join(PATH_M, "habitat_objeto.csv"))
        or_gen  = cargar_objeto_recurso(os.path.join(PATH_M, "objeto_recurso.csv"))
        recurso = make_cadena(HAB_CREABLES_M_0_RECURSOS) if HAB_CREABLES_M_0_RECURSOS else None
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, recurso))
        self.assertCountEqual(resultado, HAB_CREABLES_M_0)

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_3(self):
        """
        L — Dataset grande, verificar eficiencia.
        """
        jug_gen = cargar_juguete(os.path.join(PATH_L, "juguetes.csv"))
        jr_gen  = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        rr_gen  = cargar_recurso_recurso(os.path.join(PATH_L, "recurso_recurso.csv"))
        ho_gen  = cargar_habitat_objeto(os.path.join(PATH_L, "habitat_objeto.csv"))
        or_gen  = cargar_objeto_recurso(os.path.join(PATH_L, "objeto_recurso.csv"))
        recurso = make_cadena(HAB_CREABLES_L_0_RECURSOS) if HAB_CREABLES_L_0_RECURSOS else None
        resultado = list(habitat_creables(jug_gen, jr_gen, rr_gen, or_gen, ho_gen, recurso))
        self.assertCountEqual(resultado, HAB_CREABLES_L_0)

import os
from tests_publicos.test_tools import IICTest, timeout
from tests_publicos.solution.test_13 import (POR_APARECER_S_0_HABITATS, POR_APARECER_S_0_HORA, 
                                             POR_APARECER_S_0, POR_APARECER_M_0_HABITATS, 
                                             POR_APARECER_M_0_HORA, POR_APARECER_M_0, 
                                             POR_APARECER_L_0_HABITATS, POR_APARECER_L_0_HORA, 
                                             POR_APARECER_L_0)
from backend.consultas import (por_aparecer, cargar_juguete, cargar_juguete_habitat,
             cargar_periodo_dia)
from backend.nodo_ligado import NodoLigado

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


def make_cadena_habitats(pares):
    cabeza = None
    for id_h, tp in sorted(pares, key=lambda x: x[0]):
        nodo = NodoLigado(id=id_h, tiempo_presente=tp)
        if cabeza is None:
            cabeza = nodo
        else:
            cabeza = cabeza.insertar(nodo)
    return cabeza


class TestPorAparecerCargaDatos(IICTest):
    """
    Verifica por_aparecer cargando datos reales desde S, M y L.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_0(self):
        """
        S — Consultar juguetes que aparecerán en un hábitat específico.
        """
        jug_gen = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        jug_gen = (j for j in jug_gen if j.id_juguete > 25)
        jh_gen  = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        pd_gen  = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        habitat = make_cadena_habitats(POR_APARECER_S_0_HABITATS)
        resultado = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen,
                                      momento_dia=POR_APARECER_S_0_HORA))
        self.assertCountEqual(resultado, POR_APARECER_S_0)

    @timeout(N_SECOND)
    def test_1(self):
        """
        S — Habitat=None retorna vacío también con datos reales.
        """
        jug_gen = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        jh_gen  = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        pd_gen  = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        resultado = list(por_aparecer(jug_gen, None, jh_gen, pd_gen, momento_dia=0))
        self.assertEqual(resultado, [])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_2(self):
        """
        M — Múltiples hábitats, verificar todos los juguetes esperados.
        """
        jug_gen = cargar_juguete(os.path.join(PATH_M, "juguetes.csv"))
        jug_gen = (j for j in jug_gen if j.id_juguete > 75)
        jh_gen  = cargar_juguete_habitat(os.path.join(PATH_M, "juguete_habitat.csv"))
        pd_gen  = cargar_periodo_dia(os.path.join(PATH_M, "periodo_dia.csv"))
        habitat = make_cadena_habitats(POR_APARECER_M_0_HABITATS)
        resultado = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen,
                                      momento_dia=POR_APARECER_M_0_HORA))
        self.assertCountEqual(resultado, POR_APARECER_M_0)

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_3(self):
        """
        L — Dataset grande, verificar eficiencia y correctitud.
        """
        jug_gen = cargar_juguete(os.path.join(PATH_L, "juguetes.csv"))
        jug_gen = (j for j in jug_gen if j.id_juguete > 250)
        jh_gen  = cargar_juguete_habitat(os.path.join(PATH_L, "juguete_habitat.csv"))
        pd_gen  = cargar_periodo_dia(os.path.join(PATH_L, "periodo_dia.csv"))
        habitat = make_cadena_habitats(POR_APARECER_L_0_HABITATS)
        resultado = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen,
                                      momento_dia=POR_APARECER_L_0_HORA))
        self.assertCountEqual(resultado, POR_APARECER_L_0)

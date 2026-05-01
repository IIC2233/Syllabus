import os
from tests_publicos.test_tools import IICTest, timeout
from tests_publicos.solution.test_6 import (CADENA_CREACION_L_0, CADENA_CREACION_M_0, 
                                            CADENA_CREACION_S_0, CADENA_CREACION_S_1)
from backend.consultas import cadena_creacion, cargar_juguete_recurso, cargar_recurso_recurso

N_SECOND = 0.5
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


class TestCadenaCreacionCargaDatos(IICTest):
    """
    Verifica cadena_creacion cargando juguete_recurso y recurso_recurso desde L, M y S.
    """

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        L — recurso=1: R1 no tiene receta, solo juguetes productores.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_L, "recurso_recurso.csv"))
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 1), CADENA_CREACION_L_0)

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        M — recurso=1: R1 no tiene receta, solo juguetes productores.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_M, "recurso_recurso.csv"))
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 1), CADENA_CREACION_M_0)

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        S — recurso=1: R1 no tiene receta, solo juguetes productores.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 1), CADENA_CREACION_S_0)

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        S — recurso=2: R2 = R1*1; cadena de un nivel de profundidad.
        """
        gen_jr = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        gen_rr = cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv"))
        self.assertEqual(cadena_creacion(gen_jr, gen_rr, 2), CADENA_CREACION_S_1)

import os
from tests_publicos.test_tools import IICTest, timeout, indexes_of
from tests_publicos.solution.test_5 import (HABITATS_DE_INTERES_L_CON_TODOS, 
                                            HABITATS_DE_INTERES_L_SIN_NINGUNO,
                                            HABITATS_DE_INTERES_M_CON_TODOS, 
                                            HABITATS_DE_INTERES_M_SIN_NINGUNO, 
                                            HABITATS_DE_INTERES_S_CON_TODOS, 
                                            HABITATS_DE_INTERES_S_SIN_NINGUNO)
from backend.consultas import habitats_de_interes, cargar_juguete, cargar_juguete_habitat

N_SECOND = 0.5
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


class TestHabitatsDeInteresCargaDatos(IICTest):
    """
    Verifica habitats_de_interes cargando juguete y juguete_habitat desde L, M y S.
    Dos escenarios por tamaño:
      - Todos los juguetes del CSV presentes → ningún hábitat es de interés.
      - Ningún juguete presente → todos los hábitats son de interés.
    Resultado ordenado por id_habitat ascendente.
    """

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_L_con_todos(self):
        """
        L — todos los juguetes presentes: ningún hábitat de interés.
        """
        gen_j  = cargar_juguete(os.path.join(PATH_L, "juguetes.csv"))
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_L, "juguete_habitat.csv"))
        resultado = habitats_de_interes(gen_j, gen_jh)
        *items, largo = indexes_of(resultado, [])
        self.assertEqual(largo, len(HABITATS_DE_INTERES_L_CON_TODOS))

    @timeout(N_SECOND)
    def test_L_sin_ninguno(self):
        """
        L — ningún juguete presente: todos los 700 hábitats son de interés.
        Verifica primero, último y largo total.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_L, "juguete_habitat.csv"))
        resultado = habitats_de_interes((juguete for juguete in []), gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(HABITATS_DE_INTERES_L_SIN_NINGUNO))
        self.assertEqual(items[0], HABITATS_DE_INTERES_L_SIN_NINGUNO[0])
        self.assertEqual(items[1], HABITATS_DE_INTERES_L_SIN_NINGUNO[-1])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_M_con_todos(self):
        """
        M — todos los juguetes presentes: ningún hábitat de interés.
        """
        gen_j  = cargar_juguete(os.path.join(PATH_M, "juguetes.csv"))
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_M, "juguete_habitat.csv"))
        resultado = habitats_de_interes(gen_j, gen_jh)
        *items, largo = indexes_of(resultado, [])
        self.assertEqual(largo, len(HABITATS_DE_INTERES_M_CON_TODOS))

    @timeout(N_SECOND)
    def test_M_sin_ninguno(self):
        """
        M — ningún juguete presente: todos los 200 hábitats son de interés.
        Verifica primero, último y largo total.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_M, "juguete_habitat.csv"))
        resultado = habitats_de_interes((juguete for juguete in []), gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(HABITATS_DE_INTERES_M_SIN_NINGUNO))
        self.assertEqual(items[0], HABITATS_DE_INTERES_M_SIN_NINGUNO[0])
        self.assertEqual(items[1], HABITATS_DE_INTERES_M_SIN_NINGUNO[-1])

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_S_con_todos(self):
        """
        S — todos los juguetes presentes: ningún hábitat de interés.
        """
        gen_j  = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        *items, largo = indexes_of(habitats_de_interes(gen_j, gen_jh), [])
        self.assertEqual(largo, len(HABITATS_DE_INTERES_S_CON_TODOS))

    @timeout(N_SECOND)
    def test_S_sin_ninguno(self):
        """
        S — ningún juguete presente: todos los 50 hábitats son de interés.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        resultado = habitats_de_interes((juguete for juguete in []), gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, len(HABITATS_DE_INTERES_S_SIN_NINGUNO))
        self.assertEqual(items[0], HABITATS_DE_INTERES_S_SIN_NINGUNO[0])
        self.assertEqual(items[1], HABITATS_DE_INTERES_S_SIN_NINGUNO[-1])

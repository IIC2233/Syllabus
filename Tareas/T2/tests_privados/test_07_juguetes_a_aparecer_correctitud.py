from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import juguetes_a_aparecer
from utils import JugueteHabitat, PeriodoDia

N_SECOND_BASE = 0.3
# P1: Madrugada [0, 20)
# P2: Amanecer  [20, 35)
# P3: Dia       [35, 60)
# Ciclo total: 60 minutos
PERIODOS = [
    PeriodoDia(1, "Madrugada", "00:20"),
    PeriodoDia(2, "Amanecer", "00:15"),
    PeriodoDia(3, "Dia", "00:25"),
]

class TestJuguetesAAparecerPrivado(IICTest):
    """
    Pruebas de correctitud para juguetes_a_aparecer.
    Ciclo de 3 periodos (60 min): Madrugada [0,20), Amanecer [20,35), Dia [35,60).
    Verifica filtrado por habitat, orden por espera con desempate por id, salto a
    periodo valido y calculo relativo al momento_dia.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe ser generadora.
        """
        assert_es_generador(self, juguetes_a_aparecer)

    @timeout(N_SECOND_BASE)
    def test_habitat_sin_juguetes_asociados(self):
        """
        id_habitat que no aparece en juguete_habitat retorna generador vacio.
        """
        juguete_habitat = [
            JugueteHabitat(1, 10, "00:05", (1,)),
            JugueteHabitat(2, 11, "00:05", (1,)),
        ]
        resultado = juguetes_a_aparecer(
            (jh for jh in juguete_habitat),
            (pd for pd in PERIODOS),
            99,
            0,
        )
        *items, largo = indexes_of(resultado, [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND_BASE)
    def test_filtra_habitat_y_ordena_por_tiempo_e_id(self):
        """
        Solo considera el habitat consultado, ordena por tiempo y desempata por id_juguete.
        J5 y J2 empatan en tiempo 10; J3 salta a P3 (inicio 35); J4 salta al proximo P2 (inicio 80).
        """
        juguete_habitat = [
            JugueteHabitat(5, 7, "00:10", (1,)),
            JugueteHabitat(1, 8, "00:01", (1,)),
            JugueteHabitat(2, 7, "00:10", (1,)),
            JugueteHabitat(3, 7, "00:25", (3,)),
            JugueteHabitat(4, 7, "00:45", (2,)),
        ]
        resultado = juguetes_a_aparecer(
            (jh for jh in juguete_habitat),
            (pd for pd in PERIODOS),
            7,
            0,
        )
        self.assertEqual(list(resultado), [(2, 10), (5, 10), (3, 35), (4, 80)])

    @timeout(N_SECOND_BASE)
    def test_momento_dia_no_cero_y_salto_a_periodo_valido(self):
        """
        El tiempo retornado es relativo al momento actual.
        J10 y J11 saltan al periodo 2; J13 al inicio del periodo 3; J12 al siguiente ciclo.
        """
        juguete_habitat = [
            JugueteHabitat(10, 9, "00:01", (2,)),
            JugueteHabitat(11, 9, "00:03", (2,)),
            JugueteHabitat(12, 9, "00:20", (1,)),
            JugueteHabitat(13, 9, "00:15", (3,)),
        ]
        resultado = juguetes_a_aparecer(
            (jh for jh in juguete_habitat),
            (pd for pd in PERIODOS),
            9,
            18,
        )
        self.assertEqual(list(resultado), [(10, 2), (11, 3), (13, 17), (12, 42)])

    @timeout(N_SECOND_BASE)
    def test_filtra_solo_juguetes_del_habitat_indicado(self):
        """
        Juguetes de otro habitat son ignorados aunque tengan datos similares.
        J21 (H16) queda excluido; J20 y J22 (H15) son retornados.
        """
        juguete_habitat = [
            JugueteHabitat(20, 15, "00:05", (1,)),
            JugueteHabitat(21, 16, "00:05", (1,)),
            JugueteHabitat(22, 15, "00:25", (3,)),
        ]
        resultado = juguetes_a_aparecer(
            (jh for jh in juguete_habitat),
            (pd for pd in PERIODOS),
            15,
            0,
        )
        self.assertEqual(list(resultado), [(20, 5), (22, 35)])

    @timeout(N_SECOND_BASE)
    def test_juguete_acepta_multiples_periodos(self):
        """
        ids_periodo_dia puede tener varios ids; el juguete aparece si cae en cualquiera.
        J5 llega al minuto 12 (momento=5 + espera=7), que cae en P2 con id=2 incluido en (2,3).
        """
        PERIODOS_3 = [
            PeriodoDia(1, "manana", "00:10"),
            PeriodoDia(2, "tarde", "00:05"),
            PeriodoDia(3, "noche", "00:05"),
        ]
        jh = [JugueteHabitat(5, 20, "00:07", (2, 3))]
        resultado = juguetes_a_aparecer(
            (x for x in jh),
            (p for p in PERIODOS_3),
            20,
            5,
        )
        self.assertEqual(list(resultado), [(5, 7)])

    @timeout(N_SECOND_BASE)
    def test_limite_exacto_entre_periodos(self):
        """
        Si la llegada cae al inicio de un periodo no valido, se salta al siguiente valido.
        J8 debe esperar hasta P1 del dia siguiente.
        """
        PERIODOS_2 = [
            PeriodoDia(1, "dia", "00:10"),
            PeriodoDia(2, "noche", "00:10"),
        ]
        jh = [JugueteHabitat(8, 30, "00:10", (1,))]
        resultado = juguetes_a_aparecer(
            (x for x in jh),
            (p for p in PERIODOS_2),
            30,
            0,
        )
        self.assertEqual(list(resultado), [(8, 20)])


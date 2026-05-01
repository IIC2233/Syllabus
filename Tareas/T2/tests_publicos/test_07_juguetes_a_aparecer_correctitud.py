from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import juguetes_a_aparecer
from utils import JugueteHabitat, PeriodoDia

N_SECOND = 0.3

# P1: Madrugada 30 min → [0, 30)
# P2: Amanecer  60 min → [30, 90)
PERIODOS = [
    PeriodoDia(1, "Madrugada", "00:30"),
    PeriodoDia(2, "Amanecer",  "01:00"),
]


class TestJuguetesAAparec(IICTest):
    """
    Pruebas para juguetes_a_aparecer(generador_juguete_habitat, generador_periodo_dia,
                                      id_habitat, momento_dia).
    Retorna (id_juguete, tiempo) ordenados por (tiempo, id_juguete).
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador lazy.
        """
        assert_es_generador(self, juguetes_a_aparecer)

    @timeout(N_SECOND)
    def test_habitat_sin_juguetes_asociados(self):
        """
        id_habitat que no aparece en JugueteHabitat → generador vacío.
        """
        jh = [JugueteHabitat(1, 5, "00:10", (1,))]
        gen_jh = (juguete_habitat for juguete_habitat in jh)
        gen_pd = (periodo_dia for periodo_dia in PERIODOS)
        *items, largo = indexes_of(juguetes_a_aparecer(gen_jh, gen_pd, 99, 2), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_orden_empate_por_id(self):
        """
        Dos juguetes con idéntico tiempo de aparición calculado → el de menor
        id_juguete aparece primero.
        """
        jh = [
            JugueteHabitat(5, 7, "00:20", (1,)),
            JugueteHabitat(2, 7, "00:20", (1,)),
        ]
        gen_jh = (juguete_habitat for juguete_habitat in jh)
        gen_pd = (periodo_dia for periodo_dia in PERIODOS)
        *items, largo = indexes_of(juguetes_a_aparecer(gen_jh, gen_pd, 7, 0), [0, 1])
        self.assertEqual(largo, 2)
        self.assertEqual(items[0], (2, 20))
        self.assertEqual(items[1], (5, 20))

    @timeout(N_SECOND)
    def test_salta_al_siguiente_periodo_valido(self):
        """
        El período calculado (momento_dia + tiempo_espera) no está en ids_periodo_dia
        del juguete → el tiempo se extiende hasta el inicio del primer período válido.
        """
        jh = [JugueteHabitat(1, 8, "00:10", (2,))]
        gen_jh = (juguete_habitat for juguete_habitat in jh)
        gen_pd = (periodo_dia for periodo_dia in PERIODOS)
        *items, largo = indexes_of(juguetes_a_aparecer(gen_jh, gen_pd, 8, 0), [0])
        self.assertEqual(largo, 1)
        self.assertEqual(items[0], (1, 30))

    @timeout(N_SECOND)
    def test_orden_general(self):
        """
        Varios juguetes con distintos tiempos de aparición → orden ascendente por tiempo.
        """
        jh = [
            JugueteHabitat(1, 9, "00:40", (1,)),
            JugueteHabitat(2, 9, "00:05", (1,)),
            JugueteHabitat(3, 9, "00:15", (2,)),
            JugueteHabitat(4, 9, "00:40", (1, 2)),
        ]
        gen_jh = (juguete_habitat for juguete_habitat in jh)
        gen_pd = (periodo_dia for periodo_dia in PERIODOS)
        *items, largo = indexes_of(juguetes_a_aparecer(gen_jh, gen_pd, 9, 0), [0, 1, 2, 3])
        self.assertEqual(largo, 4)
        self.assertEqual(items[0], (2, 5))
        self.assertEqual(items[1], (3, 30))
        self.assertEqual(items[2], (4, 40))
        self.assertEqual(items[3], (1, 90))

    @timeout(N_SECOND)
    def test_momento_dia_no_cero(self):
        """
        momento_dia > 0 → el tiempo retornado es relativo al momento actual,
        no al inicio del día.
        """
        jh = [
            JugueteHabitat(1, 9, "00:40", (1,)),
            JugueteHabitat(2, 9, "00:15", (1, 2)),
            JugueteHabitat(3, 9, "00:15", (2,)),
            JugueteHabitat(4, 9, "01:10", (2,)),
        ]
        gen_jh = (juguete_habitat for juguete_habitat in jh)
        gen_pd = (periodo_dia for periodo_dia in PERIODOS)
        *items, largo = indexes_of(juguetes_a_aparecer(gen_jh, gen_pd, 9, 20), range(4))
        self.assertEqual(largo, 4)
        self.assertEqual(items[0], (2, 15))
        self.assertEqual(items[1], (3, 15))
        self.assertEqual(items[2], (1, 70))
        self.assertEqual(items[3], (4, 100))

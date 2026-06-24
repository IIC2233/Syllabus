from tests_privados.test_tools import IICTest, timeout
from backend.consultas import ahora_es
from utils import PeriodoDia

N_SECOND_BASE = 0.3
# Tres períodos: Madrugada 20 min, Amanecer 25 min, Mañana 35 min
# Ciclo total: 80 minutos
PERIODOS = [
    PeriodoDia(1, "Madrugada", "00:20"),
    PeriodoDia(2, "Amanecer",  "00:25"),
    PeriodoDia(3, "Mañana",    "00:35"),
]

# Un solo período: cubre todo el ciclo
PERIODOS_UNO = [
    PeriodoDia(1, "DiaEntero", "02:00"),
]

# Ciclo irregular no redondo: Alba 17 min, Crepusculo 23 min, Penumbra 13 min
# Ciclo total: 53 minutos
PERIODOS_IRREG = [
    PeriodoDia(1, "Alba",       "00:17"),
    PeriodoDia(2, "Crepusculo", "00:23"),
    PeriodoDia(3, "Penumbra",   "00:13"),
]

class TestAhoraEsPrivado(IICTest):
    """
    Pruebas de correctitud para ahora_es(generador_periodo_dia, minutos).
    Usa tres fixtures: PERIODOS (80 min), PERIODOS_UNO (120 min), PERIODOS_IRREG (53 min).
    Convencion de intervalos: [inicio, fin).
    """

    @timeout(N_SECOND_BASE)
    def test_inicio(self):
        """
        Caso base: minutos=0 retorna dia=0, hora 00:00 y el primer periodo del ciclo.
        """
        gen = (p for p in PERIODOS)
        self.assertEqual(ahora_es(gen, 0), (0, "00:00", "Madrugada", "00:00", "00:20"))

    @timeout(N_SECOND_BASE)
    def test_interior_primer_periodo(self):
        """
        minutos=10, interior del primer periodo (no en borde): retorna Madrugada con sus
        limites correctos sin avanzar al siguiente periodo.
        """
        gen = (p for p in PERIODOS)
        self.assertEqual(ahora_es(gen, 10), (0, "00:10", "Madrugada", "00:00", "00:20"))

    @timeout(N_SECOND_BASE)
    def test_limite_entre_periodos(self):
        """
        El minuto exacto de cambio pertenece al periodo siguiente.
        minutos=20 debe retornar Amanecer.
        """
        gen = (p for p in PERIODOS)
        self.assertEqual(ahora_es(gen, 20), (0, "00:20", "Amanecer", "00:20", "00:45"))

    @timeout(N_SECOND_BASE)
    def test_dia_completo_reinicia(self):
        """
        minutos=80 es exactamente un ciclo: reinicia a dia=1, hora 00:00.
        Evita off-by-one donde minutos=80 quedaria como dia=0, hora=01:20.
        """
        gen = (p for p in PERIODOS)
        self.assertEqual(ahora_es(gen, 80), (1, "00:00", "Madrugada", "00:00", "00:20"))

    @timeout(N_SECOND_BASE)
    def test_multiples_dias_interior(self):
        """
        minutos cruza varios dias completos y calcula la hora residual correctamente.
        200 = 2 * 80 + 40 → dia 2, minuto 40 del ciclo → Amanecer [00:20, 00:45).
        """
        gen = (p for p in PERIODOS)
        self.assertEqual(ahora_es(gen, 200), (2, "00:40", "Amanecer", "00:20", "00:45"))

    @timeout(N_SECOND_BASE)
    def test_ultimo_minuto_antes_cambio_dia(self):
        """
        minutos = ciclo - 1 es el ultimo minuto del dia antes de reiniciar.
        79 = 80 - 1 → dia 0, minuto 79 → Mañana [00:45, 01:20).
        """
        gen = (p for p in PERIODOS)
        self.assertEqual(ahora_es(gen, 79), (0, "01:19", "Mañana", "00:45", "01:20"))

    @timeout(N_SECOND_BASE)
    def test_un_solo_periodo(self):
        """
        Con un unico periodo, cualquier minuto pertenece a ese periodo.
        Ciclo = 120 min. minutos=50 → dia 0, hora 00:50, DiaEntero [00:00, 02:00).
        """
        gen = (p for p in PERIODOS_UNO)
        self.assertEqual(ahora_es(gen, 50), (0, "00:50", "DiaEntero", "00:00", "02:00"))

    @timeout(N_SECOND_BASE)
    def test_limite_entre_periodos_en_dia_no_cero(self):
        """
        El limite entre P1 y P2 pertenece a P2 aunque ya haya pasado un dia.
        minutos=100 debe retornar el inicio de Amanecer en el dia 1.
        """
        gen = (p for p in PERIODOS)
        self.assertEqual(ahora_es(gen, 100), (1, "00:20", "Amanecer", "00:20", "00:45"))

    @timeout(N_SECOND_BASE)
    def test_ciclo_no_redondo_multiples_dias(self):
        """
        Ciclo de 53 minutos (17+23+13). La division entera no es trivial.
        126 = 2 * 53 + 20 → dia 2, minuto 20 del ciclo → Crepusculo [00:17, 00:40).
        """
        gen = (p for p in PERIODOS_IRREG)
        self.assertEqual(ahora_es(gen, 126), (2, "00:20", "Crepusculo", "00:17", "00:40"))

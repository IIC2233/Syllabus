from tests_publicos.test_tools import IICTest, timeout
from backend.consultas import ahora_es
from utils import PeriodoDia

N_SECOND = 0.3

# Dos períodos: Madrugada 30 min [00:00, 00:30), Amanecer 60 min [00:30, 01:30)
# Duración total del ciclo: 90 minutos
PERIODOS = [
    PeriodoDia(1, "Madrugada", "00:30"),
    PeriodoDia(2, "Amanecer",  "01:00"),
]


class TestAhoraEs(IICTest):
    """
    Pruebas para ahora_es(generador_periodo_dia, minutos) -> tuple.
    Retorna (dia_actual, hora_actual, nombre_periodo_dia,
    hora_inicio_periodo_dia, hora_fin_periodo_dia).
    Convención de intervalos: [inicio, fin).
    """

    @timeout(N_SECOND)
    def test_minutos_cero(self):
        """
        minutos=0 → día 0, hora "00:00", primer período con sus límites.
        """
        gen = (periodo_dia for periodo_dia in PERIODOS)
        self.assertEqual(ahora_es(gen, 0), (0, "00:00", "Madrugada", "00:00", "00:30"))

    @timeout(N_SECOND)
    def test_limite_entre_periodos(self):
        """
        minutos exactamente en el límite entre dos períodos pertenece al segundo
        (convención [inicio, fin)).
        """
        gen = (periodo_dia for periodo_dia in PERIODOS)
        self.assertEqual(ahora_es(gen, 30), (0, "00:30", "Amanecer", "00:30", "01:30"))

    @timeout(N_SECOND)
    def test_dia_completo_reinicia(self):
        """
        minutos igual a la duración total del ciclo → día 1, hora "00:00",
        vuelve al primer período.
        """
        gen = (periodo_dia for periodo_dia in PERIODOS)
        self.assertEqual(ahora_es(gen, 90), (1, "00:00", "Madrugada", "00:00", "00:30"))

    @timeout(N_SECOND)
    def test_multiples_dias(self):
        """
        minutos cruza varios días completos → dia_actual correcto y hora residual
        calculada dentro del ciclo.
        """
        gen = (periodo_dia for periodo_dia in PERIODOS)
        self.assertEqual(ahora_es(gen, 315), (3, "00:45", "Amanecer", "00:30", "01:30"))

    @timeout(N_SECOND)
    def test_interior_primer_periodo(self):
        """
        minutos dentro del primer período → retorna Madrugada con sus límites.
        """
        gen = (periodo_dia for periodo_dia in PERIODOS)
        self.assertEqual(ahora_es(gen, 10), (0, "00:10", "Madrugada", "00:00", "00:30"))

    @timeout(N_SECOND)
    def test_interior_segundo_periodo(self):
        """
        minutos dentro del segundo período → retorna Amanecer con sus límites.
        """
        gen = (periodo_dia for periodo_dia in PERIODOS)
        self.assertEqual(ahora_es(gen, 60), (0, "01:00", "Amanecer", "00:30", "01:30"))

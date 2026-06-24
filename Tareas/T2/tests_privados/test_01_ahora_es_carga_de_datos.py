import os
from tests_privados.test_tools import IICTest, timeout
from backend.consultas import ahora_es, cargar_periodo_dia

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestAhoraEsCargaDatosPrivado(IICTest):
    """
    Verifica ahora_es cargando periodo_dia desde los datasets privados S, M, L y XL.
    """

    @timeout(N_SECOND)
    def test_S_0(self):
        """
        Dataset S, minutos=0: primer instante del dia, retorna dia=0 en el primer periodo.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 0), (0, "00:00", "Madrugada", "00:00", "00:25"))

    @timeout(N_SECOND)
    def test_S_1(self):
        """
        Dataset S, minutos=25: en el limite exacto entre periodos, el periodo activo es el
        que inicia en ese minuto (Amanecer), no el que termina (Madrugada).
        """
        gen = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 25), (0, "00:25", "Amanecer", "00:25", "01:00"))

    @timeout(N_SECOND)
    def test_S_2(self):
        """
        Dataset S, minutos=60: equivale a un ciclo completo, retorna dia=1 en el primer
        periodo del nuevo ciclo.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 60), (1, "00:00", "Madrugada", "00:00", "00:25"))

    @timeout(N_SECOND)
    def test_S_3(self):
        """
        Dataset S, minutos=145: 2 ciclos completos + 25 minutos, retorna dia=2 dentro del
        segundo periodo.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 145), (2, "00:25", "Amanecer", "00:25", "01:00"))

    @timeout(N_SECOND)
    def test_M_0(self):
        """
        Dataset M, minutos=54: en el limite exacto Amanecer->Alba, el periodo activo es
        Alba (el que inicia), no Amanecer (el que termina).
        """
        gen = cargar_periodo_dia(os.path.join(PATH_M, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 54), (0, "00:54", "Alba", "00:54", "01:30"))

    @timeout(N_SECOND)
    def test_M_1(self):
        """
        Dataset M, minutos=240: mas de un ciclo completo, cae en dia=1 dentro de Amanecer
        (00:24-00:54); verifica calculo correcto con multiples periodos.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_M, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 240), (1, "00:48", "Amanecer", "00:24", "00:54"))

    @timeout(N_SECOND)
    def test_L_0(self):
        """
        Dataset L, minutos=35: limite exacto Madrugada->Amanecer; misma regla de cambio de
        periodo que S y M, verificada con un dataset mayor.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_L, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 35), (0, "00:35", "Amanecer", "00:35", "01:00"))

    @timeout(N_SECOND)
    def test_L_1(self):
        """
        Dataset L, minutos=720: avanza varios periodos dentro del dia=1, cae en Aurora
        (04:19-04:57); verifica navegacion correcta por periodos no iniciales.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_L, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 720), (1, "04:36", "Aurora", "04:19", "04:57"))

    @timeout(N_SECOND)
    def test_XL_0(self):
        """
        Dataset XL, minutos=5305: equivale exactamente a un ciclo completo de 250 periodos;
        debe reiniciar al primer periodo del dia=1 sin desplazamiento residual.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_XL, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 5305), (1, "00:00", "Madrugada", "00:00", "00:21"))

    @timeout(N_SECOND)
    def test_XL_1(self):
        """
        Dataset XL, minutos=15965: tres ciclos completos + residuo, cae en dia=3 dentro de
        Manana (00:44-01:06); verifica eficiencia con dataset grande y periodo no inicial.
        """
        gen = cargar_periodo_dia(os.path.join(PATH_XL, "periodo_dia.csv"))
        self.assertEqual(ahora_es(gen, 15965), (3, "00:50", "Manana", "00:44", "01:06"))

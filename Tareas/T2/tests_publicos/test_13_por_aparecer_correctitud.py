from tests_publicos.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import por_aparecer
from utils import Juguete, JugueteHabitat, PeriodoDia
from backend.nodo_ligado import NodoLigado

N_SECOND = 0.3

# Periodos del día: un ciclo de 24 horas = 1440 min
# P1: 00:00-08:00 (480 min), P2: 08:00-16:00 (480 min), P3: 16:00-24:00 (480 min)
PD_BASE = [
    PeriodoDia(1, "Madrugada", "08:00"),
    PeriodoDia(2, "Dia",       "08:00"),
    PeriodoDia(3, "Noche",     "08:00"),
]

# Juguetes disponibles
JUGUETES_BASE = [
    Juguete(1, "Pikachu",   (1,), "001"),
    Juguete(2, "Bulbasaur", (2,), "002"),
    Juguete(3, "Charmander",(3,), "003"),
    Juguete(4, "Squirtle",  (1,2), "004"),
    Juguete(5, "Eevee",     (2,4), "005"),
]

# Hábitat H1 espera a J1 (en P1) y J2 (en P2)
# Hábitat H2 espera solo a J3 (en P3)
JH_BASE = [
    JugueteHabitat(1, 1, "01:00", (1,)),   # J1 en H1, espera 60 min, periodo P1
    JugueteHabitat(2, 1, "02:00", (2,)),   # J2 en H1, espera 120 min, periodo P2
    JugueteHabitat(3, 2, "00:30", (3,)),   # J3 en H2, espera 30 min, periodo P3
    JugueteHabitat(4, 2, "01:00", (1,2)),   # J4 en H2, espera 60 min, periodo P1 y P2
    JugueteHabitat(5, 2, "01:15", (1,3)),   # J5 en H2, espera 75 min, periodo P1 y P3

]

def make_cadena_habitats(pares):
    """pares: lista de (id_habitat, tiempo_presente)"""
    cabeza = None
    for id_h, tp in sorted(pares, key=lambda x: x[0]):
        nodo = make_habitat_nodo(id_h, tp)
        if cabeza is None:
            cabeza = nodo
        else:
            cabeza = cabeza.insertar(nodo)
    return cabeza

def make_habitat_nodo(id_habitat, tiempo_presente=0):
    return NodoLigado(id=id_habitat, tiempo_presente=tiempo_presente)

class TestPorAparecerCorrectitud(IICTest):
    """
    Pruebas de correctitud para por_aparecer(generador_juguete, Habitat,
    generador_juguete_habitat, generador_periodo_dia, momento_dia).
    Entrega generador con los Juguetes que aparecerán en cada hábitat.
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador.
        """
        jug_gen  = (j for j in JUGUETES_BASE)
        jh_gen   = (jh for jh in JH_BASE)
        pd_gen   = (pd for pd in PD_BASE)
        assert_es_generador(self, por_aparecer)

    @timeout(N_SECOND)
    def test_habitat_none_retorna_vacio(self):
        """
        Si Habitat es None (sin hábitats), retorna generador vacío.
        """
        jug_gen = (j for j in JUGUETES_BASE)
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        resultado = list(por_aparecer(jug_gen, None, jh_gen, pd_gen, momento_dia=0))
        self.assertEqual(resultado, [])

    @timeout(N_SECOND)
    def test_sin_juguetes_para_habitat_retorna_vacio(self):
        """
        Si ningún juguete está asignado al hábitat presente,
        retorna generador vacío.
        """
        # H99 no tiene juguetes asignados en JH_BASE
        jug_gen = (j for j in JUGUETES_BASE)
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        habitat = make_cadena_habitats([(99, 0)])
        resultado = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen, momento_dia=0))
        self.assertEqual(resultado, [None])

    @timeout(N_SECOND)
    def test_juguete_aparece_en_habitat_correcto(self):
        """
        J1 aparece en H1 (periodo 1). Verificar que el resultado
        incluye a J1 al consultar H1.
        """
        juguetes_sin_j1 = [j for j in JUGUETES_BASE if j.id_juguete != 1]
        jug_gen = (j for j in juguetes_sin_j1)
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        habitat = make_cadena_habitats([(1, 0)])
        resultado = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen, momento_dia=0))
        self.assertIn(1, resultado)

    @timeout(N_SECOND)
    def test_multiples_habitats_multiples_juguetes(self):
        """
        Con H1 y H2 en la cadena, el generador debe incluir juguetes
        de ambos hábitats.
        """
        juguetes_sin_j1_y_j2 = [j for j in JUGUETES_BASE if j.id_juguete != 1 and j.id_juguete != 2]
        jug_gen = (j for j in juguetes_sin_j1_y_j2)
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        habitat = make_cadena_habitats([(1, 0), (2, 0)])
        resultado = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen, momento_dia=0))
        self.assertIn(1, resultado)

    @timeout(N_SECOND)
    def test_juguetes_ya_presentes_no_aparecen(self):
        """
        Un hábitat solo puede atraer juguetes que aún no estén presentes.
        Si J1 ya está presente, no debe aparecer en el resultado de H1,
        debe aparecer solo J2 (que también espera H1).
        """
        # J1 ya está en el refugio — simulamos pasando solo J2 y J3 en JUGUETES_BASE
        juguetes_con_j1 = [j for j in JUGUETES_BASE if j.id_juguete != 2 and j.id_juguete != 3]
        # En este test simplificado verificamos que la lógica filtra
        jug_gen = (j for j in juguetes_con_j1)
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        habitat = make_cadena_habitats([(1, 0)])
        resultado = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen, momento_dia=0))
        self.assertNotIn(1, resultado)

    @timeout(N_SECOND)
    def test_juguetes_correctos_aparecen_segun_periodo_habitat(self):
        """
        J1 espera H1 en P1 y J4 en H2, J2 espera H1 en P2, J3 espera H2 en P3.
        Verificar que cada juguete aparece solo en su periodo asignado.
        """
        jug_gen = (j for j in [])
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        habitat = make_cadena_habitats([(1, 0), (2, 0)])
        resultado_p1 = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen, momento_dia=0))

        jug_gen = (j for j in [])
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        resultado_p2 = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen, momento_dia=480))

        jug_gen = (j for j in [])
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        resultado_p3 = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen, momento_dia=960))
        
        self.assertIn(1, resultado_p1)
        self.assertIn(4, resultado_p1)
        self.assertIn(2, resultado_p2)
        self.assertIn(4, resultado_p2)
        self.assertIn(3, resultado_p3)
        self.assertIn(1, resultado_p3)

    @timeout(N_SECOND)
    def test_juguetes_distintos_segun_existentes(self):
        """
        Si ciertos juegos están presentes, el resultado de por_aparecer debe incluir
        solo los juguetes que aún no estén presentes
        """
        # Simulamos que J1 y J3 ya están presentes, entonces solo J2 y J4 podrían aparecer
        juguetes_con_j1_y_j3 = [j for j in JUGUETES_BASE if j.id_juguete == 1 or j.id_juguete == 3]
        jug_gen = (j for j in juguetes_con_j1_y_j3)
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        habitat = make_cadena_habitats([(1, 0), (2, 0)])
        resultado = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen, momento_dia=0))
        self.assertNotIn(1, resultado)
        self.assertNotIn(3, resultado)
        self.assertIn(2, resultado)
        self.assertIn(4, resultado)

        # Si ahora J1, J3 y J4 ya están presentes, solo J2 y J5 podrían aparecer
        juguetes_con_j1_j3_j4 = [j for j in JUGUETES_BASE if j.id_juguete in (1, 3, 4)]
        jug_gen = (j for j in juguetes_con_j1_j3_j4)
        jh_gen  = (jh for jh in JH_BASE)
        pd_gen  = (pd for pd in PD_BASE)
        resultado = list(por_aparecer(jug_gen, habitat, jh_gen, pd_gen, momento_dia=0))
        self.assertNotIn(1, resultado)
        self.assertNotIn(3, resultado)
        self.assertNotIn(4, resultado)
        self.assertIn(2, resultado)
        self.assertIn(5, resultado)
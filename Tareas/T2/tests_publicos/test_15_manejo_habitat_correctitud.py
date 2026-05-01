from tests_publicos.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import manejo_habitat
from utils import (Juguete, JugueteHabitat, HabitatObjeto, ObjetoRecurso,
                   RecursoRecurso, JugueteObjeto, PeriodoDia)
from backend.nodo_ligado import NodoLigado

N_SECOND = 0.3

# ── Datos base mínimos ────────────────────────────────────────────────────────
PD_BASE = [
    PeriodoDia(1, "Dia",   "00:30"),
    PeriodoDia(2, "Noche", "00:30"),
]

JUGUETES_BASE = [
    Juguete(1, "Pikachu",   (1,), "001"),
    Juguete(2, "Bulbasaur", (2,), "002"),
]

# J1 aparece en H1 (periodo P1, espera 5 min)
# J2 aparece en H2 (periodo P2, espera 5 min)
JH_BASE = [
    JugueteHabitat(1, 1, "00:05", (1,)),
    JugueteHabitat(2, 2, "00:05", (2,)),
]

# H1 requiere O1×1; H2 requiere O2×1
HO_BASE = [
    HabitatObjeto(1, ((1, 1),)),
    HabitatObjeto(2, ((2, 1),)),
]

# O1 requiere R10×1; O2 requiere R20×1
OR_BASE = [
    ObjetoRecurso(1, ((10, 1),)),
    ObjetoRecurso(2, ((20, 1),)),
]

RR_BASE = []
JO_BASE = []


class TestManejoHabitatCorrectitud(IICTest):
    """
    Pruebas de correctitud para manejo_habitat(gen_juguete, gen_juguete_habitat,
    gen_habitat_objeto, gen_objeto_recurso, gen_recurso_recurso,
    gen_juguete_objeto, gen_periodo_dia, tiempo_inicial).
    Es una función generadora con send.
    """

    def _make_gen(self, tiempo_inicial=1, ho_use=None):
        return manejo_habitat(
            gen_juguete=(j for j in JUGUETES_BASE),
            gen_juguete_habitat=(jh for jh in JH_BASE),
            gen_habitat_objeto=(ho for ho in (HO_BASE if ho_use is None else ho_use)),
            gen_objeto_recurso=(or_ for or_ in OR_BASE),
            gen_recurso_recurso=(rr for rr in RR_BASE),
            gen_periodo_dia=(pd for pd in PD_BASE),
            tiempo_inicial=tiempo_inicial,
        )

    @timeout(N_SECOND)
    def test_retorna_generador_y_send_none_retorna_ids_juguetes(self):
        """
        La función debe retornar un generador.
        Enviar None avanza una unidad de tiempo y retorna tupla de ids de juguetes creados.
        No termina la simulación.
        """
        assert_es_generador(self, manejo_habitat)
        gen = self._make_gen()
        next(gen)
        resultado = gen.send(None)
        self.assertIsInstance(resultado, tuple)
        self.assertTrue(all(isinstance(id_juguete, int) for id_juguete in resultado))

    @timeout(N_SECOND)
    def test_send_crear_con_y_sin_recursos(self):
        """
        Con recursos suficientes, 'crear' retorna (set_objetos, ids_habitats) no vacíos.
        Sin recursos, 'crear' retorna conjuntos vacíos.
        Verifica estructura del retorno en ambos casos.
        """
        # ── Caso sin recursos ──
        gen_sin = self._make_gen()
        next(gen_sin)
        resultado_sin = gen_sin.send("crear")
        self.assertIsInstance(resultado_sin, tuple)
        self.assertEqual(len(resultado_sin), 2)
        set_objetos_sin, ids_habitats_sin = resultado_sin
        self.assertIsInstance(set_objetos_sin, set)
        self.assertIsInstance(ids_habitats_sin, tuple)
        self.assertEqual(len(ids_habitats_sin), 0)
        self.assertEqual(len(set_objetos_sin), 0)

        # ── Caso con recursos para H1 ──
        gen_con = self._make_gen()
        next(gen_con)
        gen_con.send(((10, 1),))
        resultado_con = gen_con.send("crear")
        self.assertIsInstance(resultado_con, tuple)
        self.assertEqual(len(resultado_con), 2)
        set_objetos_con, ids_habitats_con = resultado_con
        self.assertIsInstance(set_objetos_con, set)
        self.assertIsInstance(ids_habitats_con, tuple)
        self.assertEqual(ids_habitats_con, (1,))

    # ── Tests nuevos ──────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_tiempo_avanza_con_send_none(self):
        """
        tiempo_inicial determina el tiempo de partida del reporte.
        Cada send(None) debe incrementar el tiempo en exactamente 1.
        Se verifica con 'report' antes y después de avanzar N ticks.
        """

        gen = manejo_habitat(
            gen_juguete=(j for j in []),
            gen_juguete_habitat=(jh for jh in []),
            gen_habitat_objeto=(ho for ho in []),
            gen_objeto_recurso=(or_ for or_ in []),
            gen_recurso_recurso=(rr for rr in []),
            gen_periodo_dia=(pd for pd in PD_BASE),
            tiempo_inicial=5,
        )
        next(gen)

        tiempo_inicial_report, *_ = gen.send("report")
        self.assertEqual(tiempo_inicial_report, 5)

        for _ in range(7):
            gen.send(None)

        tiempo_final_report, *_ = gen.send("report")
        self.assertEqual(tiempo_final_report, 12)

    @timeout(N_SECOND)
    def test_crear_no_crea_habitat_si_juguete_ya_asignado(self):
        """
        Si un juguete ya fue asignado a un hábitat creado, no debe ser asignado a otro hábitat.
        """
        gen = manejo_habitat(
            gen_juguete=(j for j in [Juguete(1, "Pikachu", (1,), "001")]),
            gen_juguete_habitat=(jh for jh in [
                JugueteHabitat(1, 1, "00:05", (1,)),  # J1 → H1
                JugueteHabitat(1, 2, "00:05", (1,)),  # J1 → H2 (mismo juguete)
            ]),
            gen_habitat_objeto=(ho for ho in [
                HabitatObjeto(1, ((1, 1),)),  # H1 requiere O1
                HabitatObjeto(2, tuple()),    # H2 no requiere nada
            ]),
            gen_objeto_recurso=(or_ for or_ in [
                ObjetoRecurso(1, ((10, 1),)),
            ]),
            gen_recurso_recurso=(rr for rr in []),
            gen_periodo_dia=(pd for pd in PD_BASE),
            tiempo_inicial=1,
        )
        next(gen)

        gen.send(((10, 1),))
        _, ids_habitats = gen.send("crear")
        self.assertEqual(ids_habitats, (1,2))

        for _ in range(5):
            gen.send(None)

        # Intentar crear hábitats de nuevo: H2 NO debe crearse porque
        # J1 (su único juguete posible) ya fue asignado a H1.
        _, ids_habitats2 = gen.send("crear")
        self.assertNotIn(2, ids_habitats2,
                         "H2 no debe crearse: su único juguete posible (J1) "
                         "ya está en un hábitat construido")

    @timeout(N_SECOND)
    def test_send_tupla_recursos_agrega_recursos(self):
        """
        Enviar una tupla de recursos la agrega al NodoLigado interno de Recurso.
        No debe lanzar excepción.
        """
        gen = self._make_gen()
        next(gen)
        respuesta = gen.send(((10, 1), (20, 1)))
        self.assertEqual(respuesta, None)
        resultado = gen.send(None)
        self.assertIsInstance(resultado, tuple)

    @timeout(N_SECOND)
    def test_send_crear_crea_varios_habitats_con_recursos_distintos(self):
        """
        Si hay recursos suficientes para varios hábitats con requisitos distintos,
        'crear' debe devolverlos todos en una sola llamada.
        """
        gen = manejo_habitat(
            gen_juguete=(j for j in [
                Juguete(1, "J1", (1,), "001"),
                Juguete(2, "J2", (2,), "002"),
                Juguete(3, "J3", (3,), "003"),
            ]),
            gen_juguete_habitat=(jh for jh in [
                JugueteHabitat(1, 1, "00:05", (1,)),
                JugueteHabitat(2, 2, "00:05", (2,)),
                JugueteHabitat(3, 3, "00:05", (3,)),
            ]),
            gen_habitat_objeto=(ho for ho in [
                HabitatObjeto(1, ((1, 1),)),
                HabitatObjeto(2, ((2, 1),)),
                HabitatObjeto(3, ((3, 1),)),
            ]),
            gen_objeto_recurso=(or_ for or_ in [
                ObjetoRecurso(1, ((10, 1),)),
                ObjetoRecurso(2, ((20, 1),)),
                ObjetoRecurso(3, ((30, 1),)),
            ]),
            gen_recurso_recurso=(rr for rr in []),
            gen_periodo_dia=(pd for pd in PD_BASE),
            tiempo_inicial=1,
        )
        next(gen)
        gen.send(((10, 1), (20, 1), (30, 1)))
        resultado = gen.send("crear")
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(len(resultado), 2)
        set_objetos, ids_habitats = resultado
        self.assertEqual(set_objetos, {1, 2, 3})
        self.assertEqual(ids_habitats, (1, 2, 3))

    @timeout(N_SECOND)
    def test_send_crear_sin_recursos_no_crea_habitats(self):
        """
        Sin recursos ni objetos disponibles, 'crear' retorna conjuntos vacíos.
        """
        gen = self._make_gen()
        next(gen)
        resultado = gen.send("crear")
        set_objetos, ids_habitats = resultado
        self.assertEqual(len(ids_habitats), 0)


    @timeout(N_SECOND)
    def test_send_crear_sin_recursos_crea_habitats(self):
        """
        Sin recursos ni objetos disponibles, 'crear' un habitat si no requiere de ellos.
        """
        gen = self._make_gen(ho_use=[
            HabitatObjeto(1, tuple()),
            HabitatObjeto(2, ((2, 1),)),
        ])
        next(gen)
        resultado = gen.send("crear")
        set_objetos, ids_habitats = resultado
        self.assertEqual(len(ids_habitats), 1)

    @timeout(N_SECOND)
    def test_avanzar_harto_tiempo_crear_recursos_y_habitats(self):
        """
        Avanzar tiempo suficiente para que aparezca al menos un juguete.
        Luego enviar recursos necesarios para crear un único hábitat.
        Verificar que se crea exactamente un hábitat.
        """
        gen = manejo_habitat(
            gen_juguete=(j for j in JUGUETES_BASE[:1]),
            gen_juguete_habitat=(jh for jh in JH_BASE),
            gen_habitat_objeto=(ho for ho in [HabitatObjeto(2, tuple())]),
            gen_objeto_recurso=(or_ for or_ in []),
            gen_recurso_recurso=(rr for rr in RR_BASE),
            gen_periodo_dia=(pd for pd in PD_BASE),
            tiempo_inicial=1,
        )
        next(gen)
        for _ in range(5):
            gen.send(None)
        resultado = gen.send("crear")
        set_objetos, ids_habitats = resultado
        self.assertIsInstance(set_objetos, set)
        self.assertIsInstance(ids_habitats, tuple)
        self.assertTrue(all(isinstance(id_habitat, int) for id_habitat in ids_habitats))
        self.assertEqual(ids_habitats, (2,))

    @timeout(N_SECOND)
    def test_report_no_termina(self):
        """
        Enviar 'report' antes de que termine la simulación retorna tupla con tiempo,
        ids de juguetes y tres cadenas NodoLigado.
        """
        gen = manejo_habitat(
            gen_juguete=(j for j in [Juguete(1, "Pikachu", (1,), "001")]),
            gen_juguete_habitat=(jh for jh in JH_BASE),
            gen_habitat_objeto=(ho for ho in [HabitatObjeto(2, tuple())]),
            gen_objeto_recurso=(or_ for or_ in []),
            gen_recurso_recurso=(rr for rr in RR_BASE),
            gen_periodo_dia=(pd for pd in PD_BASE),
            tiempo_inicial=1,
        )
        next(gen)
        resultado = gen.send("report")
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(len(resultado), 5)
        tiempo, ids_juguetes, hab, obj, rec = resultado
        self.assertIsInstance(tiempo, int)
        self.assertIsInstance(ids_juguetes, set)
        self.assertEqual(ids_juguetes, set())
        self.assertIsNone(hab)
        self.assertIsNone(obj)
        self.assertIsNone(rec)

        gen.send(((10, 100),))
        for _ in range(45):
            gen.send(None)

        result_crear = gen.send("crear")
        self.assertEqual(result_crear, (set(), (2,)))

        resultado = gen.send("report")
        tiempo, ids_juguetes, hab, obj, rec = resultado
        self.assertIsInstance(tiempo, int)
        self.assertIsInstance(ids_juguetes, set)
        self.assertIsInstance(hab, NodoLigado)
        self.assertIsNone(obj)
        self.assertIsInstance(rec, NodoLigado)
from tests_privados.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import habitat_eventualmente_creables
from utils import Juguete, JugueteRecurso, RecursoRecurso, ObjetoRecurso, HabitatObjeto

N_SECOND_BASE = 0.3
JUGUETES_BASE = [
    Juguete(1, "J1", (10,), "001"),
    Juguete(2, "J2", (20,), "002"),
]
JUGUETE_RECURSO_BASE = [
    JugueteRecurso(1, 1, "00:10", 1),
    JugueteRecurso(2, 2, "00:10", 1),
]
RECURSO_RECURSO_BASE = [
    RecursoRecurso(5, ((2, 1),), 99),
    RecursoRecurso(4, ((3, 1),), 20),
    RecursoRecurso(3, ((1, 1), (2, 1)), 10),
]
OBJETO_RECURSO_BASE = [
    ObjetoRecurso(10, ((1, 1),)),
    ObjetoRecurso(20, ((3, 1),)),
    ObjetoRecurso(30, ((4, 1),)),
    ObjetoRecurso(40, ((5, 1),)),
    ObjetoRecurso(900, ((1, 1),)),
]


def ejecutar(juguetes, juguete_recurso, recurso_recurso, objeto_recurso, habitat_objeto):
    return list(
        habitat_eventualmente_creables(
            (j for j in juguetes),
            (jr for jr in juguete_recurso),
            (rr for rr in recurso_recurso),
            (or_ for or_ in objeto_recurso),
            (ho for ho in habitat_objeto),
        )
    )

class TestHabitatEventualmenteCreablesPrivado(IICTest):
    """
    Pruebas de correctitud para habitat_eventualmente_creables.
    Verifica: habitats sin objetos, recursos directos e indirectos, afinidades faltantes,
    multiples objetos requeridos, juguetes ausentes e ids solapados entre objeto y recurso.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe ser generadora.
        """
        assert_es_generador(self, habitat_eventualmente_creables)

    @timeout(N_SECOND_BASE)
    def test_habitat_sin_objetos_es_creable(self):
        """
        Un habitat sin objetos requeridos es creable aunque no haya juguetes presentes.
        """
        habitat_objeto = [HabitatObjeto(1, ())]
        self.assertEqual(ejecutar([], [], [], [], habitat_objeto), [1])

    @timeout(N_SECOND_BASE)
    def test_objetos_con_recursos_directos_e_indirectos(self):
        """
        H10 requiere O10 (R1 directo de J1); H20 requiere O20 (R3 sintetizado desde R1+R2);
        H30 requiere O30 (R4, dos niveles de sintesis). Los tres son creables.
        """
        habitat_objeto = [
            HabitatObjeto(10, ((10, 1),)),
            HabitatObjeto(20, ((20, 1),)),
            HabitatObjeto(30, ((30, 1),)),
        ]
        self.assertEqual(
            ejecutar(
                JUGUETES_BASE,
                JUGUETE_RECURSO_BASE,
                RECURSO_RECURSO_BASE,
                OBJETO_RECURSO_BASE,
                habitat_objeto,
            ),
            [10, 20, 30],
        )

    @timeout(N_SECOND_BASE)
    def test_no_creable_si_falta_afinidad(self):
        """
        Si falta la afinidad de una receta necesaria, el habitat no es creable.
        """
        habitat_objeto = [HabitatObjeto(40, ((40, 1),))]
        self.assertEqual(
            ejecutar(
                JUGUETES_BASE,
                JUGUETE_RECURSO_BASE,
                RECURSO_RECURSO_BASE,
                OBJETO_RECURSO_BASE,
                habitat_objeto,
            ),
            [],
        )

    @timeout(N_SECOND_BASE)
    def test_varios_objetos_requeridos_deben_ser_creables(self):
        """
        Todos los objetos requeridos por el habitat deben poder fabricarse.
        """
        habitat_objeto = [
            HabitatObjeto(50, ((10, 1), (20, 1))),
            HabitatObjeto(60, ((10, 1), (40, 1))),
        ]
        self.assertEqual(
            ejecutar(
                JUGUETES_BASE,
                JUGUETE_RECURSO_BASE,
                RECURSO_RECURSO_BASE,
                OBJETO_RECURSO_BASE,
                habitat_objeto,
            ),
            [50],
        )

    @timeout(N_SECOND_BASE)
    def test_solo_juguetes_presentes_aportan_recursos(self):
        """
        Un recurso producido por un juguete ausente no permite crear objetos.
        """
        habitat_objeto = [HabitatObjeto(70, ((10, 1),))]
        self.assertEqual(
            ejecutar(
                [],
                JUGUETE_RECURSO_BASE,
                RECURSO_RECURSO_BASE,
                OBJETO_RECURSO_BASE,
                habitat_objeto,
            ),
            [],
        )

    @timeout(N_SECOND_BASE)
    def test_no_confunde_id_objeto_con_id_recurso(self):
        """
        Un id de objeto puede coincidir con un id de recurso, pero no significan lo mismo.
        Debe usar ObjetoRecurso para decidir si cada habitat es creable.
        """
        juguetes = [Juguete(1, "J1", (6,), "001")]
        juguete_recurso = [JugueteRecurso(1, 7, "00:05", 1)]
        recurso_recurso = [RecursoRecurso(12, ((7, 1),), 6)]
        objeto_recurso = [ObjetoRecurso(12, ((12, 1),)), ObjetoRecurso(7, ((88, 1),))]
        habitat_objeto = [HabitatObjeto(15, ((12, 1),)), HabitatObjeto(25, ((7, 1),))]
        self.assertEqual(ejecutar(juguetes, juguete_recurso, recurso_recurso, objeto_recurso, habitat_objeto), [15])

    @timeout(N_SECOND_BASE)
    def test_generador_habitat_objeto_vacio(self):
        """
        Si el generador de habitat_objeto esta vacio, el resultado es vacio.
        """
        self.assertEqual(
            ejecutar(
                [Juguete(1, "J1", (1,), "001")],
                [JugueteRecurso(1, 5, "00:05", 1)],
                [],
                [ObjetoRecurso(10, ((5, 1),))],
                [],
            ),
            [],
        )


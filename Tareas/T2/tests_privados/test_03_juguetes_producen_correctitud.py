from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import juguetes_producen
from utils import JugueteRecurso

N_SECOND_BASE = 0.3
# Tres recursos distintos; productores de R7 intercalados con los de R3
JR_BASE = [
    JugueteRecurso(2,  7,  "00:05", 1),
    JugueteRecurso(4,  3,  "00:10", 2),
    JugueteRecurso(7,  7,  "00:08", 3),
    JugueteRecurso(9,  3,  "00:12", 1),
    JugueteRecurso(11, 7,  "00:03", 4),
    JugueteRecurso(15, 12, "00:20", 1),
]

# Todos los juguetes producen el mismo recurso
JR_TODOS = [
    JugueteRecurso(1, 7, "00:05", 1),
    JugueteRecurso(2, 7, "00:10", 2),
    JugueteRecurso(3, 7, "00:15", 3),
]

class TestJuguetesProducenPrivado(IICTest):
    """
    Pruebas de correctitud para juguetes_producen.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe ser generadora.
        """
        assert_es_generador(self, juguetes_producen)

    @timeout(N_SECOND_BASE)
    def test_ninguno_produce_el_recurso(self):
        """
        id_recurso que ningun juguete produce retorna generador vacio.
        """
        gen = (jr for jr in JR_BASE)
        *_, largo = indexes_of(juguetes_producen(gen, 99), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND_BASE)
    def test_un_juguete_produce(self):
        """
        Exactamente un juguete produce R12; los demas son filtrados.
        """
        gen = (jr for jr in JR_BASE)
        self.assertEqual(list(juguetes_producen(gen, 12)), [15])

    @timeout(N_SECOND_BASE)
    def test_multiples_intercalados(self):
        """
        Productores del recurso buscado aparecen intercalados con otros recursos.
        Debe filtrar todos los productores y mantener orden ascendente.
        """
        gen = (jr for jr in JR_BASE)
        self.assertEqual(list(juguetes_producen(gen, 7)), [2, 7, 11])

    @timeout(N_SECOND_BASE)
    def test_todos_producen_el_mismo_recurso(self):
        """
        Todos los juguetes del generador producen el mismo recurso.
        Resultado incluye todos los ids en orden ascendente.
        """
        gen = (jr for jr in JR_TODOS)
        self.assertEqual(list(juguetes_producen(gen, 7)), [1, 2, 3])

    @timeout(N_SECOND_BASE)
    def test_generador_vacio(self):
        """
        Generador sin elementos retorna vacio sin error.
        """
        self.assertEqual(list(juguetes_producen((jr for jr in []), 7)), [])

    @timeout(N_SECOND_BASE)
    def test_solo_el_ultimo_coincide(self):
        """
        Solo el ultimo juguete del generador produce el recurso buscado.
        Verifica que se recorre el generador hasta el final.
        """
        jr = [
            JugueteRecurso(1,  5,  "00:05", 1),
            JugueteRecurso(2,  9,  "00:05", 1),
            JugueteRecurso(3,  11, "00:05", 1),
            JugueteRecurso(4,  7,  "00:05", 1),
        ]
        self.assertEqual(list(juguetes_producen((x for x in jr), 7)), [4])

    @timeout(N_SECOND_BASE)
    def test_grandes_saltos_de_id(self):
        """
        Juguetes con ids no consecutivos y con grandes saltos entre ellos.
        Verifica que el orden del resultado sigue siendo ascendente por id_juguete.
        """
        jr = [
            JugueteRecurso(1,   7,  "00:01", 1),
            JugueteRecurso(50,  7,  "00:02", 2),
            JugueteRecurso(99,  13, "00:05", 1),
            JugueteRecurso(150, 13, "00:05", 1),
            JugueteRecurso(200, 7,  "00:03", 3),
        ]
        self.assertEqual(list(juguetes_producen((x for x in jr), 7)), [1, 50, 200])

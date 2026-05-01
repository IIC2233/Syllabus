from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import juguetes_producen
from utils import JugueteRecurso

N_SECOND = 0.3

JR_BASE = [
    JugueteRecurso(1, 5, "00:10", 3),
    JugueteRecurso(2, 5, "00:20", 2),
    JugueteRecurso(3, 8, "00:15", 1),
]


class TestJuguetesProducen(IICTest):
    """
    Pruebas para juguetes_producen(generador_juguete_recurso, id_recurso).
    Retorna un generador con los id_juguete capaces de producir el recurso dado.
    Resultado ordenado por id_juguete ascendente.
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador lazy.
        """
        assert_es_generador(self, juguetes_producen)

    @timeout(N_SECOND)
    def test_ninguno_produce_el_recurso(self):
        """
        Ningún juguete produce id_recurso → generador vacío.
        """
        gen = (juguete_recurso for juguete_recurso in JR_BASE)
        *items, largo = indexes_of(juguetes_producen(gen, 99), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_multiples_juguetes_producen(self):
        """
        Varios juguetes producen el mismo recurso → retorna todos sus ids
        ordenados por id_juguete ascendente.
        """
        gen = (juguete_recurso for juguete_recurso in JR_BASE)
        *items, largo = indexes_of(juguetes_producen(gen, 5), [0, 1])
        self.assertEqual(largo, 2)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 2)

    @timeout(N_SECOND)
    def test_un_juguete_produce(self):
        """
        Exactamente un juguete produce el recurso → retorna solo ese id.
        """
        gen = (juguete_recurso for juguete_recurso in JR_BASE)
        *items, largo = indexes_of(juguetes_producen(gen, 8), [0])
        self.assertEqual(largo, 1)
        self.assertEqual(items[0], 3)

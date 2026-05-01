from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import juguetes_productivos
from utils import JugueteRecurso

N_SECOND = 0.3


class TestJuguetesProductivos(IICTest):
    """
    Pruebas para juguetes_productivos(generador_juguete_recurso, minimo).
    Productividad = cantidad / tiempo_en_minutos.
    Con minimo=None retorna los más productivos (todos los que empatan el máximo).
    Con minimo dado retorna los que tienen productividad ESTRICTAMENTE mayor.
    """

    @timeout(N_SECOND)
    def test_retorna_generador_con_minimo(self):
        """
        La función debe retornar un generador lazy cuando se pasa un mínimo.
        """
        assert_es_generador(self, juguetes_productivos)

    @timeout(N_SECOND)
    def test_retorna_generador_sin_minimo(self):
        """
        La función debe retornar un generador lazy cuando minimo=None.
        """
        assert_es_generador(self, juguetes_productivos)

    @timeout(N_SECOND)
    def test_minimo_none_empate_maximo(self):
        """
        minimo=None, varios juguetes empatan el máximo → retorna los empatados
        """
        jr_lista = [
            JugueteRecurso(1, 5, "00:10", 20),
            JugueteRecurso(2, 3, "00:20", 30),
            JugueteRecurso(3, 7, "00:05", 10),
        ]
        gen = (juguete_recurso for juguete_recurso in jr_lista)
        *items, largo = indexes_of(juguetes_productivos(gen, minimo=None), [0, 1])
        self.assertEqual(largo, 2)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 3)

    @timeout(N_SECOND)
    def test_minimo_none_todos_iguales(self):
        """
        minimo=None, todos los juguetes tienen igual productividad → retorna todos.
        """
        jr_lista = [
            JugueteRecurso(1, 5, "00:10", 10),
            JugueteRecurso(2, 3, "00:20", 20),
            JugueteRecurso(3, 7, "00:05",  5),
        ]
        gen = (juguete_recurso for juguete_recurso in jr_lista)
        *items, largo = indexes_of(juguetes_productivos(gen, minimo=None), [0, 1, 2])
        self.assertEqual(largo, 3)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 2)
        self.assertEqual(items[2], 3)

    @timeout(N_SECOND)
    def test_minimo_exactamente_igual_no_retorna(self):
        """
        minimo exactamente igual a la productividad de un juguete → ese juguete no
        se retorna (la condición es estrictamente mayor).
        """
        jr_lista = [
            JugueteRecurso(1, 5, "00:10", 20),
            JugueteRecurso(2, 3, "00:20", 20),
        ]
        gen = (juguete_recurso for juguete_recurso in jr_lista)
        *items, largo = indexes_of(juguetes_productivos(gen, minimo=2.0), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_minimo_mayor_que_todos(self):
        """
        minimo mayor que la productividad de todos los juguetes → generador vacío.
        """
        jr_lista = [
            JugueteRecurso(1, 5, "00:10", 20),
            JugueteRecurso(2, 3, "00:20", 30),
        ]
        gen = (juguete_recurso for juguete_recurso in jr_lista)
        *items, largo = indexes_of(juguetes_productivos(gen, minimo=5.0), [])
        self.assertEqual(largo, 0)

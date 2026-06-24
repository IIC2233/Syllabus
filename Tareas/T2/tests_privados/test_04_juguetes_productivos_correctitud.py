from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import juguetes_productivos
from utils import JugueteRecurso

N_SECOND_BASE = 0.3
# Productividades: J1=0.5, J2=0.8, J3=0.8, J4=1.2, J5=1.2
JR_BASE = [
    JugueteRecurso(1, 5, "00:20", 10),
    JugueteRecurso(2, 3, "00:15", 12),
    JugueteRecurso(3, 7, "00:10",  8),
    JugueteRecurso(4, 9, "00:05",  6),
    JugueteRecurso(5, 2, "00:10", 12),
]

# Todos con productividad 1.0
JR_IGUALES = [
    JugueteRecurso(1, 5, "00:15", 15),
    JugueteRecurso(2, 3, "00:30", 30),
    JugueteRecurso(3, 7, "00:12", 12),
]

# Maximo al final del generador
JR_MAX_FINAL = [
    JugueteRecurso(1, 5, "00:10",  5),
    JugueteRecurso(2, 3, "00:10",  8),
    JugueteRecurso(3, 7, "00:05", 10),
]

class TestJuguetesProductivosPrivado(IICTest):
    """
    Pruebas de correctitud para juguetes_productivos.
    Productividad = cantidad / tiempo_en_minutos.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe ser generadora.
        """
        assert_es_generador(self, juguetes_productivos)

    @timeout(N_SECOND_BASE)
    def test_minimo_none_empate_maximo(self):
        """
        minimo=None retorna todos los juguetes que empatan la productividad maxima.
        J4 y J5 tienen 1.2; J1, J2, J3 quedan excluidos.
        """
        gen = (jr for jr in JR_BASE)
        self.assertEqual(list(juguetes_productivos(gen, minimo=None)), [4, 5])

    @timeout(N_SECOND_BASE)
    def test_minimo_none_todos_iguales(self):
        """
        minimo=None retorna todos cuando todos tienen igual productividad.
        """
        gen = (jr for jr in JR_IGUALES)
        self.assertEqual(list(juguetes_productivos(gen, minimo=None)), [1, 2, 3])

    @timeout(N_SECOND_BASE)
    def test_minimo_none_maximo_al_final(self):
        """
        minimo=None con el maximo al final del generador: verifica que se
        consume el generador completo antes de determinar el maximo.
        """
        gen = (jr for jr in JR_MAX_FINAL)
        self.assertEqual(list(juguetes_productivos(gen, minimo=None)), [3])

    @timeout(N_SECOND_BASE)
    def test_un_solo_juguete_es_maximo(self):
        """
        Con un unico juguete y minimo=None, ese juguete es el maximo y se retorna.
        """
        gen = (jr for jr in [JugueteRecurso(7, 5, "00:05", 3)])
        self.assertEqual(list(juguetes_productivos(gen, minimo=None)), [7])

    @timeout(N_SECOND_BASE)
    def test_minimo_exactamente_igual_no_retorna(self):
        """
        La condicion es estrictamente mayor: productividad igual al minimo no retorna.
        J4 y J5 tienen exactamente 1.2 = minimo, quedan excluidos.
        """
        gen = (jr for jr in JR_BASE)
        *_, largo = indexes_of(juguetes_productivos(gen, minimo=1.2), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND_BASE)
    def test_minimo_parcial(self):
        """
        minimo=0.5: J2, J3, J4, J5 superan estrictamente; J1 tiene exactamente 0.5
        y queda excluido.
        """
        gen = (jr for jr in JR_BASE)
        self.assertEqual(list(juguetes_productivos(gen, minimo=0.5)), [2, 3, 4, 5])

    @timeout(N_SECOND_BASE)
    def test_minimo_mayor_que_todos(self):
        """
        minimo mayor que todas las productividades retorna vacio.
        """
        gen = (jr for jr in JR_BASE)
        *_, largo = indexes_of(juguetes_productivos(gen, minimo=2.0), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND_BASE)
    def test_minimo_cero_retorna_todos(self):
        """
        minimo=0.0 retorna todos, ya que toda productividad positiva es mayor que cero.
        """
        gen = (jr for jr in JR_BASE)
        self.assertEqual(list(juguetes_productivos(gen, minimo=0.0)), [1, 2, 3, 4, 5])

    @timeout(N_SECOND_BASE)
    def test_conversion_tiempo_con_horas(self):
        """
        El tiempo "hh:mm" se convierte completo a minutos: "01:30" = 90 min, no 1.3 ni 130.
        Ambos juguetes producen 1.0 rec/min, empatan en maximo.
        """
        jr = [
            JugueteRecurso(1, 10, "01:30", 90),
            JugueteRecurso(2, 11, "00:30", 30),
        ]
        gen = (x for x in jr)
        self.assertEqual(list(juguetes_productivos(gen, minimo=None)), [1, 2])

    @timeout(N_SECOND_BASE)
    def test_conversion_horas_con_minimo_numerico(self):
        """
        La conversion de horas aplica tambien cuando minimo es numerico.
        Con minimo=0.1, solo J11 supera estrictamente el umbral.
        """
        jr = [
            JugueteRecurso(10, 5, "03:00", 6),
            JugueteRecurso(11, 3, "01:00", 12),
            JugueteRecurso(12, 7, "00:15", 1),
        ]
        self.assertEqual(list(juguetes_productivos((x for x in jr), minimo=0.1)), [11])

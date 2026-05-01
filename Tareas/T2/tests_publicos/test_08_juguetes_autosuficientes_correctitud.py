from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import juguetes_autosuficientes
from utils import Juguete, JugueteObjeto, ObjetoRecurso, JugueteRecurso, RecursoRecurso

N_SECOND = 0.3

# J1 (afinidad 3) produce R5. Sus objetos: Obj10 (→ R5) y Obj20 (→ R6).
# J2 (afinidad 5) produce R6. Su objeto: Obj30 (→ R5).
# J3 (sin afinidad) produce R8. Su objeto: Obj40 (→ R7).
J_BASE = [
    Juguete(1, "J1", (3,), "001"),
    Juguete(2, "J2", (5,), "002"),
    Juguete(3, "J3", (), "003"),
]
JO_BASE = [
    JugueteObjeto(1, 10),
    JugueteObjeto(1, 20),
    JugueteObjeto(2, 30),
    JugueteObjeto(3, 40),
]
OR_BASE = [
    ObjetoRecurso(10, ((5, 2),)),
    ObjetoRecurso(20, ((6, 1),)),
    ObjetoRecurso(30, ((5, 3),)),
    ObjetoRecurso(40, ((7, 1),)),
]
JR_BASE = [
    JugueteRecurso(1, 5, "00:10", 3),
    JugueteRecurso(2, 6, "00:20", 2),
    JugueteRecurso(3, 8, "00:15", 1),
]
RR_BASE = []


class TestJuguetesAutosuficientes(IICTest):
    """
    Pruebas para juguetes_autosuficientes(generador_juguete, generador_juguete_objeto,
                                           generador_objeto_recurso, generador_juguete_recurso,
                                           generador_recurso_recurso).
    Un juguete es autosuficiente si puede obtener, por sus propios medios, todos
    los recursos necesarios para fabricar al menos uno de sus objetos favoritos.
    Resultado ordenado por id_juguete ascendente, sin duplicados.
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador lazy.
        """
        assert_es_generador(self, juguetes_autosuficientes)

    @timeout(N_SECOND)
    def test_autosuficiente_produce_directamente(self):
        """
        J1 produce R5 y su Obj10 solo necesita R5 → puede obtener todos los
        recursos → autosuficiente.
        J2 produce R6 pero su único objeto necesita R5 ≠ R6 → no autosuficiente.
        J3 produce R8 pero su único objeto necesita R7 ≠ R8 → no autosuficiente.
        """
        gen_j  = (juguete for juguete in J_BASE)
        gen_jo = (juguete_objeto for juguete_objeto in JO_BASE)
        gen_or = (objeto_recurso for objeto_recurso in OR_BASE)
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in RR_BASE)
        *items, largo = indexes_of(
            juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr), [0]
        )
        self.assertEqual(largo, 1)
        self.assertEqual(items[0], 1)

    @timeout(N_SECOND)
    def test_juguete_sin_objetos_favoritos(self):
        """
        Juguete que produce un recurso pero no aparece en JugueteObjeto →
        no autosuficiente (no tiene objetos favoritos).
        """
        jr = JR_BASE + [JugueteRecurso(9, 9, "00:05", 5)]
        j  = J_BASE  + [Juguete(9, "J9", (), "009")]
        gen_j  = (juguete for juguete in j)
        gen_jo = (juguete_objeto for juguete_objeto in JO_BASE)
        gen_or = (objeto_recurso for objeto_recurso in OR_BASE)
        gen_jr = (juguete_recurso for juguete_recurso in jr)
        gen_rr = (recurso_recurso for recurso_recurso in RR_BASE)
        *items, largo = indexes_of(
            juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr), [0]
        )
        self.assertEqual(largo, 1)
        self.assertEqual(items[0], 1)

    @timeout(N_SECOND)
    def test_no_autosuficiente_le_faltan_recursos(self):
        """
        El objeto favorito del juguete necesita dos recursos; el juguete solo
        puede obtener uno de ellos → no puede fabricar el objeto → no autosuficiente.
        """
        jo  = [JugueteObjeto(5, 10)]
        or_ = [ObjetoRecurso(10, ((5, 1), (6, 1)))]   # Obj10 necesita R5 Y R6
        jr  = [JugueteRecurso(5, 5, "00:10", 3)]        # J5 solo produce R5
        j   = [Juguete(5, "J5", (), "005")]              # sin afinidades, no puede crear R6
        gen_j  = (juguete for juguete in j)
        gen_jo = (juguete_objeto for juguete_objeto in jo)
        gen_or = (objeto_recurso for objeto_recurso in or_)
        gen_jr = (juguete_recurso for juguete_recurso in jr)
        gen_rr = (recurso_recurso for recurso_recurso in [])
        *items, largo = indexes_of(
            juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr), []
        )
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_autosuficiente_via_cadena_recurso_recurso(self):
        """
        J1 produce R1 (afinidad 3). RecursoRecurso: R2 = R1 con afinidad 3
        → J1 puede fabricar R2. Su Obj10 solo necesita R2 → autosuficiente.
        """
        j   = [Juguete(1, "J1", (3,), "001")]
        jr  = [JugueteRecurso(1, 1, "00:10", 5)]
        rr  = [RecursoRecurso(2, ((1, 1),), 3)]
        jo  = [JugueteObjeto(1, 10)]
        or_ = [ObjetoRecurso(10, ((2, 1),))]
        gen_j  = (juguete for juguete in j)
        gen_jo = (juguete_objeto for juguete_objeto in jo)
        gen_or = (objeto_recurso for objeto_recurso in or_)
        gen_jr = (juguete_recurso for juguete_recurso in jr)
        gen_rr = (recurso_recurso for recurso_recurso in rr)
        *items, largo = indexes_of(
            juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr), [0]
        )
        self.assertEqual(largo, 1)
        self.assertEqual(items[0], 1)

    @timeout(N_SECOND)
    def test_no_autosuficiente_sin_afinidad(self):
        """
        J1 produce R1 pero no tiene la afinidad 3 que exige RecursoRecurso
        para crear R2 → no puede obtener R2 → no autosuficiente.
        """
        j   = [Juguete(1, "J1", (), "001")]
        jr  = [JugueteRecurso(1, 1, "00:10", 5)]
        rr  = [RecursoRecurso(2, ((1, 1),), 3)]
        jo  = [JugueteObjeto(1, 10)]
        or_ = [ObjetoRecurso(10, ((2, 1),))]
        gen_j  = (juguete for juguete in j)
        gen_jo = (juguete_objeto for juguete_objeto in jo)
        gen_or = (objeto_recurso for objeto_recurso in or_)
        gen_jr = (juguete_recurso for juguete_recurso in jr)
        gen_rr = (recurso_recurso for recurso_recurso in rr)
        *items, largo = indexes_of(
            juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr), []
        )
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_mismo_juguete_sin_duplicados(self):
        """
        El mismo juguete aparece múltiples veces en JugueteObjeto →
        aparece una sola vez en el resultado.
        """
        jo  = [JugueteObjeto(1, 10), JugueteObjeto(1, 20), JugueteObjeto(1, 10)]
        gen_j  = (juguete for juguete in J_BASE)
        gen_jo = (juguete_objeto for juguete_objeto in jo)
        gen_or = (objeto_recurso for objeto_recurso in OR_BASE)
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in RR_BASE)
        *items, largo = indexes_of(
            juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr), [0]
        )
        self.assertEqual(largo, 1)
        self.assertEqual(items[0], 1)

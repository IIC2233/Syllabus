from tests_publicos.test_tools import IICTest, timeout
from backend.consultas import cadena_creacion
from utils import JugueteRecurso, RecursoRecurso

N_SECOND = 0.3

# R1 y R2 solo los producen juguetes.
# R3 = R1*2 + R2*1 (sin juguetes que lo produzcan directamente).
# R4 = R3*1 + R2*2 (sin juguetes que lo produzcan directamente).
JR_BASE = [
    JugueteRecurso(1, 1, "00:10", 5),
    JugueteRecurso(2, 2, "00:20", 3),
    JugueteRecurso(3, 1, "00:15", 2),
    JugueteRecurso(4, 3, "00:05", 4),
]
RR_BASE = [
    RecursoRecurso(99, ((98, 2)), 4),
    RecursoRecurso(4, ((3, 1), (2, 2)), 3),
    RecursoRecurso(3, ((1, 2), (2, 1)), 5),
]


class TestCadenaCreacion(IICTest):
    """
    Pruebas para cadena_creacion(generador_juguete_recurso, generador_recurso_recurso, recurso).
    Retorna {id_recurso: {"recursos": {...}, "juguetes": (...)}} de forma recursiva.
    """

    @timeout(N_SECOND)
    def test_recurso_sin_receta_ni_juguetes(self):
        """
        Recurso que no lo crea ningún RecursoRecurso ni ningún juguete →
        {id: {"recursos": {}, "juguetes": ()}}.
        """
        gen_jr = (juguete_recurso for juguete_recurso in [JugueteRecurso(1, 10, "00:10", 5)])
        gen_rr = (recurso_recurso for recurso_recurso in [])
        resultado = cadena_creacion(gen_jr, gen_rr, 5)
        self.assertEqual(resultado, {5: {"recursos": {}, "juguetes": ()}})

    @timeout(N_SECOND)
    def test_recurso_producido_solo_por_juguetes(self):
        """
        Recurso sin RecursoRecurso que lo cree → "recursos" vacío,
        "juguetes" con los ids de quienes lo producen.
        """
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in [])
        resultado = cadena_creacion(gen_jr, gen_rr, 1)
        self.assertEqual(resultado, {1: {"recursos": {}, "juguetes": (1, 3)}})

    @timeout(N_SECOND)
    def test_recurso_producido_solo_por_receta(self):
        """
        Recurso que ningún juguete produce directamente → "juguetes" vacío.
        """
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in RR_BASE)
        resultado = cadena_creacion(gen_jr, gen_rr, 3)
        esperado = {
            3: {
                "recursos": {
                    1: {"recursos": {}, "juguetes": (1, 3)},
                    2: {"recursos": {}, "juguetes": (2,)},
                },
                "juguetes": (4,),
            }
        }
        self.assertEqual(resultado, esperado)

    @timeout(N_SECOND)
    def test_cadena_con_multiples_niveles(self):
        """
        Cadena con varios niveles de ingredientes → se incluyen todos los
        recursos intermedios de forma recursiva.
        """
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in RR_BASE)
        resultado = cadena_creacion(gen_jr, gen_rr, 4)
        esperado = {
            4: {
                "recursos": {
                    3: {
                        "recursos": {
                            1: {"recursos": {}, "juguetes": (1, 3)},
                            2: {"recursos": {}, "juguetes": (2,)},
                        },
                        "juguetes": (4,),
                    },
                    2: {"recursos": {}, "juguetes": (2,)},
                },
                "juguetes": (),
            }
        }
        self.assertEqual(resultado, esperado)

    def test_cadena_1(self):
        gen_jr = (juguete_recurso for juguete_recurso in JR_BASE)
        gen_rr = (recurso_recurso for recurso_recurso in RR_BASE)
        resultado = cadena_creacion(gen_jr, gen_rr, 1)
        esperado = {
            1: {'recursos': {}, 'juguetes': (1, 3)}}
        self.assertEqual(resultado, esperado)
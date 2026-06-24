from tests_privados.test_tools import IICTest, timeout
from backend.consultas import cadena_creacion
from utils import JugueteRecurso, RecursoRecurso

N_SECOND_BASE = 0.3
# R10: hoja, producido por J1 y J3
# R20: hoja, producido por J5
# R30: receta R10×1 + R20×2, producido directamente por J7
# R40: receta R30×1 + R10×1, sin productores directos
JR_BASE = [
    JugueteRecurso(1, 10, "00:05", 3),
    JugueteRecurso(3, 10, "00:10", 2),
    JugueteRecurso(5, 20, "00:08", 1),
    JugueteRecurso(7, 30, "00:12", 4),
]

RR_BASE = [
    RecursoRecurso(40, ((30, 1), (10, 1)), 8),
    RecursoRecurso(30, ((10, 1), (20, 2)), 5),
]

class TestCadenaCreacionPrivado(IICTest):
    """
    Pruebas de correctitud para cadena_creacion.
    JR_BASE/RR_BASE modelan R40 ← R30 ← {R10, R20} con productores en cada nivel.
    Verifica expansion recursiva, recursos compartidos entre ramas y juguetes por nivel.
    """

    @timeout(N_SECOND_BASE)
    def test_recurso_sin_receta_ni_juguetes(self):
        """
        Recurso sin receta ni productores retorna nodo hoja vacio.
        """
        gen_jr = (jr for jr in JR_BASE)
        gen_rr = (rr for rr in RR_BASE)
        resultado = cadena_creacion(gen_jr, gen_rr, 99)
        self.assertEqual(resultado, {99: {"recursos": {}, "juguetes": ()}})

    @timeout(N_SECOND_BASE)
    def test_recurso_producido_solo_por_juguetes(self):
        """
        Recurso hoja sin receta incluye sus juguetes productores.
        R10 producido por J1 y J3; sin ingredientes de receta.
        """
        gen_jr = (jr for jr in JR_BASE)
        gen_rr = (rr for rr in RR_BASE)
        resultado = cadena_creacion(gen_jr, gen_rr, 10)
        self.assertEqual(resultado, {10: {"recursos": {}, "juguetes": (1, 3)}})

    @timeout(N_SECOND_BASE)
    def test_recurso_con_receta_y_juguetes(self):
        """
        Recurso con receta y productores directos incluye ambos.
        R30 requiere R10 y R20; J7 lo produce directamente.
        """
        gen_jr = (jr for jr in JR_BASE)
        gen_rr = (rr for rr in RR_BASE)
        resultado = cadena_creacion(gen_jr, gen_rr, 30)
        esperado = {
            30: {
                "recursos": {
                    10: {"recursos": {}, "juguetes": (1, 3)},
                    20: {"recursos": {}, "juguetes": (5,)},
                },
                "juguetes": (7,),
            }
        }
        self.assertEqual(resultado, esperado)

    @timeout(N_SECOND_BASE)
    def test_cadena_multinivel(self):
        """
        La cadena expande requisitos recursivamente por nivel.
        R40 requiere R30 (que requiere R10 y R20) y R10 directamente.
        """
        gen_jr = (jr for jr in JR_BASE)
        gen_rr = (rr for rr in RR_BASE)
        resultado = cadena_creacion(gen_jr, gen_rr, 40)
        esperado = {
            40: {
                "recursos": {
                    30: {
                        "recursos": {
                            10: {"recursos": {}, "juguetes": (1, 3)},
                            20: {"recursos": {}, "juguetes": (5,)},
                        },
                        "juguetes": (7,),
                    },
                    10: {"recursos": {}, "juguetes": (1, 3)},
                },
                "juguetes": (),
            }
        }
        self.assertEqual(resultado, esperado)

    @timeout(N_SECOND_BASE)
    def test_subrecetas_indirectas_y_productores_por_nivel(self):
        """
        R9 requiere R7×1 y R5×2; R7 requiere R5×1.
        R5 aparece directo en R9 y anidado dentro de R7.
        """
        juguete_recurso = (
            JugueteRecurso(2, 5, "00:01", 1),
            JugueteRecurso(1, 9, "00:01", 1),
        )
        recurso_recurso = (
            RecursoRecurso(9, ((7, 1), (5, 2)), 3),
            RecursoRecurso(7, ((5, 1),), 1),
        )
        esperado = {
            9: {
                "recursos": {
                    7: {"recursos": {5: {"recursos": {}, "juguetes": (2,)}}, "juguetes": ()},
                    5: {"recursos": {}, "juguetes": (2,)},
                },
                "juguetes": (1,),
            }
        }
        self.assertEqual(
            cadena_creacion(
                (jr for jr in juguete_recurso),
                (rr for rr in recurso_recurso),
                9,
            ),
            esperado,
        )

    @timeout(N_SECOND_BASE)
    def test_dependencia_diamante(self):
        """
        Estructura en diamante donde dos ramas comparten R50.
        R50 debe expandirse dentro de R80 y tambien dentro de R90.
        """
        jr = [JugueteRecurso(4, 50, "00:01", 1)]
        rr = [
            RecursoRecurso(100, ((80, 1), (90, 1)), 7),
            RecursoRecurso(90, ((50, 1),), 4),
            RecursoRecurso(80, ((50, 1),), 3),
        ]
        esperado = {
            100: {
                "recursos": {
                    80: {"recursos": {50: {"recursos": {}, "juguetes": (4,)}}, "juguetes": ()},
                    90: {"recursos": {50: {"recursos": {}, "juguetes": (4,)}}, "juguetes": ()},
                },
                "juguetes": (),
            }
        }
        self.assertEqual(cadena_creacion((x for x in jr), (x for x in rr), 100), esperado)

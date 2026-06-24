from tests_privados.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import juguetes_autosuficientes
from utils import Juguete, JugueteObjeto, ObjetoRecurso, JugueteRecurso, RecursoRecurso

N_SECOND_BASE = 0.3
def ejecutar(juguetes, juguete_objeto, objeto_recurso, juguete_recurso, recurso_recurso):
    return list(
        juguetes_autosuficientes(
            (j for j in juguetes),
            (jo for jo in juguete_objeto),
            (or_ for or_ in objeto_recurso),
            (jr for jr in juguete_recurso),
            (rr for rr in recurso_recurso),
        )
    )

class TestJuguetesAutosuficientesPrivado(IICTest):
    """
    Pruebas de correctitud para juguetes_autosuficientes.
    Verifica: produccion directa, cadenas via RecursoRecurso, afinidades insuficientes,
    objetos con multiples recursos, juguetes sin favoritos y salida ordenada sin duplicados.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe ser generadora.
        """
        assert_es_generador(self, juguetes_autosuficientes)

    @timeout(N_SECOND_BASE)
    def test_autosuficiente_por_recurso_directo(self):
        """
        Un juguete que produce todos los recursos de un objeto favorito es autosuficiente.
        """
        juguetes = [Juguete(1, "J1", (5,), "001"), Juguete(2, "J2", (5,), "002")]
        juguete_objeto = [JugueteObjeto(1, 10), JugueteObjeto(2, 20)]
        objeto_recurso = [
            ObjetoRecurso(10, ((1, 1),)),
            ObjetoRecurso(20, ((3, 1),)),
        ]
        juguete_recurso = [
            JugueteRecurso(1, 1, "00:10", 1),
            JugueteRecurso(2, 2, "00:10", 1),
        ]
        self.assertEqual(
            ejecutar(juguetes, juguete_objeto, objeto_recurso, juguete_recurso, []),
            [1],
        )

    @timeout(N_SECOND_BASE)
    def test_autosuficiente_via_recurso_recurso_con_afinidad(self):
        """
        Un juguete puede usar cadenas de RecursoRecurso si tiene las afinidades requeridas.
        """
        juguetes = [Juguete(10, "J10", (2, 3), "010")]
        juguete_objeto = [JugueteObjeto(10, 100)]
        objeto_recurso = [ObjetoRecurso(100, ((3, 1),))]
        juguete_recurso = [JugueteRecurso(10, 1, "00:05", 1)]
        recurso_recurso = [
            RecursoRecurso(3, ((2, 1),), 3),
            RecursoRecurso(2, ((1, 1),), 2),
        ]
        self.assertEqual(
            ejecutar(juguetes, juguete_objeto, objeto_recurso, juguete_recurso, recurso_recurso),
            [10],
        )

    @timeout(N_SECOND_BASE)
    def test_no_autosuficiente_si_falta_afinidad(self):
        """
        Si una receta de la cadena exige una afinidad ausente, el recurso no es obtenible.
        """
        juguetes = [Juguete(10, "J10", (2,), "010")]
        juguete_objeto = [JugueteObjeto(10, 100)]
        objeto_recurso = [ObjetoRecurso(100, ((3, 1),))]
        juguete_recurso = [JugueteRecurso(10, 1, "00:05", 1)]
        recurso_recurso = [
            RecursoRecurso(3, ((2, 1),), 3),
            RecursoRecurso(2, ((1, 1),), 2),
        ]
        self.assertEqual(
            ejecutar(juguetes, juguete_objeto, objeto_recurso, juguete_recurso, recurso_recurso),
            [],
        )

    @timeout(N_SECOND_BASE)
    def test_objeto_favorito_requiere_todos_sus_recursos(self):
        """
        Para fabricar un objeto favorito deben obtenerse todos sus recursos requeridos.
        """
        juguetes = [Juguete(7, "J7", (4,), "007")]
        juguete_objeto = [JugueteObjeto(7, 70)]
        objeto_recurso = [ObjetoRecurso(70, ((1, 1), (3, 1)))]
        juguete_recurso = [JugueteRecurso(7, 1, "00:05", 1)]
        recurso_recurso = [RecursoRecurso(2, ((1, 1),), 4)]
        self.assertEqual(
            ejecutar(juguetes, juguete_objeto, objeto_recurso, juguete_recurso, recurso_recurso),
            [],
        )

    @timeout(N_SECOND_BASE)
    def test_juguete_sin_objetos_favoritos_no_aparece(self):
        """
        Un juguete sin objetos favoritos no es autosuficiente aunque produzca recursos.
        """
        juguetes = [Juguete(1, "J1", (1,), "001")]
        juguete_recurso = [JugueteRecurso(1, 1, "00:05", 1)]
        self.assertEqual(ejecutar(juguetes, [], [], juguete_recurso, []), [])

    @timeout(N_SECOND_BASE)
    def test_salida_ordenada_y_sin_duplicados(self):
        """
        El resultado se ordena por id_juguete y no repite juguetes con varios objetos validos.
        """
        juguetes = [
            Juguete(3, "J3", (1,), "003"),
            Juguete(1, "J1", (1,), "001"),
            Juguete(2, "J2", (1,), "002"),
        ]
        juguete_objeto = [
            JugueteObjeto(3, 30),
            JugueteObjeto(1, 10),
            JugueteObjeto(3, 31),
            JugueteObjeto(2, 20),
        ]
        objeto_recurso = [
            ObjetoRecurso(10, ((1, 1),)),
            ObjetoRecurso(20, ((9, 1),)),
            ObjetoRecurso(30, ((3, 1),)),
            ObjetoRecurso(31, ((3, 1),)),
        ]
        juguete_recurso = [
            JugueteRecurso(3, 3, "00:05", 1),
            JugueteRecurso(1, 1, "00:05", 1),
            JugueteRecurso(2, 2, "00:05", 1),
        ]
        self.assertEqual(
            ejecutar(juguetes, juguete_objeto, objeto_recurso, juguete_recurso, []),
            [1, 3],
        )

    @timeout(N_SECOND_BASE)
    def test_basta_un_favorito_creable(self):
        """
        Un juguete es autosuficiente si puede fabricar al menos un objeto favorito.
        J5 debe aparecer aunque otro de sus favoritos no sea creable.
        """
        juguetes = [Juguete(5, "J5", (9,), "005"), Juguete(6, "J6", (), "006")]
        juguete_objeto = [JugueteObjeto(5, 50), JugueteObjeto(5, 60), JugueteObjeto(6, 50)]
        objeto_recurso = [ObjetoRecurso(50, ((15, 1),)), ObjetoRecurso(60, ((99, 1),))]
        juguete_recurso = [JugueteRecurso(5, 7, "00:05", 1), JugueteRecurso(6, 7, "00:05", 1)]
        recurso_recurso = [RecursoRecurso(15, ((7, 1),), 9)]
        self.assertEqual(ejecutar(juguetes, juguete_objeto, objeto_recurso, juguete_recurso, recurso_recurso), [5])

    @timeout(N_SECOND_BASE)
    def test_objeto_con_dos_recursos_ambos_obtenibles_via_cadena(self):
        """
        El objeto favorito requiere dos recursos obtenibles por RecursoRecurso.
        J8 debe ser autosuficiente porque tiene ambas afinidades necesarias.
        """
        juguetes = [Juguete(8, "J8", (4, 6), "008")]
        juguete_objeto = [JugueteObjeto(8, 80)]
        objeto_recurso = [ObjetoRecurso(80, ((20, 1), (21, 1)))]
        juguete_recurso = [JugueteRecurso(8, 11, "00:05", 1)]
        recurso_recurso = [RecursoRecurso(20, ((11, 1),), 4), RecursoRecurso(21, ((11, 1),), 6)]
        self.assertEqual(ejecutar(juguetes, juguete_objeto, objeto_recurso, juguete_recurso, recurso_recurso), [8])

    @timeout(N_SECOND_BASE)
    def test_dos_juguetes_mismo_recurso_distinta_afinidad(self):
        """
        Dos juguetes producen el mismo recurso base, pero solo uno tiene la afinidad requerida.
        Solo el juguete con afinidad 8 debe ser autosuficiente.
        """
        juguetes = [Juguete(15, "J15", (8,), "015"), Juguete(16, "J16", (5,), "016")]
        juguete_objeto = [JugueteObjeto(15, 90), JugueteObjeto(16, 90)]
        objeto_recurso = [ObjetoRecurso(90, ((60, 1),))]
        juguete_recurso = [JugueteRecurso(15, 50, "00:05", 1), JugueteRecurso(16, 50, "00:05", 1)]
        recurso_recurso = [RecursoRecurso(60, ((50, 1),), 8)]
        self.assertEqual(ejecutar(juguetes, juguete_objeto, objeto_recurso, juguete_recurso, recurso_recurso), [15])


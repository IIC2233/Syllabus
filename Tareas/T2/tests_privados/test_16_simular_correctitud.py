from tests_privados.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import simular
from utils import (
    Juguete,
    JugueteHabitat,
    HabitatObjeto,
    ObjetoRecurso,
    RecursoRecurso,
    JugueteRecurso,
    JugueteObjeto,
    PeriodoDia,
)

N_SECOND_BASE = 2.0
def gen(iterable):
    yield from iterable


def crear_simulacion(
    juguetes,
    juguete_habitat,
    habitat_objeto,
    objeto_recurso=(),
    recurso_recurso=(),
    juguete_recurso=(),
    juguete_objeto=(),
    periodo_dia=(PeriodoDia(1, "Dia", "00:30"),),
):
    simulacion = simular(
        gen(juguetes),
        gen(juguete_habitat),
        gen(habitat_objeto),
        gen(objeto_recurso),
        gen(recurso_recurso),
        gen(juguete_recurso),
        gen(juguete_objeto),
        gen(periodo_dia),
    )
    next(simulacion)
    return simulacion


def compactar(eventos):
    resultado = []
    for tiempo, tipo, payload in eventos:
        if tipo == "juguete":
            resultado.append((tiempo, tipo, payload.id_juguete))
        else:
            resultado.append((tiempo, tipo, payload))
    return resultado

class TestSimularPrivado(IICTest):
    """
    Pruebas de correctitud para simular.
    Verifica los tres comandos send (None, "next", "end"), orden de eventos en un mismo
    tick (juguetes antes que habitats, desempate por id) y respeto de periodos validos.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe ser generadora.
        """
        assert_es_generador(self, simular)

    @timeout(N_SECOND_BASE)
    def test_send_none_avanza_un_minuto(self):
        """
        send(None) avanza una unidad de tiempo y no salta minutos vacios.
        Un juguete con espera 00:03 creado en t=0 aparece en t=4.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_habitat = (JugueteHabitat(1, 10, "00:03", (1,)),)
        habitat_objeto = (HabitatObjeto(10, ()),)
        juguete_recurso = (JugueteRecurso(1, 1, "00:01", 1),)
        simulacion = crear_simulacion(
            juguetes,
            juguete_habitat,
            habitat_objeto,
            juguete_recurso=juguete_recurso,
        )

        self.assertEqual(compactar(simulacion.send(None)), [(0, "habitat", 10)])
        self.assertEqual(compactar(simulacion.send(None)), [])
        self.assertEqual(compactar(simulacion.send(None)), [])
        self.assertEqual(compactar(simulacion.send(None)), [])
        self.assertEqual(compactar(simulacion.send(None)), [(4, "juguete", 1)])

    @timeout(N_SECOND_BASE)
    def test_send_next_salta_minutos_vacios(self):
        """
        send("next") avanza hasta el siguiente evento de interes.
        Un juguete con espera 00:03 creado en t=0 aparece en t=4.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_habitat = (JugueteHabitat(1, 10, "00:03", (1,)),)
        habitat_objeto = (HabitatObjeto(10, ()),)
        juguete_recurso = (JugueteRecurso(1, 1, "00:01", 1),)
        simulacion = crear_simulacion(
            juguetes,
            juguete_habitat,
            habitat_objeto,
            juguete_recurso=juguete_recurso,
        )

        self.assertEqual(compactar(simulacion.send("next")), [(0, "habitat", 10)])
        self.assertEqual(compactar(simulacion.send("next")), [(4, "juguete", 1)])

    @timeout(N_SECOND_BASE)
    def test_mismo_minuto_juguetes_antes_que_habitats(self):
        """
        En un mismo minuto se reportan primero juguetes y luego habitats.
        """
        juguetes = (
            Juguete(1, "uno", (1,), "001"),
            Juguete(2, "dos", (1,), "002"),
        )
        juguete_habitat = (
            JugueteHabitat(1, 10, "00:01", (1,)),
            JugueteHabitat(2, 20, "00:01", (1,)),
        )
        habitat_objeto = (
            HabitatObjeto(10, ()),
            HabitatObjeto(20, ((5, 1),)),
        )
        objeto_recurso = (ObjetoRecurso(5, ((7, 1),)),)
        juguete_recurso = (
            JugueteRecurso(1, 7, "00:01", 1),
            JugueteRecurso(2, 8, "00:01", 1),
        )
        simulacion = crear_simulacion(
            juguetes,
            juguete_habitat,
            habitat_objeto,
            objeto_recurso=objeto_recurso,
            juguete_recurso=juguete_recurso,
        )

        self.assertEqual(compactar(simulacion.send(None)), [(0, "habitat", 10)])
        self.assertEqual(compactar(simulacion.send(None)), [])
        eventos = compactar(simulacion.send(None))
        self.assertEqual([evento[1] for evento in eventos], ["juguete", "habitat"])
        self.assertEqual(eventos[0][2], 1)
        self.assertEqual(eventos[1][2], 20)

    @timeout(N_SECOND_BASE)
    def test_empates_ordenados_por_id(self):
        """
        En un mismo tick, eventos del mismo tipo se ordenan por id ascendente.
        Valida empates entre habitats creados y juguetes aparecidos.
        """
        juguetes = (
            Juguete(1, "uno", (1,), "001"),
            Juguete(2, "dos", (1,), "002"),
        )
        juguete_habitat = (
            JugueteHabitat(2, 10, "00:01", (1,)),
            JugueteHabitat(1, 20, "00:01", (1,)),
        )
        habitat_objeto = (
            HabitatObjeto(20, ()),
            HabitatObjeto(10, ()),
        )
        juguete_recurso = (
            JugueteRecurso(1, 1, "00:01", 1),
            JugueteRecurso(2, 2, "00:01", 1),
        )
        simulacion = crear_simulacion(
            juguetes,
            juguete_habitat,
            habitat_objeto,
            juguete_recurso=juguete_recurso,
        )

        self.assertEqual(
            compactar(simulacion.send("next")),
            [(0, "habitat", 10), (0, "habitat", 20)],
        )
        self.assertEqual(
            compactar(simulacion.send("next")),
            [(2, "juguete", 1), (2, "juguete", 2)],
        )

    @timeout(N_SECOND_BASE)
    def test_send_end_drena_y_cierra(self):
        """
        send("end") retorna todos los eventos restantes en un solo resultado; un send
        posterior lanza StopIteration o GeneratorExit.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_habitat = (JugueteHabitat(1, 10, "00:02", (1,)),)
        habitat_objeto = (HabitatObjeto(10, ()),)
        juguete_recurso = (JugueteRecurso(1, 1, "00:01", 1),)
        simulacion = crear_simulacion(
            juguetes,
            juguete_habitat,
            habitat_objeto,
            juguete_recurso=juguete_recurso,
        )

        self.assertEqual(
            compactar(simulacion.send("end")),
            [(0, "habitat", 10), (3, "juguete", 1)],
        )
        with self.assertRaises((StopIteration, GeneratorExit)):
            simulacion.send(None)

    @timeout(N_SECOND_BASE)
    def test_respeta_periodo_valido_para_aparicion(self):
        """
        Un juguete espera hasta el proximo periodo permitido antes de aparecer.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_habitat = (JugueteHabitat(1, 10, "00:01", (2,)),)
        habitat_objeto = (HabitatObjeto(10, ()),)
        juguete_recurso = (JugueteRecurso(1, 1, "00:01", 1),)
        periodo_dia = (
            PeriodoDia(1, "Dia", "00:02"),
            PeriodoDia(2, "Noche", "00:03"),
        )
        simulacion = crear_simulacion(
            juguetes,
            juguete_habitat,
            habitat_objeto,
            juguete_recurso=juguete_recurso,
            periodo_dia=periodo_dia,
        )

        self.assertEqual(compactar(simulacion.send("next")), [(0, "habitat", 10)])
        self.assertEqual(compactar(simulacion.send("next")), [(2, "juguete", 1)])

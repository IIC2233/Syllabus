from tests_privados.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import manejo_habitat
from utils import Juguete, JugueteHabitat, HabitatObjeto, ObjetoRecurso, RecursoRecurso, PeriodoDia

N_SECOND_BASE = 0.3
PERIODOS = (PeriodoDia(1, "dia", "00:30"),)


def gen(iterable):
    yield from iterable


def crear_generador(
    juguetes=(),
    juguete_habitat=(),
    habitat_objeto=(),
    objeto_recurso=(),
    recurso_recurso=(),
    periodo_dia=PERIODOS,
    tiempo_inicial=0,
):
    generador = manejo_habitat(
        gen(juguetes),
        gen(juguete_habitat),
        gen(habitat_objeto),
        gen(objeto_recurso),
        gen(recurso_recurso),
        gen(periodo_dia),
        tiempo_inicial,
    )
    next(generador)
    return generador


def tuplas_cadena(cabeza, *attrs):
    resultado = []
    while cabeza is not None:
        resultado.append(tuple(getattr(cabeza, attr) for attr in attrs))
        cabeza = cabeza.siguiente
    return resultado


def report(generador):
    tiempo, juguetes, habitats, objetos, recursos = generador.send("report")
    return (
        tiempo,
        sorted(juguetes),
        tuplas_cadena(habitats, "id", "tiempo_presente"),
        tuplas_cadena(objetos, "id", "cantidad"),
        tuplas_cadena(recursos, "id", "cantidad"),
    )


class TestManejoHabitatPrivado(IICTest):
    """
    Pruebas de correctitud para manejo_habitat.
    Verifica comandos send, report, creacion de habitats/objetos, consumo de
    recursos, apariciones, afinidades y habitats innecesarios.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe retornar un generador.
        """
        assert_es_generador(self, manejo_habitat)

    @timeout(N_SECOND_BASE)
    def test_report_estado_inicial(self):
        """
        El tiempo_inicial se almacena y todas las cadenas parten vacias.
        """
        generador = crear_generador(tiempo_inicial=7)

        self.assertEqual(report(generador), (7, [], [], [], []))

    @timeout(N_SECOND_BASE)
    def test_send_tupla_recursos_acumula(self):
        """
        Ids repetidos en la misma tupla se acumulan en un solo nodo.
        Enviar la tupla no avanza tiempo ni modifica otros estados.
        """
        generador = crear_generador()

        self.assertIsNone(generador.send(((7, 2), (7, 3), (8, 1))))

        self.assertEqual(report(generador), (0, [], [], [], [(7, 5), (8, 1)]))

    @timeout(N_SECOND_BASE)
    def test_crear_sin_recursos_no_crea_habitat_con_objeto(self):
        """
        Un habitat de interes no se construye si sus objetos requieren recursos
        ausentes del stock.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_habitat = (JugueteHabitat(1, 10, "00:05", (1,)),)
        habitat_objeto = (HabitatObjeto(10, ((5, 1),)),)
        objeto_recurso = (ObjetoRecurso(5, ((7, 1),)),)
        generador = crear_generador(juguetes, juguete_habitat, habitat_objeto, objeto_recurso)

        self.assertEqual(generador.send("crear"), (set(), ()))

    @timeout(N_SECOND_BASE)
    def test_crear_habitat_sin_objetos(self):
        """
        Un habitat sin objetos requeridos puede construirse sin consumir recursos.
        Tras crearlo, aparece en la cadena interna con tiempo_presente=0.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_habitat = (JugueteHabitat(1, 10, "00:05", (1,)),)
        habitat_objeto = (HabitatObjeto(10, tuple()),)
        generador = crear_generador(juguetes, juguete_habitat, habitat_objeto)

        self.assertEqual(generador.send("crear"), (set(), (10,)))
        self.assertEqual(report(generador), (0, [], [(10, 0)], [], []))

    @timeout(N_SECOND_BASE)
    def test_crear_consume_recursos_y_guarda_objetos(self):
        """
        Al crear habitats, los recursos usados se descuentan del stock y los
        objetos fabricados quedan en la cadena interna de objetos.
        """
        juguetes = (
            Juguete(1, "uno", (1,), "001"),
            Juguete(2, "dos", (2,), "002"),
        )
        juguete_habitat = (
            JugueteHabitat(1, 10, "00:02", (1,)),
            JugueteHabitat(2, 20, "00:02", (1,)),
        )
        habitat_objeto = (
            HabitatObjeto(10, ((5, 1),)),
            HabitatObjeto(20, ((6, 1),)),
        )
        objeto_recurso = (
            ObjetoRecurso(5, ((7, 2),)),
            ObjetoRecurso(6, ((8, 1),)),
        )
        generador = crear_generador(juguetes, juguete_habitat, habitat_objeto, objeto_recurso)

        generador.send(((7, 3), (8, 1)))
        self.assertEqual(generador.send("crear"), ({5, 6}, (10, 20)))
        self.assertEqual(
            report(generador),
            (0, [], [(10, 0), (20, 0)], [(5, 1), (6, 1)], [(7, 1)]),
        )

    @timeout(N_SECOND_BASE)
    def test_send_none_aparece_y_actualiza_estado(self):
        """
        Cada send(None) avanza un tick. Cuando se cumple el tiempo de espera de un
        juguete, aparece en su habitat y queda registrado como presente.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_habitat = (JugueteHabitat(1, 10, "00:02", (1,)),)
        habitat_objeto = (HabitatObjeto(10, tuple()),)
        generador = crear_generador(juguetes, juguete_habitat, habitat_objeto)
        generador.send("crear")

        self.assertEqual(generador.send(None), tuple())
        self.assertEqual(generador.send(None), tuple())
        self.assertEqual(generador.send(None), (1,))
        tiempo, juguetes, habitats, objetos, recursos = report(generador)
        self.assertEqual((tiempo, juguetes, objetos, recursos), (3, [1], [], []))
        self.assertIn(habitats, ([], [(10, 3)]))

    @timeout(N_SECOND_BASE)
    def test_no_crea_habitat_cuyo_juguete_ya_va_a_aparecer(self):
        """
        Si un juguete ya tiene habitat asignado, crear no debe construir un segundo
        habitat para ese mismo juguete aunque sea creable y de interes.
        """
        juguetes = (Juguete(1, "uno", (1,), "001"),)
        juguete_habitat = (
            JugueteHabitat(1, 10, "00:05", (1,)),
            JugueteHabitat(1, 20, "00:05", (1,)),
        )
        habitat_objeto = (
            HabitatObjeto(10, tuple()),
            HabitatObjeto(20, ((5, 1),)),
        )
        objeto_recurso = (ObjetoRecurso(5, ((7, 1),)),)
        generador = crear_generador(juguetes, juguete_habitat, habitat_objeto, objeto_recurso)

        self.assertEqual(generador.send("crear"), (set(), (10,)))
        self.assertEqual(generador.send(None), tuple())
        self.assertIsNone(generador.send(((7, 1),)))

        self.assertEqual(generador.send("crear"), (set(), ()))

    @timeout(N_SECOND_BASE)
    def test_bloqueo_selectivo_no_afecta_a_otros_juguetes(self):
        """
        Los juguetes que van a aparecer se tratan como ya aparecidos solo para
        evaluar habitats de interes. Juguetes que aun no tienen habitat asignado
        siguen generando habitats de interes que deben construirse si son creables.
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
            HabitatObjeto(10, tuple()),
            HabitatObjeto(20, ((5, 1),)),
        )
        objeto_recurso = (ObjetoRecurso(5, ((7, 1),)),)
        generador = crear_generador(juguetes, juguete_habitat, habitat_objeto, objeto_recurso)

        self.assertEqual(generador.send("crear"), (set(), (10,)))
        self.assertIsNone(generador.send(((7, 1),)))
        objetos, habitats = generador.send("crear")
        self.assertEqual(objetos, {5})
        self.assertIn(20, habitats)

    @timeout(N_SECOND_BASE)
    def test_afinidad_de_juguete_aparecido_habilita_creacion(self):
        """
        Cuando un juguete aparece, su afinidad queda disponible para sintetizar
        recursos via RecursoRecurso, habilitando habitats que antes no eran creables.
        """
        juguetes = (
            Juguete(1, "uno", (7,), "001"),
            Juguete(2, "dos", (1,), "002"),
        )
        juguete_habitat = (
            JugueteHabitat(1, 10, "00:01", (1,)),
            JugueteHabitat(2, 20, "00:01", (1,)),
        )
        habitat_objeto = (
            HabitatObjeto(10, tuple()),
            HabitatObjeto(20, ((4, 1),)),
        )
        objeto_recurso = (ObjetoRecurso(4, ((8, 1),)),)
        recurso_recurso = (RecursoRecurso(8, ((3, 2),), 7),)
        generador = crear_generador(
            juguetes, juguete_habitat, habitat_objeto, objeto_recurso, recurso_recurso
        )

        self.assertIsNone(generador.send(((3, 2),)))
        self.assertEqual(generador.send("crear"), (set(), (10,)))
        self.assertEqual(generador.send(None), tuple())
        self.assertEqual(generador.send(None), (1,))

        self.assertEqual(generador.send("crear"), ({4}, (20,)))
        tiempo, juguetes, habitats, objetos, recursos = report(generador)
        self.assertEqual((tiempo, juguetes, objetos, recursos), (2, [1], [(4, 1)], []))
        self.assertIn((20, 0), habitats)

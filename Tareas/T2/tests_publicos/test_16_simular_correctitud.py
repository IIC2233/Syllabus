import inspect
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import simular
from utils import (
    Juguete,
    JugueteHabitat,
    HabitatObjeto,
    ObjetoRecurso,
    JugueteRecurso,
    JugueteObjeto,
    RecursoRecurso,
    PeriodoDia,
)

N_SEGUNDOS = 2.0

# Escenarios simples para los tests
PERIODOS = [PeriodoDia(1, "Día", "01:00"), PeriodoDia(2, "Noche", "01:00")]

# Escenario: habitat simple con un juguete
J_SIMPLE = [Juguete(1, "Bulbasaur", (1,), "001")]
JH_SIMPLE = [JugueteHabitat(1, 1, "00:01", (1,))]
HO_SIMPLE = [HabitatObjeto(1, tuple())]
OR_SIMPLE = []
JR_SIMPLE = [JugueteRecurso(1, 1, "00:01", 1)]
JO_SIMPLE = [JugueteObjeto(1, 10)]
RR_SIMPLE = []

# Escenario complejo para probar avance en varios pasos y cierre con "end"
PERIODOS_COMPLEJO = [PeriodoDia(1, "Dia", "01:30"), PeriodoDia(2, "Tarde", "01:30"), 
                     PeriodoDia(3, "Noche", "00:30")]

J_COMPLEJO = [
    Juguete(1, "Pikachu", (1,), "001"),
    Juguete(2, "Bulbasaur", (2,), "002"),
    Juguete(3, "Charmander", (3,), "003"),
]
JH_COMPLEJO = [
    JugueteHabitat(1, 1, "00:01", (1,)),
    JugueteHabitat(2, 2, "00:02", (2,)),
    JugueteHabitat(3, 3, "00:03", (1, 2)),
]
HO_COMPLEJO = [
    HabitatObjeto(1, tuple()),
    HabitatObjeto(2, ((1, 1),)),
    HabitatObjeto(3, ((2, 1),)),
]
OR_COMPLEJO = [
    ObjetoRecurso(1, ((10, 1),)),
    ObjetoRecurso(2, ((20, 1),)),
]
JR_COMPLEJO = [
    JugueteRecurso(1, 10, "00:01", 1),
    JugueteRecurso(2, 20, "00:02", 1),
    JugueteRecurso(3, 10, "00:03", 1),
]
JO_COMPLEJO = [
    JugueteObjeto(1, 10),
    JugueteObjeto(2, 20),
    JugueteObjeto(3, 30),
]
RR_COMPLEJO = [
    RecursoRecurso(30, ((10, 1),), 1),
    RecursoRecurso(40, ((20, 1),), 2),
    RecursoRecurso(50, ((30, 1),), 1),
    RecursoRecurso(60, ((40, 1),), 2),
]

# Escenario: generadores vacíos (sin eventos)
J_VACIO = []
JH_VACIO = []
HO_VACIO = []
OR_VACIO = []
JR_VACIO = []
JO_VACIO = []
RR_VACIO = []


class TestSimular(IICTest):
    """
    Pruebas de correctitud para simular().
    Es una función generadora con send().
    """

    @timeout(N_SEGUNDOS)
    def test_es_generador(self):
        """Verifica que simular es una función generadora."""
        assert_es_generador(self, simular)

    @timeout(N_SEGUNDOS)
    def test_none_retorna_evento_cuando_debe(self):
        """send(None) retorna un generador con eventos cuando hay eventos en ese minuto."""
        simulacion = simular(
            (j for j in J_SIMPLE), (jh for jh in JH_SIMPLE), 
            (ho for ho in HO_SIMPLE), (or_ for or_ in OR_SIMPLE), 
            (rr for rr in RR_SIMPLE), (jr for jr in JR_SIMPLE),
            (jo for jo in JO_SIMPLE), (pd for pd in PERIODOS)
        )
        next(simulacion)  # inicializar
        
        gen_eventos = simulacion.send(None)
        self.assertTrue(inspect.isgenerator(gen_eventos))
        eventos = list(gen_eventos)
        # Debe haber al menos un evento de habitat en t=0
        self.assertGreater(len(eventos), 0)

    @timeout(N_SEGUNDOS)
    def test_none_no_retorna_evento_cuando_no_hay(self):
        """send(None) retorna un generador vacío cuando no hay eventos en ese minuto."""
        simulacion = simular(
            (j for j in J_VACIO), (jh for jh in JH_VACIO), 
            (ho for ho in HO_VACIO), (or_ for or_ in OR_VACIO), 
            (rr for rr in RR_VACIO), (jr for jr in JR_VACIO),
            (jo for jo in JO_VACIO), (pd for pd in [])
        )
        next(simulacion)
        
        gen_eventos = simulacion.send(None)
        self.assertTrue(inspect.isgenerator(gen_eventos))
        eventos = list(gen_eventos)
        # Sin generadores de entrada, no hay eventos
        self.assertEqual(len(eventos), 0)

    @timeout(N_SEGUNDOS)
    def test_next_avanza_minuto_con_eventos(self):
        """next() sobre el generador de eventos retorna eventos cuando existen."""
        simulacion = simular(
            (j for j in J_SIMPLE), (jh for jh in JH_SIMPLE), 
            (ho for ho in HO_SIMPLE), (or_ for or_ in OR_SIMPLE), 
            (rr for rr in RR_SIMPLE), (jr for jr in JR_SIMPLE),
            (jo for jo in JO_SIMPLE), (pd for pd in PERIODOS)
        )
        next(simulacion)
        
        gen_eventos = simulacion.send(None)
        # next() sobre el generador debería devolver eventos individuales o agotarse
        evento = next(gen_eventos, None)
        self.assertIsNotNone(evento)
        self.assertIsInstance(evento, tuple)

    @timeout(N_SEGUNDOS)
    def test_send_end_retorna_todos_eventos_restantes(self):
        """send("end") retorna un generador con todos los eventos pendientes."""
        simulacion = simular(
            (j for j in J_SIMPLE), (jh for jh in JH_SIMPLE), 
            (ho for ho in HO_SIMPLE), (or_ for or_ in OR_SIMPLE), 
            (rr for rr in RR_SIMPLE), (jr for jr in JR_SIMPLE),
            (jo for jo in JO_SIMPLE), (pd for pd in PERIODOS)
        )
        next(simulacion)
        
        # Enviar "end" para obtener todos los eventos
        gen_eventos = simulacion.send("end")
        self.assertTrue(inspect.isgenerator(gen_eventos))
        eventos = list(gen_eventos)
        # Debe haber al menos eventos de habitat
        self.assertGreater(len(eventos), 0)

    @timeout(N_SEGUNDOS)
    def test_eventos_habitat_tienen_formato_correcto(self):
        """Los eventos de habitat tienen formato (tiempo: int, "habitat", id: int)."""
        simulacion = simular(
            (j for j in J_SIMPLE), (jh for jh in JH_SIMPLE), 
            (ho for ho in HO_SIMPLE), (or_ for or_ in OR_SIMPLE), 
            (rr for rr in RR_SIMPLE), (jr for jr in JR_SIMPLE),
            (jo for jo in JO_SIMPLE), (pd for pd in PERIODOS)
        )
        next(simulacion)
        
        gen_eventos = simulacion.send(None)
        eventos = list(gen_eventos)
        
        # Filtrar eventos de habitat
        hab_eventos = [e for e in eventos if e[1] == "habitat"]
        self.assertGreater(len(hab_eventos), 0)
        
        for evento in hab_eventos:
            self.assertIsInstance(evento, tuple)
            self.assertEqual(len(evento), 3)
            self.assertIsInstance(evento[0], int)
            self.assertEqual(evento[1], "habitat")
            self.assertIsInstance(evento[2], int)

    @timeout(N_SEGUNDOS)
    def test_eventos_juguete_tienen_formato_correcto(self):
        """Los eventos de juguete tienen formato (tiempo: int, "juguete", Juguete)."""
        simulacion = simular(
            (j for j in J_SIMPLE), (jh for jh in JH_SIMPLE), 
            (ho for ho in HO_SIMPLE), (or_ for or_ in OR_SIMPLE), 
            (rr for rr in RR_SIMPLE), (jr for jr in JR_SIMPLE),
            (jo for jo in JO_SIMPLE), (pd for pd in PERIODOS)
        )
        next(simulacion)
        
        # Avanzar varios minutos para encontrar eventos de juguete
        todos_eventos = []
        for _ in range(50):
            gen = simulacion.send(None)
            todos_eventos.extend(list(gen))
            if any(e[1] == "juguete" for e in todos_eventos):
                break
        
        jug_eventos = [e for e in todos_eventos if e[1] == "juguete"]
        if jug_eventos:
            for evento in jug_eventos:
                self.assertIsInstance(evento, tuple)
                self.assertEqual(len(evento), 3)
                self.assertIsInstance(evento[0], int)
                self.assertEqual(evento[1], "juguete")
                self.assertIsInstance(evento[2], Juguete)

    @timeout(N_SEGUNDOS)
    def test_next_dos_veces_con_escenario_complejo(self):
        """Con el escenario complejo, next() dos veces debe seguir entregando generadores."""
        simulacion = simular(
            (j for j in J_COMPLEJO), (jh for jh in JH_COMPLEJO),
            (ho for ho in HO_COMPLEJO), (or_ for or_ in OR_COMPLEJO),
            (rr for rr in RR_COMPLEJO), (jr for jr in JR_COMPLEJO),
            (jo for jo in JO_COMPLEJO), (pd for pd in PERIODOS_COMPLEJO)
        )
        next(simulacion)

        gen_primero = next(simulacion)
        self.assertTrue(inspect.isgenerator(gen_primero))
        eventos_primero = list(gen_primero)
        self.assertTrue(all(isinstance(evento, tuple) for evento in eventos_primero))

        gen_segundo = next(simulacion)
        self.assertTrue(inspect.isgenerator(gen_segundo))
        eventos_segundo = list(gen_segundo)
        self.assertTrue(all(isinstance(evento, tuple) for evento in eventos_segundo))
        self.assertGreater(len(eventos_primero) + len(eventos_segundo), 0)

    @timeout(N_SEGUNDOS)
    def test_end_con_escenario_complejo(self):
        """Con el escenario complejo, send('end') debe devolver todos los eventos pendientes."""
        simulacion = simular(
            (j for j in J_COMPLEJO), (jh for jh in JH_COMPLEJO),
            (ho for ho in HO_COMPLEJO), (or_ for or_ in OR_COMPLEJO),
            (rr for rr in RR_COMPLEJO), (jr for jr in JR_COMPLEJO),
            (jo for jo in JO_COMPLEJO), (pd for pd in PERIODOS_COMPLEJO)
        )
        next(simulacion)

        gen_eventos = simulacion.send("end")
        self.assertTrue(inspect.isgenerator(gen_eventos))
        eventos = list(gen_eventos)
        self.assertGreater(len(eventos), 0)
        self.assertTrue(any(evento[1] == "habitat" for evento in eventos))
        self.assertTrue(any(evento[1] == "juguete" for evento in eventos))

    @timeout(N_SEGUNDOS)
    def test_despues_de_end_genera_error(self):
        """Después de send("end"), intentar avanzar más genera error o StopIteration."""
        simulacion = simular(
            (j for j in J_SIMPLE), (jh for jh in JH_SIMPLE), 
            (ho for ho in HO_SIMPLE), (or_ for or_ in OR_SIMPLE), 
            (rr for rr in RR_SIMPLE), (jr for jr in JR_SIMPLE),
            (jo for jo in JO_SIMPLE), (pd for pd in PERIODOS)
        )
        next(simulacion)
        
        # Consumir eventos con "end"
        gen_final = simulacion.send("end")
        list(gen_final)
        
        # Intentar enviar más debe resultar en error
        with self.assertRaises((StopIteration, GeneratorExit)):
            simulacion.send(None)

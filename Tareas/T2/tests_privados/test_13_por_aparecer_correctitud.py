from tests_privados.test_tools import IICTest, timeout, assert_es_generador
from backend.consultas import por_aparecer
from backend.nodo_ligado import NodoLigado
from utils import Juguete, JugueteHabitat, PeriodoDia

N_SECOND_BASE = 0.3
PERIODO_SIMPLE = (PeriodoDia(1, "dia", "00:30"),)


def gen(iterable):
    yield from iterable


def cadena_habitats(pares):
    cabeza = None
    for id_habitat, tiempo_presente in sorted(pares):
        nodo = NodoLigado(id=id_habitat, tiempo_presente=tiempo_presente)
        cabeza = nodo if cabeza is None else cabeza.insertar(nodo)
    return cabeza


class TestPorAparecerPrivado(IICTest):
    """
    Pruebas de correctitud para por_aparecer.
    Verifica generador, habitats vacios, tiempo_presente, desempates, juguetes
    ya presentes y periodos validos.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe retornar un generador.
        """
        assert_es_generador(self, por_aparecer)

    @timeout(N_SECOND_BASE)
    def test_habitat_none_retorna_vacio(self):
        """
        Si no hay cadena de habitats, no hay posiciones que reportar.
        """
        resultado = list(por_aparecer(gen(()), None, gen(()), gen(PERIODO_SIMPLE), 0))

        self.assertEqual(resultado, [])

    @timeout(N_SECOND_BASE)
    def test_habitat_sin_juguetes_retorna_none(self):
        """
        Si un habitat no tiene juguetes asociados en JugueteHabitat, la posicion
        correspondiente debe ser None.
        """
        habitats = cadena_habitats(((99, 0),))

        resultado = list(por_aparecer(gen(()), habitats, gen(()), gen(PERIODO_SIMPLE), 0))

        self.assertEqual(resultado, [None])

    @timeout(N_SECOND_BASE)
    def test_usa_tiempo_presente_del_habitat(self):
        """
        Si el juguete ya debio aparecer, no cuenta. Si aparece en el minuto exacto
        del tiempo_presente del habitat, si cuenta.
        """
        juguete_habitat = (
            JugueteHabitat(1, 10, "00:05", (1,)),
            JugueteHabitat(2, 20, "00:05", (1,)),
        )
        habitats = cadena_habitats(((10, 6), (20, 5)))

        resultado = list(por_aparecer(
            gen(()), habitats, gen(juguete_habitat), gen(PERIODO_SIMPLE), 0
        ))

        self.assertEqual(resultado, [None, 2])

    @timeout(N_SECOND_BASE)
    def test_mismo_juguete_en_dos_habitats_gana_menor_habitat(self):
        """
        Si el mismo juguete podria aparecer al mismo tiempo en dos habitats,
        aparece solo en el habitat de menor id.
        """
        juguete_habitat = (
            JugueteHabitat(3, 20, "00:02", (1,)),
            JugueteHabitat(3, 10, "00:02", (1,)),
        )
        habitats = cadena_habitats(((10, 0), (20, 0)))

        resultado = list(por_aparecer(
            gen(()), habitats, gen(juguete_habitat), gen(PERIODO_SIMPLE), 0
        ))

        self.assertEqual(resultado, [3, None])

    @timeout(N_SECOND_BASE)
    def test_dos_juguetes_mismo_habitat_gana_menor_id(self):
        """
        Si dos juguetes aparecen al mismo tiempo en el mismo habitat, aparece el
        juguete de menor id.
        """
        juguete_habitat = (
            JugueteHabitat(2, 10, "00:05", (1,)),
            JugueteHabitat(1, 10, "00:05", (1,)),
        )
        habitats = cadena_habitats(((10, 0),))

        resultado = list(por_aparecer(
            gen(()), habitats, gen(juguete_habitat), gen(PERIODO_SIMPLE), 0
        ))

        self.assertEqual(resultado, [1])

    @timeout(N_SECOND_BASE)
    def test_juguete_ya_presente_no_aparece_y_sigue_otro(self):
        """
        Si el primer candidato ya esta presente, debe buscarse otro juguete que
        pueda aparecer en ese habitat.
        """
        juguetes_presentes = (Juguete(1, "uno", (1,), "001"),)
        juguete_habitat = (
            JugueteHabitat(1, 10, "00:01", (1,)),
            JugueteHabitat(2, 10, "00:02", (1,)),
        )
        habitats = cadena_habitats(((10, 0),))

        resultado = list(por_aparecer(
            gen(juguetes_presentes), habitats, gen(juguete_habitat), gen(PERIODO_SIMPLE), 0
        ))

        self.assertEqual(resultado, [2])

    @timeout(N_SECOND_BASE)
    def test_momento_dia_no_cero_espera_siguiente_ciclo(self):
        """
        Periodos: P1(0-10), P2(10-20), ciclo=20 min. momento_dia=12 -> en P2, P1 ya paso.
        J1 y J3 necesitan P1: esperan al proximo ciclo (min 20), t_espera=5 -> aparecen
        en min 25, tiempo_de_espera=13.
        H10: J2 (P2, t_espera=3) aparece en min 13, tiempo_de_espera=1 -> gana a J1.
        H20: solo J3, sin competencia -> J3 aparece.
        """
        periodos = (
            PeriodoDia(1, "manana", "00:10"),
            PeriodoDia(2, "tarde", "00:10"),
        )
        juguete_habitat = (
            JugueteHabitat(1, 10, "00:05", (1,)),
            JugueteHabitat(2, 10, "00:03", (2,)),
            JugueteHabitat(3, 20, "00:05", (1,)),
        )
        habitats = cadena_habitats(((10, 0), (20, 0)))

        resultado = list(por_aparecer(
            gen(()), habitats, gen(juguete_habitat), gen(periodos), 12
        ))

        self.assertEqual(resultado, [2, 3])

    @timeout(N_SECOND_BASE)
    def test_respeta_periodos_para_escoger_primero(self):
        """
        Un juguete con menor tiempo_espera puede no ser el primero si debe esperar
        al siguiente periodo valido.
        """
        periodos = (
            PeriodoDia(1, "manana", "00:10"),
            PeriodoDia(2, "tarde", "00:10"),
            PeriodoDia(3, "noche", "00:10"),
        )
        juguete_habitat = (
            JugueteHabitat(1, 10, "00:05", (2,)),
            JugueteHabitat(2, 10, "00:08", (1,)),
        )
        habitats = cadena_habitats(((10, 0),))

        resultado = list(por_aparecer(
            gen(()), habitats, gen(juguete_habitat), gen(periodos), 0
        ))

        self.assertEqual(resultado, [2])

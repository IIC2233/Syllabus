from tests_privados.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import habitats_de_interes
from utils import Juguete, JugueteHabitat

N_SECOND_BASE = 0.3
# H1: necesita J1
# H2: necesita J1, J2, J3
# H3: necesita J2
# H4: necesita J3, J4
# H5: necesita J5
JH_BASE = [
    JugueteHabitat(1, 1, "00:10", (1,)),
    JugueteHabitat(1, 2, "00:15", (1,)),
    JugueteHabitat(2, 2, "00:20", (2,)),
    JugueteHabitat(3, 2, "00:25", (1,)),
    JugueteHabitat(2, 3, "00:30", (2,)),
    JugueteHabitat(3, 4, "00:10", (1,)),
    JugueteHabitat(4, 4, "00:15", (1,)),
    JugueteHabitat(5, 5, "00:10", (1,)),
]


def juguete(id_j: int) -> Juguete:
    return Juguete(id_j, f"J{id_j}", (1,), f"{id_j:03d}")

class TestHabitatsDeInteresPrivado(IICTest):
    """
    Pruebas de correctitud para habitats_de_interes.
    Un habitat es de interes si aun falta al menos un juguete asociado.
    """

    @timeout(N_SECOND_BASE)
    def test_retorna_generador(self):
        """
        La funcion debe ser generadora.
        """
        assert_es_generador(self, habitats_de_interes)

    @timeout(N_SECOND_BASE)
    def test_ambos_generadores_vacios(self):
        """
        Sin juguetes ni habitats, el resultado es vacio.
        """
        self.assertEqual(list(habitats_de_interes((j for j in []), (jh for jh in []))), [])

    @timeout(N_SECOND_BASE)
    def test_ningun_juguete_en_refugio(self):
        """
        Sin juguetes presentes, todos los habitats son de interes.
        """
        gen_j = (j for j in [])
        gen_jh = (jh for jh in JH_BASE)
        self.assertEqual(list(habitats_de_interes(gen_j, gen_jh)), [1, 2, 3, 4, 5])

    @timeout(N_SECOND_BASE)
    def test_todos_los_juguetes_presentes(self):
        """
        Con todos los juguetes en el refugio, ningun habitat es de interes.
        """
        gen_j = (juguete(i) for i in [1, 2, 3, 4, 5])
        gen_jh = (jh for jh in JH_BASE)
        *_, largo = indexes_of(habitats_de_interes(gen_j, gen_jh), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND_BASE)
    def test_juguete_sin_habitat_asociado(self):
        """
        Un juguete presente que no aparece en juguete_habitat no cierra ningun habitat.
        """
        gen_j = (juguete(i) for i in [99])
        gen_jh = (jh for jh in JH_BASE)
        self.assertEqual(list(habitats_de_interes(gen_j, gen_jh)), [1, 2, 3, 4, 5])

    @timeout(N_SECOND_BASE)
    def test_juguete_presente_no_cierra_habitat_con_otros_faltantes(self):
        """
        J1 y J2 presentes: H1 cerrado, H3 cerrado; H2 sigue abierto porque falta J3.
        """
        gen_j = (juguete(i) for i in [1, 2])
        gen_jh = (jh for jh in JH_BASE)
        self.assertEqual(list(habitats_de_interes(gen_j, gen_jh)), [2, 4, 5])

    @timeout(N_SECOND_BASE)
    def test_habitat_con_varios_juguetes_aparece_solo_una_vez(self):
        """
        H2 tiene 3 entradas en juguete_habitat (J1, J2, J3 faltantes).
        Debe aparecer una sola vez en el resultado.
        """
        gen_j = (j for j in [])
        gen_jh = (jh for jh in JH_BASE)
        resultado = list(habitats_de_interes(gen_j, gen_jh))
        self.assertEqual(resultado.count(2), 1)

    @timeout(N_SECOND_BASE)
    def test_cierre_parcial_resultado_ordenado(self):
        """
        J1, J2, J3 presentes: H1 cerrado, H2 cerrado, H3 cerrado.
        Quedan H4 y H5 de interes, en orden ascendente.
        """
        gen_j = (juguete(i) for i in [1, 2, 3])
        gen_jh = (jh for jh in JH_BASE)
        self.assertEqual(list(habitats_de_interes(gen_j, gen_jh)), [4, 5])

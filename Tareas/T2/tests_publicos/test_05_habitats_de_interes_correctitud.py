from tests_publicos.test_tools import IICTest, timeout, assert_es_generador, indexes_of
from backend.consultas import habitats_de_interes
from utils import Juguete, JugueteHabitat

N_SECOND = 0.3

# Hábitat 10: necesita juguetes {1, 2}
# Hábitat 11: necesita juguetes {3}
# Hábitat 12: necesita juguetes {4}
# Hábitat 13: necesita juguetes {5} 
# Hábitat 14: necesita juguetes {1, 3}
JH_BASE = [
    JugueteHabitat(1, 10, "01:00", (1,)),
    JugueteHabitat(2, 10, "02:00", (1,)),
    JugueteHabitat(3, 11, "00:30", (1,)),
    JugueteHabitat(4, 12, "00:30", (1,)),
    JugueteHabitat(5, 13, "00:30", (1,)),
    JugueteHabitat(1, 14, "00:30", (1,)),
    JugueteHabitat(3, 14, "00:30", (2,)),
]


def juguete(id_j: int) -> Juguete:
    return Juguete(id_j, f"J{id_j}", (1,), f"{id_j:03d}")


class TestHabitatsDeInteres(IICTest):
    """
    Pruebas para habitats_de_interes(generador_juguete, generador_juguete_habitat).
    Un hábitat es de interés si aún falta al menos un juguete asociado por aparecer.
    """

    @timeout(N_SECOND)
    def test_retorna_generador(self):
        """
        La función debe retornar un generador lazy.
        """
        assert_es_generador(self, habitats_de_interes)

    @timeout(N_SECOND)
    def test_ningún_juguete_en_refugio(self):
        """
        Sin juguetes en el refugio → todos los hábitats con al menos un juguete
        asociado son de interés.
        """
        gen_j  = (juguete for juguete in [])
        gen_jh = (juguete_habitat for juguete_habitat in JH_BASE)
        *items, largo = indexes_of(habitats_de_interes(gen_j, gen_jh), [0, 1, 2, -1])
        self.assertEqual(largo, 5)
        self.assertEqual(items[0], 10)
        self.assertEqual(items[1], 11)
        self.assertEqual(items[2], 12)
        self.assertNotIn(items[3], (10, 11, 12))  

    @timeout(N_SECOND)
    def test_habitat_con_todos_los_juguetes_presentes(self):
        """
        Hábitat cuyos juguetes asociados están todos en el refugio → no es de interés.
        El hábitat que aún le falta algún juguete sí es de interés.
        """
        gen_j  = (juguete for juguete in [juguete(i) for i in [1, 2, 3]])
        gen_jh = (juguete_habitat for juguete_habitat in JH_BASE)
        *items, largo = indexes_of(habitats_de_interes(gen_j, gen_jh), [0, 1])
        self.assertEqual(largo, 2)
        self.assertEqual(items[0], 12)
        self.assertEqual(items[1], 13)

    @timeout(N_SECOND)
    def test_juguete_en_refugio_sin_habitat_asociado(self):
        """
        Juguete en el refugio que no aparece en JugueteHabitat → no afecta el interés
        de ningún hábitat.
        """
        gen_j  = (juguete for juguete in [juguete(99)])
        gen_jh = (juguete_habitat for juguete_habitat in JH_BASE)
        *items, largo = indexes_of(habitats_de_interes(gen_j, gen_jh), [0, 1, 2, 3, 4])
        self.assertEqual(largo, 5)
        self.assertEqual(items[0], 10)
        self.assertEqual(items[1], 11)
        self.assertEqual(items[2], 12)
        self.assertEqual(items[3], 13)
        self.assertEqual(items[4], 14)


    @timeout(N_SECOND)
    def test_todos_los_habitats_completos(self):
        """
        Todos los juguetes de todos los hábitats están en el refugio → generador vacío.
        """
        gen_j  = (juguete for juguete in [juguete(i) for i in [1, 2, 3, 4, 5]])
        gen_jh = (juguete_habitat for juguete_habitat in JH_BASE)
        *items, largo = indexes_of(habitats_de_interes(gen_j, gen_jh), [])
        self.assertEqual(largo, 0)

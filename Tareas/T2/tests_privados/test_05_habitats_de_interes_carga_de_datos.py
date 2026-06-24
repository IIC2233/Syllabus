import os
from tests_privados.test_tools import IICTest, timeout, indexes_of
from backend.consultas import habitats_de_interes, cargar_juguete, cargar_juguete_habitat

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


def primeros_juguetes(path: str, max_id: int):
    for juguete in cargar_juguete(path):
        if juguete.id_juguete <= max_id:
            yield juguete


class TestHabitatsDeInteresCargaDatosPrivado(IICTest):
    """
    Verifica habitats_de_interes cargando juguete y juguete_habitat desde datasets privados
    S, M, L y XL. Cubre los casos: todos presentes, ninguno presente y presencia parcial.
    """

    @timeout(N_SECOND)
    def test_S_con_todos(self):
        """
        Dataset S, todos los juguetes presentes: ningun habitat queda de interes;
        retorna generador vacio.
        """
        gen_j = cargar_juguete(os.path.join(PATH_S, "juguetes.csv"))
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        *items, largo = indexes_of(habitats_de_interes(gen_j, gen_jh), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_S_sin_ninguno(self):
        """
        Dataset S, ningun juguete presente: los 50 habitats son de interes (ids 1 a 50).
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        resultado = habitats_de_interes((j for j in []), gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 50)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 50)

    @timeout(N_SECOND)
    def test_S_parcial(self):
        """
        Dataset S, juguetes 1 a 12 presentes: quedan 46 habitats de interes (ids 1 a 50).
        """
        gen_j = primeros_juguetes(os.path.join(PATH_S, "juguetes.csv"), 12)
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv"))
        resultado = habitats_de_interes(gen_j, gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 46)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 50)

    @timeout(N_SECOND)
    def test_M_sin_ninguno(self):
        """
        Dataset M, ningun juguete presente: los 200 habitats son de interes (ids 1 a 200).
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_M, "juguete_habitat.csv"))
        resultado = habitats_de_interes((j for j in []), gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 200)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 200)

    @timeout(N_SECOND)
    def test_M_parcial(self):
        """
        Dataset M, juguetes 1 a 12 presentes: quedan 192 habitats de interes (ids 1 a 200).
        """
        gen_j = primeros_juguetes(os.path.join(PATH_M, "juguetes.csv"), 12)
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_M, "juguete_habitat.csv"))
        resultado = habitats_de_interes(gen_j, gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 192)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 200)

    @timeout(N_SECOND)
    def test_L_con_todos(self):
        """
        Dataset L, todos los juguetes presentes: ningun habitat queda de interes;
        retorna generador vacio.
        """
        gen_j = cargar_juguete(os.path.join(PATH_L, "juguetes.csv"))
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_L, "juguete_habitat.csv"))
        *items, largo = indexes_of(habitats_de_interes(gen_j, gen_jh), [])
        self.assertEqual(largo, 0)

    @timeout(N_SECOND)
    def test_L_sin_ninguno(self):
        """
        Dataset L, ningun juguete presente: los 1000 habitats son de interes (ids 1 a 1000).
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_L, "juguete_habitat.csv"))
        resultado = habitats_de_interes((j for j in []), gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 1000)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 1000)

    @timeout(N_SECOND)
    def test_L_parcial(self):
        """
        Dataset L, juguetes 1 a 12 presentes: quedan 976 habitats de interes (ids 1 a 1000).
        """
        gen_j = primeros_juguetes(os.path.join(PATH_L, "juguetes.csv"), 12)
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_L, "juguete_habitat.csv"))
        resultado = habitats_de_interes(gen_j, gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 976)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 1000)

    @timeout(N_SECOND)
    def test_XL_sin_ninguno(self):
        """
        Dataset XL, ningun juguete presente: los 2500 habitats son de interes (ids 1 a 2500).
        Verifica deduplicacion de habitats que aparecen multiples veces en juguete_habitat.
        """
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_XL, "juguete_habitat.csv"))
        resultado = habitats_de_interes((j for j in []), gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 2500)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 2500)

    @timeout(N_SECOND)
    def test_XL_parcial(self):
        """
        Dataset XL, juguetes 1 a 100 presentes: quedan 2222 habitats de interes
        (del id 2 al 2500); verifica deduplicacion y orden ascendente.
        """
        gen_j = primeros_juguetes(os.path.join(PATH_XL, "juguetes.csv"), 100)
        gen_jh = cargar_juguete_habitat(os.path.join(PATH_XL, "juguete_habitat.csv"))
        resultado = habitats_de_interes(gen_j, gen_jh)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 2222)
        self.assertEqual(items[0], 2)
        self.assertEqual(items[1], 2500)

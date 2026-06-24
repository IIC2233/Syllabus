import os

from tests_privados.test_tools import IICTest, timeout, indexes_of
from backend.consultas import (
    habitat_eventualmente_creables,
    cargar_juguete,
    cargar_juguete_recurso,
    cargar_recurso_recurso,
    cargar_objeto_recurso,
    cargar_habitat_objeto,
)

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


def cargar_resultado(path: str):
    gen_j = cargar_juguete(os.path.join(path, "juguetes.csv"))
    gen_jr = cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv"))
    gen_rr = cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv"))
    gen_or = cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv"))
    gen_ho = cargar_habitat_objeto(os.path.join(path, "habitat_objeto.csv"))
    return habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho)


def cargar_resultado_con_juguetes_filtrados(path: str, max_id_juguete: int):
    gen_j = (
        j for j in cargar_juguete(os.path.join(path, "juguetes.csv"))
        if j.id_juguete <= max_id_juguete
    )
    gen_jr = cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv"))
    gen_rr = cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv"))
    gen_or = cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv"))
    gen_ho = cargar_habitat_objeto(os.path.join(path, "habitat_objeto.csv"))
    return habitat_eventualmente_creables(gen_j, gen_jr, gen_rr, gen_or, gen_ho)


class TestHabitatEventualmenteCreablesCargaDatosPrivado(IICTest):
    """
    Verifica habitat_eventualmente_creables con datasets privados S, M, L y XL.
    Comprueba el rango completo de habitats creables y el efecto de reducir los juguetes
    presentes sobre cuantos habitats son alcanzables.
    """

    @timeout(N_SECOND)
    def test_S(self):
        """
        S privado: todos los habitats 1..50 son eventualmente creables.
        """
        resultado = cargar_resultado(PATH_S)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 50)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 50)

    @timeout(N_SECOND)
    def test_M(self):
        """
        M privado: todos los habitats 1..200 son eventualmente creables.
        """
        resultado = cargar_resultado(PATH_M)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 200)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 200)

    @timeout(N_SECOND)
    def test_L(self):
        """
        L privado: todos los habitats 1..1000 son eventualmente creables.
        """
        resultado = cargar_resultado(PATH_L)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 1000)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 1000)

    @timeout(N_SECOND)
    def test_XL_todos(self):
        """
        XL privado con todos los juguetes: los 2500 habitats son eventualmente creables.
        Cubre cadenas recursivas de recursos en un dataset grande.
        """
        resultado = cargar_resultado(PATH_XL)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 2500)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 2500)

    @timeout(N_SECOND)
    def test_XL_juguetes_filtrados(self):
        """
        XL privado con juguetes id <= 50: solo 97 habitats son eventualmente creables.
        Debe descartar habitats que dependen de juguetes ausentes.
        """
        resultado = cargar_resultado_con_juguetes_filtrados(PATH_XL, 50)
        *items, largo = indexes_of(resultado, [0, -1])
        self.assertEqual(largo, 97)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 2472)


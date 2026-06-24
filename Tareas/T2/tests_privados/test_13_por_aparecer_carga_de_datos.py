import os

from tests_privados.test_tools import IICTest, timeout
from backend.consultas import (
    cargar_juguete,
    cargar_juguete_habitat,
    cargar_periodo_dia,
    por_aparecer,
)
from backend.nodo_ligado import NodoLigado

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


def cadena_habitats(pares):
    cabeza = None
    for id_habitat, tiempo_presente in sorted(pares):
        nodo = NodoLigado(id=id_habitat, tiempo_presente=tiempo_presente)
        cabeza = nodo if cabeza is None else cabeza.insertar(nodo)
    return cabeza


def ejecutar(path, habitats, momento_dia, presentes=None, max_presente=None):
    gen_juguete = cargar_juguete(os.path.join(path, "juguetes.csv"))
    if presentes is not None:
        presentes = set(presentes)
        gen_juguete = (j for j in gen_juguete if j.id_juguete in presentes)
    elif max_presente is not None:
        gen_juguete = (j for j in gen_juguete if j.id_juguete <= max_presente)

    habitat = None if habitats is None else cadena_habitats(habitats)
    gen_jh = cargar_juguete_habitat(os.path.join(path, "juguete_habitat.csv"))
    gen_pd = cargar_periodo_dia(os.path.join(path, "periodo_dia.csv"))
    return list(por_aparecer(gen_juguete, habitat, gen_jh, gen_pd, momento_dia))


class TestPorAparecerCargaDatosPrivado(IICTest):
    """
    Verifica por_aparecer con datasets privados S, M, L y XL.
    Comprueba juguetes presentes, tiempo_presente por habitat, posiciones None
    y eficiencia sobre datos reales.
    """

    @timeout(N_SECOND)
    def test_S_habitats_sin_presentes(self):
        """
        Dataset S sin juguetes presentes: los tres habitats consultados atraen su
        primer juguete disponible.
        """
        resultado = ejecutar(PATH_S, [(1, 0), (2, 0), (10, 0)], 0, presentes=())

        self.assertEqual(resultado, [1, 3, 11])

    @timeout(N_SECOND)
    def test_S_presentes_y_tiempo_presente(self):
        """
        Dataset S con J1 y J11 ya presentes: los habitats deben escoger otros
        juguetes y respetar su tiempo_presente.
        """
        resultado = ejecutar(PATH_S, [(1, 1), (2, 2), (10, 20)], 20, presentes=(1, 11))

        self.assertEqual(resultado, [2, 3, 14])

    @timeout(N_SECOND)
    def test_S_habitat_none_real(self):
        """
        Dataset S con Habitat=None: no hay posiciones de habitat que reportar.
        """
        resultado = ejecutar(PATH_S, None, 0, presentes=())

        self.assertEqual(resultado, [])

    @timeout(N_SECOND)
    def test_M_multiples_habitats_reales(self):
        """
        Dataset M con varios habitats y juguetes de id bajo ya presentes.
        """
        resultado = ejecutar(
            PATH_M,
            [(1, 0), (2, 0), (50, 0), (90, 0)],
            30,
            max_presente=75,
        )

        self.assertEqual(resultado, [104, 77, 85, 130])

    @timeout(N_SECOND)
    def test_L_resultado_con_none_intermedio(self):
        """
        Dataset L con tiempo_presente=0 en todos los habitats: todos atraen su
        juguete disponible (sin posiciones None).
        """
        resultado = ejecutar(
            PATH_L,
            [(1, 0), (10, 0), (161, 0), (300, 0)],
            100,
            max_presente=250,
        )

        self.assertEqual(resultado, [315, 498, 297, 490])

    @timeout(N_SECOND)
    def test_XL_eficiencia_con_periodos(self):
        """
        Dataset XL con 8 habitats dispersos, momento_dia=100 y juguetes con id<=500
        ya presentes. Verifica eficiencia con el dataset mas grande y que el calculo
        de periodos funcione correctamente con datos reales.
        """
        resultado = ejecutar(
            PATH_XL,
            [(1, 0), (10, 0), (161, 0), (200, 0), (300, 0), (500, 0), (600, 0), (700, 0)],
            100,
            max_presente=500,
        )

        self.assertEqual(resultado, [None, None, 751, 778, 573, 692, 558, None])

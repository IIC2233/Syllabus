import os

from tests_privados.test_tools import IICTest, timeout
from backend.consultas import (
    simular,
    cargar_juguete,
    cargar_juguete_habitat,
    cargar_habitat_objeto,
    cargar_objeto_recurso,
    cargar_recurso_recurso,
    cargar_juguete_recurso,
    cargar_juguete_objeto,
    cargar_periodo_dia,
)

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


def crear_simulacion(path: str):
    simulacion = simular(
        cargar_juguete(os.path.join(path, "juguetes.csv")),
        cargar_juguete_habitat(os.path.join(path, "juguete_habitat.csv")),
        cargar_habitat_objeto(os.path.join(path, "habitat_objeto.csv")),
        cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv")),
        cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv")),
        cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv")),
        cargar_juguete_objeto(os.path.join(path, "juguete_objeto.csv")),
        cargar_periodo_dia(os.path.join(path, "periodo_dia.csv")),
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
    return tuple(resultado)


class TestSimularCargaDatosPrivado(IICTest):
    """
    Verifica simular con datasets privados S, M, L y XL.
    """

    def verificar_primeros_eventos(self, path: str):
        simulacion = crear_simulacion(path)

        primer_batch = compactar(simulacion.send("next"))
        segundo_batch = compactar(simulacion.send("next"))

        self.assertEqual(primer_batch, ((0, "habitat", 1),))
        self.assertEqual(segundo_batch, ((1, "habitat", 1),))

    @timeout(N_SECOND)
    def test_S(self):
        """
        S privado: primeros eventos deterministas.
        """
        self.verificar_primeros_eventos(PATH_S)

    @timeout(N_SECOND)
    def test_M(self):
        """
        M privado: primeros eventos deterministas.
        """
        self.verificar_primeros_eventos(PATH_M)

    @timeout(N_SECOND)
    def test_L(self):
        """
        L privado: primeros eventos deterministas.
        """
        self.verificar_primeros_eventos(PATH_L)

    @timeout(N_SECOND)
    def test_XL(self):
        """
        XL privado: primeros eventos deterministas.
        """
        self.verificar_primeros_eventos(PATH_XL)

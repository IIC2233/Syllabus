import os

from tests_privados.test_tools import IICTest, timeout
from backend.consultas import (
    juguetes_autosuficientes,
    cargar_juguete,
    cargar_juguete_objeto,
    cargar_objeto_recurso,
    cargar_juguete_recurso,
    cargar_recurso_recurso,
)

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")

JUGUETES_AUTOSUFICIENTES_S = [1, 4, 6, 20, 26, 39, 47]
JUGUETES_AUTOSUFICIENTES_M = [1, 4, 6]
JUGUETES_AUTOSUFICIENTES_L = [1, 4, 6]
JUGUETES_AUTOSUFICIENTES_XL = [1, 4, 6, 541]


def cargar_resultado(path: str):
    gen_j = cargar_juguete(os.path.join(path, "juguetes.csv"))
    gen_jo = cargar_juguete_objeto(os.path.join(path, "juguete_objeto.csv"))
    gen_or = cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv"))
    gen_jr = cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv"))
    gen_rr = cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv"))
    return juguetes_autosuficientes(gen_j, gen_jo, gen_or, gen_jr, gen_rr)


class TestJuguetesAutosuficientesCargaDatosPrivado(IICTest):
    """
    Verifica juguetes_autosuficientes con datasets privados S, M, L y XL.
    Comprueba resultado completo cruzando los cinco generadores requeridos.
    """

    @timeout(N_SECOND)
    def test_S(self):
        """
        Dataset S: 7 juguetes autosuficientes (J1, J4, J6, J20, J26, J39, J47);
        verifica lista completa en orden ascendente.
        """
        self.assertEqual(list(cargar_resultado(PATH_S)), JUGUETES_AUTOSUFICIENTES_S)

    @timeout(N_SECOND)
    def test_M(self):
        """
        Dataset M: 3 juguetes autosuficientes (J1, J4, J6); verifica lista completa.
        """
        self.assertEqual(list(cargar_resultado(PATH_M)), JUGUETES_AUTOSUFICIENTES_M)

    @timeout(N_SECOND)
    def test_L(self):
        """
        Dataset L: mismos 3 autosuficientes que M (J1, J4, J6) con dataset mas grande;
        verifica que el resultado no crece al escalar los datos.
        """
        self.assertEqual(list(cargar_resultado(PATH_L)), JUGUETES_AUTOSUFICIENTES_L)

    @timeout(N_SECOND)
    def test_XL(self):
        """
        Dataset XL: 4 juguetes autosuficientes (J1, J4, J6, J541); J541 aparece en XL
        pero no en M ni L, verificando que se detectan nuevos autosuficientes al escalar.
        """
        self.assertEqual(list(cargar_resultado(PATH_XL)), JUGUETES_AUTOSUFICIENTES_XL)


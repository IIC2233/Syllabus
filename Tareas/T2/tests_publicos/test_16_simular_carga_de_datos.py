import inspect
import os
from tests_publicos.test_tools import IICTest, timeout
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

N_SEGUNDOS = 5.0

PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")
PATH_XL = os.path.join("data", "XL")


def _crear_simulacion(path):
    sim = simular(
        cargar_juguete(os.path.join(path, "juguetes.csv")),
        cargar_juguete_habitat(os.path.join(path, "juguete_habitat.csv")),
        cargar_habitat_objeto(os.path.join(path, "habitat_objeto.csv")),
        cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv")),
        cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv")),
        cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv")),
        cargar_juguete_objeto(os.path.join(path, "juguete_objeto.csv")),
        cargar_periodo_dia(os.path.join(path, "periodo_dia.csv")),
    )
    next(sim)
    return sim


class TestSimularXL(IICTest):

    @timeout(N_SEGUNDOS/2)
    def test_S(self):
        sim = _crear_simulacion(PATH_S)
        
        sim.send("next")
        evento1 = tuple(sim.send("next"))
        for _ in range(5):
            sim.send("next")
        evento2 = tuple(sim.send("next"))

        self.assertEqual((evento1[0][0], evento2[0][0]), ((18), (68)))

    @timeout(N_SEGUNDOS/2)
    def test_M(self):
        sim = _crear_simulacion(PATH_M)
        sim.send("next")
        evento1 = tuple(sim.send("next"))
        for _ in range(4):
            sim.send("next")
        evento2 = tuple(sim.send("next"))
        for _ in range(3):
            sim.send("next")
        evento3 = tuple(sim.send("next"))

        self.assertEqual((evento1[0][0], evento2[0][0], evento3[0][0]), ((1), (39), (43)))


    @timeout(N_SEGUNDOS)
    def test_L(self):
        sim = _crear_simulacion(PATH_L)

        evento1 = tuple(sim.send("next"))
        evento2 = tuple(sim.send("next"))
        for _ in range(1):
            sim.send("next")
        evento3 = tuple(sim.send("next"))

        self.assertEqual((evento1[0][0], evento2[0][0], evento3[0][0]), ((0), (1), (238)))

    @timeout(N_SEGUNDOS)
    def test_XL(self):
        sim = _crear_simulacion(PATH_XL)

        evento1 = tuple(sim.send("next"))
        evento2 = tuple(sim.send("next"))
        evento3 = tuple(next(sim))

        self.assertEqual((evento1[0][0], evento2[0][0]), ((0), (1)))
        self.assertEqual(evento3, tuple())

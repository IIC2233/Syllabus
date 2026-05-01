import os
from tests_publicos.test_tools import IICTest, timeout
from tests_publicos.solution.test_10 import (AVANZAR_PROD_S_0, AVANZAR_PROD_S_0_PRODUCTORES, 
                                             AVANZAR_PROD_S_1, AVANZAR_PROD_S_1_PRODUCTORES,
                                             AVANZAR_PROD_S_1_MINUTOS,
                                             AVANZAR_PROD_M_0, AVANZAR_PROD_M_0_PRODUCTORES,
                                             AVANZAR_PROD_M_0_MINUTOS,
                                             AVANZAR_PROD_L_0, AVANZAR_PROD_L_0_PRODUCTORES,
                                             AVANZAR_PROD_L_0_MINUTOS)
from backend.consultas import avanzar_produccion, cargar_juguete_recurso, cargar_juguete_objeto
from backend.nodo_ligado import NodoLigado

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")

def make_nodo_productor_ids(ids_con_tiempo):
    """
    Construye cadena de NodoLigado de JugueteProductor desde pares (id, tiempo_actual).
    """
    cabeza = None
    for id_j, t in sorted(ids_con_tiempo, key=lambda x: x[0]):
        nodo = NodoLigado(id=id_j, tiempo_actual=t)
        if cabeza is None:
            cabeza = nodo
        else:
            cabeza = cabeza.insertar(nodo)
    return cabeza

class TestAvanzarProduccionCargaDatos(IICTest):
    """
    Verifica avanzar_produccion cargando juguete_recurso y juguete_objeto
    desde S, M y L con distintas configuraciones de JugueteProductor.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_0(self):
        """
        S — Avanzar 1 minuto con juguetes en distintos estados de producción.
        """
        jr_gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        jo_gen = cargar_juguete_objeto(os.path.join(PATH_S, "juguete_objeto.csv"))
        productor = make_nodo_productor_ids(AVANZAR_PROD_S_0_PRODUCTORES)
        resultado = list(avanzar_produccion(jr_gen, jo_gen, productor, set(), minutos=1))
        self.assertCountEqual(resultado, AVANZAR_PROD_S_0)

    @timeout(N_SECOND)
    def test_1(self):
        """
        S — Avanzar varios minutos: múltiples ciclos completados.
        """
        jr_gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        jo_gen = cargar_juguete_objeto(os.path.join(PATH_S, "juguete_objeto.csv"))
        productor = make_nodo_productor_ids(AVANZAR_PROD_S_1_PRODUCTORES)
        resultado = list(avanzar_produccion(jr_gen, jo_gen, productor, set(),
                                            minutos=AVANZAR_PROD_S_1_MINUTOS))
        self.assertCountEqual(resultado, AVANZAR_PROD_S_1)

    @timeout(N_SECOND)
    def test_2(self):
        """
        S — JugueteProductor=None retorna vacío.
        """
        jr_gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        jo_gen = cargar_juguete_objeto(os.path.join(PATH_S, "juguete_objeto.csv"))
        resultado = list(avanzar_produccion(jr_gen, jo_gen, None, set(), minutos=10))
        self.assertEqual(resultado, [])

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_3(self):
        """
        M — Avanzar minutos con varios juguetes productores.
        """
        jr_gen = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        jo_gen = cargar_juguete_objeto(os.path.join(PATH_M, "juguete_objeto.csv"))
        productor = make_nodo_productor_ids(AVANZAR_PROD_M_0_PRODUCTORES)
        resultado = list(avanzar_produccion(jr_gen, jo_gen, productor, set(),
                                            minutos=AVANZAR_PROD_M_0_MINUTOS))
        self.assertCountEqual(resultado, AVANZAR_PROD_M_0)

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_4(self):
        """
        L — Dataset grande, verificar eficiencia y correctitud.
        """
        jr_gen = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        jo_gen = cargar_juguete_objeto(os.path.join(PATH_L, "juguete_objeto.csv"))
        productor = make_nodo_productor_ids(AVANZAR_PROD_L_0_PRODUCTORES)
        resultado = list(avanzar_produccion(jr_gen, jo_gen, productor, set(),
                                            minutos=AVANZAR_PROD_L_0_MINUTOS))
        self.assertCountEqual(resultado, AVANZAR_PROD_L_0)

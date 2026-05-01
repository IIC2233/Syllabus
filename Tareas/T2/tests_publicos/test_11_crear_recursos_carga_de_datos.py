import os
from tests_publicos.test_tools import IICTest, timeout
from tests_publicos.solution.test_11 import (CREAR_RECURSOS_S_0_JUGUETES, 
                                             CREAR_RECURSOS_S_0_MINUTOS, CREAR_RECURSOS_S_0,
                                            CREAR_RECURSOS_S_1_JUGUETES, 
                                            CREAR_RECURSOS_S_1_MINUTOS, 
                                            CREAR_RECURSOS_S_1_IDS_ESPERADOS,
                                            CREAR_RECURSOS_M_0_JUGUETES, 
                                            CREAR_RECURSOS_M_0_SET_OBJETOS, 
                                            CREAR_RECURSOS_M_0_MINUTOS,
                                            CREAR_RECURSOS_M_0,
                                            CREAR_RECURSOS_L_0_JUGUETES, 
                                            CREAR_RECURSOS_L_0_MINUTOS, CREAR_RECURSOS_L_0)
from backend.consultas import crear_recursos, cargar_juguete_recurso, cargar_juguete_objeto

N_SECOND = 2.0
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


class TestCrearRecursosCargaDatos(IICTest):
    """
    Verifica crear_recursos cargando juguete_recurso y juguete_objeto
    desde S, M y L, ejercitando distintos tipos de send.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_0(self):
        """
        S — Agregar juguetes y avanzar tiempo, verificar recursos producidos.
        """
        jr_gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        jo_gen = cargar_juguete_objeto(os.path.join(PATH_S, "juguete_objeto.csv"))
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        for juguete in CREAR_RECURSOS_S_0_JUGUETES:
            gen.send(juguete)
        resultado = gen.send(CREAR_RECURSOS_S_0_MINUTOS)
        self.assertCountEqual(resultado, CREAR_RECURSOS_S_0)

    @timeout(N_SECOND)
    def test_1(self):
        """
        S — Verificar estado final con 'end' tras varios sends.
        """
        jr_gen = cargar_juguete_recurso(os.path.join(PATH_S, "juguete_recurso.csv"))
        jo_gen = cargar_juguete_objeto(os.path.join(PATH_S, "juguete_objeto.csv"))
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        for juguete in CREAR_RECURSOS_S_1_JUGUETES:
            gen.send(juguete)
        gen.send(CREAR_RECURSOS_S_1_MINUTOS)
        resultado = gen.send("end")
        cadena, set_objs = resultado
        self.assertIsInstance(set_objs, set)
        # Verificar ids de juguetes en cadena
        ids_en_cadena = set()
        nodo = cadena
        while nodo is not None:
            ids_en_cadena.add(nodo.id)
            nodo = nodo.siguiente
        self.assertCountEqual(ids_en_cadena, CREAR_RECURSOS_S_1_IDS_ESPERADOS)

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_3(self):
        """
        M — Agregar juguetes, set de objetos y avanzar tiempo.
        """
        jr_gen = cargar_juguete_recurso(os.path.join(PATH_M, "juguete_recurso.csv"))
        jo_gen = cargar_juguete_objeto(os.path.join(PATH_M, "juguete_objeto.csv"))
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        for juguete in CREAR_RECURSOS_M_0_JUGUETES:
            gen.send(juguete)
        gen.send(CREAR_RECURSOS_M_0_SET_OBJETOS)
        resultado = gen.send(CREAR_RECURSOS_M_0_MINUTOS)
        self.assertCountEqual(resultado, CREAR_RECURSOS_M_0)

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_4(self):
        """
        L — Dataset grande, verificar eficiencia con muchos juguetes.
        """
        jr_gen = cargar_juguete_recurso(os.path.join(PATH_L, "juguete_recurso.csv"))
        jo_gen = cargar_juguete_objeto(os.path.join(PATH_L, "juguete_objeto.csv"))
        gen = crear_recursos(jr_gen, jo_gen)
        next(gen)
        for juguete in CREAR_RECURSOS_L_0_JUGUETES:
            gen.send(juguete)
        resultado = gen.send(CREAR_RECURSOS_L_0_MINUTOS)
        self.assertCountEqual(resultado, CREAR_RECURSOS_L_0)

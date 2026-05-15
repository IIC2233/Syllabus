import os
from tests_publicos.test_tools import IICTest, timeout, assert_es_generador
from tests_publicos.solution.test_15 import (MANEJO_HAB_S_0_RECURSOS,
                                             MANEJO_HAB_S_0_IDS_CREADOS,
                                             MANEJO_HAB_S_1_RECURSOS,
                                             MANEJO_HAB_S_1_TIEMPO_INICIAL,
                                             MANEJO_HAB_S_1_PASOS,
                                             MANEJO_HAB_S_1_TIEMPO_ACTUAL,
                                             MANEJO_HAB_S_1_JUGUETES_ESPERADOS,
                                             MANEJO_HAB_S_1_HABITATS,
                                             MANEJO_HAB_S_1_OBJETOS,
                                             MANEJO_HAB_S_1_RECURSOS_ESPERADOS,
                                             MANEJO_HAB_M_0_RECURSOS,
                                             MANEJO_HAB_M_0_IDS_CREADOS,
                                             MANEJO_HAB_L_0_RECURSOS,
                                             MANEJO_HAB_L_0_PASOS,
                                             MANEJO_HAB_L_0_TIEMPO_ACTUAL,
                                             MANEJO_HAB_L_0_JUGUETES_ESPERADOS,
                                             MANEJO_HAB_L_0_HABITATS,
                                             MANEJO_HAB_L_0_OBJETOS,
                                             MANEJO_HAB_L_0_RECURSOS_ESPERADOS)
from backend.consultas import (manejo_habitat, cargar_juguete, cargar_juguete_habitat,
                                cargar_habitat_objeto, cargar_objeto_recurso,
                                cargar_recurso_recurso, cargar_juguete_recurso,
                                cargar_juguete_objeto, cargar_periodo_dia)

N_SECOND = 5.0
PATH_S = os.path.join("data", "S")
PATH_M = os.path.join("data", "M")
PATH_L = os.path.join("data", "L")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _make_gen_from_path(path, tiempo_inicial=0):
    return manejo_habitat(
        cargar_juguete(os.path.join(path, "juguetes.csv")),
        cargar_juguete_habitat(os.path.join(path, "juguete_habitat.csv")),
        cargar_habitat_objeto(os.path.join(path, "habitat_objeto.csv")),
        cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv")),
        cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv")),
        cargar_periodo_dia(os.path.join(path, "periodo_dia.csv")),
        tiempo_inicial,
    )


def _recorrer_cadena(cabeza):
    nodo = cabeza
    while nodo is not None:
        yield nodo
        nodo = nodo.siguiente


def _obtener_ids_recursos(path):
    objeto_recursos = list(cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv")))
    recurso_recurso = list(cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv")))
    juguete_recurso = list(cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv")))

    return sorted({
        id_recurso
        for objeto_recurso in objeto_recursos
        for id_recurso, _ in objeto_recurso.recursos
    } | {
        rr.id_recurso
        for rr in recurso_recurso
    } | {
        id_recurso
        for rr in recurso_recurso
        for id_recurso, _ in rr.recursos
    } | {
        jr.id_recurso
        for jr in juguete_recurso
    })


def _es_nodo_o_none(cadena):
    return cadena is None or hasattr(cadena, "siguiente")


def _crear_simulador_s():
    return manejo_habitat(
        cargar_juguete(os.path.join(PATH_S, "juguetes.csv")),
        cargar_juguete_habitat(os.path.join(PATH_S, "juguete_habitat.csv")),
        cargar_habitat_objeto(os.path.join(PATH_S, "habitat_objeto.csv")),
        cargar_objeto_recurso(os.path.join(PATH_S, "objeto_recurso.csv")),
        cargar_recurso_recurso(os.path.join(PATH_S, "recurso_recurso.csv")),
        cargar_periodo_dia(os.path.join(PATH_S, "periodo_dia.csv")),
    )


# ── Tests ─────────────────────────────────────────────────────────────────────

class TestManejoHabitatCargaDatos(IICTest):
    """
    Verifica manejo_habitat cargando datos reales desde S, M y L.
    """

    # ── S ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_0(self):
        """
        S — Agregar recursos y llamar 'crear': verificar hábitats creados.
        """
        gen = _make_gen_from_path(PATH_S)
        next(gen)
        gen.send(MANEJO_HAB_S_0_RECURSOS)
        _, ids_creados = gen.send("crear")
        self.assertCountEqual(ids_creados, MANEJO_HAB_S_0_IDS_CREADOS)

    @timeout(N_SECOND)
    def test_1(self):
        """
        S — Verificar report tras pasos y crear.
        """
        gen = _make_gen_from_path(PATH_S, tiempo_inicial=MANEJO_HAB_S_1_TIEMPO_INICIAL)
        next(gen)
        gen.send(MANEJO_HAB_S_1_RECURSOS)
        gen.send("crear")
        for _ in range(MANEJO_HAB_S_1_PASOS):
            gen.send(None)
        tiempo, juguetes, habitats, objetos, recursos = gen.send("report")

        habitats_ids = [h.id for h in _recorrer_cadena(habitats)]
        objetos_ids  = [o.id for o in _recorrer_cadena(objetos)]
        recursos_ids = [r.id for r in _recorrer_cadena(recursos)]

        self.assertEqual(tiempo, MANEJO_HAB_S_1_TIEMPO_ACTUAL)
        self.assertCountEqual(juguetes, MANEJO_HAB_S_1_JUGUETES_ESPERADOS)
        self.assertCountEqual(habitats_ids, MANEJO_HAB_S_1_HABITATS)
        self.assertCountEqual(objetos_ids, MANEJO_HAB_S_1_OBJETOS)
        self.assertCountEqual(recursos_ids, MANEJO_HAB_S_1_RECURSOS_ESPERADOS)

    @timeout(N_SECOND)
    def test_7(self):
        """
        S — Cargar recursos 0-20 y verificar que 'crear' encuentre hábitats.
        """
        gen = _crear_simulador_s()
        next(gen)
        self.assertIsNone(gen.send(tuple((i, 100) for i in range(21))))
        obj_usados, habs_creados = gen.send("crear")
        self.assertGreater(len(obj_usados), 0)
        self.assertGreater(len(habs_creados), 0)

    # ── M ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_2(self):
        """
        M — Crear hábitats con inventario parcial.
        """
        gen = _make_gen_from_path(PATH_M)
        next(gen)
        gen.send(MANEJO_HAB_M_0_RECURSOS)
        _, ids_creados = gen.send("crear")
        self.assertCountEqual(ids_creados, MANEJO_HAB_M_0_IDS_CREADOS)

    @timeout(N_SECOND)
    def test_4(self):
        """
        M — Con recursos suficientes, 'crear' debe fabricar objetos y hábitats.
        """
        ids_recursos = _obtener_ids_recursos(PATH_M)
        gen = _make_gen_from_path(PATH_M)
        next(gen)
        self.assertIsNone(gen.send(tuple((id_recurso, 100) for id_recurso in ids_recursos)))

        obj_usados, habs_creados = gen.send("crear")
        self.assertGreater(len(obj_usados), 0)
        self.assertGreater(len(habs_creados), 0)

        tiempo, juguetes, habitats, objetos, recursos = gen.send("report")
        cantidades_finales = {nodo.id: nodo.cantidad for nodo in _recorrer_cadena(recursos)}

        self.assertIsInstance(tiempo, int)
        self.assertIsInstance(juguetes, set)
        self.assertTrue(any(cantidades_finales.get(id_recurso, 0) < 100 for id_recurso in ids_recursos))
        self.assertIsNotNone(habitats)
        self.assertIsNotNone(objetos)

    @timeout(N_SECOND)
    def test_5(self):
        """
        M — Al avanzar tiempo, deben aparecer ids de juguetes y actualizarse el tiempo.
        """
        gen = _make_gen_from_path(PATH_M)
        next(gen)
        ids_creados = gen.send(None)
        self.assertIsInstance(ids_creados, tuple)
        self.assertTrue(all(isinstance(id_juguete, int) for id_juguete in ids_creados))

        tiempo, juguetes, _, _, _ = gen.send("report")
        self.assertGreaterEqual(tiempo, 1)
        self.assertEqual(juguetes, set(ids_creados))

    @timeout(N_SECOND)
    def test_6(self):
        """
        M — Enviar una tupla de recursos debe agregarlos a la cadena interna.
        """
        ids_recursos = _obtener_ids_recursos(PATH_M)
        tupla_data_recursos = tuple((id_recurso, 7) for id_recurso in ids_recursos[:3])

        gen = _make_gen_from_path(PATH_M)
        next(gen)
        self.assertIsNone(gen.send(tupla_data_recursos))

        _, _, _, _, recursos = gen.send("report")
        cantidades_finales = {nodo.id: nodo.cantidad for nodo in _recorrer_cadena(recursos)}
        for id_recurso, cantidad in tupla_data_recursos:
            self.assertGreaterEqual(cantidades_finales.get(id_recurso, 0), cantidad)

    @timeout(N_SECOND)
    def test_m_end_retorna_estructura_completa(self):
        """
        M — 'report' debe retornar cinco elementos con tipos esperados:
        tiempo (int), ids de juguetes (set) y tres cadenas NodoLigado o None.
        """
        gen = _make_gen_from_path(PATH_M)
        next(gen)
        retorno = gen.send("report")
        self.assertIsInstance(retorno, tuple)
        self.assertEqual(len(retorno), 5)

        tiempo, ids_juguetes, hab, obj, rec = retorno
        self.assertIsInstance(tiempo, int)
        self.assertIsInstance(ids_juguetes, set)
        self.assertTrue(_es_nodo_o_none(hab))
        self.assertTrue(_es_nodo_o_none(obj))
        self.assertTrue(_es_nodo_o_none(rec))

    # ── L ────────────────────────────────────────────────────────────────

    @timeout(N_SECOND)
    def test_3(self):
        """
        L — Dataset grande, verificar eficiencia del generador.
        """
        gen = _make_gen_from_path(PATH_L)
        next(gen)
        gen.send(MANEJO_HAB_L_0_RECURSOS)
        gen.send("crear")
        for _ in range(MANEJO_HAB_L_0_PASOS):
            gen.send(None)
        tiempo, juguetes, habitats, objetos, recursos = gen.send("report")

        habitats_ids = [h.id for h in _recorrer_cadena(habitats)]
        objetos_ids  = [o.id for o in _recorrer_cadena(objetos)]
        recursos_ids = [r.id for r in _recorrer_cadena(recursos)]

        self.assertEqual(tiempo, MANEJO_HAB_L_0_TIEMPO_ACTUAL)
        self.assertTrue(set(MANEJO_HAB_L_0_JUGUETES_ESPERADOS).issubset(set(juguetes)))
        self.assertCountEqual(habitats_ids, MANEJO_HAB_L_0_HABITATS)
        self.assertCountEqual(objetos_ids, MANEJO_HAB_L_0_OBJETOS)
        self.assertCountEqual(recursos_ids, MANEJO_HAB_L_0_RECURSOS_ESPERADOS)
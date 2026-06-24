import os

from tests_privados.test_tools import IICTest, timeout
from backend.consultas import (
    cargar_habitat_objeto,
    cargar_juguete,
    cargar_juguete_recurso,
    cargar_objeto_recurso,
    cargar_recurso_recurso,
    habitat_creables,
)
from backend.nodo_ligado import NodoLigado

N_SECOND = 5.0
PATH_S = os.path.join("tests_privados", "data", "S")
PATH_M = os.path.join("tests_privados", "data", "M")
PATH_L = os.path.join("tests_privados", "data", "L")
PATH_XL = os.path.join("tests_privados", "data", "XL")


def cadena_recursos(pares):
    cabeza = None
    for id_recurso, cantidad in sorted(pares):
        nodo = NodoLigado(id=id_recurso, cantidad=cantidad)
        cabeza = nodo if cabeza is None else cabeza.insertar(nodo)
    return cabeza


def ejecutar(path, recurso, max_juguete=None):
    gen_juguete = cargar_juguete(os.path.join(path, "juguetes.csv"))
    if max_juguete is not None:
        gen_juguete = (j for j in gen_juguete if j.id_juguete <= max_juguete)

    return list(habitat_creables(
        gen_juguete,
        cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv")),
        cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv")),
        cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv")),
        cargar_habitat_objeto(os.path.join(path, "habitat_objeto.csv")),
        cadena_recursos(recurso),
    ))


def ejecutar_filtrado(path, recurso, max_juguete, max_habitat, max_objeto, max_recurso):
    gen_juguete = (
        juguete
        for juguete in cargar_juguete(os.path.join(path, "juguetes.csv"))
        if juguete.id_juguete <= max_juguete
    )
    gen_juguete_recurso = (
        jr
        for jr in cargar_juguete_recurso(os.path.join(path, "juguete_recurso.csv"))
        if jr.id_juguete <= max_juguete
    )
    gen_recurso_recurso = (
        rr
        for rr in cargar_recurso_recurso(os.path.join(path, "recurso_recurso.csv"))
        if rr.id_recurso <= max_recurso
        and all(id_recurso <= max_recurso for id_recurso, _ in rr.recursos)
    )
    gen_objeto_recurso = (
        or_
        for or_ in cargar_objeto_recurso(os.path.join(path, "objeto_recurso.csv"))
        if or_.id_objeto <= max_objeto
        and all(id_recurso <= max_recurso for id_recurso, _ in or_.recursos)
    )
    gen_habitat_objeto = (
        ho
        for ho in cargar_habitat_objeto(os.path.join(path, "habitat_objeto.csv"))
        if ho.id_habitat <= max_habitat
        and all(id_objeto <= max_objeto for id_objeto, _ in ho.objetos)
    )

    return list(habitat_creables(
        gen_juguete,
        gen_juguete_recurso,
        gen_recurso_recurso,
        gen_objeto_recurso,
        gen_habitat_objeto,
        cadena_recursos(recurso),
    ))


class TestHabitatCreablesCargaDatosPrivado(IICTest):
    """
    Verifica habitat_creables con datasets privados S, M, L y XL.
    Usa stock generoso para enfocarse en orden, carga de datos y eficiencia sin
    activar casos base poco legibles de RecursoRecurso.
    """

    @timeout(N_SECOND)
    def test_S_stock_generoso_lista_completa(self):
        """
        Dataset S con stock amplio: todos los habitats eventualmente creables por
        los juguetes presentes deben aparecer ordenados.
        """
        resultado = ejecutar(PATH_S, [(id_recurso, 20) for id_recurso in range(1, 80)])

        self.assertEqual(resultado, list(range(2, 51)))

    @timeout(N_SECOND)
    def test_M_stock_generoso_eficiencia(self):
        """
        Dataset M con stock amplio y juguetes de id bajo presentes: verifica largo,
        comienzo, punto medio y final de la salida ordenada.
        """
        resultado = ejecutar(
            PATH_M,
            [(id_recurso, 20) for id_recurso in range(1, 200)],
            max_juguete=75,
        )

        self.assertEqual(len(resultado), 199)
        self.assertEqual(resultado[:5], [2, 3, 4, 5, 6])
        self.assertEqual(resultado[len(resultado) // 2], 101)
        self.assertEqual(resultado[-5:], [196, 197, 198, 199, 200])

    @timeout(N_SECOND)
    def test_L_stock_generoso_eficiencia(self):
        """
        Dataset L con stock amplio y muchos habitats: verifica eficiencia y orden
        sin comparar una lista completa demasiado larga.
        """
        resultado = ejecutar(
            PATH_L,
            [(id_recurso, 20) for id_recurso in range(1, 700)],
            max_juguete=250,
        )

        self.assertEqual(len(resultado), 999)
        self.assertEqual(resultado[:5], [2, 3, 4, 5, 6])
        self.assertEqual(resultado[len(resultado) // 2], 501)
        self.assertEqual(resultado[-5:], [996, 997, 998, 999, 1000])

    @timeout(N_SECOND)
    def test_XL_filtrado_eficiencia(self):
        """
        Dataset XL filtrado a juguetes/habitats/objetos<=500 y recursos<=1000.
        Valida integracion completa de los cinco generadores con datos reales.
        """
        resultado = ejecutar_filtrado(
            PATH_XL,
            [(id_recurso, 20) for id_recurso in range(1, 1001)],
            max_juguete=500,
            max_habitat=500,
            max_objeto=500,
            max_recurso=1000,
        )

        self.assertEqual(len(resultado), 99)
        self.assertEqual(resultado[:10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 14])
        self.assertEqual(resultado[len(resultado) // 2], 235)
        self.assertEqual(resultado[-5:], [480, 485, 487, 490, 500])

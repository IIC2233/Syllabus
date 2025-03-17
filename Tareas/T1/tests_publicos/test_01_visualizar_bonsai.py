from tests_publicos.timeout_function import timeout
from dccortaramas import Bonsai
import unittest
import os
import sys
sys.stdout = open(os.devnull, 'w')

N_SECOND = 10


class TestVisualizarBonsai(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_00_bonsai_vacio(self):
        bonsai = Bonsai("Leafeon", 15, 20, [])

        resultado_estudiante = bonsai.visualizar_bonsai("Vertical", True, True)
        archivo_estudiante = open(
            "visualizaciones/Leafeon.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = ""

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

    @timeout(N_SECOND)
    def test_01_vertical_no_emojis(self):
        bonsai = Bonsai("Venusaur", 15, 20, [["1", True, True, ["2", "3"]], ["2", True, False, ["4", "0"]], [
                        "3", False, True, ["0", "5"]], ["4", False, False, ["0", "0"]], ["5", True, True, ["0", "0"]]])

        resultado_estudiante = bonsai.visualizar_bonsai(
            "Vertical", False, True)
        archivo_estudiante = open(
            "visualizaciones/Venusaur.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "     1: H T\n    ┌──┴───┐\n  2: H F 3: _ T \n  ┌─┴─┐  ┌─┴─┐  \n4: _ F    5: H T"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

    @timeout(N_SECOND)
    def test_02_vertical_emojis(self):
        bonsai = Bonsai("Sceptile", 15, 20, [["1", True, True, ["2", "3"]], ["2", True, False, ["0", "4"]], [
                        "3", False, True, ["5", "0"]], ["4", False, False, ["0", "0"]], ["5", True, True, ["0", "0"]]])

        resultado_estudiante = bonsai.visualizar_bonsai("Vertical", True, True)
        archivo_estudiante = open(
            "visualizaciones/Sceptile.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "      1: 🌸 ✅\n   ┌─────┴──────┐\n2: 🌸 🚫     3: ⬛️ ✅\n ┌─┴──┐       ┌─┴──┐ \n  4: ⬛️ 🚫 5: 🌸 ✅"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

    @timeout(N_SECOND)
    def test_03_horizontal_no_emojis(self):
        bonsai = Bonsai("Rillaboom", 15, 20, [["1", True, True, ["B", "C"]], ["B", True, False, ["D", "0"]], [
                        "C", False, True, ["0", "E"]], ["D", False, False, ["0", "0"]], ["E", True, True, ["0", "0"]]])

        resultado_estudiante = bonsai.visualizar_bonsai(
            "Horizontal", False, True)
        archivo_estudiante = open(
            "visualizaciones/Rillaboom.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "             ┌D: _ F\n      ┌B: H F┤      \n      │      └\n1: H T┤       \n      │      ┌\n      └C: _ T┤\n             └E: H T"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

    @timeout(N_SECOND)
    def test_04_horizontal_emojis(self):
        bonsai = Bonsai("Roserade", 15, 20, [["1", True, True, ["Y", "X"]], ["Y", True, False, ["0", "W"]], [
                        "X", False, True, ["V", "0"]], ["W", False, False, ["0", "0"]], ["V", True, True, ["0", "0"]]])

        resultado_estudiante = bonsai.visualizar_bonsai(
            "Horizontal", True, True)
        archivo_estudiante = open(
            "visualizaciones/Roserade.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "                 ┌\n        ┌Y: 🌸 🚫┤\n        │        └W: ⬛️ 🚫\n1: 🌸 ✅┤                 \n        │        ┌V: 🌸 ✅\n        └X: ⬛️ ✅┤        \n                 └"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

    @timeout(N_SECOND)
    def test_05_horizontal_emojis_desorden(self):
        bonsai = Bonsai("Exeggutor", 15, 20, [["Estoy", False, True, ["Feliz", "Hambriento"]], ["Hambriento", True, True, ["0", "0"]], ["Soy", True, False, ["Exeggutor", "Groot"]], [
                        "Feliz", True, True, ["0", "0"]], ["1", True, True, ["Soy", "Estoy"]], ["Groot", False, False, ["0", "0"]], ["Exeggutor", True, True, ["0", "0"]]])

        resultado_estudiante = bonsai.visualizar_bonsai(
            "Horizontal", True, True)
        archivo_estudiante = open(
            "visualizaciones/Exeggutor.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "                   ┌Exeggutor: 🌸 ✅\n        ┌Soy: 🌸 🚫┤                \n        │          └Groot: ⬛️ 🚫\n1: 🌸 ✅┤                       \n        │            ┌Feliz: 🌸 ✅\n        └Estoy: ⬛️ ✅┤            \n                     └Hambriento: 🌸 ✅"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

    @timeout(N_SECOND)
    def test_06_horizontal_no_emojis_desorden(self):
        bonsai = Bonsai("Torterra", 15, 20, [["Estoy", False, True, ["Feliz", "Hambriento"]], ["Hambriento", True, True, ["0", "0"]], ["Soy", True, False, ["Torterra", "Groot"]], [
                        "Feliz", True, True, ["0", "0"]], ["1", True, True, ["Soy", "Estoy"]], ["Groot", False, False, ["0", "0"]], ["Torterra", True, True, ["0", "0"]]])

        resultado_estudiante = bonsai.visualizar_bonsai(
            "Horizontal", False, True)
        archivo_estudiante = open(
            "visualizaciones/Torterra.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "               ┌Torterra: H T\n      ┌Soy: H F┤             \n      │        └Groot: _ F\n1: H T┤                   \n      │          ┌Feliz: H T\n      └Estoy: _ T┤          \n                 └Hambriento: H T"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

    @timeout(N_SECOND)
    def test_07_vertical_emojis_desorden(self):
        bonsai = Bonsai("Serperior", 15, 20, [["Estoy", False, True, ["Feliz", "Hambriento"]], ["Hambriento", True, True, ["0", "0"]], ["Soy", True, False, ["Serperior", "Groot"]], [
                        "Feliz", True, True, ["0", "0"]], ["1", True, True, ["Soy", "Estoy"]], ["Groot", False, False, ["0", "0"]], ["Serperior", True, True, ["0", "0"]]])

        resultado_estudiante = bonsai.visualizar_bonsai("Vertical", True, True)
        archivo_estudiante = open(
            "visualizaciones/Serperior.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "                         1: 🌸 ✅\n              ┌─────────────┴──────────────┐\n          Soy: 🌸 🚫                  Estoy: ⬛️ ✅          \n       ┌──────┴───────┐            ┌───────┴───────┐        \nSerperior: 🌸 ✅ Groot: ⬛️ 🚫 Feliz: 🌸 ✅ Hambriento: 🌸 ✅"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

    @timeout(N_SECOND)
    def test_08_vertical_no_emojis_desorden(self):
        bonsai = Bonsai("Meganium", 15, 20, [["Estoy", False, True, ["Feliz", "Hambriento"]], ["Hambriento", True, True, ["0", "0"]], ["Soy", True, False, ["Meganium", "Groot"]], [
                        "Feliz", True, True, ["0", "0"]], ["1", True, True, ["Soy", "Estoy"]], ["Groot", False, False, ["0", "0"]], ["Meganium", True, True, ["0", "0"]]])

        resultado_estudiante = bonsai.visualizar_bonsai(
            "Vertical", False, True)
        archivo_estudiante = open(
            "visualizaciones/Meganium.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "                      1: H T\n            ┌───────────┴───────────┐\n         Soy: H F               Estoy: _ T         \n      ┌─────┴─────┐          ┌──────┴──────┐       \nMeganium: H T Groot: _ F Feliz: H T Hambriento: H T"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

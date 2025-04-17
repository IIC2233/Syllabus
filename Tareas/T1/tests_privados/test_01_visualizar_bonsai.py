from tests_privados.timeout_function import timeout
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
        bonsai = Bonsai("", 0, 0, [])

        resultado_estudiante = bonsai.visualizar_bonsai("Vertical", True, True)
        archivo_estudiante = open(
            "visualizaciones/.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = ""

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)


    @timeout(N_SECOND)
    def test_01_bonsai_emojis_desorden_salto_vertical(self):
        bonsai = Bonsai("Leaf Erickson", 10, 30, [["1", True, True, ["2\nhola", "3\nchao"]], ["4", False, False, ["0", "0"]], ["5", True, True, ["0", "0"]], [
                        "3\nchao", False, True, ["0", "5"]], ["2\nhola", True, False, ["4", "0"]]])
        
        resultado_estudiante = bonsai.visualizar_bonsai("Vertical", True, True)
        archivo_estudiante = open(
            "visualizaciones/Leaf Erickson.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "        1: 🌸 ✅\n     ┌─────┴─────┐\n2           3           \nhola: 🌸 🚫 chao: ⬛️ ✅ \n   ┌─┴──┐      ┌─┴──┐   \n4: ⬛️ 🚫        5: 🌸 ✅"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)


    @timeout(N_SECOND)
    def test_02_bonsai_emojis_desorden_salto_horizontal(self):
        bonsai = Bonsai("Twiggly Smalls", 10, 30, [["beep\nboop", False, True, ["0", "0"]], ["rico el\ncompleto", False, False, ["0", "0"]], ["", True, True, ["0", "0"]], [
                        "saludos\nviajero", False, True, ["beep\nboop", "taca\ntaca"]], ["hola\ny\nchao", True, False, ["rico el\ncompleto", ""]], ["1", True, True, ["hola\ny\nchao", "saludos\nviajero"]], ["taca\ntaca", True, False, ["0", "0"]]])
        
        resultado_estudiante = bonsai.visualizar_bonsai("Horizontal", True, True)
        archivo_estudiante = open(
            "visualizaciones/Twiggly Smalls.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "                     rico el\n         hola       ┌completo: ⬛️ 🚫\n        ┌y          ┤               \n        │chao: 🌸 🚫└: 🌸 ✅\n1: 🌸 ✅┤                   \n        │               beep\n        │saludos       ┌boop: ⬛️ ✅\n        └viajero: ⬛️ ✅┤           \n                       │taca\n                       └taca: 🌸 🚫"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)


    @timeout(N_SECOND)
    def test_03_bonsai_emojis_salto_vertical(self):
        bonsai = Bonsai("Sir Stumps-a-lot", 10, 30, [["1", True, True, ["2\n2\n2", "3\n3\n3\n3"]], ["2\n2\n2", True, False, ["\n", "0"]], [
                        "3\n3\n3\n3", False, True, ["0", "5"]], ["\n", False, False, ["0", "0"]], ["5", True, True, ["0", "0"]]])
        
        resultado_estudiante = bonsai.visualizar_bonsai("Vertical", True, True)
        archivo_estudiante = open(
            "visualizaciones/Sir Stumps-a-lot.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "      1: 🌸 ✅\n     ┌───┴────┐\n  2        3         \n  2        3         \n  2: 🌸 🚫 3         \n   ┌─┴─┐   3: ⬛️ ✅  \n            ┌─┴──┐   \n: ⬛️ 🚫      5: 🌸 ✅"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)


    @timeout(N_SECOND)
    def test_04_bonsai_emojis_salto_horizontal(self):
        bonsai = Bonsai("Bark Twain", 10, 30, [["1", True, True, ["2\n2\n2", "3\n3\n3\n3"]], ["2\n2\n2", True, False, ["\n", "0"]], [
                        "3\n3\n3\n3", False, True, ["0", "5"]], ["\n", False, False, ["0", "0"]], ["5", True, True, ["0", "0"]]])
        
        resultado_estudiante = bonsai.visualizar_bonsai("Horizontal", True, True)
        archivo_estudiante = open(
            "visualizaciones/Bark Twain.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "                  \n         2       ┌: ⬛️ 🚫\n        ┌2       ┤       \n        │2: 🌸 🚫└\n1: 🌸 ✅┤         \n        │3       \n        │3       ┌\n        └3       ┤\n         3: ⬛️ ✅└5: 🌸 ✅"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)


    @timeout(N_SECOND)
    def test_05_bonsai_noemojis_vertical(self):
        bonsai = Bonsai("Rootie Patootie", 10, 30, [["1", True, True, ["2", "3"]], ["2", True, False, ["4", "0"]], [
                        "3", False, True, ["0", "5"]], ["4", False, False, ["0", "0"]], ["5", True, True, ["0", "0"]]])
        
        resultado_estudiante = bonsai.visualizar_bonsai("Vertical", False, True)
        archivo_estudiante = open(
            "visualizaciones/Rootie Patootie.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "     1: H T\n    ┌──┴───┐\n  2: H F 3: _ T \n  ┌─┴─┐  ┌─┴─┐  \n4: _ F    5: H T"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

        
    @timeout(N_SECOND)
    def test_06_bonsai_emojis_vertical(self):
        bonsai = Bonsai("Tinyent Leaves", 10, 30, [["1", True, True, ["2", "3"]], ["2", True, False, ["0", "0"]], [
                        "3", False, True, ["0", "4"]], ["4", False, False, ["5", "0"]], ["5", True, True, ["0", "0"]]])
        
        resultado_estudiante = bonsai.visualizar_bonsai("Vertical", True, True)
        archivo_estudiante = open(
            "visualizaciones/Tinyent Leaves.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "    1: 🌸 ✅\n   ┌───┴────┐\n2: 🌸 🚫 3: ⬛️ ✅   \n         ┌──┴───┐   \n            4: ⬛️ 🚫\n             ┌─┴──┐ \n          5: 🌸 ✅"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)


    @timeout(N_SECOND)
    def test_07_bonsai_noemojis_horizontal(self):
        bonsai = Bonsai("Sproutacus", 10, 30, [["1", True, True, ["2", "0"]], ["2", True, False, ["3", "0"]], [
                        "3", False, True, ["5", "4"]], ["4", False, False, ["0", "0"]], ["5", True, True, ["0", "0"]]])
        
        resultado_estudiante = bonsai.visualizar_bonsai("Horizontal", False, True)
        archivo_estudiante = open(
            "visualizaciones/Sproutacus.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "                    ┌5: H T\n             ┌3: _ T┤      \n      ┌2: H F┤      └4: _ F\n      │      │             \n1: H T┤      └\n      │       \n      └"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)


    @timeout(N_SECOND)
    def test_08_bonsai_emojis_horizontal(self):
        bonsai = Bonsai("Bonsaiah", 10, 30, [["1", True, True, ["2", "3"]], ["2", True, False, ["4", "5"]], [
                        "3", False, True, ["6", "7"]], ["4", False, False, ["8", "9"]], ["5", True, True, ["10", "11"]],
                        ["6", True, False, ["12", "13"]], ["7", False, True, ["14", "15"]], ["8", False, False, ["0", "0"]], ["9", True, True, ["0", "0"]],
                        ["10", True, False, ["0", "0"]], ["11", False, True, ["0", "0"]], ["12", False, False, ["0", "0"]], ["13", True, True, ["0", "0"]],
                        ["14", True, False, ["0", "0"]], ["15", False, True, ["0", "0"]]])
        
        resultado_estudiante = bonsai.visualizar_bonsai("Horizontal", True, True)
        archivo_estudiante = open(
            "visualizaciones/Bonsaiah.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "                          ┌8: ⬛️ 🚫\n                 ┌4: ⬛️ 🚫┤        \n                 │        └9: 🌸 ✅\n        ┌2: 🌸 🚫┤                 \n        │        │        ┌10: 🌸 🚫\n        │        └5: 🌸 ✅┤         \n        │                 └11: ⬛️ ✅\n1: 🌸 ✅┤                           \n        │                 ┌12: ⬛️ 🚫\n        │        ┌6: 🌸 🚫┤         \n        │        │        └13: 🌸 ✅\n        └3: ⬛️ ✅┤                  \n                 │        ┌14: 🌸 🚫\n                 └7: ⬛️ ✅┤         \n                          └15: ⬛️ ✅"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)


    @timeout(N_SECOND)
    def test_09_bonsai_un_lado(self):
        bonsai = Bonsai("Shrubbaca", 10, 30, [["1", True, True, ["2", "0"]], ["2", True, False, ["3", "0"]], [
                        "3", False, True, ["4", "0"]], ["4", False, False, ["5", "0"]], ["5", True, True, ["6", "0"]],
                        ["6", True, False, ["7", "0"]], ["7", False, True, ["8", "0"]], ["8", False, False, ["9", "0"]], ["9", True, True, ["10", "0"]],
                        ["10", True, False, ["11", "0"]], ["11", False, True, ["12", "0"]], ["12", False, False, ["13", "0"]], ["13", True, True, ["14", "0"]],
                        ["14", True, False, ["15", "0"]], ["15", False, True, ["0", "0"]]])
        
        resultado_estudiante = bonsai.visualizar_bonsai("Horizontal", True, True)
        archivo_estudiante = open(
            "visualizaciones/Shrubbaca.txt", "r", encoding="utf-8")
        texto_estudiante = archivo_estudiante.read()
        texto_esperado = "                                                                                                                                  ┌15: ⬛️ ✅\n                                                                                                                        ┌14: 🌸 🚫┤         \n                                                                                                              ┌13: 🌸 ✅┤         └\n                                                                                                              │         │          \n                                                                                                    ┌12: ⬛️ 🚫┤         └\n                                                                                                    │         │          \n                                                                                          ┌11: ⬛️ ✅┤         └\n                                                                                          │         │          \n                                                                                ┌10: 🌸 🚫┤         └\n                                                                                │         │          \n                                                                       ┌9: 🌸 ✅┤         └\n                                                                       │        │          \n                                                              ┌8: ⬛️ 🚫┤        └\n                                                              │        │         \n                                                     ┌7: ⬛️ ✅┤        └\n                                                     │        │         \n                                            ┌6: 🌸 🚫┤        └\n                                            │        │         \n                                   ┌5: 🌸 ✅┤        └\n                                   │        │         \n                          ┌4: ⬛️ 🚫┤        └\n                          │        │         \n                 ┌3: ⬛️ ✅┤        └\n                 │        │         \n        ┌2: 🌸 🚫┤        └\n        │        │         \n1: 🌸 ✅┤        └\n        │         \n        └"

        self.assertIsNone(resultado_estudiante)
        self.assertEqual(texto_esperado, texto_estudiante)

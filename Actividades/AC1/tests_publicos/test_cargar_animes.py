import unittest
import os
import main
from utilidades import Anime


class VerificarCargarAnimes(unittest.TestCase):
    def test_tipo_dato(self):
        """
        Verifica que lo retornado sea una lista.
        """
        path = os.path.join("data", "ejemplo.chan")
        animes = main.cargar_animes(path)
        self.assertIsInstance(animes, list)

    def test_tipo_dato_2(self):
        """
        Verifica que lo retornado sea una lista.
        """
        path = os.path.join("data", "tests.kun")
        animes = main.cargar_animes(path)
        self.assertIsInstance(animes, list)

    def test_tipo_dato_vacio(self):
        """
        Verifica que lo retornado sea una lista.
        """
        path = os.path.join("data", "vacio.sama")
        animes = main.cargar_animes(path)
        self.assertIsInstance(animes, list)

    def test_largo(self):
        """
        Verifica que lo retornado contenga la cantidad de datos esperadas.
        """
        path = os.path.join("data", "ejemplo.chan")
        animes = main.cargar_animes(path)
        self.assertEqual(len(animes), 2)

    def test_largo_2(self):
        """
        Verifica que lo retornado contenga la cantidad de datos esperadas.
        """
        path = os.path.join("data", "tests.kun")
        animes = main.cargar_animes(path)
        self.assertEqual(len(animes), 3)

    def test_largo_vacio(self):
        """
        Verifica que lo retornado contenga la cantidad de datos esperadas.
        """
        path = os.path.join("data", "vacio.sama")
        animes = main.cargar_animes(path)
        self.assertEqual(len(animes), 0)

    def test_contenido(self):
        """
        Verifica que lo retornado contenga los datos esperadas.
        """
        path = os.path.join("data", "ejemplo.chan")
        respuesta_main = main.cargar_animes(path)

        anime_1 = Anime("Hunter x Hunter", 62, 9, 1999, "Nippon Animation",
                        {"Aventura", "Comedia", "Shonen", "Acción"})

        anime_2 = Anime("Sakura Card Captor", 70, 10, 1998, "Madhouse",
                        {"Shoujo", "Comedia", "Acción", "Romance"})

        self.assertSequenceEqual(respuesta_main[0], anime_1)
        self.assertSequenceEqual(respuesta_main[1], anime_2)

    def test_contenido_2(self):
        """
        Verifica que lo retornado contenga los datos esperadas.
        """
        path = os.path.join("data", "tests.kun")
        respuesta_main = main.cargar_animes(path)

        anime_1 = Anime("Spy x Family", 37, 9, 2022, "Wit Studio",
                        {"Acción", "Aventura", "Comedia"})
        anime_2 = Anime("Gintama", 201, 10, 2006, "Sunrise", {"Parodia"})
        anime_3 = Anime("Viaje de Chihiro", 1, 9, 2011, "Studio Ghibli", {"Fantasía", "Aventura"})

        self.assertSequenceEqual(respuesta_main[0], anime_1)
        self.assertSequenceEqual(respuesta_main[1], anime_2)
        self.assertSequenceEqual(respuesta_main[2], anime_3)

    def test_contenido_vacio(self):
        """
        Verifica que lo retornado contenga los datos esperadas.
        """
        path = os.path.join("data", "vacio.sama")
        animes = main.cargar_animes(path)
        respuesta = []
        self.assertSequenceEqual(animes, respuesta)


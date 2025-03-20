import unittest
import main
from utilidades import Anime


def obtener_animes(variacion):
    """
    Función que retorna distintas instancias de animes.
    """
    anime_1 = Anime("BnHA", 24, 6, 2016, "Sunrise", {"Acción", "Aventura", "Comedia"})
    anime_2 = Anime("Gintama", 201, 10, 2016, "Sunrise", {"Parodia"})
    anime_3 = Anime("Chihiro", 1, 9, 2011, "Ghibli", {"Fantasía", "Aventura"})
    anime_4 = Anime("Amapolas", 1, 3, 2011, "Ghibli", {"Romance"})
    anime_5 = Anime(
        "Sakura", 70, 10, 1998, "Madhouse", {"Comedia", "Acción", "Romance"}
    )

    if variacion == 0:
        return []
    elif variacion == 1:
        return [anime_1]
    elif variacion == 2:
        return [anime_1, anime_3]
    elif variacion == 3:
        return [anime_1, anime_2]
    elif variacion == 4:
        return [anime_1, anime_2, anime_3, anime_4, anime_5]


class VerificarConsultasDescartarAnimes(unittest.TestCase):

    def test_tipo_dato_caso_vacio(self):
        """
        Verifica que lo retornado sea una lista.
        """
        # animes_por_estreno
        datos = obtener_animes(0)
        no_descartados = main.descartar_animes({}, datos)
        self.assertIsInstance(no_descartados, list)

    def test_tipo_dato_caso_no_vacio(self):
        """
        Verifica que lo retornado sea un diccionario
        """
        # animes_por_estreno
        datos = obtener_animes(1)
        no_descartados = main.descartar_animes({"Comedia"}, datos)
        self.assertIsInstance(no_descartados, list)

    def test_resultado_animes_vacio(self):
        """
        Verifica el contenido cuando no hay animes
        """
        datos = obtener_animes(0)
        no_descartados = main.descartar_animes({"Comedia"}, datos)
        respuesta_esperada = []
        self.assertListEqual(no_descartados, respuesta_esperada)

    def test_resultado_generos_vacio(self):
        """
        Verifica el contenido cuando no hay géneros por descartar
        """
        datos = obtener_animes(3)
        no_descartados = main.descartar_animes(set(), datos)
        respuesta_esperada = ["BnHA", "Gintama"]
        self.assertListEqual(no_descartados, respuesta_esperada)

    def test_resultado_descartar_todo(self):
        """
        Verifica el contenido cuando se descartan todos los animes
        """
        datos = obtener_animes(2)
        no_descartados = main.descartar_animes({"Aventura"}, datos)
        respuesta_esperada = []
        self.assertListEqual(no_descartados, respuesta_esperada)

    def test_resultado_descartar_algunos(self):
        """
        Verifica el contenido cuando se descartan algunos animes
        """
        datos = obtener_animes(4)
        no_descartados = main.descartar_animes({"Acción"}, datos)
        respuesta_esperada = ["Gintama", "Chihiro", "Amapolas"]
        self.assertListEqual(no_descartados, respuesta_esperada)

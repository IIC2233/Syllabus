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


class VerificarConsultasAnimesPorEstreno(unittest.TestCase):

    def test_tipo_dato_caso_vacio(self):
        """
        Verifica que lo retornado sea un diccionario.
        """
        # animes_por_estreno
        datos = obtener_animes(0)
        estrenos = main.animes_por_estreno(datos)
        self.assertIsInstance(estrenos, dict)

    def test_tipo_dato_caso_no_vacio(self):
        """
        Verifica que lo retornado sea un diccionario
        """
        # animes_por_estreno
        datos = obtener_animes(1)
        estrenos = main.animes_por_estreno(datos)
        self.assertIsInstance(estrenos, dict)

    def test_resultado_vacio(self):
        """
        Verifica el contenido cuando no hay animes
        """
        datos = obtener_animes(0)
        estrenos = main.animes_por_estreno(datos)
        self.assertDictEqual(estrenos, {})

    def test_resultado_1_estreno(self):
        """
        Verifica el contenido cuando solo hay 1 anime
        """
        datos = obtener_animes(1)
        estrenos = main.animes_por_estreno(datos)
        respuesta_esperada = {2016: ["BnHA"]}
        self.assertCountEqual(estrenos, respuesta_esperada)
        for key in respuesta_esperada:
            text = f'Año {key}. Se entrega {estrenos[key]} pero se espera {respuesta_esperada[key]}'
            self.assertCountEqual(estrenos[key], respuesta_esperada[key], text)

    def test_resultado_2_estrenos(self):
        """
        Verifica el contenido cuando solo hay 2 anime de fecha distinta
        """
        datos = obtener_animes(2)
        estrenos = main.animes_por_estreno(datos)
        respuesta_esperada = {2016: ["BnHA"], 2011: ["Chihiro"]}
        self.assertCountEqual(estrenos, respuesta_esperada)
        for key in respuesta_esperada:
            text = f'Año {key}. Se entrega {estrenos[key]} pero se espera {respuesta_esperada[key]}'
            self.assertCountEqual(estrenos[key], respuesta_esperada[key], text)

    def test_resultado_1_repetido(self):
        """
        Verifica el contenido cuando solo hay 2 anime de misma fecha
        """
        datos = obtener_animes(3)
        estrenos = main.animes_por_estreno(datos)
        respuesta_esperada = {2016: ["Gintama", "BnHA"]}
        self.assertCountEqual(estrenos, respuesta_esperada)
        for key in respuesta_esperada:
            text = f'Año {key}. Se entrega {estrenos[key]} pero se espera {respuesta_esperada[key]}'
            self.assertCountEqual(estrenos[key], respuesta_esperada[key], text)

    def test_resultado_varios_repetidos(self):
        """
        Verifica el contenido cuando solo hay varios animes, algunos con misma fecha y otros no
        """
        datos = obtener_animes(4)
        estrenos = main.animes_por_estreno(datos)
        respuesta_esperada = {
            1998: ["Sakura"],
            2011: ["Amapolas", "Chihiro"],
            2016: ["BnHA", "Gintama"],
        }
        self.assertCountEqual(estrenos, respuesta_esperada)
        for key in respuesta_esperada:
            text = f'Año {key}. Se entrega {estrenos[key]} pero se espera {respuesta_esperada[key]}'
            self.assertCountEqual(estrenos[key], respuesta_esperada[key], text)

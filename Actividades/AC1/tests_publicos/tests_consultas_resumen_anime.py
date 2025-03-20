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


class VerificarConsultasResumenAnimes(unittest.TestCase):

    def test_tipo_dato_caso_vacio(self):
        """
        Verifica que lo retornado sea un diccionario.
        """
        # animes_por_estreno
        resumen = main.resumen_animes_por_ver()
        self.assertIsInstance(resumen, dict)

    def test_tipo_dato_caso_no_vacio(self):
        """
        Verifica que lo retornado sea un diccionario
        """
        # animes_por_estreno
        datos = obtener_animes(2)
        resumen = main.resumen_animes_por_ver(datos[0], datos[1])
        self.assertIsInstance(resumen, dict)

    def test_verificar_llaves_diccionario_vacio(self):
        """
        Verifica el diccionario contenga las llaves correspondiente
        """
        resumen = main.resumen_animes_por_ver()
        self.assertIn("puntaje promedio", resumen)
        self.assertIn("capitulos total", resumen)
        self.assertIn("generos", resumen)

    def test_verificar_llaves_diccionario_no_vacio(self):
        """
        Verifica el diccionario contenga las llaves correspondiente
        """
        datos = obtener_animes(1)
        resumen = main.resumen_animes_por_ver(*datos)
        self.assertIn("puntaje promedio", resumen)
        self.assertIn("capitulos total", resumen)
        self.assertIn("generos", resumen)

    def test_resultado_vacio(self):
        """
        Verifica el contenido cuando no hay géneros por descartar
        """
        resumen = main.resumen_animes_por_ver()

        self.assertEqual(resumen["puntaje promedio"], 0)
        self.assertEqual(resumen["capitulos total"], 0)
        self.assertSetEqual(resumen["generos"], set())

    def test_resultado_1_anime(self):
        """
        Verifica el contenido cuando solo pasamos 1 anime
        """
        datos = obtener_animes(1)
        resumen = main.resumen_animes_por_ver(datos[0])

        self.assertAlmostEqual(resumen["puntaje promedio"], 6.0, delta=0.1)
        self.assertEqual(resumen["capitulos total"], 24)
        self.assertSetEqual(resumen["generos"], {"Aventura", "Comedia", "Acción"})

    def test_resultado_2_anime(self):
        """
        Verifica el contenido cuando solo pasamos 2 animes
        """
        datos = obtener_animes(2)
        resumen = main.resumen_animes_por_ver(datos[0], datos[1])

        self.assertAlmostEqual(resumen["puntaje promedio"], 7.5, delta=0.1)
        self.assertEqual(resumen["capitulos total"], 25)
        self.assertSetEqual(
            resumen["generos"], {"Fantasía", "Aventura", "Comedia", "Acción"}
        )

    def test_resultado_varios_anime(self):
        """
        Verifica el contenido cuando solo pasamos varios animes
        """
        datos = obtener_animes(4)
        resumen = main.resumen_animes_por_ver(
            datos[0], datos[1], datos[2], datos[3], datos[4]
        )

        self.assertAlmostEqual(resumen["puntaje promedio"], 7.6, delta=0.1)
        self.assertEqual(resumen["capitulos total"], 297)
        self.assertSetEqual(
            resumen["generos"],
            {"Fantasía", "Aventura", "Romance", "Parodia", "Comedia", "Acción"},
        )

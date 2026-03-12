import unittest
import subprocess


class VerificarSalidasTerminal(unittest.TestCase):

    def ejecutar_python_y_obtener_resultado(self, script_name):
        """
        Este método prueba llamando el programa main con los comandos consola de la lista commands.
        Los outputs de la llamada a consola luego son utilizados por el método test_flujo_programa
        para combrobar que sea correcto
        """

        commands = ["python3", "py3", "python3.12", "py3.12", "python", "py"]
        for c in commands:
            try:
                result = subprocess.run(
                    [c, script_name],
                    capture_output=True,
                    text=True,
                    check=True,
                )
                return result.stdout
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        return ""

    def test_flujo_programa(self):
        """
        Verifica la ejecución del programa y que el output sea el esperado.
        """
        self.maxDiff = None
        result_print = self.ejecutar_python_y_obtener_resultado("main.py")

        mensaje_out = [
            "Ingrid Solberg logró el Oro olímpico en Esquí Alpino representando a Noruega\n",
            "Camille Tremblay logró el Plata olímpico en Biatlón representando a Canadá\n",
            "Lena Hoffmann logró el Oro olímpico en Bobsleigh representando a Alemania\n",
            "Madison Carter logró el Plata olímpico en Esquí de Fondo representando a Estados Unidos\n",
            "Elin Andersson logró el Bronce olímpico en Patinaje Artístico representando a Suecia\n",
            "Sofia Meier logró el Plata olímpico en Esquí Acrobático representando a Suiza\n",
            "Yui Nakamura logró el Bronce olímpico en Hockey sobre Hielo representando a Japón\n",
            "Park Ji-woo logró el Bronce olímpico en Luge representando a Corea del Sur\n",
            "Chloé Martin logró el Plata olímpico en Patinaje de Velocidad en Pista Corta representando a Francia\n",
            "Giulia Romano logró el Bronce olímpico en Snowboard representando a Italia\n",
            "Astrid Nilsen logró el Oro olímpico en Biatlón representando a Noruega\n",
            "Hailey Brooks logró el Oro olímpico en Esquí Alpino representando a Canadá\n",
            "Klara Vogel logró el Plata olímpico en Patinaje Artístico representando a Alemania\n",
            "Samantha Reed logró el Oro olímpico en Snowboard representando a Estados Unidos\n",
            "Maja Lindström logró el Plata olímpico en Esquí de Fondo representando a Suecia\n",
            "Nina Keller logró el Bronce olímpico en Luge representando a Suiza\n",
            "Aiko Tanaka logró el Plata olímpico en Esquí Acrobático representando a Japón\n",
            "Kim Hae-in logró el Oro olímpico en Patinaje de Velocidad en Pista Corta representando a Corea del Sur\n",
            "Lucie Bernard logró el Bronce olímpico en Bobsleigh representando a Francia\n",
            "Alessandra Conti logró el Bronce olímpico en Hockey sobre Hielo representando a Italia\n",
            "Solveig Hansen logró el Oro olímpico en Esquí Acrobático representando a Noruega\n",
            "Danielle Lefebvre logró el Oro olímpico en Hockey sobre Hielo representando a Canadá\n",
            "Anika Schneider logró el Bronce olímpico en Esquí Alpino representando a Alemania\n",
            "Brianna Hayes logró el Plata olímpico en Biatlón representando a Estados Unidos\n",
            "Tilda Johansson logró el Bronce olímpico en Snowboard representando a Suecia\n",
            "Larissa Baumann logró el Bronce olímpico en Esquí de Fondo representando a Suiza\n",
            "Mei Sato logró el Plata olímpico en Patinaje Artístico representando a Japón\n",
            "Lee Soo-jin logró el Plata olímpico en Bobsleigh representando a Corea del Sur\n",
            "Manon Dubois logró el Bronce olímpico en Luge representando a Francia\n",
            "Federica Bianchi logró el Plata olímpico en Patinaje de Velocidad en Pista Corta representando a Italia\n",
            "Noruega (15)\n",
            "Oros = 3, Platas = 0, Bronces = 0\n",
            "Canadá (13)\n",
            "Oros = 2, Platas = 1, Bronces = 0\n",
            "Estados Unidos (11)\n",
            "Oros = 1, Platas = 2, Bronces = 0\n",
            "Alemania (9)\n",
            "Oros = 1, Platas = 1, Bronces = 1\n",
            "Corea del Sur (9)\n",
            "Oros = 1, Platas = 1, Bronces = 1\n",
            "Japón (7)\n",
            "Oros = 0, Platas = 2, Bronces = 1\n",
            "Suecia (5)\n",
            "Oros = 0, Platas = 1, Bronces = 2\n",
            "Suiza (5)\n",
            "Oros = 0, Platas = 1, Bronces = 2\n",
            "Francia (5)\n",
            "Oros = 0, Platas = 1, Bronces = 2\n",
            "Italia (5)\n",
            "Oros = 0, Platas = 1, Bronces = 2\n",
        ]

        resultado_esperado = "".join(mensaje_out)

        self.assertEqual(result_print, resultado_esperado)

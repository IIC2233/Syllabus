import unittest
import subprocess


class VerificarSalidasTerminal(unittest.TestCase):

    def ejecutar_python_y_obtener_resultado(self, script_name):
        commands = ["python3", "py3", "python3.11", "py3.11", "python", "py"]
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

        result_print = self.ejecutar_python_y_obtener_resultado("main.py")

        mensaje_out_con = [
            "> Usuario con suscripcion. Puntos: 0\n",
            "> Items para elegir:\n",
            "1) harina sin polvos: $1500 / 10 puntos\n",
            "2) papas rusticas: $4000 / 50 puntos\n",
            "3) te en hoja: $3500 / 35 puntos\n",
            "4) detergente ropa blanca: $20800 / 200 puntos\n",
            "5) queso azul: $6800 / 70 puntos\n",
            "6) arroz grano largo: $2140 / 22 puntos\n",
            "7) salsa de tomate: $3200 / 32 puntos\n",
            "8) palmitos rodajas: $1800 / 20 puntos\n",
            "9) bistec posta rosada: $4600 / 50 puntos\n",
            "> Canasta actual del usuario:\n",
            "\t1) harina sin polvos: $1500 / 20 puntos\n",
            "\t2) papas rusticas: $4000 / 100 puntos\n",
            "\t3) te en hoja: $3500 / 70 puntos\n",
            "\t4) detergente ropa blanca: $20800 / 400 puntos\n",
            "\t5) queso azul: $6800 / 140 puntos\n",
            "\t6) arroz grano largo: $2140 / 44 puntos\n",
            "\t7) salsa de tomate: $3200 / 64 puntos\n",
            "\t8) palmitos rodajas: $1800 / 40 puntos\n",
            "\t9) bistec posta rosada: $4600 / 100 puntos\n",
            "> Usuario con suscripcion. Puntos: 978\n",
        ]

        mensaje_out_sin = [
            "> Usuario sin suscripcion. Puntos: 0\n",
            "> Items para elegir:\n",
            "1) harina sin polvos: $1500 / 10 puntos\n",
            "2) papas rusticas: $4000 / 50 puntos\n",
            "3) te en hoja: $3500 / 35 puntos\n",
            "4) detergente ropa blanca: $20800 / 200 puntos\n",
            "5) queso azul: $6800 / 70 puntos\n",
            "6) arroz grano largo: $2140 / 22 puntos\n",
            "7) salsa de tomate: $3200 / 32 puntos\n",
            "8) palmitos rodajas: $1800 / 20 puntos\n",
            "9) bistec posta rosada: $4600 / 50 puntos\n",
            "> Canasta actual del usuario:\n",
            "\t1) harina sin polvos: $1500 / 10 puntos\n",
            "\t2) papas rusticas: $4000 / 50 puntos\n",
            "\t3) te en hoja: $3500 / 35 puntos\n",
            "\t4) detergente ropa blanca: $20800 / 200 puntos\n",
            "\t5) queso azul: $6800 / 70 puntos\n",
            "\t6) arroz grano largo: $2140 / 22 puntos\n",
            "\t7) salsa de tomate: $3200 / 32 puntos\n",
            "\t8) palmitos rodajas: $1800 / 20 puntos\n",
            "\t9) bistec posta rosada: $4600 / 50 puntos\n",
            "> Usuario sin suscripcion. Puntos: 489\n",
        ]
        resultado = False
        if result_print == "".join(mensaje_out_sin) or result_print == "".join(
            mensaje_out_con
        ):
            resultado = True

        self.assertTrue(
            resultado,
            "La ejecución no entrega el output esperado según las instrucciones",
        )

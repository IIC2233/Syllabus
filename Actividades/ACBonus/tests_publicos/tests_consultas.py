from unittest import TestCase
from pathlib import Path

from consultas import consulta1, consulta2, consulta3, consulta4, consulta5, consulta6
from tests_publicos.respuestas import respuestas


consultas = [
    consulta1,
    consulta2,
    consulta3,
    consulta4,
    consulta5,
    consulta6
]

archivo = Path("wikis") / f"Chile.txt"
texto = archivo.read_text(encoding="utf-8")

def crear_clase_consulta(i: int):
    """Crea una clase VerificarConsulta {i + 1}."""

    class TestConsulta(TestCase):
        def test_consulta(self):
            """Verifica que la consulta {i + 1} funcione correctamente."""

            self.maxDiff = None
            self.assertCountEqual(
                consultas[i](texto),
                respuestas[i]
            )

    TestConsulta.test_consulta.__doc__ = f"Verifica que la consulta {i + 1} funcione correctamente."
    TestConsulta.__name__ = f"VerificarConsulta{i + 1}"
    TestConsulta.__qualname__ = f"VerificarConsulta{i + 1}"

    return TestConsulta


for i in range(len(consultas)):
    globals()[f'VerificarConsulta{i + 1}'] = crear_clase_consulta(i)

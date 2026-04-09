from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from tablero import Tablero, Posicion
from camino import CaminoIterator, CaminoIterable
from tests_publicos.utils import timeout

class VerificarCaminoIterator(TestCase):
    """."""

    def setUp(self):
        """Crea objetos antes de cada test, para ser usados por estos."""
        self.grilla = [
            ["@", "@", "@"],
            ["@", ".", "."],
            ["@", ".", "."]
        ]

        self.inicio = Posicion(2, 1)
        self.tablero = Tablero(self.grilla, self.inicio)

    def test_init(self):
        """."""
        movimientos = [
            "ARRIBA",
            "DERECHA"
        ]

        iterador = CaminoIterator(self.tablero, movimientos)

        self.assertEqual(
            iterador.tablero,
            self.tablero
        )

        self.assertEqual(
            iterador.movimientos,
            movimientos
        )

    def test_next(self):
        """."""
        movimientos = [
            "ARRIBA",
            "DERECHA"
        ]

        self.inicio = Posicion(2, 1)
        iterador = CaminoIterator(self.tablero, movimientos)

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.assertEqual(
                iterador.__next__(),
                Posicion(1, 1)
            )

            self.assertEqual(
                iterador.__next__(),
                Posicion(1, 2)
            )

            self.assertRaises(StopIteration, iterador.__next__)

            output_esperado = [
                "Intentando movimiento ARRIBA",
                "Vidas restantes 3",
                "Intentando movimiento DERECHA",
                "Vidas restantes 3",
                "Posición final (1, 2)"
            ]

            output = stdout.getvalue().splitlines()
            self.assertEqual(
                output,
                output_esperado
            )

    @timeout(1)
    def test_iterando(self):
        """Verifica una iteración válida."""
        movimientos = [
            "ARRIBA",
            "ARRIBA",

            "NOSTOY",

            "DERECHA",
            "DERECHA",
            "DERECHA",
        ]

        posiciones_esperadas = [
            Posicion(1, 1),
            Posicion(1, 1),

            Posicion(1, 1),

            Posicion(1, 2),
            Posicion(1, 2),
            Posicion(1, 2),
        ]

        iterador = CaminoIterable(self.tablero, movimientos)

        # TODO: Si iterador es de tamaño 0 pasará epicamente.
        with patch('sys.stdout', new=StringIO()) as stdout:
            for pos, pos_esperada in zip(iterador, posiciones_esperadas):
                self.assertEqual(pos, pos_esperada)

            output_esperado = [
                "Intentando movimiento ARRIBA",
                "Vidas restantes 3",
                "Intentando movimiento ARRIBA",
                "Vidas restantes 2",

                "Intentando movimiento NOSTOY",
                "Vidas restantes 2",

                "Intentando movimiento DERECHA",
                "Vidas restantes 3",
                "Intentando movimiento DERECHA",
                "Vidas restantes 2",
                "Intentando movimiento DERECHA",
                "Vidas restantes 1",

                "Posición final (1, 2)"
            ]

            output = stdout.getvalue().splitlines()
            self.assertEqual(
                output,
                output_esperado
            )

    @timeout(1)
    def test_iterando_muerte(self):
        """Verifica una iteración en la que el jugador muere."""
        movimientos = [
            "IZQUIERDA",
            "IZQUIERDA",
            "ABAJO",
            "ARRIBA"
        ]

        iterador = CaminoIterable(self.tablero, movimientos)

        with patch('sys.stdout', new=StringIO()) as stdout:
            for posicion in iterador:
                self.assertEqual(posicion, self.inicio)

                output_esperado = [
                    "Intentando movimiento IZQUIERDA",
                    "Vidas restantes 2",
                    "Intentando movimiento IZQUIERDA",
                    "Vidas restantes 1",

                    "Intentando movimiento ABAJO",
                    "Vidas restantes 0",
                    "Has muerto"
                ]

            output = stdout.getvalue().splitlines()
            self.assertEqual(
                output,
                output_esperado
            )

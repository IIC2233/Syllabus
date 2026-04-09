from unittest import TestCase
from tablero import Tablero, Posicion


class VerificarTablero(TestCase):
    """Verifica el movimiento del tablero."""

    def setUp(self):
        """."""

        self.grilla = [
            ["@", "@", "@"],
            ["@", ".", "."],
            ["@", ".", "."]
        ]

    def test_init(self):
        """Verifica que el tablero se inicie de forma correcta."""
        inicio = Posicion(1, 1)

        tablero = Tablero(self.grilla, inicio)

        self.assertEqual(
            tablero.grilla,
            self.grilla
        )

        self.assertEqual(
            tablero.inicio,
            inicio
        )

    def test_mover(self):
        """Verifica que retorne las posiciones correspondientes."""
        inicio = Posicion(2, 1)
        tablero = Tablero(self.grilla, inicio)

        direcciones = [
            "ARRIBA",
            "DERECHA",
            "ABAJO",
            "IZQUIERDA"
        ]

        posiciones = [
            Posicion(1, 1),
            Posicion(1, 2),
            Posicion(2, 2),
            Posicion(2, 1)
        ]

        posicion_actual = inicio
        for direccion, posicion in zip(direcciones, posiciones):
            self.assertEqual(
                tablero.mover(posicion_actual, direccion),
                posicion
            )

            posicion_actual = posicion


    def test_mover_invalido(self):
        """Verifica que lance las excepciones correspondientes cuando se le entregan movimientos inválidos."""
        self.grilla = [
            ["."]
        ]

        inicio = Posicion(0, 0)
        tablero = Tablero(self.grilla, inicio)

        direcciones = [
            "ARRIBA",
            "DERECHA",
            "ABAJO",
            "IZQUIERDA"
        ]

        for direccion in direcciones:
            self.assertRaises(IndexError, tablero.mover, inicio, direccion)

        self.assertRaises(KeyError, tablero.mover, inicio, "PaArria")

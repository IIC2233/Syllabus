import unittest

from caracteristicas import (
    OjosAzules,
    OjosCafes,
    OjosVerdes
)
from dominancia import Dominante
from bases import Mutable, Gen
from unittest.mock import patch

class VerificarGetProbabilidadesMutar(unittest.TestCase):
    """Clase que comprueba el funcionamiento correcto de la mutacion"""

    def test_implementacion(self):
        """
        Verifica que esté implementada la multiherencia y el método
        get_probabilidades_mutar correctamente
        """

        mro = OjosCafes.__mro__

        self.assertIn(Dominante, mro)
        self.assertIn(Mutable, mro)

        ojos = OjosCafes()
        probabilidades = ojos.get_probabilidades_mutar()

        self.assertCountEqual(
            probabilidades,
            [
                ("Cafes", 0.7),
                ("Verdes", 0.1),
                ("Azules", 0.2)
            ]
        )

    def test_mutacion(self):
        """
        Verifica que las mutaciones funcionan correctamente al 
        elegir un gen aleatorio
        """
        Gen.registrar(OjosAzules)
        Gen.registrar(OjosVerdes)
        Gen.registrar(OjosCafes)

        with patch('bases.elegir_con_probabilidades', return_value="Cafes"):
            par_de_genes = OjosCafes() + OjosCafes()
            alelo_aleatorio = par_de_genes.elegir_alelo_aleatorio()
            self.assertEqual(alelo_aleatorio.valor, "Cafes")

        with patch('bases.elegir_con_probabilidades', return_value="Verdes"):
            par_de_genes = OjosCafes() + OjosCafes()
            alelo_aleatorio = par_de_genes.elegir_alelo_aleatorio()
            self.assertEqual(alelo_aleatorio.valor, "Verdes")

        with patch('bases.elegir_con_probabilidades', return_value="Azules"):
            par_de_genes = OjosCafes() + OjosCafes()
            alelo_aleatorio = par_de_genes.elegir_alelo_aleatorio()
            self.assertEqual(alelo_aleatorio.valor, "Azules")

            

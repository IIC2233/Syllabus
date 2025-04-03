import unittest

from utils import Conductor, PatenteError
from main import DCConductor


class VerificarChequearRut(unittest.TestCase):

    def test_rut_valido(self):
        """
        Verifica que el método no retorne al funcionar correctamente.
        """
        conductor = Conductor("Jessica", "23098400-K",
                              "grv@estudiante.uc.cl", "", "")

        retorno = DCConductor(dict(), list()).chequear_rut(conductor)
        self.assertEqual(retorno, None)

    def test_rut_sin_guion(self):
        """
        Verifica que se levante el tipo de excepción y texto
        correspondientes al recibir un RUT sin guion.
        """
        conductor = Conductor("Jessica", "23098400K",
                              "", "", "")

        with self.assertRaises(Exception) as err:
            DCConductor(dict(), list()).chequear_rut(conductor)

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0],
                         "El rut 23098400K no contiene"
                         " el guión en la penultima posicion.")

    def test_run_con_puntos(self):
        """
        Verifica que se levante el tipo de excepción y texto
        correspondientes al recibir un RUT con puntos.
        """
        conductor = Conductor("Jessica", "23.098.400-K",
                              "", "", "")

        with self.assertRaises(Exception) as err:
            DCConductor(dict(), list()).chequear_rut(conductor)

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0],
                         "El rut 23.098.400-K contiene puntos.")


class VerificarChequearCelular(unittest.TestCase):

    def test_numero_valido(self):
        """
        Verifica que el método no retorne al funcionar correctamente.
        """
        conductor = Conductor("Jessica", "23098400-K", "",
                              "904346822", "")

        retorno = DCConductor(dict(), list()).chequear_celular(conductor)
        self.assertEqual(None, retorno)

    def test_numero_prefijo_invalido(self):
        """
        Verifica que levante la excepción y texto correspondientes
        al recibir un número con prefijo inválido.
        """
        conductor = Conductor("DCC", "81698900-0", "",
                              "223544439", "")

        with self.assertRaises(Exception) as err:
            DCConductor(dict(), list()).chequear_celular(conductor)

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0],
                         "El celular 223544439 no comienza con 9.")

    def test_numero_largo_invalido(self):
        """
        Verifica que levante la excepción y texto correspondientes
        al recibir un número de largo inválido.
        """
        conductor_1 = Conductor("DCC", "81698900-0", "",
                                "92223544439", "")

        conductor_2 = Conductor("DCC", "81698900-0", "",
                                "91", "")

        for conductor in [conductor_1, conductor_2]:
            with self.assertRaises(Exception) as err:
                DCConductor(dict(), list()).chequear_celular(conductor)

            self.assertEqual(type(err.exception), ValueError)
            self.assertEqual(err.exception.args[0],
                             f"El celular {conductor.celular} no tiene el largo correcto.")

    def test_numero_caracteres_invalidos(self):
        """
        Verifica que levante la excepción y texto correspondientes
        al recibir un número de con carácteres inválidos.
        """
        conductor_1 = Conductor("DCC", "81698900-0", "",
                                "9 4042 3272", "")

        conductor_2 = Conductor("DCC", "81698900-0", "",
                                "9902989ç1", "")

        for conductor in [conductor_1, conductor_2]:
            with self.assertRaises(Exception) as err:
                DCConductor(dict(), list()).chequear_celular(conductor)

            self.assertEqual(type(err.exception), ValueError)
            self.assertEqual(err.exception.args[0],
                             f"El celular {conductor.celular} contiene caracteres no numericos.")


class VerificarChequearNombre(unittest.TestCase):

    def test_nombre_existente(self):
        """
        Verifica que el método no retorne al funcionar correctamente.
        """
        conductor = Conductor("Jessica", "23098400-K", "",
                              "904346822", "")

        retorno = DCConductor({"Jessica": "UWU7U7"},
                              list()).chequear_nombre(conductor)

        self.assertEqual(retorno, None)

    def test_nombre_inexistente(self):
        """
        Verifica que levante la excepción y texto correspondientes
        cuando el nombre no está en el registro.
        """
        conductor = Conductor("Jessica", "23098400-K", "",
                              "904346822", "")

        with self.assertRaises(Exception) as err:
            DCConductor({"Pedro": "F0DL4L"}, list()).chequear_nombre(conductor)

        self.assertEqual(type(err.exception), KeyError)
        self.assertEqual(err.exception.args[0],
                         "El conductor Jessica no esta en el registro.")


class VerificarChequearPatente(unittest.TestCase):

    def test_patente_coincide_con_registro(self):
        """
        Verifica que el método no retorne al funcionar correctamente.
        """
        conductor = Conductor("Emily Brontë", "", "",
                              "", "70XLOL")

        retorno = DCConductor({"Emily Brontë": "70XLOL"},
                              list()).chequear_patente(conductor)
        self.assertEqual(retorno, None)

    def test_patente_difiere_de_registro(self):
        """
        Verifica que levante la excepción de forma correcta cuando
        la patente del conductor es distinta a la del registro.
        """
        conductor = Conductor("Emily Brontë", "", "",
                              "", "NYAA809")

        with self.assertRaises(Exception) as err:
            DCConductor({"Emily Brontë": "70XLOL"}, list()
                        ).chequear_patente(conductor)

        self.assertEqual(err.exception.args[0],
                         conductor)
        self.assertEqual(type(err.exception), PatenteError)

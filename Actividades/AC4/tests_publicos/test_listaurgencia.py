from unittest import TestCase

from main import ListaUrgencias
from utils import Urgencia
from tests_publicos.utils_privado import list_to_LU, LU_to_list


class VerificarAgregarUrgencia(TestCase):

    def test_agregar_urgencia_vacio(self):
        """
        Verifica que se agregue una urgencia a una ListaUrgencias vacía.
        """
        lista_urgencias = ListaUrgencias()
        urgencia = Urgencia('Paciente 1', 7.0)

        lista_urgencias.agregar_urgencia(urgencia)

        self.assertEqual(LU_to_list(lista_urgencias), [urgencia])

    def test_agregar_urgencia_supremo(self):
        """
        Verifica cuando se agrega una urgencia de mayor nivel
        que todas las demás en una ListaUrgencias no vacía.
        """
        urgencias = [Urgencia('Paciente 1', 12.0), Urgencia('Paciente 2', 8.0)]
        lista_urgencias = list_to_LU(urgencias)

        lista_urgencias.agregar_urgencia(Urgencia('Paciente 3', 14.0))
        urgencias.append(Urgencia('Paciente 3', 14.0))

        self.assertEqual(LU_to_list(lista_urgencias),
                         sorted(urgencias, reverse=True))

    def test_agregar_urgencia_igualdad(self):
        """
        Verifica cuando se agrega una urgencia de igual nivel
        que otra ya existente, en una ListaUrgencias no vacía.
        """
        urgencias = [Urgencia('Paciente 1', 3.0)]
        lista_urgencias = list_to_LU(urgencias)

        urgencias.append(Urgencia('Paciente 2', 3.0))
        lista_urgencias.agregar_urgencia(Urgencia('Paciente 2', 3.0))

        self.assertEqual(LU_to_list(lista_urgencias),
                         sorted(urgencias, reverse=True))

    def test_agregar_urgencia(self):
        """
        Verifica cuando se agregan diversas urgencias a
        una ListaUrgencias no vacía.
        """
        urgencias = [Urgencia('Paciente 1', 14.0), Urgencia(
            'Paciente 2', 3.0), Urgencia('Paciente 3', 1.0)]
        lista_urgencias = list_to_LU(urgencias)

        urgencias.append(Urgencia('Paciente 4', 2.0))
        lista_urgencias.agregar_urgencia(Urgencia('Paciente 4', 2.0))

        urgencias.append(Urgencia('Paciente 5', 7.0))
        lista_urgencias.agregar_urgencia(Urgencia('Paciente 5', 7.0))

        urgencias.append(Urgencia('Paciente 6', 7.0))
        lista_urgencias.agregar_urgencia(Urgencia('Paciente 6', 7.0))

        self.assertEqual(LU_to_list(lista_urgencias),
                         sorted(urgencias, reverse=True))

    def test_agregar_retorno(self):
        """
        Verifica que el método no retorne.
        """
        retorno = ListaUrgencias().agregar_urgencia(Urgencia('Juan', 10))

        self.assertEqual(retorno, None)


class VerificarQuitarUrgencia(TestCase):

    def test_quitar_urgencia_vacio(self):
        """
        Verifica el caso en el que se intenta eliminar
        a alguien de una ListaUrgencia vacío.
        """
        with self.assertRaises(Exception) as err:
            ListaUrgencias().quitar_urgencia("Jake")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], 'ListaUrgencias no contiene a Jake')

    def test_quitar_urgencia_inexistente(self):
        """
        Verifica el caso en el que se intenta eliminar
        a alguien que no está en la ListaUrgencia.
        """
        lista_urgencias = list_to_LU(
            [Urgencia('Juan', 10), Urgencia('Ignacio', 11)])
        with self.assertRaises(Exception) as err:
            lista_urgencias.quitar_urgencia("Jake")

        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], 'ListaUrgencias no contiene a Jake')

    def test_quitar_urgencia_existente(self):
        """
        Verifica el caso en el que intenta eliminar
        a alguien que sí está en la ListaUrgencia.
        """
        lista_urgencias = list_to_LU(
            [Urgencia('Juan', 10), Urgencia('Ignacio', 11), Urgencia('Pedro', 9)])

        self.assertEqual(lista_urgencias.quitar_urgencia('Ignacio'),
                         Urgencia('Ignacio', 11))
        self.assertEqual(lista_urgencias.cabeza.urgencia,
                         Urgencia('Juan', 10))
        self.assertEqual(LU_to_list(lista_urgencias), [
                         Urgencia('Juan', 10), Urgencia('Pedro', 9)])

    def test_quitar_urgencia_cabeza(self):
        """
        Verifica el caso en el que se intenta eliminar
        a alguien que justo es la cabeza.
        """
        lista_urgencias = list_to_LU(
            [Urgencia('Juan', 10), Urgencia('Ignacio', 11)])

        self.assertEqual(lista_urgencias.quitar_urgencia('Juan'),
                         Urgencia('Juan', 10))
        self.assertEqual(LU_to_list(lista_urgencias),
                         [Urgencia('Ignacio', 11)])

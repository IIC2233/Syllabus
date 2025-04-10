from unittest import TestCase
from collections.abc import Iterable

from main import ListaUrgencias, IteradorListarUrgencias
from utils import Urgencia
from tests_publicos.utils_privado import timeout, list_to_LU, LU_to_list


N_SECOND = 1


class VerificarIteradorListarUrgencias(TestCase):

    def test_iter(self):
        """
        Verifica que se haya implementado __iter__ y que retorne un iterable.
        """
        iterador = iter(IteradorListarUrgencias(ListaUrgencias()))

        self.assertIsInstance(iterador, Iterable)

    def test_next_retornar(self):
        """
        Verifica que se haya implementado __next__,
        y al usarlo en una LU no vacía retorne una Urgencia.
        """

        urgencias = [Urgencia('Paciente 1', 3.0), Urgencia('Paciente 2', 1.0)]
        lista_urgencias = list_to_LU(urgencias)

        iterador = IteradorListarUrgencias(lista_urgencias)

        siguiente = next(iterador)
        self.assertEqual(siguiente, Urgencia('Paciente 1', 3.0))

    def test_next_consumir(self):
        """
        Verifica que __next__ levante una excepción
        apropiada cuando se consume el iterador.
        """
        urgencias = [Urgencia('Paciente 1', 3.0)]
        lista_urgencias = list_to_LU(urgencias)

        iterador = IteradorListarUrgencias(lista_urgencias)

        with self.assertRaises(Exception) as err:
            next(iterador)
            next(iterador)

        self.assertIsInstance(err.exception, StopIteration)

    def test_next(self):
        """
        Verifica un correcto funcionamiento de __next__,
        es decir que retorne en el orden correspondiente.
        """

        urgencias = [Urgencia('Paciente 1', 3.0), Urgencia('Paciente 2', 8.0),
                     Urgencia('Paciente 3', -3.0), Urgencia('Paciente 4', 11.0)]
        lista_urgencias = list_to_LU(urgencias, False)

        iterador = IteradorListarUrgencias(lista_urgencias)

        lista_urgencias = []
        for _ in range(len(urgencias)):
            lista_urgencias.append(next(iterador))

        self.assertEqual(lista_urgencias, sorted(urgencias, reverse=True))

    @timeout(N_SECOND)
    def test_iterar(self):
        """
        Verifica un correcto funcionamiento de __iter__ y __next__
        """

        urgencias = [Urgencia('Paciente 1', 3.0), Urgencia('Paciente 2', 8.0),
                     Urgencia('Paciente 3', -3.0), Urgencia('Paciente 4', 11.0)]
        lista_urgencias = list_to_LU(urgencias, False)

        iterador = IteradorListarUrgencias(lista_urgencias)

        self.assertEqual(list(iterador), sorted(urgencias, reverse=True))


class VerificarIterListaUrgencias(TestCase):

    def test_lista_urgencias_inmutable(self):
        """
        Verifica que no sea posible modificar
        la lista original al iterar sobre esta.
        """

        urgencias = [Urgencia('Paciente 1', 3.0), Urgencia('Paciente 2', 1.0)]
        lista_urgencias = list_to_LU(urgencias)

        iterador = iter(lista_urgencias)
        next(iterador)
        next(iterador)

        self.assertEqual(LU_to_list(lista_urgencias), urgencias)

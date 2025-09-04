import unittest

from main import SistemaColas, IteradorSistemaColas, NodoCliente
from tests_publicos.utils import timeout


class VerificarIterSistemaColas(unittest.TestCase):

    @timeout()
    def test_iter_sistema_colas_retorno(self):
        """
        Verifica que el método retorne el tipo de dato solicitado.
        """
        queues = SistemaColas()
        self.assertIsInstance(iter(queues), IteradorSistemaColas)

    @timeout()
    def test_iter_sistema_colas_consumir(self):
        """
        Verifica que al consumir el iterable no se hayan modificado los datos de los nodos.
        """
        queues = SistemaColas()
        head = NodoCliente(False)
        tail = NodoCliente(False)
        head.siguiente = tail

        queues.cola_normal = head
        queues.cola_preferencial = NodoCliente(True)

        for _ in queues:
            pass

        self.assertIsNone(queues.cola_preferencial.siguiente)

        self.assertEqual(head.siguiente, tail)
        self.assertIsNone(tail.siguiente)

        self.assertFalse(head.preferencial)
        self.assertFalse(tail.preferencial)

        self.assertTrue(queues.cola_preferencial.preferencial)


class VerificarIteradorSistemaColas(unittest.TestCase):

    def setUp(self):
        """
        Para cada tests que se ejecute, se reiniciará el valor del
        atributo de clase 'identificador'
        """
        NodoCliente.identificador = 0

    @timeout()
    def test_iter_iterador_retorno(self):
        """
        Verifica que el método retorne una instancia de sí mismo.
        """
        iterator = IteradorSistemaColas(NodoCliente(True), NodoCliente(False))
        self.assertIsInstance(iter(iterator), IteradorSistemaColas)

    @timeout()
    def test_next_iterador_exception(self):
        """
        Verifica que el método levante la exception correspondiente cuando
        se queda sin nodos por los que iterar.
        """
        iterator = IteradorSistemaColas(NodoCliente(True), NodoCliente(False))

        with self.assertRaises(StopIteration):
            next(iterator)
            next(iterator)
            next(iterator)

    @timeout()
    def test_iterador_prioriza_normal(self):
        """
        Verifica que el iterador siga el algoritmo indicado para entregar
        a la siguiente persona cuando no hay clientes prioritarios.
        """
        expected_order = [1, 3, 0, 2]
        nodes = []
        for _ in range(4):
            node = NodoCliente(False)
            nodes.append(node)

        nodes[1].siguiente = nodes[3]
        nodes[3].siguiente = nodes[0]
        nodes[0].siguiente = nodes[2]

        iterator = IteradorSistemaColas(None, nodes[1])
        for expected_index in expected_order:
            person = next(iterator)
            self.assertEqual(person.identificador, expected_index)

    @timeout()
    def test_iterador_prioriza_prioritarios(self):
        """
        Verifica que el iterador siga el algoritmo indicado para entregar
        a la siguiente persona cuando solo hay clientes prioritarios.
        """
        expected_order = [3, 2, 1, 0]
        nodes = []
        for _ in range(4):
            node = NodoCliente(True)
            nodes.append(node)

        nodes[3].siguiente = nodes[2]
        nodes[2].siguiente = nodes[1]
        nodes[1].siguiente = nodes[0]

        iterator = IteradorSistemaColas(nodes[3], None)
        for expected_index in expected_order:
            person = next(iterator)
            self.assertEqual(person.identificador, expected_index)

    @timeout()
    def test_iterador_prioriza_completo(self):
        """
        Verifica que el iterador siga el algoritmo indicado para entregar
        a la siguiente persona cuando hay clientes prioritarios y normales.
        """
        expected_order = [1, 3, 0, 4, 2, 5]
        nodes = []
        for _ in range(4):
            node = NodoCliente(True)
            nodes.append(node)

        nodes[1].siguiente = nodes[3]
        nodes[3].siguiente = nodes[0]
        nodes[0].siguiente = nodes[2]

        for _ in range(4, 6):
            node = NodoCliente(False)
            nodes.append(node)

        nodes[4].siguiente = nodes[5]

        iterator = IteradorSistemaColas(nodes[1], nodes[4])
        for expected_index in expected_order:
            person = next(iterator)
            self.assertEqual(person.identificador, expected_index)

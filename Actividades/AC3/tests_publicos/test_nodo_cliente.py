import unittest

from main import NodoCliente
from tests_publicos.utils import timeout


class VerificarAgregarNodo(unittest.TestCase):

    @timeout()
    def test_agregar_nodo_retorno(self):
        """
        Verifica que el método no retorne nada al ser llamado.
        """
        head = NodoCliente(False)
        tail = NodoCliente(False)

        value = head.agregar_nodo(tail)
        self.assertIsNone(value)

    @timeout()
    def test_agregar_un_nodo(self):
        """
        Verifica que el método funcione correctamente al intentar
        agregar solo un nodo.
        """
        head = NodoCliente(False)
        tail = NodoCliente(False)

        head.agregar_nodo(tail)
        self.assertEqual(head.siguiente , tail)

    @timeout()
    def test_agregar_dos_nodos(self):
        """
        Verifica que el método funcione correctamente al agregar dos nodos.
        """
        head = NodoCliente(False)
        node_1 = NodoCliente(False)
        node_2 = NodoCliente(False)

        head.agregar_nodo(node_1)
        node_1.agregar_nodo(node_2)

        self.assertEqual(head.siguiente, node_1)
        self.assertEqual(node_1.siguiente, node_2)

    @timeout()
    def test_agregar_nodos_revueltos(self):
        """
        Verifica que el método funcione correctamente al agregar varios nodos.
        """
        nodes = []
        for _ in range(4):
            node = NodoCliente(False)
            nodes.append(node)

        nodes[1].agregar_nodo(nodes[2])
        nodes[2].agregar_nodo(nodes[0])
        nodes[0].agregar_nodo(nodes[3])

        self.assertEqual(nodes[1].siguiente, nodes[2])
        self.assertEqual(nodes[2].siguiente, nodes[0])
        self.assertEqual(nodes[0].siguiente, nodes[3])


class Verificar__str__(unittest.TestCase):

    def setUp(self):
        """
        Para cada tests que se ejecute, se reiniciará el valor del
        atributo de clase 'identificador'
        """
        NodoCliente.identificador = 0

    @timeout()
    def test__str__retorno(self):
        """
        Verifica que el método retorne el tipo de dato indicado.
        """
        head = NodoCliente(False)
        tail = NodoCliente(False)
        head.siguiente = tail

        nodos_cliente = str(head)
        self.assertIsInstance(nodos_cliente, str)

    @timeout()
    def test__str__un_nodo(self):
        """
        Verifica que el método al ser utilizado en un nodo individual
        funcione correctamente.
        """
        head = NodoCliente(False)

        nodes_from_head = str(head)
        self.assertEqual(nodes_from_head, "C(0) -> None")

    @timeout()
    def test__str__dos_nodos(self):
        """
        Verifica que el método al ser utilizado en una cadena de dos nodos
        funcione correctamente.
        """
        head = NodoCliente(False)
        tail = NodoCliente(False)
        head.siguiente = tail

        nodes_from_head = str(head)
        nodes_from_tail = str(tail)
        self.assertEqual(nodes_from_head, "C(0) -> C(1) -> None")
        self.assertEqual(nodes_from_tail, "C(1) -> None")

    @timeout()
    def test__str__nodos_revueltos(self):
        """
        Verifica que el método funcione correctamente al utilizar una cadena
        de varios nodos de forma desordenada.
        """
        nodes = []
        for _ in range(4):
            node = NodoCliente(False)
            nodes.append(node)

        nodes[1].siguiente = nodes[3]
        nodes[3].siguiente = nodes[0]
        nodes[0].siguiente = nodes[2]
        head = nodes[1]

        nodes_from_head = str(head)
        self.assertEqual(nodes_from_head, "C(1) -> C(3) -> C(0) -> C(2) -> None")


class Verificar__len__(unittest.TestCase):

    @timeout()
    def test__len__retorno(self):
        """
        Verifica que el método retorne el tipo de dato indicado.
        """
        head = NodoCliente(False)
        length = len(head)

        self.assertIsInstance(length, int)

    @timeout()
    def test__len__un_nodo(self):
        """
        Verifica que el método retorne 1 cuando solo existe un nodo en la cadena.
        """
        head = NodoCliente(False)
        length = len(head)

        self.assertEqual(length, 1)

    @timeout()
    def test__len__dos_nodos(self):
        """
        Verifica que el método retorne 2 cuando hay dos nodos en la cadena.
        """
        head = NodoCliente(False)
        tail = NodoCliente(False)

        head.siguiente = tail
        length = len(head)
        self.assertEqual(length, 2)

    @timeout()
    def test__len__varios_nodos(self):
        """
        Verifica que el método retorne el largo esperado en una cadena de varios nodos.
        """
        expected_length = 11

        for i in range(expected_length - 1):
            if i == 0:
                head = NodoCliente(False)

            node = NodoCliente(False)
            node.siguiente = head
            head = node

        length = len(head)
        self.assertEqual(length, expected_length)

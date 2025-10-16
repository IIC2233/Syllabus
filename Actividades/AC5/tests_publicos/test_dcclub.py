from unittest import TestCase
from unittest.mock import call, patch, MagicMock

from tests_publicos.utils import timeout

from main import DCClub


class VerificarDCClub(TestCase):

    def setUp(self):
        self.capacidad = 3
        self.artista = "Lorde"
        self.instrumentos = ["Bajo", "Alto", "Mediano"]

        self.DCClub = DCClub(self.capacidad, self.artista, self.instrumentos)

        self.DCClub.TIEMPO_ESPERA_INSTRUMENTOS = 0
        self.DCClub.TIEMPO_ESPERA_MESA_SONIDO = 0
        self.DCClub.PROBABILIDAD_ERROR_MESA_SONIDO = 0
        self.DCClub.DURACION_CLUB_ABIERTO = 0.1

    @timeout(1)
    def test_preparar_escenario(self):
        """
        Verifica que se usen correctamente los contenidos de Threading
        en el método preparar_escenario y que se llamen los métodos que correspondan.
        """

        # Correcto uso y asociación de Threads
        threading_mock = MagicMock()
        thread_instance = threading_mock.return_value

        with patch("main.Thread", threading_mock):
            self.DCClub.preparar_escenario()

            self.assertEqual(2, threading_mock.call_count)
            self.assertEqual(2, thread_instance.start.call_count)
            self.assertEqual(2, thread_instance.join.call_count)

            threading_arguments = str(threading_mock.call_args_list)
            self.assertIn("revisar_mesa_sonido", threading_arguments)
            self.assertIn("revisar_instrumentos", threading_arguments)

        # Correcto llamado de métodos
        revisar_mesa_sonido_mock = MagicMock()
        revisar_instrumentos_mock = MagicMock()

        with patch.object(DCClub, "revisar_mesa_sonido", revisar_mesa_sonido_mock), \
             patch.object(DCClub, "revisar_instrumentos", revisar_instrumentos_mock):
            self.DCClub.preparar_escenario()

            self.assertEqual(1, revisar_mesa_sonido_mock.call_count)
            self.assertEqual(1, revisar_instrumentos_mock.call_count)

    @timeout(1)
    def test_manejar_llegada_cliente_lock_blocking(self):
        """
        Verifica que utilice Locks con el correcto estado de blocking.
        """
        cliente = MagicMock()
        cliente.id = 0
        lock = MagicMock()
        lock.acquire.return_value = True

        self.DCClub.lock_capacidad = lock
        self.DCClub.capacidad_actual = 1
        self.DCClub.capacidad_maxima = 2

        self.DCClub.manejar_llegada_cliente(cliente)

        lock.acquire.assert_called_once()

        call_args = lock.acquire.call_args_list[0]
        self.assertIn(call_args, [call(False), call(blocking=False)])

    @timeout(1)
    @patch("main.DCClub.llegada_cliente")
    def test_manejar_llegada_cliente_con_capacidad(self, llegada_cliente_mock):
        """
        Verifica que se utilice Locks correctamente y que se llame el método
        llegada_cliente, cuando el DCClub NO ha alcanzado la capacidad máxima.
        """

        cliente = MagicMock()
        lock = MagicMock()
        lock.acquire.return_value = True

        self.DCClub.lock_capacidad = lock
        self.DCClub.capacidad_actual = 1
        self.DCClub.capacidad_maxima = 2

        resultado_llegada = self.DCClub.manejar_llegada_cliente(cliente)

        lock.acquire.assert_called_once()
        lock.release.assert_called_once()
        llegada_cliente_mock.assert_called_once_with(cliente)
        self.assertTrue(resultado_llegada)

    @timeout(1)
    @patch("main.DCClub.llegada_cliente")
    def test_manejar_llegada_cliente_sin_capacidad(self, llegada_cliente_mock):
        """
        Verifica que se utilice Locks correctamente y que NO se llame el método
        llegada_cliente, cuando el DCClub SÍ ha alcanzado la capacidad máxima.
        """

        cliente = MagicMock()
        lock = MagicMock()
        lock.acquire.return_value = True

        self.DCClub.lock_capacidad = lock
        self.DCClub.capacidad_actual = 2
        self.DCClub.capacidad_maxima = 2

        resultado_llegada = self.DCClub.manejar_llegada_cliente(cliente)

        lock.acquire.assert_called_once()
        lock.release.assert_called_once()
        llegada_cliente_mock.assert_not_called()
        self.assertFalse(resultado_llegada)

    @timeout(1)
    @patch("main.DCClub.llegada_cliente")
    def test_manejar_llegada_cliente_no_obtiene_lock(self, llegada_cliente_mock):
        """
        Verifica que el método se comporte correctamente cuando 
        no se puede adquirir el lock.
        """

        cliente = MagicMock()
        lock = MagicMock()
        lock.acquire.return_value = False

        self.DCClub.lock_capacidad = lock
        self.DCClub.capacidad_actual = 0
        self.DCClub.capacidad_maxima = 2

        resultado_llegada = self.DCClub.manejar_llegada_cliente(cliente)

        lock.acquire.assert_called_once()
        lock.release.assert_not_called()
        llegada_cliente_mock.assert_not_called()
        self.assertFalse(resultado_llegada)

    @timeout(1)
    def test_manejar_salida_cliente_lock_blocking(self):
        """
        Verifica que utilice Locks con el correcto estado de blocking.
        """
        cliente = MagicMock()
        cliente.id = 0
        lock = MagicMock()
        lock.acquire.return_value = True

        self.DCClub.lock_capacidad = lock

        self.DCClub.manejar_salida_cliente(cliente)

        lock.acquire.assert_called_once()

        call_args = lock.acquire.call_args_list[0]
        self.assertIn(call_args, [call(False), call(blocking=False)])

    @timeout(1)
    @patch("main.DCClub.salida_cliente")
    def test_manejar_salida_cliente_obtiene_lock(self, salida_cliente_mock):
        """
        Verifica que se utilice Locks correctamente y que se llame el método
        salida_cliente.
        """

        cliente = MagicMock()
        lock = MagicMock()
        lock.acquire.return_value = True

        self.DCClub.lock_capacidad = lock

        resultado_salida = self.DCClub.manejar_salida_cliente(cliente)

        lock.acquire.assert_called_once()
        lock.release.assert_called_once()
        salida_cliente_mock.assert_called_once_with(cliente)
        self.assertTrue(resultado_salida)

    @timeout(1)
    @patch("main.DCClub.salida_cliente")
    def test_manejar_salida_cliente_no_obtiene_lock(self, salida_cliente_mock):
        """
        Verifica que el método se comporte correctamente cuando 
        no se puede adquirir el lock.
        """

        cliente = MagicMock()
        lock = MagicMock()
        lock.acquire.return_value = False

        self.DCClub.lock_capacidad = lock

        resultado_salida = self.DCClub.manejar_salida_cliente(cliente)

        lock.acquire.assert_called_once()
        lock.release.assert_not_called()
        salida_cliente_mock.assert_not_called()
        self.assertFalse(resultado_salida)

    @timeout(2)
    def test_run(self):
        """
        Verifica que el run llame correctamente los métodos que correspondan,
        actualice el estado del event y que duerma el tiempo que le corresponde.
 
        IMPORTANTE: Para revisar este método, deben estar funcionando
        correctamente el método preparar_escenario.
        """
        self.test_preparar_escenario()

        senal_abierto_mock = MagicMock()
        sleep_mock = MagicMock()

        self.DCClub.senal_abierto = senal_abierto_mock

        with patch("main.sleep", sleep_mock), \
             patch("main.DCClub.preparar_escenario") as preparar_escenario_mock:
            self.DCClub.run()

            preparar_escenario_mock.assert_called_once()
            senal_abierto_mock.set.assert_called_once()
            sleep_mock.assert_called_once_with(self.DCClub.DURACION_CLUB_ABIERTO)

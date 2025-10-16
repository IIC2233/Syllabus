from unittest import TestCase
from unittest.mock import call, patch, MagicMock

from tests_publicos.utils import timeout, ExpectedException

from main import Cliente, DCClub


class VerificarCliente(TestCase):

    def setUp(self):
        self.capacidad = 3
        self.artista = "Lorde"
        self.instrumentos = ["Bajo", "Alto", "Mediano"]

        lock = MagicMock()
        senal_abierto = MagicMock()

        self.DCClub = DCClub(self.capacidad, self.artista, self.instrumentos)

        self.DCClub.TIEMPO_ESPERA_INSTRUMENTOS = 0
        self.DCClub.TIEMPO_ESPERA_MESA_SONIDO = 0
        self.DCClub.PROBABILIDAD_ERROR_MESA_SONIDO = 0
        self.DCClub.DURACION_CLUB_ABIERTO = 0.1
        self.DCClub.lock_capacidad = lock
        self.DCClub.senal_abierto = senal_abierto

        self.cliente = Cliente(self.DCClub.senal_abierto,
                               self.DCClub.manejar_llegada_cliente,
                               self.DCClub.manejar_salida_cliente)

        self.cliente.TIEMPO_ESPERA_NUEVO_INTENTO = 0.01
        self.cliente.MIN_TIEMPO_EN_CLUB = 0
        self.cliente.RANGO_TIEMPO_EN_CLUB = 0

    def test_daemon(self):
        """
        Verifica que Cliente defina correctamente los objectos como daemon.
        """

        self.assertTrue(self.cliente.daemon)

    @timeout(1)
    def test_intentar_entrar_dcclub_exitoso(self):
        """
        Verifica el caso en que no sea posible entrar al club en el primer intento,
        pero sí en el segundo.
        """

        def manejar_llegada_cliente_mock(cliente) -> bool:
            cliente.intentos += 1
            return cliente.intentos == 2

        sleep_mock = MagicMock()
        self.cliente.intentos = 0
        self.cliente.entrar_al_club = manejar_llegada_cliente_mock

        with patch("main.sleep", sleep_mock):
            resultado_entrada = self.cliente.intentar_entrar_dcclub()

            self.assertEqual(2, self.cliente.intentos)
            sleep_mock.assert_called_once_with(self.cliente.TIEMPO_ESPERA_NUEVO_INTENTO)
            self.assertTrue(resultado_entrada)

    @timeout(1)
    def test_intentar_entrar_dcclub_fallido(self):
        """
        Verifica que en el caso en que no es posible entrar al club,
        vuelva a intentarlo nuevamente hasta que lo logre.
        """
        def manejar_llegada_cliente_mock(cliente):
            cliente.intentos += 1

            if cliente.intentos >= 5:
                raise ExpectedException("Excepción Esperada")

            return False

        sleep_mock = MagicMock()
        self.cliente.intentos = 0
        self.cliente.entrar_al_club = manejar_llegada_cliente_mock

        with patch("main.sleep", sleep_mock):
            with self.assertRaises(ExpectedException):
                self.cliente.intentar_entrar_dcclub()

        self.assertEqual(
            [call(self.cliente.TIEMPO_ESPERA_NUEVO_INTENTO)] * 4,
            sleep_mock.call_args_list
        )

    @timeout(1)
    def test_intentar_salir_dcclub(self):
        """
        Verifica que sea posible salir cuando se obtiene la confirmación.
        """
        def manejar_salida_cliente_mock(cliente) -> bool:
            cliente.intentos += 1
            return cliente.intentos == 2

        sleep_mock = MagicMock()
        self.cliente.intentos = 0
        self.cliente.salir_del_club = manejar_salida_cliente_mock

        with patch("main.sleep", sleep_mock):
            resultado_salida = self.cliente.intentar_salir_dcclub()

            self.assertEqual(2, self.cliente.intentos)
            sleep_mock.assert_not_called()
            self.assertTrue(resultado_salida)

    @timeout(3)
    def test_run(self):
        """
        Verifica que el run llame correctamente los métodos que correspondan,
        y que duerma el tiempo que le corresponde.

        IMPORTANTE: Para revisar este método, deben estar funcionando
        correctamente los métodos intentar_entrar_dcclub e intentar_salir_dcclub.
        """

        self.test_intentar_entrar_dcclub_exitoso()
        self.test_intentar_salir_dcclub()

        sleep_mock = MagicMock()

        with patch("main.sleep", sleep_mock), \
             patch("main.Cliente.intentar_entrar_dcclub") as intentar_entrar_dcclub, \
             patch("main.Cliente.intentar_salir_dcclub") as intentar_salir_dcclub, \
             patch("main.Cliente.calcular_tiempo_en_club") as calcular_tiempo:

            self.cliente.run()

            self.cliente.senal_abrio_club.wait.assert_any_call()

            intentar_entrar_dcclub.assert_called_once()
            intentar_salir_dcclub.assert_called_once()
            calcular_tiempo.assert_called_once()
            sleep_mock.assert_called_once_with(calcular_tiempo())

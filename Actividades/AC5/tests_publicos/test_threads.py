from unittest import TestCase
from unittest.mock import MagicMock, patch
from clases import Equipo, Atleta, Carrera
from threading import Event
from tests_publicos.utils import timeout


class VerificarAtletaRun(TestCase):
    """Verifica la implementación del método Run."""

    def assert_lock_and_reset(self):
        """Verifica que el lock haya sido usado de forma correcta, y luego lo resetea."""

        acquire = self.lock.acquire.called or self.lock.__enter__.called
        release = self.lock.release.called or self.lock.__exit__.called

        self.assertTrue(acquire and release,
                        "El lock no fue usado correctamente.")

        self.lock.reset_mock()

    def tearDown(self):
        """'Reseteamos' todos los patch luego de cada test."""
        patch.stopall()

    def setUp(self):
        """Creamos mocks para usar en cada test."""
        self.patcher_lock = patch('clases.Carrera.lock_timestamps')
        self.lock = self.patcher_lock.start()

        self.patcher_run = patch('clases.random_tiempo_corriendo')
        self.mock_run = self.patcher_run.start()
        self.mock_run.return_value = 10.382

        self.patcher_caer = patch('clases.random_se_cae_testigo')
        self.mock_caer = self.patcher_caer.start()
        self.mock_caer.return_value = False

        self.patcher_perdido = patch('clases.random_tiempo_perdido')
        self.mock_perdido = self.patcher_perdido.start()
        self.mock_perdido.return_value = 10.382

    def assert_tiempo_corriendo(self, sleep: MagicMock):
        """Verifica que se corra el tiempo indicado."""
        sleep.assert_called_with(10.382)

    @patch('clases.datetime')
    @patch('clases.time.sleep')
    def test_entrenamiento(self, sleep, datetime):
        """Cuando solo hay un atleta participando. Es decir, salir, correr y llegar a la meta."""
        evento_salida = MagicMock()

        equipo = Equipo("Team Chile")

        atleta = Atleta("Martina", evento_salida)
        equipo.append(atleta)

        # Salir
        atleta.run()
        evento_salida.wait.assert_called_once()

        # Correr
        self.assert_tiempo_corriendo(sleep)

        self.assertEqual(
            Carrera.timestamps_llegada.get("Team Chile"),
            datetime.now.return_value
        )

        self.assert_lock_and_reset()


    @timeout(1)
    @patch('clases.datetime')
    @patch('clases.time.sleep')
    def test_entrenamiento_en_equipo_sin_caida(self, sleep, datetime):
        """Cuando hay dos atletas del mismo equipo entrenando, y logran entregar la posta."""

        evento_salida = Event()
        evento_final = Event()

        equipo = Equipo("Team Chile")

        atleta = Atleta("Martina", evento_salida)
        atleta_final = Atleta("Fernanda", evento_final)

        equipo.append(atleta)
        equipo.append(atleta_final)

        atleta.start()
        atleta_final.start()

        evento_salida.set()

        atleta.join(0.1)
        atleta_final.join(0.1)

        self.assert_tiempo_corriendo(sleep)

        self.assertEqual(
            Carrera.timestamps_llegada.get("Team Chile"),
            datetime.now.return_value
        )
        self.assert_lock_and_reset()

        self.mock_caer.assert_called_once()
        self.assertEqual(sleep.call_count, 2)
        self.mock_perdido.assert_not_called()

    @timeout(1)
    @patch('clases.datetime')
    @patch('clases.time.sleep')
    def test_entrenamiento_en_equipo_con_caida(self, sleep, datetime):
        """Cuando hay dos atletas del mismo equipo entrenando, y se cae la posta."""

        evento_salida = Event()
        evento_final = Event()

        equipo = Equipo("Team Chile")

        atleta = Atleta("Martina", evento_salida)
        atleta_final = Atleta("Fernanda", evento_final)

        equipo.append(atleta)
        equipo.append(atleta_final)

        atleta.start()
        atleta_final.start()

        self.mock_caer.return_value = True
        evento_salida.set()

        atleta.join(0.1)
        atleta_final.join(0.1)

        self.assert_tiempo_corriendo(sleep)

        self.assertEqual(
            Carrera.timestamps_llegada.get("Team Chile"),
            datetime.now.return_value
        )
        self.assert_lock_and_reset()

        self.mock_caer.assert_called_once()
        self.mock_perdido.assert_called_once()

        self.assertEqual(sleep.call_count, 3)

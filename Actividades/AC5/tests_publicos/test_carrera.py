from unittest import TestCase
from unittest.mock import MagicMock, patch
from clases import Equipo, Atleta, Carrera
from threading import Event, current_thread
from tests_publicos.utils import timeout
from datetime import datetime, timedelta


class VerificarCarrera(TestCase):
    """Verifica que se implemente la Carrera de forma correcta."""

    tiempo_inicial = datetime.now()

    def obtener_escenario(self):
        """Busca el escenario de un atleta, si no lo encuentra entrega uno por defecto."""
        atleta = current_thread()
        llave = (atleta.equipo.nombre, atleta.nombre)

        return self.escenarios.get(llave, (10.0, False, 0.0))

    def datetime_now(self, total_atletas):
        """Imita un llamado a datetime.now, ya sea para obtener el tiempo inicial o el final, agregando los sleeps."""

        hilo = current_thread()
        if type(hilo) != Atleta:
            return self.tiempo_inicial

        tiempo_total_equipo = 0
        equipo_nombre = hilo.equipo.nombre
        for i in range(total_atletas):
            atleta_nombre = str(i)

            corriendo, cae, perdido = self.escenarios.get(
                (equipo_nombre, atleta_nombre),
                (10.0, False, 0.0)
            )

            tiempo_total_equipo += corriendo
            if cae:
                tiempo_total_equipo += perdido

        return self.tiempo_inicial + timedelta(seconds=tiempo_total_equipo)
    
    @timeout(1)
    def test_init(self):
        """Verifica que el init agregue le agregue los eventos correspondientes a los participantes."""
        carrera = Carrera(2, 2)

        self.assertEqual(
            carrera.equipos[0].primero.evento,
            carrera.equipos[1].primero.evento
        )

        self.assertNotEqual(
            carrera.equipos[0].ultimo.evento,
            carrera.equipos[0].primero.evento
        )

        self.assertNotEqual(
            carrera.equipos[1].ultimo.evento,
            carrera.equipos[1].primero.evento
        )

    @timeout(1)
    @patch("clases.Atleta.join")
    @patch("clases.Atleta.start")
    def test_iniciar_atletas(self, start, join):
        """Verifica que la carrera inicie todos los atletas."""
        cantidad_equipos = 4
        cantidad_atletas = 2

        carrera = Carrera(cantidad_equipos, cantidad_atletas)

        carrera.simular_carrera()

        atletas_totales = cantidad_equipos * cantidad_atletas
        self.assertEqual(start.call_count, atletas_totales)

    @timeout(1)
    @patch('clases.random_tiempo_perdido')
    @patch('clases.random_se_cae_testigo')
    @patch('clases.random_tiempo_corriendo')
    @patch('clases.datetime')
    @patch('clases.time.sleep')
    def test_simular_carrera(self, sleep, datetime, random_corriendo, random_cae, random_perdido):
        """Simula una carrera entre 3 equipos de 3 atletas cada uno, gana el primero, el segundo queda segundo."""

        Carrera.timestamps_llegada.clear()

        datetime.now.side_effect = lambda: self.datetime_now(total_atletas=3)

        random_corriendo.side_effect = lambda: self.obtener_escenario()[0]
        random_cae.side_effect = lambda: self.obtener_escenario()[1]
        random_perdido.side_effect = lambda: self.obtener_escenario()[2]

        # La tupla consiste, en tiempo que se demora en correr, si es que la posta cae,
        # y el tiempo que se demora si la posta cae.
        self.escenarios = {
            ("0", "0"): (3.0, True, 2.0),   # Atleta 0, Equipo 0: 5 segundos
            ("0", "1"): (3.0, False, 0.0),  # 3 segundos
            ("0", "2"): (3.0, False, 0.0),  # 3 segundos

            ("1", "0"): (3.0, False, 5.0),  # Atleta 0, Equipo 1: 3 segundos
            ("1", "1"): (5.0, False, 5.0),  # 5 segundos
            ("1", "2"): (5.0, False, 5.0),  # 5 segundo

            ("2", "0"): (10.0, True, 5.0),  # Atleta 0, Equipo 2: 15 segundos
            ("2", "1"): (10.0, False, 5.0),  # 10 segundos
            ("2", "2"): (10.0, False, 5.0),  # 10 segundo
        }


        carrera = Carrera(3, 3)
        resultados = carrera.simular_carrera()

        self.assertDictEqual(
            resultados,
            {
                '0': timedelta(seconds=11),
                '1': timedelta(seconds=13),
                '2': timedelta(seconds=35)
            }
        )

from unittest import TestCase
from unittest.mock import patch, MagicMock, mock_open
from servidor import app
from io import StringIO
import json


class VerificarGetControl(TestCase):
    """Verifica get_control del servidor."""

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.contenido = {
            "id_control": 0,
            "materia": "Entorno de trabajo"
        }

        self.contenido_json = json.dumps(self.contenido)

    @patch("servidor.json.dumps")
    @patch("servidor.json.loads")
    @patch("servidor.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_get_control_valido(
        self,
        open_mock,
        load,
        loads,
        dumps
    ):
        """Verifica el caso de un get exitoso."""
        load.return_value = self.contenido
        loads.return_value = self.contenido
        dumps.return_value = self.contenido_json

        response = self.client.get("/controles/00-Entorno de trabajo.json")

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertDictEqual(data, self.contenido)

        leyo_json = load.call_count > 0 or loads.call_count > 0
        if leyo_json:
            dumps.assert_called_once_with(self.contenido)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_control_inexistente(self, open_file):
        """Verifica 404 con mensaje si el control no existe"""
        response = self.client.get("/controles/control_invalido.json")

        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(
            "Control no encontrado: control_invalido.json",
            data.get("Mensaje"),

            "Se debe retornar un mensaje indicando que dicho control no existe."
        )


class VerificarPostControlAnswer(TestCase):
    """Verifica post_control_answer del servidor."""

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.nombre = "00-Entorno de trabajo.json"
        self.alumno = "alopez7"
        self.respuestas = [2, 0, 3]
        self.respuestas_json = json.dumps(self.respuestas)

    @patch("servidor.json.load")
    @patch("pathlib.Path.is_file")
    @patch("builtins.open")
    def test_post_control_valido(self, open_mock, is_file, load):
        """Verifica el caso de un post exitoso"""
        load.return_value = {
            "id_control": 0, "materia": "Entorno de trabajo"
        }
        is_file.side_effect = [True, False]

        string_io = StringIO()
        string_io.close = lambda: None
        open_mock.return_value.__enter__.return_value = string_io
        open_mock.return_value = string_io

        response = self.client.post(
            f"/controles/{self.nombre}?alumno={self.alumno}",
            json=self.respuestas
        )

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(
            data.get("Mensaje"),
            "Respuesta guardada correctamente"
        )

        self.assertEqual(
            string_io.getvalue().strip(), self.respuestas_json,
            "El archivo debe contener las respuestas en JSON"
        )

        open_mock.assert_called()
        nombre_archivo = open_mock.call_args[0][0]
        self.assertIn(f"{self.alumno}-{self.nombre}", str(nombre_archivo))

    @patch("servidor.json.load")
    @patch("builtins.open")
    def test_post_control_inexistente(self, open_mock, load):
        """Verifica el caso en que el control no existe."""
        open_mock.side_effect = FileNotFoundError

        response = self.client.post(
            "/controles/control_falso.json?alumno=" + self.alumno,
            json=self.respuestas
        )

        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(
            data.get("Mensaje"),
            "Control no encontrado: controles/control_falso.json"
        )

    @patch("servidor.json.load")
    @patch("pathlib.Path.is_file")
    @patch("builtins.open")
    def test_post_sobreescribir(self, open_mock, is_file, load):
        """Verifica que no modifique un archivo existente"""
        load.return_value = {}
        is_file.return_value = True

        contenido_previo = "[0, 0, 0]"
        string_io = StringIO(contenido_previo)
        open_mock.return_value.__enter__.return_value = string_io

        response = self.client.post(
            f"/controles/{self.nombre}?alumno={self.alumno}",
            json=self.respuestas
        )

        self.assertEqual(response.status_code, 409)
        data = response.get_json()
        self.assertEqual(
            data.get("Mensaje"),
            "No se pueden sobreescribir las respuestas"
        )

        # Verifica que el archivo no fue modificado
        self.assertEqual(
            string_io.getvalue().strip(), contenido_previo,
            "No se debe modificar el archivo de respuestas existente"
        )

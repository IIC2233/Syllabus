from unittest import TestCase
from unittest.mock import patch, MagicMock
from cliente import Cliente


def _obtener_data(post_mock):
    """Obtiene el valor pasado como data al mock, sin importar si es arg o kwarg."""
    if "data" in post_mock.call_args.kwargs:
        return post_mock.call_args.kwargs.get("data")
    # data es el segundo argumento posicional de requests.post
    if len(post_mock.call_args.args) > 1:
        return post_mock.call_args.args[1]

    return None

class VerificarGetControles(TestCase):
    """Verifica get_controles del Cliente."""

    def setUp(self):
        """."""
        self.cliente = Cliente("http://localhost", 4444, "test_user")
        self.response = MagicMock()
        self.response.status_code = 200

    @patch("cliente.requests.get")
    def test_get_controles_valido(self, get):
        """Verifica que retorne lo pedido."""
        controles_esperados = [
            "00-Entorno de trabajo.json",
            "01-Estructuras de datos.json"
        ]

        self.response.json.return_value = controles_esperados
        get.return_value = self.response

        code, lista = self.cliente.get_controles()

        get.assert_called_once()
        url_llamada = get.call_args[0][0]
        self.assertIn("/controles", url_llamada)

        self.assertEqual(int(code), 200, "Debe retornar el status code 200")
        self.assertEqual(
            lista,
            controles_esperados,
            "Debe retornar la lista obtenida del servidor"
        )

    @patch("cliente.requests.get")
    def test_get_controles_invalido(self, get):
        """Verifica el caso en que GET no retorna 200"""
        self.response.status_code = 404
        self.response.json.return_value = {"error": "not found"}

        get.return_value = self.response

        code, lista = self.cliente.get_controles()

        self.assertEqual(lista, [],
                         "Debe retornar una lista vacía si el status no es 200")

class VerificarGetPreguntasControl(TestCase):
    """Verifica get_preguntas_control del Cliente."""

    def setUp(self):
        self.cliente = Cliente("http://localhost", 4444, "test_user")
        self.response = MagicMock()
        self.response.status_code = 200
        self.response.json.return_value = {}

    @patch("cliente.requests.get")
    def test_get_preguntas_hace_get_correcto(self, get):
        """Verifica que haga el GET al endpoint correcto"""
        datos_esperados = {"id_control": 0, "materia": "Entorno de trabajo"}
        get.return_value = self.response
        self.response.json.return_value = datos_esperados

        code, data = self.cliente.get_preguntas_control("00-Entorno de trabajo.json")

        get.assert_called_once()
        url_llamada = get.call_args[0][0]

        self.assertIn("/controles/00-Entorno de trabajo.json", url_llamada)

        self.assertEqual(int(code), 200)
        self.assertEqual(data, datos_esperados)

    @patch("cliente.requests.get")
    def test_get_preguntas_control_inexistente(self, get):
        """Verifica caso en que el control no existe"""
        self.response.status_code = 404
        self.response.json.return_value = {
            "Mensaje": "Control no encontrado: control_inexistente"
        }
        get.return_value = self.response

        code, data = self.cliente.get_preguntas_control("control_inexistente.json")

        self.assertEqual(code, 404)
        self.assertDictEqual(
            dict(data), self.response.json.return_value
        )


class PostRespuestasControl(TestCase):
    """Verifica post_respuestas_control del Cliente."""

    def setUp(self):
        self.cliente = Cliente("http://localhost", 4444, "alopez7")
        self.response = MagicMock()
        self.respuestas = [2, 0, 3]
        self.nombre_control = "00-Entorno de trabajo.json"
        self.alumno = "alopez7"

        self.response.status_code = 200
        self.response.json.return_value = {}

    @patch("cliente.json.dumps")
    @patch("cliente.requests.post")
    def test_post_correcto(self, post, dumps):
        """Verifica que serialice y envie los datos de forma correcta"""
        dump_esperado = '[2, 0, 3]'
        dumps.return_value = dump_esperado

        post.return_value = self.response

        self.cliente.post_respuestas_control(
            self.nombre_control, self.respuestas, self.alumno
        )

        dumps.assert_called_once_with(self.respuestas)
        post.assert_called_once()

        data = _obtener_data(post)
        self.assertEqual(data, dump_esperado,
                         "Las respuestas deben ir en el body como data")


        url = post.call_args[0][0]
        self.assertIn(f"/controles/{self.nombre_control}", url)
        self.assertIn(f"alumno={self.alumno}", url)

    @patch("cliente.requests.post")
    def test_post_respuestas_guardado(self, post):
        """Verifica caso exitoso: respuesta guardada."""
        self.response.json.return_value = {
            "Mensaje": "Respuesta guardada correctamente"
        }

        post.return_value = self.response

        code, data = self.cliente.post_respuestas_control(
            self.nombre_control, self.respuestas, self.alumno
        )

        self.assertEqual(code, 200)
        self.assertDictEqual(dict(data), self.response.json.return_value)

    @patch("cliente.requests.post")
    def test_post_respuestas_control_inexistente(self, post):
        """Verifica caso control no encontrado."""
        self.response.status_code = 404
        self.response.json.return_value = {
            "Mensaje": "Control no encontrado: control_falso.json"
        }

        post.return_value = self.response

        code, data = self.cliente.post_respuestas_control(
            "control_falso.json", self.respuestas, self.alumno
        )

        self.assertEqual(code, 404)
        self.assertDictEqual(
            dict(data), self.response.json.return_value
        )

    @patch("cliente.requests.post")
    def test_post_respuestas_sobreescribir(self, post):
        """Verifica caso conflicto: respuesta ya existe."""
        self.response.status_code = 409
        self.response.json.return_value = {
            "Mensaje": "No se pueden sobreescribir las respuestas"
        }
        post.return_value = self.response

        code, data = self.cliente.post_respuestas_control(
            self.nombre_control, self.respuestas, self.alumno
        )

        self.assertEqual(code, 409)
        self.assertDictEqual(
            dict(data), self.response.json.return_value
        )

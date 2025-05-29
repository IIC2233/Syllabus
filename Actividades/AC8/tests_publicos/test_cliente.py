import unittest

from json import loads
from unittest.mock import patch, Mock, ANY

from cliente.main import ClienteApi


class VerificarCliente(unittest.TestCase):
    def setUp(self):
        host = 'localhost'
        port = 2905
        self.base_url = f'http://{host}:{port}'
        self.cliente = ClienteApi(host, port)


    def test_obtener_saldo(self):
        """
        Verifica que retorne el saldo en caso de éxito.
        """
        banco = 'BancoDCC'

        response = Mock()
        response.status_code = 200
        response.json.return_value = {'result': 1}

        with patch('requests.get', return_value=response) as get :
            saldo = self.cliente.obtener_saldo(banco)

            get.assert_called_with(
                f'{self.base_url}/obtener_saldo/{banco}'
            )
            self.assertEqual(saldo, response.json.return_value['result'])

    def test_obtener_saldo_error(self):
        """
        Verifica que retorne el error en caso de fallar.
        """
        banco = 'NotBank'
        response = Mock()
        response.status_code = 404
        response.json.return_value = {'error': 'Cuenta NotBank no encontrada'}

        with patch('requests.get', return_value=response) as get :
            saldo = self.cliente.obtener_saldo(banco)

            get.assert_called_with(
                f'{self.base_url}/obtener_saldo/{banco}'
            )
            self.assertEqual(saldo, response.json.return_value['error'])

    def test_obtener_transacciones(self):
        """
        Verifica que retorne las transacciones cuando se solicita de forma correcta.
        """
        cuenta = 'PepaBank'
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'result': {
            'Pan': 1200,
            'PS5': 3000
        }}

        with patch('requests.get', return_value=response) as get :
            saldo = self.cliente.obtener_transacciones(cuenta)

            self.assertIn(f'{self.base_url}/obtener_transacciones/{cuenta}',
                          get.call_args.args
            )
            self.assertEqual(saldo, response.json.return_value['result'])

    def test_obtener_transacciones_error(self):
        """
        Verifica que retorne el error al solicitar un banco inexistente.
        """
        cuenta = 'NotBank'
        response = Mock()
        response.status_code = 404
        response.json.return_value = {'error': 'Cuenta NotBank no encontrada'}

        with patch('requests.get', return_value=response) as get :
            saldo = self.cliente.obtener_transacciones(cuenta)

            self.assertIn(f'{self.base_url}/obtener_transacciones/{cuenta}',
                          get.call_args.args
                          )
            self.assertEqual(saldo, response.json.return_value['error'])

    def test_agregar_gasto_error(self):
        """
        Verifica que retorne el error al solicitar un banco inexistente.
        """
        cuenta = 'NotBank'
        response = Mock()
        response.status_code = 404
        response.json.return_value = {'error': 'Cuenta NotBank no encontrada'}

        with patch('requests.post', return_value=response) as get :
            saldo = self.cliente.agregar_gasto(cuenta, 'Comida China', 1300)

            self.assertIn(f'{self.base_url}/agregar_gasto/{cuenta}',
                          get.call_args.args
                          )
            self.assertEqual(saldo, response.json.return_value['error'])

    def test_agregar_gasto(self):
        """
        Verifica que retorne el mensaje al ser usado correctamente.
        """
        cuenta = 'PepaBank'
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'msg': 'Gasto agregado'}

        with patch('requests.post', return_value=response) as get :
            saldo = self.cliente.agregar_gasto(cuenta, 'Comida China', 1300)

            get.assert_called_with(
                f'{self.base_url}/agregar_gasto/{cuenta}',
                params={'titulo': 'Comida China', 'monto': 1300}
            )
            self.assertEqual(saldo, response.json.return_value['msg'])

    def test_ajustar_saldo(self):
        """
        Verifica que retorne el mensaje al ser usado correctamente.
        """
        cuenta = 'BancoDCC'
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'msg': 'Saldo ajustado'}

        with patch('requests.patch', return_value=response) as get :
            saldo = self.cliente.ajustar_saldo(cuenta, 25000)

            get.assert_called_with(
                f'{self.base_url}/ajustar_saldo/{cuenta}',
                params={'saldo': 25000}
            )
            self.assertEqual(saldo, response.json.return_value['msg'])

    def test_ajustar_saldo_error(self):
        """
        Verifica que retorne el error al fallar.
        """

        cuenta = 'NotBank'
        response = Mock()
        response.status_code = 404
        response.json.return_value = {'error': 'Cuenta NotBank no encontrada'}

        with patch('requests.patch', return_value=response) as get :
            saldo = self.cliente.ajustar_saldo(cuenta, 25000)

            get.assert_called_with(
                f'{self.base_url}/ajustar_saldo/{cuenta}',
                params={'saldo': 25000}
            )

            self.assertEqual(saldo,
                             response.json.return_value['error'])

    def test_ajustar_saldo_error_params(self):
        """
        Verifica que retorne el error cuando falta algún parámetro.
        """
        cuenta = 'PepaBank'
        response = Mock()
        response.status_code = 400
        response.json.return_value = {'error': 'Faltan argumentos'}

        with patch('requests.patch', return_value=response) as get :
            saldo = self.cliente.ajustar_saldo(cuenta, None)

            get.assert_called_with(
                f'{self.base_url}/ajustar_saldo/{cuenta}',
                params={'saldo': None}
            )
            self.assertEqual(saldo, response.json.return_value['error'])

    def test_hacer_transferencia(self):
        """
        Verifica que se retorne la transferencia.
        """
        cuenta = 'PepaBank'
        response = Mock()
        response.status_code = 200
        response.json.return_value = {'msg': 'Transferencia realizada'}

        token = 'UwUTOKENoWo'
        data = {
            "banco": "PepaBank",
            "destinatario": {"nombre": "Juanito", "n_cuenta": 10010873981},
            "monto": 1000
        }

        headers = {'Authorization': token}
        with patch('requests.post', return_value=response) as get :
            saldo = self.cliente.hacer_transferencia(
                cuenta,
                'Juanito',
                10010873981,
                1000,
                token
            )

            get.assert_called_with(
                f'{self.base_url}/hacer_transferencia',
                data=ANY,
                headers=ANY
            )

            self.assertDictEqual(get.call_args.kwargs['headers'], headers)
            self.assertDictEqual(loads(get.call_args.kwargs['data']), data)
            self.assertEqual(saldo, response.json.return_value['msg'])

    def test_hacer_transferencia_error(self):
        """
        Verifica que se retorne el error si el banco no existe.
        """
        cuenta = 'JoeBank'
        response = Mock()
        response.status_code = 404
        response.json.return_value = {'error': 'Cuenta JoeBank no encontrada'}
        
        token = 'UwUTOKENoWo'
        data = {
            "banco": 'JoeBank',
            "destinatario": {"nombre": "Juanito", "n_cuenta": 10010873981},
            "monto": 1000
        }

        headers = {'Authorization': token}
        with patch('requests.post', return_value=response) as get :
            saldo = self.cliente.hacer_transferencia(
                cuenta,
                'Juanito',
                10010873981,
                1000,
                token
            )

            get.assert_called_with(
                f'{self.base_url}/hacer_transferencia',
                data=ANY,
                headers=ANY
            )
                
            self.assertDictEqual(get.call_args.kwargs['headers'], headers)
            self.assertDictEqual(loads(get.call_args.kwargs['data']), data)
            self.assertEqual(saldo, response.json.return_value['error'])

    def test_hacer_transferencia_token_invalido(self):
        """
        Verifica que se retorne el error cuando el token no está.
        """
        cuenta = 'JoeBank'
        response = Mock()
        response.status_code = 401
        response.json.return_value = {'error': 'Token Invalido'}
        
        token = None
        
        data = {
            "banco": 'JoeBank',
            "destinatario": {"nombre": "Juanito", "n_cuenta": 10010873981},
            "monto": 1000
        }

        headers = {'Authorization': token}
        with patch('requests.post', return_value=response) as get :
            saldo = self.cliente.hacer_transferencia(
                cuenta,
                'Juanito',
                10010873981,
                1000,
                token
            )

            get.assert_called_with(
                f'{self.base_url}/hacer_transferencia',
                data=ANY,
                headers=ANY
            )

            self.assertDictEqual(get.call_args.kwargs['headers'], headers)
            self.assertDictEqual(loads(get.call_args.kwargs['data']), data)
            self.assertEqual(saldo, response.json.return_value['error'])

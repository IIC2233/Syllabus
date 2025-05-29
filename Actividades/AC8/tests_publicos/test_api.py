import os
import unittest

from unittest.mock import patch

from servidor.main import app, dcconsumo


class VerificarApi(unittest.TestCase):
    def restaurar_archivos_json(self):
        path_write = dcconsumo.path_data
        path_read = os.path.join('tests_publicos', 'data_tests.json')

        with open(path_write, 'w', encoding='utf-8') as file_w:
            with open(path_read, 'r', encoding='utf-8') as file_r:
                file_w.write(file_r.read())

        dcconsumo.cargar_data()

    def setUp(self):
        self.maxDiff = None

        self.restaurar_archivos_json()

        self.app = app # esto no crea una nueva app :O
        self.app.config['TESTING'] = True

        self.saldo_total = {'result': 200000}
        self.saldo = {
            'BancoDCC': {'result': 150000},
            'NotBank': {'error': 'Cuenta NotBank no encontrada'}
        }

        self.transacciones = {
            'PepaBank': {
                'result': [
                    {'monto': 20000, 'tipo': 'gasto',
                     'titulo': 'Transferencia Luna (10101010)'},
                    {'monto': 70000, 'tipo': 'ingreso', 'titulo': 'Ajuste saldo'},
                    {'monto': 993000, 'tipo': 'gasto', 'titulo': 'Ajuste saldo'},
                    {'monto': 5000, 'tipo': 'gasto', 'titulo': 'Gusanos'},
                    {'monto': 2000, 'tipo': 'gasto', 'titulo': 'Lechuga'},
                    {'monto': 1000000, 'tipo': 'ingreso', 'titulo': 'Salgo base'}
                ]
            }
        }

    def test_obtener_saldo_total(self):
        """
        Verifica que al hacer GET "/obtener_saldo" se entregue
        la respuesta adecuada.
        """
        with self.app.test_client() as client:
            response = client.get('/obtener_saldo')

            self.assertEqual(response.status, '200 OK')
            self.assertEqual(response.get_json(), self.saldo_total)

    def test_obtener_saldo_banco_existente(self):
        """
        Verifica que GET "/obtener_saldo/" responda cuando se
        le solicita un banco existente.
        """
        with self.app.test_client() as client:
            response = client.get('/obtener_saldo/BancoDCC')

            self.assertEqual(response.status, '200 OK')
            self.assertEqual(response.get_json(), self.saldo['BancoDCC'])

    def test_obtener_saldo_banco_inexistente(self):
        """
        Verifica que GET /obtener_saldo respondan correctamente al
        solicitarle un banco inexistente.
        """
        with self.app.test_client() as client:
            response = client.get('/obtener_saldo/NotBank')

            self.assertEqual(response.status, '404 NOT FOUND')
            self.assertEqual(response.get_json(), self.saldo['NotBank'])

    def test_obtener_transacciones(self):
        """
        Verifica que GET "/obtener_transacciones/" responda
        correctamente al no explicitar cantidad.
        """
        with self.app.test_client() as client:
            response = client.get('/obtener_transacciones/PepaBank')

            self.assertEqual(response.status, '200 OK')
            self.assertEqual(response.get_json(), self.transacciones['PepaBank'])

    def test_obtener_transacciones_cantidad(self):
        """
        Verifica que GET  responda con la cantidad de transacciones solicitadas.
        """
        cantidad = 3
        with self.app.test_client() as client:
            response = client.get('/obtener_transacciones/PepaBank',
                                  query_string={'cantidad': cantidad}
                                  )

            self.assertEqual(response.status, '200 OK')
            self.assertCountEqual(response.get_json()['result'],
                             self.transacciones['PepaBank']['result'][0:cantidad])

    def test_obtener_transacciones_inexistente(self):
        """
        Verifica que GET "/obtener_transacciones/" responda de
        la forma correcta ante un banco que no existe.
        """
        with self.app.test_client() as client:
            response = client.get('/obtener_transacciones/NotBank')

            self.assertEqual(response.status, '404 NOT FOUND')
            self.assertCountEqual(response.get_json(),
                             self.saldo['NotBank'])

    def test_agregar_gasto(self):
        """
        Verifica que POST "/agregar_gasto/" funcione correctamente
        al agregar un nuevo gasto válido.
        """
        banco = 'BancoDCC'
        titulo = 'Compra auto de juguete'
        monto = 12000
        with self.app.test_client() as client:
            # Para no modificar data.json
            with patch('servidor.main.dcconsumo.agregar_gasto') as ag:
                response = client.post(f'/agregar_gasto/{banco}',
                                query_string = {
                                    'titulo': titulo,
                                    'monto': monto
                                }
                )

                self.assertEqual(response.status, '200 OK')
                self.assertEqual(response.get_json(), {'msg': 'Gasto agregado'})
                ag.assert_called_once_with(banco, titulo, monto)

    def test_agregar_gasto_sin_un_argumento(self):
        """
        Verifica que el servidor no guarda los gastos sin argumentos
        (o sin uno de estos), además de devolver su respectiva response.
        """
        banco = 'BancoDCC'
        titulo = 'Compra auto de juguete'
        monto = None

        with self.app.test_client() as client:
            # Para no modificar data.json
            with patch('servidor.main.dcconsumo.agregar_gasto') as ag:
                response = client.post(f'/agregar_gasto/{banco}',
                                query_string = {
                                    'titulo': titulo,
                                    'monto': monto
                                }
                )

                self.assertEqual(response.status, '400 BAD REQUEST')
                self.assertEqual(response.get_json(), {'error': 'Faltan argumentos'})
                ag.assert_not_called()

    def test_agregar_gasto_invalido(self):
        """
        Verifica que el servidor no guarda los gastos inválidos,
        además de devolver su respectiva response.
        """
        banco = 'NotBank'
        titulo = 'Compra auto de juguete'
        monto = 30000

        with self.app.test_client() as client:
            # Para no modificar data.json
            with patch('servidor.main.dcconsumo.agregar_gasto') as ag:
                response = client.post(f'/agregar_gasto/{banco}',
                                query_string = {
                                    'titulo': titulo,
                                    'monto': monto
                                }
                )

                self.assertEqual(response.status, '404 NOT FOUND')

                self.assertEqual(response.get_json(), self.saldo['NotBank'])

                ag.assert_not_called()

    def test_ajustar_saldo(self):
        """
        Verifica que al usar PATCH "/ajustar_saldo/" el dato se actualice correctamente.
        """
        banco = 'PepaBank'
        saldo = 2000
        with self.app.test_client() as client:
            # Para no modificar data.json
            with patch('servidor.main.dcconsumo.ajustar_saldo') as ag:
                response = client.patch(f'/ajustar_saldo/{banco}',
                                query_string = {
                                    'saldo': saldo
                                }
                )

                self.assertEqual(response.status, '200 OK')

                self.assertEqual(response.get_json(), {'msg': 'Saldo ajustado'})

                ag.assert_called_once_with(banco, saldo)

    def test_ajustar_saldo_sin_un_argumento(self):
        """
        Verifica que al usar PATCH "/ajustar_saldo/" el dato se
        no actualice si es que no se entrega el nuevo saldo.
        """
        banco = 'PepaBank'
        saldo = None
        with self.app.test_client() as client:
            # Para no modificar data.json
            with patch('servidor.main.dcconsumo.ajustar_saldo') as ag:
                response = client.patch(f'/ajustar_saldo/{banco}',
                                query_string = {
                                    'saldo': saldo
                                }
                )

                self.assertEqual(response.status, '400 BAD REQUEST')
                self.assertEqual(response.get_json(), {'error': 'Faltan argumentos'})
                ag.assert_not_called()
    def test_ajustar_saldo_invalido(self):
        """
        Verifica que al usar PATCH "/ajustar_saldo/" el dato se no
        actualice si es que el banco no existe.
        """
        banco = 'NotBank'
        saldo = 3500
        with self.app.test_client() as client:
            # Para no modificar data.json
            with patch('servidor.main.dcconsumo.ajustar_saldo') as ag:
                response = client.patch(f'/ajustar_saldo/{banco}',
                                query_string = {
                                    'saldo': saldo
                                }
                )

                self.assertEqual(response.status, '404 NOT FOUND')
                self.assertEqual(response.get_json(), self.saldo[banco])
                ag.assert_not_called()

    def test_hacer_transferencia(self):
        """
        Verifica que al usar POST "/hacer_transferencia" todo funcione correctamente.
        """
        token = "SuperValidToken"
        banco = 'BancoDCC'
        dest_nombre = 'Jessica'
        dest = 1032083
        monto = 12000

        data = {
            "banco": banco,
            "destinatario": {"nombre": dest_nombre, "n_cuenta": dest},
            "monto": monto
        }
        header = {"Authorization": token}

        with self.app.test_client() as client:
            # Para no modificar data.json
            with patch('servidor.main.dcconsumo.hacer_transferencia') as ag:
                response = client.post(
                    '/hacer_transferencia',
                    json=data,
                    headers=header
                )

                self.assertEqual(response.status, '200 OK')
                self.assertEqual(response.get_json(), {'msg': 'Transferencia realizada'})
                ag.assert_called_once_with(banco, {"nombre": dest_nombre, "n_cuenta": dest}, monto)

    def test_hacer_transferencia_token_invalido(self):
        """
        Verifica que al usar POST "/hacer_transferencia" que retorne
        el error cuando el token es inválido, además de que no la guarde.
        """
        token = ''
        banco = 'BancoDCC'
        dest_nombre = 'Jessica'
        dest = 1032083
        monto = 12000

        data = {
            "banco": banco,
            "destinatario": {"nombre": dest_nombre, "n_cuenta": dest},
            "monto": monto
        }
        header = {"Authorization": token}

        with self.app.test_client() as client:
            # Para no modificar data.json
            with patch('servidor.main.dcconsumo.hacer_transferencia') as ag:
                response = client.post(
                    '/hacer_transferencia',
                    json=data,
                    headers=header
                )

                self.assertEqual(response.status, '401 UNAUTHORIZED')
                self.assertEqual(response.get_json(), {'error': 'Token invalido'})

                ag.assert_not_called()

    def test_hacer_transferencia_error_404(self):
        """
        Verifica que al usar POST "/hacer_transferencia" que retorne
        el error cuando el banco es inválido.
        """
        token = 'ValidToken'
        banco = ''
        dest_nombre = 'Jessica'
        dest = 1032083
        monto = 1300

        data = {
            "banco": banco,
            "destinatario": {"nombre": dest_nombre, "n_cuenta": dest},
            "monto": monto
        }
        header = {"Authorization": token}

        with self.app.test_client() as client:
            with patch('servidor.main.dcconsumo.hacer_transferencia',
                       side_effect=KeyError('No te BANCO')):
                response = client.post(
                    '/hacer_transferencia',
                    json=data,
                    headers=header
                )

                self.assertEqual(response.status, '404 NOT FOUND')
                self.assertEqual(response.get_json(), {'error': 'No te BANCO'})

    def test_hacer_transferencia_error_400(self):
        """
        Verifica que al usar POST "/hacer_transferencia" que retorne
        el error cuando se supera el monto máximo a transferir.
        """
        token = 'ValidToken'
        banco = 'PepaBank'
        dest_nombre = 'Jessica'
        dest = 1032083
        monto = -1300000000000

        data = {
            "banco": banco,
            "destinatario": {"nombre": dest_nombre, "n_cuenta": dest},
            "monto": monto
        }
        header = {"Authorization": token}

        with self.app.test_client() as client:
            with patch('servidor.main.dcconsumo.hacer_transferencia',
                       side_effect=ValueError('Transferencia supera el saldo de la cuenta')):
                response = client.post(
                    '/hacer_transferencia',
                    json=data,
                    headers=header
                )

                self.assertEqual(response.status, '400 BAD REQUEST')
                self.assertEqual(response.get_json(),
                                 {'error':'Transferencia supera el saldo de la cuenta'})

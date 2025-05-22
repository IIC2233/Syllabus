import pickle
import socket
import sys

from cliente.utils import Mensaje


class Cliente:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        # TODO: Parte II
        self.socket = 'Completar'

        self.acciones = {
            'consultar_deudas': self.pedir_consultar_deudas,
            'agregar_transaccion': self.pedir_agregar_transaccion,
            'desconectar_cliente': self.pedir_desconectar
        }

    def iniciar_cliente(self):
        '''
        Conecta el cliente al servidor y empieza a
        manejar el flujo del programa.
        '''
        self.conectar()
        self.manejar_flujo()

    def conectar(self):
        '''
        Conecta el cliente al servidor
        '''
        # TODO: Parte II
        print('[Cliente] Conectado al servidor.')

    def manejar_flujo(self) -> None:
        '''
        Función encargada de manejar el flujo del programa.
        Esto consiste en la interacción con el usuario y
        la comunicación con el servidor.
        '''
        while True:
            accion = self.pedir_accion()
            mensaje_solicitud = self.procesar_accion(accion)
            print(f'[Cliente] Nueva solicitud: {mensaje_solicitud}')

            self.enviar_mensaje(mensaje_solicitud)
            print('[Cliente] Solicitud enviada')

            if accion == 'desconectar_cliente':
                return

            mensaje_respuesta = self.recibir_mensaje()
            print(f'[Cliente] Respuesta solicitud: {mensaje_respuesta}')

            self.procesar_respuesta(mensaje_respuesta)


    def enviar_mensaje(self, mensaje: Mensaje) -> bytes:
        '''
        Transforma el mensaje a bytes y lo envía al servidor.
        '''
        # TODO: Parte III

    def recibir_mensaje(self) -> Mensaje:
        '''
        Recibe el mensaje y lo retorna.
        '''
        # TODO: Parte III

    def pedir_accion(self) -> str:
        '''
        Recibe la acción del usuario y llama el método encargado de la acción
        '''
        mensaje = '''
Acciones disponibles:
1) Consultar deudas
2) Agregar transacción
3) Salir
Indica 1, 2 o 3'''
        print(mensaje)
        eleccion = input('> ')

        while eleccion not in ['1', '2', '3']:
            print('Opción invalida. Indica 1, 2 o 3')
            eleccion = input('> ')

        print()

        id_accion = int(eleccion) - 1
        accion = list(self.acciones.keys())[id_accion]

        return accion

    def procesar_accion(self, accion: str) -> Mensaje:
        '''
        Llama la acción correspondiente a lo pedido en la acción.
        '''
        return self.acciones[accion]()

    # Acciones
    def pedir_consultar_deudas(self):
        '''
        Pide los argumentos y crea el mensaje encargado de la acción.
        '''
        print('Nombre a consultar:')
        usuario = input('> ')

        return Mensaje(
            accion='consultar_deudas',
            argumentos={'usuario': usuario}
        )

    def pedir_agregar_transaccion(self) -> Mensaje:
        '''
        Pide los argumentos y crea el mensaje encargado de la acción.
        '''
        print('Nombre prestador:')
        prestador = input('> ')

        print('Nombres deudores (separador por espacios):')
        deudores = input('> ').split(' ')

        print('Monto transacción:')
        gasto = int(input('> '))

        return Mensaje(
            accion='agregar_transaccion',
            argumentos={
                'prestador': prestador,
                'deudores': deudores,
                'gasto_total': gasto,
            }
        )

    def pedir_desconectar(self) -> Mensaje:
        '''
        Crea el mensaje encargado de la acción.
        '''
        return Mensaje(accion='desconectar_cliente')

    def procesar_respuesta(self, mensaje_respuesta: Mensaje):
        '''
        Procesa la respuesta recibida en el mensaje y se la muestra al cliente.
        '''
        print('')

        if mensaje_respuesta.accion == 'agregar_transaccion':
            print('Transacción agregada con éxito')

        elif mensaje_respuesta.accion == 'consultar_deudas':
            usuario = mensaje_respuesta.argumentos['usuario']
            print(f'Listado de deudas de {usuario}:')
            for usuario, monto in mensaje_respuesta.respuesta.items():
                print(f' - {usuario}: ${monto}')



if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 4160 if len(sys.argv) < 2 else int(sys.argv[1])

    cliente = Cliente(HOST, PORT)
    cliente.iniciar_cliente()

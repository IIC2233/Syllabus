import json
import os
import pickle
import socket
import sys

from threading import Thread
from typing import Any

from servidor.utils import Mensaje


class Servidor:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        # TODO: Parte II
        self.socket_servidor = 'Completar'

        self.clientes = {}
        self.contador_clientes = 0

        self.transacciones = {}
        self.path_transacciones = os.path.join('servidor', 'data.json')

        self.acciones = {
            'agregar_transaccion': self.agregar_transaccion,
            'consultar_deudas': self.consultar_deudas,
            'desconectar_cliente': self.desconectar_cliente,
        }

    # Conexión y comunicación del servidor
    def iniciar_servidor(self) -> None:
        '''
        Inicio el servidor y llama los métodos correspondientes.
        '''
        self.cargar_transacciones()
        self.bind_listen()
        self.aceptar_clientes()

    def bind_listen(self) -> None:
        '''
        Asocia el servidor al host y port dado.
        Habilita el servidor para recibir conexiones.
        '''
        # TODO: Parte II
        print(f'[Servidor] Escuchando en {self.host} : {self.port}')

    def aceptar_clientes(self) -> None:
        '''
        Acepta un nuevo cliente y lo agrega al diccionario de clientes.
        Inicia un thread que escuchará su comunicación y le responderá.
        '''
        while True:
            id_cliente = self.contador_clientes
            self.contador_clientes += 1

            # TODO: Parte II

            thread_cliente = Thread(
                target=self.manejar_flujo_cliente,
                kwargs={'id_cliente': id_cliente},
                daemon=True
            )
            thread_cliente.start()

    def manejar_flujo_cliente(self, id_cliente: int) -> None:
        '''
        Función encargada de manejar el flujo del cliente.
        '''
        print(f'[Cliente {id_cliente}] Nuevo cliente conectado')
        while True:
            mensaje_solicitud = self.recibir_mensaje(id_cliente)
            print(f'[Cliente {id_cliente}] Nueva solicitud: {mensaje_solicitud}')

            if mensaje_solicitud.accion == 'desconectar_cliente':
                self.desconectar_cliente(id_cliente)
                return

            respuesta = self.procesar_mensaje_cliente(mensaje_solicitud)
            mensaje_respuesta = self.crear_mensaje(mensaje_solicitud, respuesta)
            print(f'[Cliente {id_cliente}] Respuesta solicitud: {mensaje_respuesta}')

            self.enviar_mensaje(id_cliente, mensaje_respuesta)
            print(f'[Cliente {id_cliente}] Respuesta enviada')

    def recibir_mensaje(self, id_cliente: int) -> Mensaje:
        '''
        Recibe el mensaje y lo retorna
        '''
        # TODO: Parte III

    def procesar_mensaje_cliente(self, solicitud: Mensaje) -> Any:
        '''
        Llama la acción correspondiente a lo pedido en el mensaje y
        le entrega los argumentos presentes en el mensaje.
        '''
        func_accion = self.acciones[solicitud.accion]
        return func_accion(**solicitud.argumentos)

    def crear_mensaje(self, solicitud: Mensaje, respuesta: Any) -> Mensaje:
        '''
        Crea una instancia de Mensaje a partir de la acción del
        mensaje de solicitud y la respuesta obtenida.
        '''
        print()
        solicitud.respuesta = respuesta
        return solicitud

    def enviar_mensaje(self, id_cliente: int, mensaje: Mensaje) -> bytes:
        '''
        Transforma el mensaje a bytes y lo envía al cliente
        '''
        # TODO: Parte III

    def desconectar_cliente(self, id_cliente: int) -> None:
        '''
        Cierra el socket de un cliente y lo saca del diccionario de clientes.
        '''
        # TODO: Parte II
        del self.clientes[id_cliente]
        print(f'[Cliente {id_cliente}] Cliente desconectado')

    def cerrar_servidor(self) -> None:
        '''
        Cierra el socket y guarda las transacciones actuales.
        '''
        self.socket_servidor.close()
        self.guardar_transacciones()
        print('\n[Servidor] Cerrando programa')

    # Acciones del servidor
    def cargar_transacciones(self) -> None:
        '''
        Carga el contenido del archivo de transacciones.
        '''
        # TODO: Parte I

    def guardar_transacciones(self) -> None:
        '''
        Guarda el contenido del archivo de transacciones.
        '''
        # TODO: Parte I

    def consultar_deudas(self, usuario: str) -> dict:
        '''
        Busca las deudas de un usuario.
        '''
        if usuario not in self.transacciones:
            self.transacciones[usuario] = {}
        return self.transacciones[usuario]

    def agregar_transaccion(self, prestador: str, deudores: list, gasto_total: int) -> None:
        '''
        Agrega una nueva transacción al diccionario de transacciones.
        Una vez actualizado, guarda las transacciones en su archivo.
        '''
        gasto_ind = gasto_total / len(deudores)

        for usuario in deudores:
            if prestador == usuario:
                continue

            deudas_usuario = self.consultar_deudas(usuario)

            if prestador not in deudas_usuario:
                deudas_usuario[prestador] = 0
            deudas_usuario[prestador] += gasto_ind

        self.guardar_transacciones()



if __name__ == '__main__':
    print(
        'Iniciando programa.',
        'Utiliza "Ctrl + C" o "Cmd + C" para finalizar el programa.'
    )

    HOST = 'localhost'
    PORT = 4160 if len(sys.argv) < 2 else int(sys.argv[1])

    servidor = Servidor(HOST, PORT)
    try:
        servidor.iniciar_servidor()
    except KeyboardInterrupt:
        pass
    finally:
        servidor.cerrar_servidor()

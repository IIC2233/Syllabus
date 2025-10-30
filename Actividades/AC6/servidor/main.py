import math
import os
import pickle
import socket

from threading import Thread
from typing import Any

from servidor.utils import Mensaje


class Servidor:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        self.socket_servidor = 'Completar'  # TODO: Parte I

        self.clientes = {}
        self.contador_clientes = 0

        self.solicitudes_archivos = {}
        self.data_path = os.path.join('servidor', 'data')
        self.tamano_chunk = 6000

        self.acciones = {
            'listar_archivos': self.listar_archivos,
            'solicitar_archivo': self.solicitar_archivo,
            'solicitar_chunk': self.solicitar_chunk,
            'terminar_solicitud_archivo': self.terminar_solicitud_archivo,
            'desconectar_cliente': self.desconectar_cliente,
        }

    # Conexión y comunicación del servidor
    def iniciar_servidor(self) -> None:
        '''
        Inicio el servidor y llama los métodos correspondientes.
        '''
        self.bind_listen()
        self.aceptar_clientes()

    def bind_listen(self) -> None:
        '''
        Asocia el servidor al host y port dado.
        Habilita el servidor para recibir conexiones.
        '''
        # TODO: Parte I
        print(f'[Servidor] Escuchando en {self.host} : {self.port}')

    def aceptar_clientes(self) -> None:
        '''
        Acepta un nuevo cliente y lo agrega al diccionario de clientes.
        Inicia un thread que escuchará su comunicación y le responderá.
        '''
        while True:
            id_cliente = self.contador_clientes
            self.contador_clientes += 1

            # TODO: Parte I

            thread_cliente = Thread(
                target=self.manejar_flujo_cliente,
                kwargs={'id_cliente': id_cliente},
                daemon=True
            )
            thread_cliente.start()

    def desconectar_cliente(self, id_cliente: int) -> None:
        '''
        Cierra el socket de un cliente y lo saca del diccionario de clientes.
        '''
        # TODO: Parte I
        del self.clientes[id_cliente]
        print(f'[Cliente {id_cliente}] Cliente desconectado')

    def manejar_flujo_cliente(self, id_cliente: int) -> None:
        '''
        Función encargada de manejar el flujo del cliente.
        '''
        print(f'[Cliente {id_cliente}] Nuevo cliente conectado')
        while True:
            mensaje_solicitud = self.recibir_mensaje(id_cliente)
            print(f'[Cliente {id_cliente}] Nueva solicitud: {mensaje_solicitud}')

            if mensaje_solicitud.accion == 'desconectar_cliente':
                self.procesar_mensaje_cliente(id_cliente, mensaje_solicitud)
                return
            elif mensaje_solicitud.accion == 'terminar_solicitud_archivo':
                self.procesar_mensaje_cliente(id_cliente, mensaje_solicitud)
            else:
                respuesta = self.procesar_mensaje_cliente(id_cliente, mensaje_solicitud)
                mensaje_respuesta = self.crear_mensaje(mensaje_solicitud, respuesta)
                print(f'[Cliente {id_cliente}] Respuesta solicitud: {mensaje_respuesta}')

                self.enviar_mensaje(id_cliente, mensaje_respuesta)
                print(f'[Cliente {id_cliente}] Respuesta enviada')

    def recibir_mensaje(self, id_cliente: int) -> Mensaje:
        '''
        Recibe el mensaje y lo retorna.
        '''
        # TODO: Parte II

    def procesar_mensaje_cliente(self, id_cliente: int, solicitud: Mensaje) -> Any:
        '''
        Llama la acción correspondiente a lo pedido en el mensaje y
        le entrega los argumentos presentes en el mensaje.
        '''
        func_accion = self.acciones[solicitud.accion]
        return func_accion(id_cliente = id_cliente, **solicitud.argumentos)

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
        Transforma el mensaje a bytes y lo envía al cliente.
        '''
        # TODO: Parte II

    def cerrar_servidor(self) -> None:
        '''
        Cierra el socket y guarda las transacciones actuales.
        '''
        self.socket_servidor.close()
        print('\n[Servidor] Cerrando programa')

    # Acciones del servidor
    def listar_archivos(self, id_cliente: int):
        '''
        Retorna una lista con el nombre y peso en bytes de los archivos
        almacenados en "servidor/data".
        '''
        archivos = []

        for (_, _, nombres_archivos) in os.walk(self.data_path):
            for nombre_archivo in nombres_archivos:
                path_archivo = os.path.join(self.data_path, nombre_archivo)
                peso_archivo = os.path.getsize(path_archivo)
                archivos.append((nombre_archivo, peso_archivo))

        return archivos

    def solicitar_archivo(self, id_cliente: int, nombre_archivo: str) -> int:
        '''
        Actualiza la información de la solicitud en el diccionario 'solicitudes_archivos'.
        Retorna la cantidad de chunks que se necesitarán para enviar el archivo.
        '''
        self.solicitudes_archivos[id_cliente] = nombre_archivo

        path_archivo = os.path.join(self.data_path, nombre_archivo)
        peso_archivo = os.path.getsize(path_archivo)
        cantidad_chunks = math.ceil(peso_archivo / self.tamano_chunk)

        return cantidad_chunks

    def solicitar_chunk(self, id_cliente: int, n_chunk: int) -> bytearray | bytes:
        '''
        Lee el contenido del archivo asociado al cliente y envía los bytes
        correspondientes a ese chunk. 
        '''
        # TODO: Parte III


    def terminar_solicitud_archivo(self, id_cliente: int) -> None:
        '''
        Elimina la solicitud asociada al cliente del diccionario
        'solicitudes_archivos'. No retorna.
        '''
        del self.solicitudes_archivos[id_cliente]

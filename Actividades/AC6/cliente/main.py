import pickle
import os
import socket

from cliente.utils import Mensaje


class Cliente:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        self.socket = 'Completar'  # TODO: Parte I

        self.archivo_completo = False
        self.archivo_nombre = ''
        self.chunks_totales = 0
        self.chunk_actual = 0
        self.bytes_por_chunk = {}
        self.data_path = os.path.join('cliente', 'data')

        self.acciones = {
            'listar_archivos': self.pedir_listar_archivos,
            'solicitar_archivo': self.solicitar_archivo,
            'pedir_archivo': self.pedir_archivo_completo,
            'desconectar_cliente': self.pedir_desconectar,
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
        # TODO: Parte I
        print('[Cliente] Conectado al servidor.')

    def manejar_flujo(self) -> None:
        '''
        Función encargada de manejar el flujo del programa.
        Esto consiste en la interacción con el usuario y
        la comunicación con el servidor.
        '''
        accion = None

        while True:
            if not self.archivo_completo:
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
        # TODO: Parte II

    def recibir_mensaje(self) -> Mensaje:
        '''
        Recibe el mensaje y lo retorna.
        '''
        # TODO: Parte II

    def pedir_accion(self) -> str:
        '''
        Recibe la acción del usuario y llama el método encargado de la acción
        '''
        opciones = ['1', '2', '3', '4']
        mensaje = f'''
Acciones disponibles:
1) Listar archivos
2) Registrar solicitud archivo
3) Guardar archivo
4) Salir
Indica {', '.join(opciones)}'''
        print(mensaje)
        eleccion = input('> ')

        while eleccion not in opciones:
            print(f'''Opción invalida. Indica {', '.join(opciones)}''')
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
    def pedir_listar_archivos(self):
        '''
        Crea el mensaje encargado de la acción.
        '''
        return Mensaje(accion='listar_archivos')

    def solicitar_archivo(self) -> Mensaje:
        '''
        Pide los argumentos y crea el mensaje encargado de la acción.
        '''
        print('Nombre y extensión del archivo:')
        nombre_archivo = input('> ')

        self.archivo_nombre = nombre_archivo
        return Mensaje(
            accion='solicitar_archivo',
            argumentos={
                'nombre_archivo': nombre_archivo,
            }
        )

    def pedir_chunk(self, n_chunk=int) -> Mensaje:
        '''
        Pide los argumentos y crea el mensaje encargado de la acción.
        '''
        return Mensaje(
            accion='solicitar_chunk',
            argumentos={
                'n_chunk': n_chunk,
            }
        )

    def guardar_chunk(self, bytes_archivo=bytes) -> None:
        '''
        Pide los argumentos y crea el mensaje encargado de la acción.
        '''
        self.bytes_por_chunk[self.chunk_actual] = bytes_archivo

    def pedir_archivo_completo(self) -> Mensaje:
        '''
        Crea el mensaje encargado de pedir cada chunk del archivo.
        Adicionalmente, actualiza los atributos encargados de mantener estados.
        '''
        if not self.archivo_completo:
            self.archivo_completo = True

        return self.pedir_chunk(self.chunk_actual)

    def guardar_archivo(self) -> None:
        '''
        Crea el archivo solicitado y guarda en el todos los bytes recibidos.
        Puedes encontrar los bytes en el diccionario 'bytes_por_chunk'.
        '''
        # TODO: Parte III
    def terminar_solicitud_archivo(self) -> None:
        '''
        Reinicia los atributos a sus valores iniciales y envía un mensaje al
        servidor indicando que se terminó la solicitud del archivo.
        '''
        # TODO: Parte III

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

        if mensaje_respuesta.accion == 'listar_archivos':
            for archivo, peso in mensaje_respuesta.respuesta:
                peso_kilobytes = peso / 1000
                print(f'- {archivo} ({peso_kilobytes:.0f} bytes)')

        elif mensaje_respuesta.accion == 'solicitar_archivo':
            cantidad_chunks = mensaje_respuesta.respuesta

            self.chunks_totales = cantidad_chunks
            self.chunk_actual = 0

            print(f'Solicitud registrada. Será necesario descargar {cantidad_chunks} chunks.')

        elif mensaje_respuesta.accion == 'solicitar_chunk':
            self.guardar_chunk(mensaje_respuesta.respuesta)
            print('Chunk de bytes recibidos y guardados')

            if self.archivo_completo:
                self.chunk_actual += 1
                if self.chunk_actual >= self.chunks_totales:
                    self.guardar_archivo()
                    print(f'Archivo {self.archivo_nombre} guardado.')
                    self.terminar_solicitud_archivo()

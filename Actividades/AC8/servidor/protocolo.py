"""
Protocolo de comunicación (el mismo de la semana 11): cada mensaje se envía
precedido por 4 bytes que indican su largo, y se recibe por chunks hasta
completar ese largo.

Este archivo es idéntico en el cliente y en el servidor: ambos programas
deben hablar el mismo protocolo.
"""
import socket

TAMAÑO_CHUNK = 4096


def enviar(sock: socket.socket, mensaje: bytes) -> None:
    largo = len(mensaje).to_bytes(4, byteorder="big")
    sock.sendall(largo + mensaje)


def recibir(sock: socket.socket) -> bytes:
    largo = int.from_bytes(recibir_bytes(sock, 4), byteorder="big")
    return recibir_bytes(sock, largo)


def recibir_bytes(sock: socket.socket, cantidad: int) -> bytes:
    datos = bytearray()
    while len(datos) < cantidad:
        chunk = sock.recv(min(TAMAÑO_CHUNK, cantidad - len(datos)))
        # recv retorna b"" cuando la otra parte cerró la conexión
        if not chunk:
            raise ConnectionError("La conexión se cerró")
        datos.extend(chunk)
    return bytes(datos)

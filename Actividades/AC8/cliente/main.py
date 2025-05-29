import json
import requests
import sys

from typing import Any


class ClienteApi:
    def __init__(self, host, port) -> None:
        self.base = f'http://{host}:{port}'

    def obtener_saldo(self, banco: str | None = None) -> Any:
        # TODO: Parte II
        pass

    def obtener_transacciones(self, banco: str, cantidad: int | None = None) -> Any:
        # TODO: Parte II
        pass

    def agregar_gasto(self, banco: str, titulo: str, monto: int) -> Any:
        # TODO: Parte II
        pass

    def ajustar_saldo(self, banco: str, saldo: int) -> Any:
        # TODO: Parte II
        pass

    def hacer_transferencia(self, banco: str, dest_nombre: str,
                            dest_cuenta: int, monto: int, token: str) -> Any:
        # TODO: Parte II
        pass


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 4160 if len(sys.argv) < 2 else int(sys.argv[1])

    cliente = ClienteApi(HOST, PORT)

    print(cliente.obtener_saldo())
    print(cliente.obtener_saldo('PepaBank'))

    print(cliente.agregar_gasto('PepaBank', 'Lechuga', 2000))
    print(cliente.agregar_gasto('PepaBank', 'Gusanos', 5000))

    print(cliente.ajustar_saldo('PepaBank', 0))
    print(cliente.ajustar_saldo('PepaBank', 70000))

    print(cliente.hacer_transferencia('PepaBank', 'Luna', 10101010, 20000,
                                      'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'))

    print(cliente.obtener_transacciones('PepaBank'))
    print(cliente.obtener_transacciones('PepaBank', 2))

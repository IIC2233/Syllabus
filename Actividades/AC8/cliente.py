import sys

from cliente.main import ClienteApi


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

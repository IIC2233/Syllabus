from unittest.mock import MagicMock
from random import randint
from socket import socket, AF_INET, SOCK_STREAM, error


def get_port():
    """
    Libera el puerto entregado y retorna uno nuevo :)
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 0))
    add = sock.getsockname()
    sock.close()

    return add[1]

def assert_call_arguments(call, expected_value, expected_key):
    """
    Revisa que el llamado del método incluya el argumento esperado,
    ya sea por posición o por llave.
    """
    if isinstance(call, MagicMock):
        call = call.call_args

    if expected_value in call.args:
        return

    if expected_key in call.kwargs and \
       call.kwargs[expected_key] == expected_value:
        return

    raise AssertionError(
        f"{call} no fue llamado con el parámetros '{expected_key}' y valor {expected_value}"
    )

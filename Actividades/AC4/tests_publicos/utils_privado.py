import threading
import functools

from main import ListaUrgencias
from utils import NodoUrgencia


def timeout(seconds=10, error_message=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if error_message is None:
                final_message = (
                    "El tests no finaliza dentro del tiempo máximo asignado."
                )
            else:
                final_message = error_message

            result = [TimeoutError(final_message)]

            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    result[0] = e

            thread = threading.Thread(target=target, daemon=True)
            thread.start()
            thread.join(seconds)
            if isinstance(result[0], Exception):
                raise result[0]

            return result[0]

        return wrapper

    return decorator


def list_to_LU(lista: list, valid: bool = True) -> ListaUrgencias:
    """
    A parir de una lista se crea una LU válida si así se requiere.
    """
    if valid:
        lista = sorted(lista, reverse=True)

    LU = ListaUrgencias()

    for i, urgencia in enumerate(lista):
        if i == 0:
            LU.cabeza = NodoUrgencia(urgencia)
            actual = LU.cabeza
        else:
            actual.siguiente = NodoUrgencia(urgencia)
            actual = actual.siguiente

    return LU


def LU_to_list(LU: ListaUrgencias) -> list:
    """
    Recorre una ListaUrgencias (LU) guardando las urgencias
    en una lista.
    """

    lista_urgencias = []

    cabeza = LU.cabeza
    while cabeza:
        lista_urgencias.append(cabeza.urgencia)
        cabeza = cabeza.siguiente

    return lista_urgencias

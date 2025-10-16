import functools
import threading
import time


class ExpectedException(Exception):
    def __init__(self, message):
        super().__init__(message)


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

            result = []

            def target():
                try:
                    # Ejecutamos todo el test
                    result.append(func(*args, **kwargs))
                except Exception as e:
                    # Atrapa excepciones durante la ejecución del testo o
                    # al ejecutar los asserts
                    result.append(e)

            thread = threading.Thread(target=target, daemon=True)
            thread.start()
            thread.join(seconds)

            # Damos unos segundos para que "result" sea actualizado
            time.sleep(0.2)

            if not result:
                raise TimeoutError(final_message)
            if isinstance(result[0], Exception):
                raise result[0]
            return result[0]

        return wrapper
    return decorator

import threading
import functools


def timeout(seconds=1, error_message=None):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if error_message is None:
                final_message = f"El test no finaliza dentro del tiempo " \
                                f"máximo asignado de {seconds} segundo(s)."
            else:
                final_message = error_message

            result = [Exception(final_message)]

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

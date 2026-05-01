# type: ignore
import functools
import sys
import threading
import tracemalloc
import types
import unittest
import inspect
from typing import Any, Iterable, Sequence, Generator
from backend.nodo_ligado import NodoLigado


class IICTest(unittest.TestCase):
    """
    Clase base para pruebas unitarias que traduce los parámetros
    'first' y 'second' a 'estudiante' y 'esperada'.
    """

    def __str__(self):
        """
        Controla el nombre del test. Inyecta el encabezado de la clase antes
        del primer test, y un salto de línea simple para los demás.
        """
        base_str = super().__str__()

        # only print header once
        if not getattr(self.__class__, "_doc_clase_impreso", False):
            doc_clase = self.__class__.__doc__
            self.__class__._doc_clase_impreso = True  # pyright: ignore[reportAttributeAccessIssue]

            if doc_clase and doc_clase.strip():
                # header
                encabezado = (
                    f"\n\033[96m{'-' * 70}\033[0m\n"
                    f"\033[1;96m{self.__class__.__name__}\033[0m\n"
                    f"\033[96m{doc_clase.strip()}\n"
                    f"{'-' * 70}\033[0m\n"
                )
                return f"{encabezado}{base_str}"

        # check first test
        return f"\n{base_str}"

    def shortDescription(self) -> str | None:
        """
        Retorna la descripción del test
        """
        doc = self._testMethodDoc
        if doc and doc.strip():
            lineas = [f"    {line.strip()}" for line in doc.strip().split("\n") if line.strip()]
            doc_indented = "\n".join(lineas)

            return f"{doc_indented}\n"

        return None

    @staticmethod
    def _procesar_msg(
            estudiante: Any, esperada: Any, msg_original: Any, texto_extra: str = ""
    ) -> str:
        """
        Formatea el mensaje de error
        """
        if msg_original is not None and "Obtenido (estudiante)" in str(msg_original):
            return msg_original

        if len(str(estudiante)) < 500:
            separador = f" {texto_extra}" if texto_extra else ""
            base_msg = (
                f"\n[Error]{separador}\nObtenido (estudiante): "
                f"{estudiante}\nEsperado (esperada): {esperada}"
            )
        else:
            base_msg = ""
        return base_msg if msg_original is None else f"{msg_original}\n{base_msg}"

    # --- Igualdad Básica ---
    def assertEqual(self, estudiante: Any, esperada: Any, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg)
        super().assertEqual(estudiante, esperada, msg=msg)

    def assertNotEqual(self, estudiante: Any, esperada: Any, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg)
        super().assertNotEqual(estudiante, esperada, msg=msg)

    # --- Aproximaciones ---
    def assertAlmostEqual(
            self,
            estudiante: Any,
            esperada: Any,
            places: int | None = None,
            msg: Any = None,
            delta: Any = None,
    ) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "Los valores no son casi iguales.")
        super().assertAlmostEqual(estudiante, esperada, places=places, msg=msg, delta=delta)

    def assertNotAlmostEqual(
            self,
            estudiante: Any,
            esperada: Any,
            places: int | None = None,
            msg: Any = None,
            delta: Any = None,
    ) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "Los valores son demasiado similares.")
        super().assertNotAlmostEqual(estudiante, esperada, places=places, msg=msg, delta=delta)

    # --- Comparaciones de Magnitud ---
    def assertGreater(self, estudiante: Any, esperada: Any, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "El valor del estudiante no es mayor.")
        super().assertGreater(estudiante, esperada, msg=msg)

    def assertGreaterEqual(self, estudiante: Any, esperada: Any, msg: Any = None) -> None:
        msg = self._procesar_msg(
            estudiante, esperada, msg, "El valor del estudiante no es mayor o igual."
        )
        super().assertGreaterEqual(estudiante, esperada, msg=msg)

    def assertLess(self, estudiante: Any, esperada: Any, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "El valor del estudiante no es menor.")
        super().assertLess(estudiante, esperada, msg=msg)

    def assertLessEqual(self, estudiante: Any, esperada: Any, msg: Any = None) -> None:
        msg = self._procesar_msg(
            estudiante, esperada, msg, "El valor del estudiante no es menor o igual."
        )
        super().assertLessEqual(estudiante, esperada, msg=msg)

    # --- Colecciones y Secuencias ---
    def assertCountEqual(
            self, estudiante: Iterable[Any], esperada: Iterable[Any], msg: Any = None
    ) -> None:
        msg = self._procesar_msg(
            estudiante, esperada, msg, "Los elementos o sus cantidades no coinciden."
        )
        super().assertCountEqual(estudiante, esperada, msg=msg)

    def assertSequenceEqual(
            self,
            estudiante: Sequence[Any],
            esperada: Sequence[Any],
            msg: Any = None,
            seq_type: type[Sequence[Any]] | None = None,
    ) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "Las secuencias no son iguales.")
        super().assertSequenceEqual(estudiante, esperada, msg=msg, seq_type=seq_type)

    def assertListEqual(self, estudiante: list, esperada: list, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "Las listas no son iguales.")
        super().assertListEqual(estudiante, esperada, msg=msg)

    def assertTupleEqual(self, estudiante: tuple, esperada: tuple, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "Las tuplas no son iguales.")
        super().assertTupleEqual(estudiante, esperada, msg=msg)

    def assertSetEqual(self, estudiante: set, esperada: set, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "Los sets no son iguales.")
        super().assertSetEqual(estudiante, esperada, msg=msg)

    def assertDictEqual(self, estudiante: dict, esperada: dict, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "Los diccionarios no son iguales.")
        super().assertDictEqual(estudiante, esperada, msg=msg)

    # --- Identidad y Membresía ---
    def assertIs(self, estudiante: Any, esperada: Any, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "No son el mismo objeto en memoria.")
        super().assertIs(estudiante, esperada, msg=msg)

    def assertIsNot(self, estudiante: Any, esperada: Any, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "Son el mismo objeto en memoria.")
        super().assertIsNot(estudiante, esperada, msg=msg)

    def assertIn(self, estudiante: Any, esperada: Iterable[Any], msg: Any = None) -> None:
        if msg is None or "Obtenido (estudiante)" not in str(msg):
            base_msg = f"\n[Error] El elemento '{estudiante}' no se encontró en '{esperada}'"
            msg = base_msg if msg is None else f"{msg}\n{base_msg}"
        super().assertIn(estudiante, esperada, msg=msg)

    def assertNotIn(self, estudiante: Any, esperada: Iterable[Any], msg: Any = None) -> None:
        if msg is None or "Obtenido (estudiante)" not in str(msg):
            base_msg = f"\n[Error] El elemento '{estudiante}' no debería estar en '{esperada}'"
            msg = base_msg if msg is None else f"{msg}\n{base_msg}"
        super().assertNotIn(estudiante, esperada, msg=msg)

    def assertIsInstance(
            self, estudiante: Any, esperada: type | tuple[type, ...], msg: Any = None
    ) -> None:
        if msg is None or "Obtenido (estudiante)" not in str(msg):
            base_msg = f"\n[Error] {estudiante} no es una instancia de la clase {esperada}"
            msg = base_msg if msg is None else f"{msg}\n{base_msg}"
        super().assertIsInstance(estudiante, esperada, msg=msg)

    # --- Cadenas y RegEx ---
    def assertMultiLineEqual(self, estudiante: str, esperada: str, msg: Any = None) -> None:
        msg = self._procesar_msg(estudiante, esperada, msg, "Los textos multilínea no coinciden.")
        super().assertMultiLineEqual(estudiante, esperada, msg=msg)

    def assertRegex(self, estudiante: str, esperada: Any, msg: Any = None) -> None:
        msg = self._procesar_msg(
            estudiante,
            esperada,
            msg,
            "El texto no coincide con la expresión regular esperada.",
        )
        super().assertRegex(estudiante, esperada, msg=msg)

    # --- Booleanos y Nulos ---
    def assertTrue(self, estudiante: Any, msg: Any = None) -> None:
        if msg is None or "Obtenido (estudiante)" not in str(msg):
            base_msg = f"\n[Error] Se esperaba True, pero el estudiante devolvió: {estudiante}"
            msg = base_msg if msg is None else f"{msg}\n{base_msg}"
        super().assertTrue(estudiante, msg=msg)

    def assertFalse(self, estudiante: Any, msg: Any = None) -> None:
        if msg is None or "Obtenido (estudiante)" not in str(msg):
            base_msg = f"\n[Error] Se esperaba False, pero el estudiante devolvió: {estudiante}"
            msg = base_msg if msg is None else f"{msg}\n{base_msg}"
        super().assertFalse(estudiante, msg=msg)

    def assertIsNone(self, estudiante: Any, msg: Any = None) -> None:
        if msg is None or "Obtenido (estudiante)" not in str(msg):
            base_msg = f"\n[Error] Se esperaba None, pero el estudiante devolvió: {estudiante}"
            msg = base_msg if msg is None else f"{msg}\n{base_msg}"
        super().assertIsNone(estudiante, msg=msg)

    def assertIsNotNone(self, estudiante: Any, msg: Any = None) -> None:
        if msg is None or "Obtenido (estudiante)" not in str(msg):
            base_msg = "\n[Error] No se esperaba None, pero eso fue lo que el estudiante devolvió."
            msg = base_msg if msg is None else f"{msg}\n{base_msg}"
        super().assertIsNotNone(estudiante, msg=msg)


# ─── Helpers ──────────────────────────────────────────────────────────────────


def timeout(seconds=1, error_message=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if error_message is None:
                final_message = (
                    f"El test no finaliza dentro del tiempo "
                    f"máximo asignado de {seconds} segundo(s)."
                )
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


def max_memory(mb: float = 1.0, msg: str | None = None, debug: bool = False):
    """
    Falla el test si el pico de memoria durante su ejecución supera `mb` MB.

    Usa `tracemalloc` para medir la memoria asignada. Sirve para verificar que
    las funciones cargar_* usen memoria constante (O(1)) en vez de cargar todo
    el archivo a una lista/tupla antes de hacer yield.

    Parámetros:
        mb  (float): Límite de memoria pico en megabytes.
        msg (str):   Mensaje de error personalizado (opcional).

    Ejemplo:
        @max_memory(mb=0.5)
        def test_cargar_juguete_memoria(self):
            gen = cargar_juguete('data/XL/juguetes.csv')
            for _ in gen:   # iterar no debe acumular todo en memoria
                pass
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tracemalloc.start()
            try:
                result = func(*args, **kwargs)
            finally:
                _, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                if debug:
                    print(f"Uso de memoria: {peak / 1024 / 1024:.3f} MB en {func.__name__}")

            peak_mb = peak / 1024 / 1024
            mensaje = msg or (
                f"Uso de memoria máxima: ({peak_mb:.3f} MB) supera el límite "
                f"({mb} MB).\n"
            )
            if peak_mb > mb:
                raise AssertionError(mensaje)
            return result

        return wrapper

    return decorator


LAZY_TYPES = (types.GeneratorType,)


def indexes_of(iterator, indexes):
    """
    Recorre un iterador y hace yield de los elementos en las posiciones indicadas.
    Si -1 está en indexes, también retorna el último elemento visto.
    Siempre retorna el largo total como último valor.

    Uso: *items, largo = indexes_of(gen, [0, 24, -1])
    """
    indexes = set(indexes)
    elem = None
    i = -1
    for i, elem in enumerate(iterator):
        if i in indexes:
            yield elem
    if -1 in indexes and elem is not None:
        yield elem
    yield i + 1


def assert_es_generador(test_case: IICTest, valor, nombre: str = "la función"):
    """Verifica que `valor` sea una función generadora (GeneratorType con yield)."""
    test_case.assertTrue(
        inspect.isgeneratorfunction(valor),
        msg=(
            f"\n[Error] {nombre} debe retornar una función generadora (función con yield), "
            f"pero retornó: {type(valor).__name__}"
        )
    )

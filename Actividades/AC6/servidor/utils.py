from typing import Any


class Mensaje:
    def __init__(self, accion: str,
                 argumentos: dict | None = None,
                 respuesta: Any = None) -> None:
        if not argumentos:
            argumentos = dict()

        self.accion = accion
        self.argumentos = argumentos
        self.respuesta = respuesta

    def __str__(self):
        texto = self.accion

        if self.argumentos:
            texto += f' arg={self.argumentos}'

        if self.respuesta is not None:
            texto += f' resp={str(self.respuesta):.50s}'

        return texto

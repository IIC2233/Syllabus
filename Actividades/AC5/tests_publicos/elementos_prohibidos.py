import ast
import inspect


class ComandoProhibidoError(BaseException):
    def __init__(self, comando: str, archivo: str, linea: int, *args: object) -> None:
        mensaje = f'Se ha hecho uso de "{comando}", en: "{archivo}", line {linea}.'
        super().__init__(mensaje, *args[2:])


def revisar_comandos_prohibidos(funcion: object) -> None:
    codigo = ast.parse(inspect.getsource(funcion))
    archivo = inspect.getfile(funcion)
    linea_inicial = inspect.getsourcelines(funcion)[1] - 1

    for nodo in ast.walk(codigo):
        if hasattr(nodo, 'lineno'):
            linea = linea_inicial + nodo.lineno
        else:
            linea = linea_inicial

        if isinstance(nodo, (ast.While, ast.For, ast.List, ast.Dict, ast.Tuple, ast.Set)):
            comando = type(nodo).__name__.lower()
            raise ComandoProhibidoError(comando, archivo, linea)

        if isinstance(nodo, (ast.ListComp, ast.DictComp, ast.SetComp)):
            comando = type(nodo).__name__.lower()
            comando = comando.replace('comp', ' por comprensión')
            raise ComandoProhibidoError(comando, archivo, linea)

        if isinstance(nodo, ast.Name):
            if nodo.id in ('list', 'dict', 'set', 'tuple', 'sorted'):
                linea = linea_inicial + nodo.lineno
                raise ComandoProhibidoError(nodo.id, archivo, linea)

        if isinstance(nodo, ast.Assign):
            if isinstance(nodo.value, (ast.List, ast.Dict, ast.Tuple, ast.Set)):
                comando = type(nodo.value).__name__.lower()
                linea = linea_inicial + nodo.lineno
                raise ComandoProhibidoError(comando, archivo, linea)

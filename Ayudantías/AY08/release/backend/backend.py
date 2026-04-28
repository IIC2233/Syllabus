import os
from PyQt6.QtCore import QObject, pyqtSignal


def obtener_path_icon(usuario: str) -> str:
    icon_path = os.path.join('assets', usuario, 'icon.png')

    if not os.path.exists(icon_path):
        # no tiene carpeta o icon, usar icon default
        return os.path.join('assets', 'generic.png')

    return icon_path  # tenia icon en su carpeta, poner su icon


def obtener_biografia(usuario: str) -> str:
    biografia_path = os.path.join('assets', usuario, 'biografia.txt')

    if not os.path.exists(biografia_path):
        # no tiene carpeta o biografia, usar biografia default
        return ''

    biografia = ''
    with open(biografia_path, 'r') as bio:
        for line in bio:
            biografia += line

    return biografia  # biografia del archivo leido


def obtener_stories(usuario: str) -> list[str]:

    carpeta_stories_path = os.path.join('assets', usuario, 'stories')
    if not os.path.exists(os.path.abspath(carpeta_stories_path)) or not os.path.isdir(os.path.abspath(carpeta_stories_path)):
        return []  # no tiene carpeta, usar stories default (sin stories)

    archivos = os.listdir(carpeta_stories_path)

    stories = [os.path.abspath(os.path.join(carpeta_stories_path, f))
               for f in archivos if f.endswith('.png')]

    stories.sort(key=lambda path: int(
        os.path.splitext(os.path.basename(path))[0]))

    return stories


class Logica(QObject):
    """
    Clase que realiza la validación de la contraseña para acceder.
    """

    # TODO Parte 1: Definir señal de resultado de validación

    def __init__(self) -> None:
        super().__init__()
        directorio_backend = os.path.dirname(os.path.abspath(__file__))
        self.ruta_clave = os.path.join(directorio_backend, "clave_acceso.txt")

    def validar_o_registrar_clave(self, clave: str) -> None:
        # TODO Parte 1: Completar método

        raise NotImplementedError

    def registrar_clave(self, clave: str) -> None:
        # TODO Parte 1: Completar método

        raise NotImplementedError

    def validar_clave_existente(self, clave: str) -> None:
        # TODO Parte 1: Completar método

        raise NotImplementedError

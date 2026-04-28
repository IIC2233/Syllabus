from PyQt6.QtCore import QObject, pyqtSignal
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_perfiles import VentanaPerfiles
from frontend.ventana_perfil import VentanaPerfil
from frontend.ventana_historia import VentanaHistoria


class Frontend(QObject):

    # TODO Parte 1: Completar con senal_validar_clave

    def __init__(self, perfiles: list[str]) -> None:
        super().__init__()
        self.n_historia = 0
        self.ventana_inicio = VentanaInicio("Inicio")
        self.ventana_perfiles = VentanaPerfiles(perfiles)

        self.crear_perfiles(perfiles)
        self.crear_historias(perfiles)
        self.conectar_senales()

    def crear_perfiles(self, perfiles):
        self.ventana_perfil = {}
        for usuario in perfiles:
            self.ventana_perfil[usuario] = VentanaPerfil(usuario)

    def crear_historias(self, perfiles):
        self.historias = {}
        for perfil in perfiles:
            paths = self.ventana_perfil[perfil].historias
            self.historias[perfil] = []
            for historia in paths:
                self.historias[perfil].append(
                    VentanaHistoria(perfil, historia))

    def conectar_senales(self) -> None:
        """
        Conecta las señales entre las ventanas del frontend.

        Señales Parte 1. Completar
        La ventana de inicio debe emitir una señal para que el frontend envie la clave al backend.
        La ventana de perfiles debe emitir una señal para volver a la ventana de inicio.
        La ventana de perfiles debe emitir una señal para abrir una ventana de perfil.
        La ventana de un perfil debe emitir una señal para para volver a la ventana de perfiles

        Señales Parte 2. Ya implementadas:
        La ventana de un perfil debe emitir una señal para abrir una historia
        La ventana de una historia debe emitir una señal para pasar a la siguiente historia
        La ventana de una historia debe emitir una señal para pasar a la historia anterior_historia
        La ventana de una historia debe emitir una señal para volver a la ventana del perfil
        """

        # TODO Parte 1: Completar señales faltantes

        for nombre_usuario, perfil in self.ventana_perfil.items():
            # TODO Parte 1: Aqui también falta completar una señal...

            # Señales Parte 2 Ya implementadas. No tocar!
            perfil.senal_ver_historias.connect(self.abrir_historias)
            for historia in self.historias[nombre_usuario]:
                historia.senal_anterior_historia.connect(
                    self.anterior_historia)
                historia.senal_siguiente_historia.connect(
                    self.siguiente_historia)
                historia.senal_salir_historia.connect(self.salir_historia)

    def mostrar(self) -> None:
        self.ventana_inicio.show()

    def manejar_resultado_validacion(self, es_valida: bool, mensaje: str) -> None:
        self.ventana_inicio.mostrar_mensaje(mensaje)
        if es_valida:
            self.ventana_inicio.hide()
            self.ventana_inicio.limpiar_input()
            self.ventana_perfiles.show()

    def volver_a_inicio(self) -> None:
        """
        Maneja el comportamiento de las ventanas al volver a la ventana de inicio
        """
        self.ventana_perfiles.hide()
        for ventana_perfil in self.ventana_perfil.values():
            ventana_perfil.hide()

        self.ventana_inicio.limpiar_input()
        self.ventana_inicio.limpiar_mensaje()
        self.ventana_inicio.show()

    def abrir_perfil(self, usuario: str) -> None:
        """
        Maneja el comportamiento de las ventanas al navegar a un perfil específico
        """
        self.ventana_perfiles.hide()
        self.ventana_perfil[usuario].show()
        self.ventana_perfil[usuario].raise_()
        self.ventana_perfil[usuario].activateWindow()

    def volver_a_perfiles(self) -> None:
        """
        Maneja el comportamiento de las ventanas al navegar a la ventana de perfiles
        """
        for ventana_perfil in self.ventana_perfil.values():
            ventana_perfil.hide()
        self.ventana_perfiles.show()
        self.ventana_perfiles.raise_()
        self.ventana_perfiles.activateWindow()

    def abrir_historias(self, usuario: str):
        if len(self.historias[usuario]) == 0:
            return
        self.n_historia = 0
        self.ventana_perfil[usuario].hide()
        self.historias[usuario][self.n_historia].show()
        self.historias[usuario][self.n_historia].raise_()
        self.historias[usuario][self.n_historia].activateWindow()

    def siguiente_historia(self, usuario: str):
        if self.n_historia + 1 < len(self.historias[usuario]):
            self.historias[usuario][self.n_historia].hide()
            self.n_historia += 1
            self.historias[usuario][self.n_historia].show()
            self.historias[usuario][self.n_historia].raise_()
            self.historias[usuario][self.n_historia].activateWindow()

    def anterior_historia(self, usuario: str):
        if self.n_historia - 1 >= 0:
            self.historias[usuario][self.n_historia].hide()
            self.n_historia -= 1
            self.historias[usuario][self.n_historia].show()
            self.historias[usuario][self.n_historia].raise_()
            self.historias[usuario][self.n_historia].activateWindow()

    def salir_historia(self, usuario: str):
        self.historias[usuario][self.n_historia].hide()
        self.ventana_perfil[usuario].show()
        self.ventana_perfil[usuario].raise_()
        self.ventana_perfil[usuario].activateWindow()

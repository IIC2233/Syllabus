from frontend import main

class Backend:
    def __init__(self):
        self.ventana_principal = main.VentanaPrincipal()
        self.ventana_secundaria = main.VentanaSecundario()
        self.ventana_principal.mostrar()

    def conectar(self):
        self.ventana_principal.senal_label_seleccionado.connect(self.ventana_secundaria.mostrar_imagen)
        self.ventana_secundaria.senal_mostrar_principal.connect(self.ventana_principal.mostrar)


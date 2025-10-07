import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventanas import Inicio, Entrada, Living
from backend.logica import Procesador


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear el procesador
    procesador = Procesador()

    # Crear las ventanas
    inicio = Inicio()
    entrada = Entrada()
    living = Living()

    # Conexiones de señales entre ventanas
    inicio.senal_nueva_contrasena.connect(procesador.nueva_contrasena)
    inicio.senal_ir_entrada.connect(entrada.show)
    entrada.senal_emitir_contrasena.connect(procesador.verificar_acceso)
    entrada.senal_ir_living.connect(living.abrir_ventana)
    procesador.senal_puede_entrar.connect(entrada.recibir_verificacion)
    living.senal_volver_entrada.connect(entrada.abrir_ventana)

    # Mostrar la ventana inicial
    inicio.show()

    sys.exit(app.exec())

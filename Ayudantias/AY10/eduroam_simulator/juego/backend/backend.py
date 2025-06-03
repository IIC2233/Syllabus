from PyQt5.QtCore import QObject, pyqtSignal, QThread
import requests

class Procesardor(QObject):
    senal_clasificador = pyqtSignal(list)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Asignamos una ip y puerto
        self.url = 'http://localhost:4631'
        self.variable_nombre = None

    def nombre(self, nombre):
        # Funcion que recibe el nombre que ingresó el usuario
        if self.variable_nombre is None:
            self.variable_nombre = nombre
            print(nombre)

    def obtener_clasificador(self):
        #-----Explicación-----
        # La libreria request hace que el codigo de python se quede
        # Esperando hasta recibir una respuesta, esto hace que se congele el juego
        # Solución: debemos tenerlo separado en otro thread

        thread = QThread()

        # Defino la función que maneja la libreria request       
        def tarea():
            try:
                respuesta = requests.get(self.url + "/puntajes", timeout=5)
                clasificador = respuesta.json()
                self.senal_clasificador.emit(clasificador)
            except Exception as e:
                print(f"Error en GET: {e}")
            thread.quit()

        thread.run = tarea
        thread.start()



    def perder(self, puntaje):
        # Misma idea que en Get pero realizando una solicitud post
        thread = QThread()

        def tarea():
            try:
                contenido = {
                    "nombre": self.variable_nombre,
                    "puntaje": puntaje
                }
                requests.post(self.url + "/puntajes", json=contenido, timeout=5)
            except Exception as e:
                print(f"Error en POST: {e}")
            finally:
                self.obtener_clasificador()
                thread.quit()
        thread.run = tarea
        thread.start()

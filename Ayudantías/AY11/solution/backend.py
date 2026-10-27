from PyQt6.QtCore import QObject, pyqtSignal
#from itertools import reduce

class LogIn(QObject):
    login_result_signal = pyqtSignal(bool, str)

    def __init__(self):
        super().__init__()
        self.cuentas = {}

    def recibir_login(self, nombre, contrasena):
        if not nombre in self.cuentas:
            self.cuentas[nombre] = contrasena
            self.login_result_signal.emit(True, "Has creado tu cuenta con exito")

        elif nombre in self.cuentas and self.cuentas[nombre] == contrasena:
            self.login_result_signal.emit(True, "Has Logeado en tu cuenta con exito")

        else:
            self.login_result_signal.emit(False, "Nombre de usuario o contrasena incorrecta")




class Calculadora(QObject):
    signal_resultado = pyqtSignal(str)
    signal_pantalla = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.operacion_actual = ""

    def eliminar(self):
        self.operacion_actual = ''
        self.signal_pantalla.emit(self.operacion_actual)
        
    def procesar_boton(self, texto):
        if texto == "=":
            if self.operacion_actual:
                self.recibir_operacion(self.operacion_actual)
                self.operacion_actual = ""
            return

        self.operacion_actual += texto
        self.signal_pantalla.emit(self.operacion_actual)

    def recibir_operacion(self, operacion):
        try:
            for operador in "+-*/":
                if operador in operacion:
                    break
            else:
                return

            numero_1, numero_2 = operacion.split(operador, 1)

            numeros = (
                float(numero_1),
                float(numero_2)
            )

            operaciones = {
                "+": self.sumar,
                "-": self.restar,
                "*": self.multiplicar,
                "/": self.dividir,
            }

            resultado = operaciones[operador](*numeros)
            self.signal_resultado.emit(str(resultado))
        
        except ValueError:
            self.signal_resultado.emit("Los operandos ingresados son invalidos")

        except ZeroDivisionError:
            self.signal_resultado.emit("No se puede dividir por cero")
    
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        
        return a / b




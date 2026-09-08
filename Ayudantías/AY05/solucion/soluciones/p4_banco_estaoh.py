def registrar_operacion(metodo):
    """Decorador que loggea la ejecución y captura errores de un método."""
    def aplicar_(self, *args, **kwargs):
        print(f"\n[LOG] Intentando ejecutar: {metodo.__name__.upper()} con parámetros {args}")
        try:
            resultado = metodo(self, *args, **kwargs)
        except ValueError as e:
            print(f"[LOG] {metodo.__name__.upper()} ha fallado. Motivo: {e}")
            raise 
        else:
            print(f"[LOG] {metodo.__name__.upper()} finalizado. Nuevo estado/resultado: {resultado}")
            return resultado
    return aplicar_ 

class Cuenta:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nuevo_nombre):
        if len(nuevo_nombre.strip()) == 0:
            raise ValueError("El nombre del titular no puede estar vacío.")
        self._titular = nuevo_nombre

    @property
    def saldo(self):
        return self._saldo

    @registrar_operacion
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self._saldo += monto
        return self.saldo

    @registrar_operacion
    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a cero.")
        if monto > self._saldo:
            raise ValueError("Fondos insuficientes.")
        self._saldo -= monto
        return self.saldo

# --- EJECUCIÓN ---

cuenta = Cuenta("Juan Pérez", 1000)

print(f"Titular original: {cuenta.titular}")
cuenta.titular = "Juan Pérez Gómez"
print(f"Nuevo titular: {cuenta.titular}")

cuenta.depositar(500)
cuenta.retirar(200)

try:
    cuenta.retirar(-50)
except ValueError as e:
    print(f"Mensaje final al usuario: {e}")

try:
    cuenta.titular = ""
except ValueError as e:
    print(f"Mensaje final al usuario: {e}")
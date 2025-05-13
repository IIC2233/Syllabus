import threading
import time
import random

class CajeroAutomatico:
    # Creamos el lock para controlar el acceso al fondo
    retiro_lock = threading.Lock()

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def retirar(self, monto):
        # Usamos el lock para asegurar que no hayan retiros concurrentes
        with CajeroAutomatico.retiro_lock: 
            if monto > self.saldo: # Saldo insuficiente
                print(f"\nRetiro de {monto} no autorizado. Saldo insuficiente.")
                return False
            else:
                print(f"\nRetirando {monto}...")
                self.saldo -= monto # Efectuamos el retiro
                # Simulamos el tiempo de retiro con un tiempo aleatorio
                time.sleep(random.random())

class RetiroThread(threading.Thread): # Heredamos de Thread
    def __init__(self, cajero, nombre, monto):
        super().__init__(name=nombre) # LLamamos a la clase padre, indicando el nombre
        self.cajero = cajero
        self.monto = monto

    # Sobreescribimos el metodo run para personalizar la ejecucion del thread
    def run(self):
        for i in range(random.randint(1, 10)): # numero aleatorio de retiros
            print(f"\n{self.name}, solicitando retiro de {self.monto}...")
            self.cajero.retirar(self.monto) # Realizamos el retiro
        print(f'\n{self.name} ha terminado de procesar los retiros.')

class MonitoreoThread(threading.Thread): # Heredamos de Thread
    def __init__(self, cajero):
        # ¿Por qué daemon?
        super().__init__(daemon=True)
        self.cajero = cajero

    def run(self):
        while True:
            print(f"\nMonitoreando saldo actual: {self.cajero.saldo}")
            time.sleep(2)  # Monitorea cada 2 segundos

if __name__ == "__main__":
    # Instanciamos el cajero
    cajero = CajeroAutomatico(1000)

    # Instanciamos los threads de retiro
    agustin = RetiroThread(cajero, "Agustin", 10)
    julio = RetiroThread(cajero, "Julio", 20)
    francisca = RetiroThread(cajero, "Francisca", 30)
    carlos = RetiroThread(cajero, "Carlos", 40)
    diego = RetiroThread(cajero, "Diego", 50)

    # Instanciamos e iniciamos el thread de monitoreo
    monitoreo = MonitoreoThread(cajero)  # Daemon thread para monitoreo
    monitoreo.start()

    # Iniciamos los threads de retiro
    agustin.start()
    julio.start()
    francisca.start()
    carlos.start()
    diego.start()

    # Hacemo join a los threads de retiro
    agustin.join()
    julio.join()
    francisca.join()
    carlos.join()
    diego.join()
    # ¿Por que hacemos join? 

    print("\nTodos los retiros han sido procesados.")
    print(f"\nSaldo final: {cajero.saldo}")
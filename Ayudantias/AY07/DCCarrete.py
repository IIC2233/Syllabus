import threading
import time
import random

class Fiesta:
    def __init__(self, nombre_fiesta="Fiesta en Casa"):
        self.nombre_fiesta = nombre_fiesta
        self.lock_bano = threading.Lock()
        self.lock_pisco = threading.Lock()
        self.evento_pizzas_listas = threading.Event()
        self.evento_feliz_cumpleanos = threading.Event()
        print(f"¡Comienza la {self.nombre_fiesta}!")


    def llegan_las_pizzas(self):
        print("------------------------------------")
        print("🍕🍕🍕 ¡Llegaron las pizzas! 🍕🍕🍕")
        print("------------------------------------")
        self.evento_pizzas_listas.set()


    def momento_torta(self):
        print("\n------------------------------------")
        print("🎂 ¡Es hora de cantar el Feliz Cumpleaños! 🎂")
        print("------------------------------------")
        self.evento_feliz_cumpleanos.set()


class Persona(threading.Thread):
    def __init__(self, nombre: str, fiesta: Fiesta, descanso_seg: int):
        super().__init__(name=nombre) 
        self.nombre_persona = nombre 
        self.fiesta = fiesta
        self.descanso_seg = descanso_seg
        self.daemon = True
        self.comio_pizza = False

    def run(self):
        print(f"{self.nombre_persona} ha llegado a la {self.fiesta.nombre_fiesta}.")

        while not self.fiesta.evento_feliz_cumpleanos.is_set():
            if self.fiesta.evento_pizzas_listas.is_set() and not self.comio_pizza:
                print(f"{self.nombre_persona} está comiendo pizza. 🍕")
                time.sleep(self.descanso_seg)
                self.comio_pizza = True
                continue

            print(f"{self.nombre_persona} quiere un pisquito. 🍹")
            with self.fiesta.lock_pisco:
                print(f"LOCK PISCO: {self.nombre_persona} tiene la botella.")
                print(f"{self.nombre_persona} se está sirviendo pisco.")
                time.sleep(random.uniform(0.5, 1.5))
                print(f"{self.nombre_persona} se sirvió pisco. ¡Salud! 🥳")
            time.sleep(self.descanso_seg)

            print(f"{self.nombre_persona} quiere ir al baño. 🚻")
            with self.fiesta.lock_bano:
                print(f"LOCK BAÑO: {self.nombre_persona} está en el baño.")
                print(f"{self.nombre_persona} está usando el baño...")
                time.sleep(random.uniform(1, 3))
                print(f"{self.nombre_persona} salió del baño. ¡Qué alivio!😌")
            time.sleep(self.descanso_seg)            
            print(f"{self.nombre_persona} sigue disfrutando la fiesta...")

        print(f"🏃 {self.nombre_persona} va corriendo a cantar el cumpleaños!")


def organizar_fiesta():
    la_fiesta = Fiesta(nombre_fiesta="Fiesta Épica de Threads")
    nombres_personas = ["Julio", "Fran", "Diego", "Agustin", "Carlos"]
    threads_personas = []
    descanso_general = 2

    for nombre in nombres_personas:
        persona = Persona(nombre=nombre, fiesta=la_fiesta, descanso_seg=descanso_general)
        threads_personas.append(persona)

    tiempo_pizzas = 10
    timer_pizzas = threading.Timer(tiempo_pizzas, la_fiesta.llegan_las_pizzas)
    print(f"Las pizzas llegarán en {tiempo_pizzas} segundos...")
    timer_pizzas.start()

    for p_thread in threads_personas:
        p_thread.start()

    tiempo_para_torta = 35
    timer_cumpleanos = threading.Timer(tiempo_para_torta, la_fiesta.momento_torta)
    print(f"El feliz cumpleaños se cantará en {tiempo_para_torta} segundos...")
    timer_cumpleanos.start()

    for persona in threads_personas:
        persona.join()

    print("\n🎉🎉🎉 TODOS CANTANDO: ¡FELIZ CUMPLEAÑOS! 🎉🎉🎉")
    print(f"La {la_fiesta.nombre_fiesta} ha sido un éxito gracias a los Threads!")

if __name__ == "__main__":
    organizar_fiesta()
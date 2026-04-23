from threading import Thread, Event, Lock
from datetime import datetime, timedelta
import time
from eventos_random import (
    random_se_cae_testigo,
    random_tiempo_corriendo,
    random_tiempo_perdido
)


class Equipo:
    """
    Funciona como una lista ligada, donde cada nodo es un atleta.
    Equipo tiene una referencia a el primer y el ultimo atleta
    """

    def __init__(self, nombre: str) -> None:
        """
        Se inicializa vacio con el nombre del equipo,
        sin atletas.
        """
        self.nombre = nombre
        self.primero = None
        self.ultimo = None

    def append(self, atleta: "Atleta") -> None:
        """
        Agrega un nuevo atleta a la lista ligada de atletas
        conectandolo al final
        """
        atleta.equipo = self
        if not self.primero:
            # Cuando el equipo esta vacio
            self.primero = atleta
            self.ultimo = atleta
        else:
            # Cuando ya hay atletas
            self.ultimo.siguiente = atleta
            self.ultimo = atleta

class Atleta(Thread):
    """
    Un atleta funciona como un nodo de lista ligada.
    Tiene un nombre, un equipo al que pertenece y
    una referencia al siguiente atleta.
    También tiene un evento que indica cuando partir corriendo
    """
    def __init__(self, nombre: str, evento: Event = None) -> None:
        """
        inicializa el nombre del atleta y el evento y parte
        sin equipo y sin atleta siguiente.
        self.equipo se asigna cuando este atleta es
        agregado a un equipo
        self.siguiente se asigna cuando se agrega
        otro atleta al aquipo
        """
        super().__init__()
        self.nombre = nombre
        self.equipo = None
        self.siguiente = None
        self.evento = evento
    
    def run(self) -> None:
        """
        Simula al atleta corriendo.
        Usa time.sleep(x) para hacer que el thread espere
        x segundos.
        Usa los métodos del archivo eventos_random para
        determinar cuanto tiempo demora cada atleta en correr,
        determinar si bota el testigo, y para determinar
        cuanto tiempo pierde usando el testigo

        Si es el atleta final del equipo, registra el 
        momento de llegada usando datetime.now()
        """
        pass

class Carrera:
    """
    Maneja la logica global de la simulación de la carrera
    """
    # Diccionario con el timestamp de llegada de cada equipo
    timestamps_llegada = {}
    # Lock necesario para escribir en a timestamps_llegada
    lock_timestamps = Lock()

    def __init__(self, num_equipos = 8, atletas_por_equipo = 4) -> None:
        """
        Inicializa 8 equipos con 4 atletas cada uno.
        Luego inicializa el Event que indica el disparo inicial
        que da inicio a la carrera.
        Debes modificar este método para asignar los eventos a cada atleta
        """
        self.evento_salida = Event()
        self.equipos = {}
        for eq in range(num_equipos):
            equipo = Equipo(nombre=str(eq))
            for atl in range(atletas_por_equipo):
                atleta = Atleta(nombre=str(atl))
                equipo.append(atleta)
            self.equipos[eq] = equipo


    def simular_carrera(self) -> dict[str, timedelta]:
        """
        Simula la carrera usando el evento_salida para dar
        inicio a la carrera.
        Retorna un diccionario que contiene los nombres de los
        equipos y los tiempos.
        """
        pass

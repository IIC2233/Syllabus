class Medallista:
    # Tiene el nombre, el deporte, el tipo de medalla y el pais
    def __init__(self, nombre: str, deporte: str, medalla: str, nombre_pais: str):
        self.nombre = nombre
        self.deporte = deporte
        self.medalla = medalla
        self.nombre_pais = nombre_pais

class Pais:
    # Cuenta el puntaje de cada país y sus medallas
    def __init__(self, nombre_pais: str):
        self.nombre_pais = nombre_pais
        self.puntaje = 0
        self.oros = 0
        self.platas = 0
        self.bronces = 0

    # Agrega al contador de la medalla correspondiente y el puntaje correspondiente
    def agregar_medallista(self, medallista: Medallista):
        if medallista.medalla == "Oro":
            self.oros += 1
            self.puntaje += 5
        elif medallista.medalla == "Plata":
            self.platas += 1
            self.puntaje += 3
        elif medallista.medalla == "Bronce":
            self.bronces += 1
            self.puntaje += 1

class TablaPuntajes:
    # Tabla de resultados por países
    def __init__(self):
        # diccionario donde la key es el nombre el pais y el value es el objeto Pais
        self.paises = {}

    # Metodo para agregar un medallista a la tabla
    def agregar_medallista(self, medallista: Medallista):
        # Crear el pais si no existe
        nombre_pais = medallista.nombre_pais
        if not nombre_pais in self.paises:
            self.paises[nombre_pais] = Pais(nombre_pais)

        # Agregar el medallista al pais correspondiente
        self.paises[nombre_pais].agregar_medallista(medallista)
        

    # Ordena a los paises por puntaje en una lista y retorna la lista
    def ordenar_paises(self) -> list[Pais]:
        lista_paises = self.paises.values()
        return sorted(lista_paises, key = lambda x : x.puntaje, reverse = True)


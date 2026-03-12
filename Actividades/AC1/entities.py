def get_puntaje(pais) -> int:
    """
    Retorna el puntaje de un pais. Se usa para el método de ordenar
    """
    return pais.puntaje

class Medallista:
    """
    Tiene el nombre, el deporte, el tipo de medalla y el pais
    """
    def __init__(self, nombre: str, deporte: str, medalla: str, nombre_pais: str):
        self.nombre = nombre
        self.deporte = deporte
        self.medalla = medalla
        self.nombre_pais = nombre_pais

class Pais:
    """
    Cuenta el puntaje de cada país y sus medallas
    """
    def __init__(self, nombre_pais: str):
        self.nombre_pais = nombre_pais
        self.puntaje = 0
        self.oros = 0
        self.platas = 0
        self.bronces = 0

    def agregar_medallista(self, medallista: Medallista):
        """
        Agrega al contador de la medalla correspondiente y el puntaje correspondiente
        """
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
    def __init__(self):
        """
        Tabla de resultados por países
        """
        # lista con paises
        self.paises = []

    def agregar_medallista(self, medallista: Medallista):
        """
        Metodo para agregar un medallista a la tabla
        """
        # Crear el pais si no existe
        nombre_pais = medallista.nombre_pais
        existe = False
        for pais in self.paises:
            if nombre_pais == pais.nombre_pais:
                existe = True
                pais.agregar_medallista(medallista)
                break
        if not existe:
            nuevo_pais = Pais(nombre_pais)
            nuevo_pais.agregar_medallista(medallista)
            self.paises.append(nuevo_pais)

    def ordenar_paises(self) -> list[Pais]:
        """
        Ordena a los paises por puntaje los retorna
        """
        return sorted(self.paises, key = get_puntaje, reverse = True)


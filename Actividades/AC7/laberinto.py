from collections import namedtuple
import random

Dimensiones = namedtuple("Dimensiones", ["filas", "columnas"])

class Celda:
    """
    Una celda del laberinto y a la vez un nodo del grafo del laberinto
    Tiene una posición (fila, columna) y también una lista de conexiones.
    """
    def __init__(self, fila: int, columna: int):
        """
        Cada celda tiene fila, columna y conexiones
        """
        self.fila = fila
        self.columna = columna
        self.conexiones = []

        # El representante se usa para generar el laberinto aleatorio
        # Cada celda pertenece a 1 conjunto. Si dos celdas tienen el mismo
        # represetante, entonces son del mismo conjunto
        self.representante = self

    def buscar_representante(self) -> "Celda":
        """
        Parte del algoritmo de creación de laberintos aleatorios.
        Busca al representante hacia arriba y luego actualiza el valor
        pare optimizar. Si el representante es el mismo, solo retorna
        """
        if self.representante == self:
            return self
        
        representante = self.representante.buscar_representante()
        self.representante = representante
        return representante
    
    def __repr__(self) -> str:
        return f"({self.fila}, {self.columna})"
    
    def distancia(self, punto: "Celda") -> int:
        """
        Calcula la distancia entre la celda actual y la entregada
        Usa distancia Manhattan
        """
        return abs(self.fila - punto.fila) + abs(self.columna - punto.columna)
    
    def conexiones_ordenadas(self, fin: "Celda") -> list["Celda"]:
        """
        Ordena las conexiones segun la distancia a un punto dado
        EL ORDEN ES DE MAYOR A MENOR DISTANCIA
        """
        return sorted(self.conexiones, key = lambda x : x.distancia(fin), reverse = True)

class Laberinto:
    """
    Clase que maneja el laberinto y los construye aleatoriamente
    Usa el algorimot de Kruskal para crear un laberinto aleatorio
    y luego elimina paredes extra dependiendo de la redundancia
    especificada
    """
    def __init__(self, n_filas: int, n_columnas: int, redundancia: float = 0.1):
        """
        n_filas y n_columnas con el alto y el ancho del laberinto
        redundancia es un valor entre 0 y 1 donde 0 redundancia
        crea un laberinto son una sola solución, mientras que redundancia
        mayor a 0 elimina muros aleatorios. Redundancia 1 es una grilla cuadrada sin muros
        """
        self.dimensiones = Dimensiones(n_filas, n_columnas)
        self.grilla = [[Celda(f, c) for c in range(n_columnas)]for f in range(n_filas)]
        self.generar_laberinto_aleatorio()
        self.agregar_ciclos(redundancia)
        self.randomizar_conexiones()

    def generar_laberinto_aleatorio(self):
        """
        Genera un laberinto aleatorio usando el algoritmo de kruskal
        con orden aleatorio de muros
        """

        # Generar lista de muros: Cada muro conecta 2 celdas
        muros = []
        for fila in range(self.dimensiones.filas):
            for columna in range(self.dimensiones.columnas):
                # Desde cada celda genero un muro hacia abajo y la derecha
                # Los de arriba y la izquierda los genera la celda del otro
                # lado del muro
                if columna < self.dimensiones.columnas - 1:
                    muros.append((self.grilla[fila][columna], self.grilla[fila][columna + 1]))
                if fila < self.dimensiones.filas - 1:
                    muros.append((self.grilla[fila][columna], self.grilla[fila + 1][columna]))

        # Barajo la lista de muros para que sea aleatoria
        random.shuffle(muros)

        # Uno a uno voy "Eliminando muros", pero si las celdas ya 
        # pertenecen al mismo conjunto, entonces no lo elimino
        for muro in muros:
            representante_1 = muro[0].buscar_representante()
            representante_2 = muro[1].buscar_representante()
            if representante_1 == representante_2:
                continue

            # Si no tienen el mismo representante, entonces:
            # 1. Hago que pertenezcan al mismo conjunto actualizando 1 representante
            # 2. Conecto las celdas, eliminando el muro del laberinto
            representante_1.representante = representante_2.representante
            muro[0].conexiones.append(muro[1])
            muro[1].conexiones.append(muro[0])

    def generar_celda_aleatoria(self):
        """
        Retorna una celda aleatoria del laberinto
        """
        fila = random.randint(0, self.dimensiones.filas - 1)
        columna = random.randint(0, self.dimensiones.columnas - 1)
        return self.grilla[fila][columna]

    def agregar_ciclos(self, redundancia):
        """
        Elimina algunos muros extra para crear rutas alternativas.
        """
        if redundancia == 0:
            return

        muros_restantes = []

        for fila in range(self.dimensiones.filas):
            for columna in range(self.dimensiones.columnas):
                celda = self.grilla[fila][columna]

                # Muro a la derecha
                if columna < self.dimensiones.columnas - 1:
                    vecino = self.grilla[fila][columna + 1]
                    if vecino not in celda.conexiones:
                        muros_restantes.append((celda, vecino))

                # Muro abajo
                if fila < self.dimensiones.filas - 1:
                    vecino = self.grilla[fila + 1][columna]
                    if vecino not in celda.conexiones:
                        muros_restantes.append((celda, vecino))

        random.shuffle(muros_restantes)

        cantidad = int(len(muros_restantes) * redundancia)

        for celda1, celda2 in muros_restantes[:cantidad]:
            celda1.conexiones.append(celda2)
            celda2.conexiones.append(celda1)

    def randomizar_conexiones(self):
        """
        Reordena las conexiones de cada Celda de forma random
        """
        for fila in self.grilla:
            for celda in fila:
                random.shuffle(celda.conexiones)

    def imprimir_laberinto(self) -> None:
        """
        Imprime el laberinto usando muros
        """
        filas = self.dimensiones.filas
        columnas = self.dimensiones.columnas

        # Borde superior
        print("+" + "---+" * columnas)

        for f in range(filas):
            # Línea con paredes verticales
            linea_celdas = "|"

            # Línea con paredes horizontales
            linea_pisos = "+"

            for c in range(columnas):
                celda = self.grilla[f][c]

                # ¿Hay conexión hacia la derecha?
                if c < columnas - 1 and self.grilla[f][c + 1] in celda.conexiones:
                    linea_celdas += "    "
                else:
                    linea_celdas += "   |"

                # ¿Hay conexión hacia abajo?
                if f < filas - 1 and self.grilla[f + 1][c] in celda.conexiones:
                    linea_pisos += "   +"
                else:
                    linea_pisos += "---+"

            print(linea_celdas)
            print(linea_pisos)
 
    def obtener_celda(self, fila: int, columna: int) -> Celda:
        """
        Retorna una celda dada la fila ya la columna
        """
        return self.grilla[fila][columna]

if __name__ == "__main__":
    for redundancia in [0, 0.2, 0.4, 0.6, 0.8]:
        laberinto = Laberinto(30, 30, redundancia)
        print(f"Redundancia {redundancia}")
        laberinto.imprimir_laberinto()
        print("\n")

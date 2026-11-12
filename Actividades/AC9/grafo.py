class Grafo:
    """
    Grafo no dirigido representado mediante listas de adyacencia
    """

    def __init__(self):
        """
        El grafo tiene una lista de adyacencia y nada más
        """
        self.adyacencia = {}

    def agregar_nodo(self, nodo):
        """
        Solo agrega un nodo (si existe no hace nada)
        """
        if nodo not in self.adyacencia:
            self.adyacencia[nodo] = []

    def agregar_arista(self, origen, destino):
        """
        Si no existen los nodos, los crea
        Luego conecta de manera bidireccional
        """
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)
        if origen not in self.adyacencia[destino]:
            self.adyacencia[destino].append(origen)

    def vecinos(self, nodo):
        """
        Si un nodo no existe, se retorna una lista vacia
        """
        return self.adyacencia.get(nodo, [])

    def __len__(self):
        """
        El largo de la lista de adyacencia dice el numero
        de nodos de grafo
        """
        return len(self.adyacencia)

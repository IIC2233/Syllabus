from abc import ABC, abstractmethod



class Aldeano(ABC):
    """
    Clase base de los aldeanos del pueblo. Es una clase abstracta, por
    lo que no se espera que se instancie por si sola.
    """

    def __init__(self, nombre: str, especie: str, **kwargs) -> None:
        """
        Inicializa nombre, especie y amistad, y llama a super init para
        permitir inicializar mas facil con multiherencia
        """
        super().__init__(**kwargs)
        self.nombre = nombre
        self.especie = especie
        self.amistad = 0

    def sumar_amistad(self, puntos: int) -> None:
        """
        Suma (o resta) puntos de amistad, sin salirse del rango 0 a 100
        """
        self.amistad = max(0, min(100, self.amistad + puntos))

    @abstractmethod
    def __add__(self, regalo):
        """
        Metodo abstracto que debe ser completado en las sub clases.
        Define que pasa al regalarle algo a un aldeano.
        Retorna una Interaccion.
        """
        pass

    def __str__(self) -> str:
        """
        Representacion pensada para el usuario
        """
        return f"{self.nombre} ({self.especie}) - amistad: {self.amistad}"

    def __repr__(self) -> str:
        """
        Representacion pensada para quien programa
        """
        return (f"{type(self).__name__}(nombre='{self.nombre}', "
                f"especie='{self.especie}', amistad={self.amistad})")



class Interaccion:
    """
    Clase que registra que paso cuando un aldeano recibio un regalo
    """

    def __init__(self, aldeano: Aldeano, regalo, puntos: int) -> None:
        self.aldeano = aldeano
        self.regalo = regalo
        self.puntos = puntos

    def __str__(self) -> str:
        return (f"{self.aldeano.nombre} recibio {self.regalo.nombre} "
                f"({self.puntos:+d} de amistad)")

    def __repr__(self) -> str:
        return (f"Interaccion(aldeano='{self.aldeano.nombre}', "
                f"regalo='{self.regalo.nombre}', puntos={self.puntos})")

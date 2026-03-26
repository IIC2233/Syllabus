from abc import ABC, abstractmethod
from utils_random import elegir_gen, elegir_con_probabilidades

class Gen(ABC):
    """
    Clase base de los genes. Es una clase abstracta, por lo que no
    se espera que se instancie por si sola.
    """
    REGISTRO = {}

    def __init__(self, rasgo: str, valor: str, **kwargs) -> None:
        """
        Inicializa rasgo y valor, y llama a super init
        para permitir inicializar mas facil con multiherencia
        """
        super().__init__(**kwargs)
        self.rasgo = rasgo
        self.valor = valor

    @classmethod
    def registrar(cls, subclase: type["Gen"]) -> None:
        """
        Metodo de clase usado para registrar las sub clases finales
        en la variable de clase REGISTRO
        """
        instancia = subclase()
        rasgo = instancia.rasgo
        valor = instancia.valor

        if rasgo not in cls.REGISTRO:
            cls.REGISTRO[rasgo] = {}

        cls.REGISTRO[rasgo][valor] = subclase

    @abstractmethod
    def __add__(self, other: type["Gen"]) -> type["ParDeGenes"]:
        """
        Metodo abstracto que debe ser completado en las sub clases
        """
        pass

    def __repr__(self) -> str:
        """
        Al imprimir un Gen, se imprime el valor
        """
        return self.valor

class Mutable(ABC):
    """
    Clase abstracta que se puede agregar a un gen para hacerlo mutable
    """
    def __init__(self, **kwargs) -> None:
        """
        Se inicializan las probabilidades de mutar usando el metodo 
        get_probabilidades_mutar e cada sub clase que herede de Mutar.
        Tambien de llama a super init para facilitar inicializacion con
        multiherencia
        """
        super().__init__(**kwargs)
        self.probabilidades_mutar = self.get_probabilidades_mutar()

    def mutar_random(self) -> str:
        """
        Elige un nuevo valor para el gen basado en las probabilidades
        de mutar
        """
        return elegir_con_probabilidades(self.probabilidades_mutar)
    
    @abstractmethod
    def get_probabilidades_mutar(self) -> list[tuple[str, float]]:
        """
        Metodo abstracto que debe ser implementado en las sub clases 
        que hereden de Mutable.
        El valor de retorno es una lista con tuplas de probabilidades que suman 1.
        Por ejemplo [("Verdes": 0.1), ("Azules": 0.2), ("Cafes": 0.7)]
        """
        pass

class ParDeGenes:
    """
    Clase que modela el comportamniento de 2 genes juntos
    """
    def __init__(self, gen1: Gen, gen2: Gen, fenotipo: str) -> None:
        """
        Cada par de genes se expresa a traves del fenotipo.
        El fenotipo se obtiene al sumar los 2 genes.
        Inicializa par_de_genes, rasgo y fenotipo.
        """
        self.par_de_genes = (gen1, gen2)
        self.rasgo = gen1.rasgo
        self.fenotipo = fenotipo

    def elegir_alelo_aleatorio(self) -> Gen:
        """
        Elige uno de los 2 genes aleatorios (50% cada uno).
        En el caso de que el gen elegido sea mutable, ve si este muta
        dependiendo de las probabilidades.
        """
        gen = self.par_de_genes[elegir_gen()]
        if isinstance(gen, Mutable):
            rasgo = gen.rasgo
            valor_nuevo = gen.mutar_random()
            return Gen.REGISTRO[rasgo][valor_nuevo]()
        return gen
    
    def __repr__(self) -> str:
        """
        Al imprimir un ParDeGenes se muestra el fenotipo
        """
        return self.fenotipo
        
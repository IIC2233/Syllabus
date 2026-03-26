from bases import Mutable
from dominancia import Dominante, Recesivo, Codominante

class PeloBlanco(Recesivo):
    """
    Es un gen recesivo
    """
    def __init__(self) -> None:
        """
        Llama a super init para llamar a init de la clase padre
        """
        super().__init__(rasgo="pelo", valor="Blanco")

class PeloNegro(Dominante):
    """
    Es un gen dominante
    """
    def __init__(self) -> None:
        """
        Llama a super init para llamar a init de la clase padre
        """
        super().__init__(rasgo="pelo", valor="Negro")

class OjosAzules(Codominante):
    """
    Es un gen codominante
    """
    def __init__(self) -> None:
        """
        Llama a super init para llamar a init de la clase padre
        """
        super().__init__(rasgo="ojos", valor="Azules")

class OjosVerdes(Codominante):
    """
    Es un gen codominante
    """
    def __init__(self) -> None:
        """
        Llama a super init para llamar a init de la clase padre
        """
        super().__init__(rasgo="ojos", valor="Verdes")

class OjosCafes(Dominante):
    """
    Es un gen dominante
    """
    def __init__(self) -> None:
        """
        Llama a super init para llamar a init de la clase padre
        """
        super().__init__(rasgo="ojos", valor="Cafes")

class OrejasLargas(Codominante):
    """
    Es un gen codominante
    """
    def __init__(self) -> None:
        """
        Llama a super init para llamar a init de la clase padre
        """
        super().__init__(rasgo="orejas", valor="Largas")

class OrejasCortas(Codominante):
    """
    Es un gen codominante
    """
    def __init__(self) -> None:
        """
        Llama a super init para llamar a init de la clase padre
        """
        super().__init__(rasgo="orejas", valor="Cortas")

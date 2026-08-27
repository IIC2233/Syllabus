from bases import Aldeano, Interaccion
from regalo import Regalo

PRECIO_CARO = 5000


class Cascarrabias(Aldeano):
    """
    Aldeanos a los que solo los impresionan los regalos caros
    """

    def __add__(self, regalo: Regalo) -> Interaccion:
        """
        POR COMPLETAR (Parte 3):
        """
        pass


class Alegre(Aldeano):
    """
    Aldeanos que agradecen cualquier regalo, y que se vuelven locos
    con la fruta
    """

    def __add__(self, regalo: Regalo) -> Interaccion:
        """
        POR COMPLETAR (Parte 3)
        """
        pass


class Presumida(Aldeano):
    """
    Aldeanos que solo valoran la ropa, y que ademas exigen que sea cara
    """

    def __add__(self, regalo: Regalo) -> Interaccion:
        """
        POR COMPLETAR (Parte 3)
        """
        pass

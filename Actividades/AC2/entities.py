from collections import namedtuple

# Namedtupe que contiene 2 elementos: name (nombre de la persona) y
# award_name (nombre del premio)
Winner = namedtuple('Winner', ('name', 'award_name'))

class AwardStatistics:
    """
    Clase encargada de calcular estadisticas de ganadores de premios (awards)
    """

    def __init__(self):
        """
        Por completar: Inicializa las Estructuras de datos que necesites
        para la clase para poder contestar las consultas eficientemente
        """

    def add_winner(self, name: str, award_name: str) -> None:
        """
        Por completar: Agrega nuevos ganadores de premios
        """

    def get_top_winner(self) -> tuple[str, int]:
        """
        Por completar: retorna el nombre de la persona con más premios en
        total, y el número de premios.
        En caso de empate retorna cualquiera.
        """

    def get_top_winner_in_award(self, award_name: str) -> tuple[str, int]:
        """
        Por completar: retorna el nombre de la persona con más premios
        del premio indicado (award_name) y el número correspondiente.
        En caso de empate retorna cualquiera.
        """
    def get_all_winners_in_award(self, award_name: str) -> set[str]:
        """
        Por completar: retorna un set con todos los ganadores del premio
        indicado (award_name)
        """

    def get_egot_winners(self) -> set[str]:
        """
        Por completar: retorna un set con los nombres de las personas
        que han ganado un EGOT (Emmy, Grammy, Oscar, Tony)
        """
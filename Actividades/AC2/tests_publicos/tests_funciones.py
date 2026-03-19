import unittest
from entities import AwardStatistics
from pathlib import Path
from utils import read_file, AWARD_NAMES


class VerificarFunciones(unittest.TestCase):
    """
    Clase que revisa que los resultados sean correctos con los tests publicos
    """

    def load_data(self):
        """
        Crea la clase AwardStatistics y lee el archivo
        """
        stats = AwardStatistics()

        for award in AWARD_NAMES:
            path = Path("data", award + ".csv")
            winners = read_file(path, award)
            for winner in winners:
                stats.add_winner(*winner)

        return stats

    def test_get_top_winner(self):
        """
        Testea el funcionamiento correcto del metodo get_top_winner
        """

        stats = self.load_data()
        name, wins = stats.get_top_winner()

        valid_winners = {
            "Alan Menken"
        }

        self.assertEqual(wins, 12)
        self.assertIn(name, valid_winners)


    def test_get_top_winner_in_award(self):
        """
        Testea el funcionamiento correcto del metodo get_top_winner_in_award en cada premio.
        """

        stats = self.load_data()

        name, wins = stats.get_top_winner_in_award("Oscar")

        valid_winners = {
            "Alan Menken",
            "Anthony Hopkins",
            "Denzel Washington",
            "Frances McDormand",
            "John Legend",
            "Leonardo DiCaprio",
            "Meryl Streep",
            "Natalie Portman",
            "Tom Hanks",
            "Whoopi Goldberg"
        }

        self.assertEqual(wins, 3)
        self.assertIn(name, valid_winners)

        test_cases = [
            ("Bryan Cranston", "Emmy"),
            ("Lin-Manuel Miranda", "Tony"),
            ("Taylor Swift", "Grammy")
        ]

        for expected_name, award in test_cases:
            with self.subTest(award=award):
                # Para evitar verificar empates otro agregamos otro Winner del mismo.
                stats.add_winner(expected_name, award)
                name, wins = stats.get_top_winner_in_award(award)

                self.assertEqual(wins, 4)
                self.assertEqual(name, expected_name)

    def test_get_all_winners_in_award(self):
        """
        Testea el funcionamiento correcto del metodo get_all_winners_in_award
        """

        stats = self.load_data()

        winners = stats.get_all_winners_in_award("Oscar")

        expected = {
            "Tom Hanks",
            "Leonardo DiCaprio",
            "Meryl Streep",
            "Denzel Washington",
            "Natalie Portman",
            "Anthony Hopkins",
            "Frances McDormand",
            "John Legend",
            "Whoopi Goldberg",
            "Andrew Lloyd Webber",
            "Tim Rice",
            "Elton John",
            "Rita Moreno",
            "Jennifer Hudson",
            "Alan Menken",
            "Scott Rudin",
            "Robert Lopez",
            "Mel Brooks",
            "Audrey Hepburn",
            "Mike Nichols"
        }

        self.assertEqual(winners, expected)


    def test_get_egot_winners(self):
        """
        Testea el funcionamiento correcto del metodo get_egot_winners
        """

        stats = self.load_data()

        egot = stats.get_egot_winners()

        expected = {
            "Whoopi Goldberg",
            "John Legend",
            "Andrew Lloyd Webber",
            "Tim Rice",
            "Elton John",
            "Audrey Hepburn",
            "Mel Brooks",
            "Mike Nichols",
            "Rita Moreno",
            "Jennifer Hudson",
            "Alan Menken",
            "Scott Rudin",
            "Robert Lopez"
        }

        self.assertEqual(egot, expected)

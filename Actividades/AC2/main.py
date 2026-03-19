from pathlib import Path
from utils import read_file, AWARD_NAMES
from entities import AwardStatistics

if __name__ == "__main__":
    # Crear clase de estadisticas
    award_statistics = AwardStatistics()

    # Lee los 4 archivos de ganadores y los agrega a award_statistics
    for award in AWARD_NAMES:
        path = Path("data", award + ".csv")
        winners = read_file(path, award)
        for winner in winners:
            award_statistics.add_winner(*winner)

    # Descomenta para probar cada consulta
    # print(award_statistics.get_top_winner())
    # print(award_statistics.get_top_winner_in_award("Oscar"))
    # print(award_statistics.get_all_winners_in_award("Emmy"))
    # print(award_statistics.get_egot_winners())

     

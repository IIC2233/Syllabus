from pathlib import Path
from entities import Winner

AWARD_NAMES = ["Oscar", "Emmy", "Grammy", "Tony"]

def read_file(path: Path, award: str) -> list[Winner]:
    """
    Lee el archivo en el path dado y retorna la lista de winners.
    Notar como usando la namedtuple Winner se puede leer el contenido
    del archivo de manera eficiente y ordenada
    """
    winners = []
    with path.open("r") as file:
        for line in file.readlines():
            artist_name = line.strip()
            winner = Winner(artist_name, award)
            winners.append(winner)

    return winners
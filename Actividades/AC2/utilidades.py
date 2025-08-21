from collections import namedtuple

# Cada instancia del tipo Anime tendrá usará esta namedtuple
Anime = namedtuple('Anime', ["nombre", "capitulos", "puntaje",
                             "estreno", "estudio", "generos"])

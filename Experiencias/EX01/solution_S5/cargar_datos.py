from artista import ArtistaPop, ArtistaRock, ArtistaTrapChileno, ArtistaReggaeton
from suministro import Suministro


def cargar_artistas(archivo_artistas):
    lista_artistas = []
    with open(archivo_artistas, "r", encoding="utf-8") as datos_artistas:
        for artista in datos_artistas:
            artista = artista.split(";")
            if artista[1] == "Pop":
                cantante = ArtistaPop(artista[0], artista[1], int(artista[2]),
                                      artista[3])
                lista_artistas.append(cantante)
            elif artista[1] == "Rock":
                cantante = ArtistaRock(artista[0], artista[1], int(artista[2]),
                                       artista[3])
                lista_artistas.append(cantante)
            elif artista[1] == "Trap Chileno":
                cantante = ArtistaTrapChileno(artista[0], artista[1], int(artista[2]),
                                      artista[3])
                lista_artistas.append(cantante)
            elif artista[1] == "Reggaeton":
                cantante = ArtistaReggaeton(artista[0], artista[1],
                                            int(artista[2]), artista[3])
                lista_artistas.append(cantante)
    return lista_artistas


def cargar_suministros(archivo_suministros):
    lista_suministros = []
    with open(archivo_suministros, "r", encoding="utf-8") as datos_suministros:
        datos_suministros.readline()
        for suministro in datos_suministros:
            suministro = suministro.split(";")
            objeto_suministro = Suministro(suministro[0], int(suministro[1]))
            lista_suministros.append(objeto_suministro)
    return lista_suministros

def print_medallista(medallista) -> None:
    """
    imprimir a una medallista
    """
    print(f"{medallista.nombre} logró el {medallista.medalla} olímpico en {medallista.deporte} representando a {medallista.nombre_pais}")

def print_pais(pais) -> None:
    """
    imprimir resultados de 1 país
    """
    print(f"{pais.nombre_pais} ({pais.puntaje})")
    print(f"Oros = {pais.oros}, Platas = {pais.platas}, Bronces = {pais.bronces}")

def print_puntajes(paises) -> None:
    """
    Imprime la lista de paises
    """
    for pais in paises:
        print_pais(pais)
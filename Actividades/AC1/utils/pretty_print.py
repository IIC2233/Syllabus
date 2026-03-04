# imprimir a una medallista
def print_medallista(medallista) -> None:
    print(f"{medallista.nombre} logró el {medallista.medalla} olímpico en {medallista.deporte} representando a {medallista.nombre_pais}")

# imprimir resultados de 1 país
def print_pais(pais) -> None:
    print(f"{pais.nombre_pais} ({pais.puntaje})")
    print(f"Oros = {pais.oros}, Platas = {pais.platas}, Bronces = {pais.bronces}")

# Imprime la lista de paises
def print_puntajes(paises) -> None:
    for pais in paises:
        print_pais(pais)
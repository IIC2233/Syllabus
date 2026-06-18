import sys
from pathlib import Path
import pyrematch as REmatch

def consulta1(texto_wiki: str) -> list[str]:
    return []

def consulta2(texto_wiki: str) -> list[str]:
    return []

def consulta3(texto_wiki: str) -> list[str]:
    return []

def consulta4(texto_wiki: str) -> list[str]:
    return []

def consulta5(texto_wiki: str) -> list[str]:
    return []

def consulta6(texto_wiki: str) -> list[str]:
    return []


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Debes pasar un parámetro")
        sys.exit(1)

    nombre_wiki = sys.argv[1]
    archivo = Path("wikis") / f"{nombre_wiki}.txt"

    if not archivo.exists():
        print(f"No existe el archivo '{archivo}'")
        sys.exit(1)

    texto_wiki = archivo.read_text(encoding="utf-8")

    print("# Consulta 1")
    for i in consulta1(texto_wiki):
        print(i)
    print("")
    print("# Consulta 2")
    for i in consulta2(texto_wiki):
        print(i)
    print("")
    print("# Consulta 3")
    for i in consulta3(texto_wiki):
        print(i)
    print("")
    print("# Consulta 4")
    for i in consulta4(texto_wiki):
        print(i)
    print("")
    print("# Consulta 5")
    for i in consulta5(texto_wiki):
        print(i)
    print("")
    print("# Consulta 6")
    for i in consulta6(texto_wiki):
        print(i)

    
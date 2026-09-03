from clases.fabrica import Caja


def codigo_valido(codigo: str) -> bool:
    """Retorna True si el código tiene el formato CJA-XXXX."""
    return (
        len(codigo) == 8
        and codigo.startswith("CJA-")
        and all(caracter in "0123456789" for caracter in codigo[4:])
    )


def cargar_cajas(ruta: str) -> list[Caja]:
    """Lee el archivo y retorna las cajas en el orden en que aparecen."""
    cajas = []

    with open(ruta, encoding="utf-8") as archivo:
        next(archivo)
        for linea in archivo:
            if not linea.strip():
                continue
            codigo, nombre, peso = linea.rstrip("\n").split(",")
            cajas.append(Caja(codigo.strip(), nombre.strip(), peso.strip()))

    return cajas

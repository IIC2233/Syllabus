def imprimir_mapa(celdas, vacio="-", cell_w=3):

    if not celdas:
        print("+---+\n| ∅ |\n+---+")
        return

    filas = len(celdas)
    columnas = len(celdas[0])

    def celda_char(v):
        if not v or v == []: return vacio
        if isinstance(v, list): return str(v[0])[0].upper() if v else vacio
        return str(v)[0].upper()
    tabla = [[celda_char(v) for v in fila] for fila in celdas]
    idx_w = max(1, len(str(filas - 1)))
    cell_w = max(2, int(cell_w))

    def border(char="-"):
        parts = ["+" + (char * idx_w)]
        for i in range(columnas):
            parts.append("+" + (char * cell_w))
        return "".join(parts) + "+"

    def row(celdas, is_header=False):
        left = f"|{celdas[0]:^{idx_w}}"
        rest = "".join(f"|{c:^{cell_w}}" for c in celdas[1:])
        return left + rest + "|"

    print(border("-"))
    header_cells = [""] + [str(i) for i in range(columnas)]
    print(row(header_cells, is_header=True))
    print(border("="))

    for y, fila in enumerate(tabla):
        celdas_fila = [str(y)] + fila
        print(row(celdas_fila))
        print(border("-"))

loot_cofres = [
    "diamante",
    "redstone",
    "estrella",
    "moneda",
    "espada",
    "pocion",
    "pokeball",
    "rupias",
    "seta",
    "escudo",
    "espada"
]

probabilidad_loot = {
    "diamante": 0.2,
    "redstone": 0.35,
    "estrella": 0.5,
    "moneda": 0.1,
    "espada": 0.4,
}



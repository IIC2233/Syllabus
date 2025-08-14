# imprimir al usuario
def print_usuario(usuario) -> None:
    if usuario.suscripcion:
        print(f"> Usuario con suscripcion. Puntos: {usuario.puntos}")
    else:
        print(f"> Usuario sin suscripcion. Puntos: {usuario.puntos}")

# imprimir la canasta
def print_canasta(usuario) -> None:
    print("> Canasta actual del usuario:")
    for i in range(len(usuario.canasta)):
        print(
            f"\t{i + 1}) {usuario.canasta[i].nombre}: "
            f"${usuario.canasta[i].precio} / {usuario.canasta[i].puntos} puntos"
        )

# imprimir todos los items de la lista
def print_items(items) -> None:
    print("> Items para elegir:")
    for i in range(len(items)):
        print(
            f"{i+1}) {items[i].nombre}: ${items[i].precio} / {items[i].puntos} puntos"
        )
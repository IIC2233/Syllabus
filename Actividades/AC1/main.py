from regalo import Regalo
from aldeanos import Cyrano, Rosie, Peanut, Whitney, TomNook, Canela

if __name__ == "__main__":
    # Esta seccion es tuya: agrega aca las pruebas que quieras para
    # revisar que tu codigo funciona. Los ejemplos de mas abajo son
    # solo un punto de partida, borralos o modificalos libremente.

    ###### Parte 1: regalos ######
    manzana = Regalo("Manzana", "fruta", 250)
    vestido = Regalo("Vestido de gala", "ropa", 8600)

    print(f"Regalo: {manzana}")
    print(f"Lista de regalos: {[manzana, vestido]}")

    manzana.precio = 400
    print(f"Precio actualizado: {manzana}")

    manzana.precio = -100
    print(f"Despues de un precio invalido: {manzana}")

    ###### Parte 2: aldeanos ######
    # Crea a los otros aldeanos e imprimelos con print() y con repr()
    cyrano = Cyrano()
    print(cyrano)
    print(repr(cyrano))

    ###### Parte 3: regalarle cosas a un aldeano ######
    # Prueba cada personalidad con regalos de distinta categoria y precio
    print(cyrano + manzana)
    print(cyrano)

    '''

    El Output esperado de estos inputs son: 

    Regalo: Manzana (250)

    Lista de regalos:
    [Regalo(nombre='Manzana', categoria='fruta', precio=250), Regalo(nombre='Vestido de gala', categoria='ropa', precio=8600)]

    Precio actualizado: Manzana (400)

    [Aviso] -100 no es un precio valido (0 a 500000). Se mantiene 400.

    Despues de un precio invalido: Manzana (400)

    Cyrano (oso hormiguero) - amistad: 0

    Cyrano(nombre='Cyrano', especie='oso hormiguero', amistad=0)

    Cyrano recibio Manzana (-5 de amistad)

    Cyrano (oso hormiguero) - amistad: 0

    '''



import random
from collections import defaultdict

inventario = {}
precios = {} 
with open("productos.txt", "r") as acciones_file:
    for line in acciones_file.readlines():
        values = line.strip().split(",")
        inventario[values[0]] = int(values[2])
        precios[values[0]] = int(values[1])

usuarios = [f"{str(i)*8}-{i}" for i in range(1,10)]

carros = defaultdict(dict)

for i in range(2000):
    usuario = random.choice(usuarios)

    acciones = [
        "Agregar al carro",
        "Sacar del carro",
        "Cerrar sesion",
        "Pagar"
    ]
    probs = [
        1,
        0.3,
        0.05,
        0.1
    ]
    accion = random.choices(acciones, probs, k = 1)[0]
    
    if accion == "Agregar al carro":
        objetos = list(inventario.keys())
        pesos = list(map(lambda x : inventario[x] + 5, objetos))
        item = random.choices(objetos, pesos, k = 1)[0]
        print(f"Agregar al carro,{usuario},{item}")
        if inventario[item] > 0:
            inventario[item] -= 1
    elif accion == "Sacar del carro":
        print(f"Sacar del carro,{usuario}")
    elif accion == "Cerrar sesion":
        print(f"Cerrar sesion,{usuario}")
    else:
        print(f"Pagar,{usuario}")
    
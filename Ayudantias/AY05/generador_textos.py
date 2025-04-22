import random
import string

def generar_gastos_area(area:str, filas:int):
    lineas = {"presupuestos": [],
              "gastos": []}
    
    for _ in range(filas):
        actual = random.randint(10000, 1000000)
        lineas["presupuestos"].append(actual)
    presupuesto_a_gastar = sum(lineas["presupuestos"])

    for _ in range(filas - 1):
        actual = random.randint(1, presupuesto_a_gastar//10)
        presupuesto_a_gastar -= actual
        lineas["gastos"].append(actual)
    
    lineas["gastos"].append(presupuesto_a_gastar - random.randint(1,1000))

    resultado = list(map(lambda x, y: [area, str(x), str(y)], lineas["presupuestos"], lineas["gastos"]))

    return resultado

def linea_encriptada(linea):
    linea = ";".join(linea)[::-1]
    nueva_linea = ""
    for letra in linea:
        nueva_linea += letra
        nueva_linea += random.choice(string.ascii_letters)
    return nueva_linea + "\n"


areas = ["Administracion", "Marketing", "TI","Operaciones", "Recursos Humanos", "Ventas", "Legal", "Finanzas", "Produccion"]


archivo_final = []
for area in areas:
    archivo_final += generar_gastos_area(area, 30)
random.shuffle(archivo_final)

with open("gastos_por_area.csv", "w") as archivo:
    archivo.write("area;presupuesto;monto_gastado_realmente\n")
    for linea in archivo_final:
        archivo.write(linea_encriptada(linea))

    

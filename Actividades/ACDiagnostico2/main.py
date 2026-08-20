import os
import collections

if __name__ == "__main__":
    carpeta = input("Ingrese nombre de carpeta: ")
    productos_path = os.path.join(carpeta, "productos.txt")
    acciones_path = os.path.join(carpeta, "acciones.txt")

    # Aqui se leen los productos
    # Por completar: Crear inventario
    with open(productos_path, "r") as productos_file:
        for producto_line in productos_file.readlines():
            valores = producto_line.strip().split(",")
            nombre = valores[0]
            precio = int(valores[1])
            cantidad = int(valores[2])

    # Aqui se leen las acciones
    # Por completar: Hacer las acciones
    with open(acciones_path, "r") as acciones_file:
        for accion_line in acciones_file.readlines():
            valores = accion_line.strip().split(",")
            accion = valores[0]
            rut = valores[1]
            if accion == "Agregar al carro":
                nombre_producto = valores[2]
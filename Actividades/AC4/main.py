from utilidades import imprimir_reporte



if __name__ == "__main__":
    # COMPLETAR Parte 3: instancia la Cocina y guárdala en la variable "cocina".
    # Luego, simula el servicio y guarda lo que retorna en "resultado".
    cocina = None
    resultado = None

    if resultado is None:
        print("\nsimular_servicio() no retornó nada: debe retornar la tupla "
              "(tiempos, no_entregados).")
    else:
        tiempos, no_entregados = resultado
        imprimir_reporte(cocina.pedidos, tiempos, no_entregados)

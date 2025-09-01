from dccpalooza import DCCPalooza
from cargar_datos import cargar_artistas, cargar_suministros
from random import choice

from parametros import (ANIMO_MINIMO, PUBLICO_ACCION, PUBLICO_FIN_ARTISTA,
                        PUBLICO_HIT)


def menu_inicio():
    while True:
        print(" MENU DE INICIO ".center(80, "="))
        print("Selecciona una opción")
        print("[1] Ingresar")
        print("[0] Salir :c")

        opcion = input("Indique su opción: ")

        if opcion == "1":  # Ingresar
            dccpalooza = DCCPalooza()
            todos_artistas = cargar_artistas('artistas.csv')
            dccpalooza.artistas = todos_artistas
            for artista in dccpalooza.artistas:
                print(artista.nombre)
            dccpalooza.asignar_lineup()
            lista_suministros = cargar_suministros('suministros.csv')
            dccpalooza.suministros = lista_suministros
            menu_palooza(dccpalooza)

        elif opcion == "0":  # Salir
            print("Vuelve pronto!")
            break

        else:
            print("La opción ingresada no es válida")


def menu_palooza(dccpalooza):
    while dccpalooza.funcionando:
        print(f" MENU DÍA {dccpalooza.dia} ".center(80, "="))
        print("Selecciona un artista")
        contador = 1
        for artista in dccpalooza.line_up:
            print(f"[{contador}] {artista.nombre} ")
            contador += 1
        print(f'[{contador}] Estado del Concierto')
        contador += 1
        print(f'[{contador}] Pasar Día')

        op = input("Seleccione la opción: ")

        if 0 < int(op) <= len(dccpalooza.line_up):
            artista = dccpalooza.line_up[int(op) - 1]
            dccpalooza.artista_actual = artista
            menu_artista(artista, dccpalooza)

        elif (
            len(dccpalooza.line_up) < int(op) <= len(dccpalooza.line_up) + 2
             ):
            if op == str(len(dccpalooza.line_up) + 1):
                dccpalooza.imprimir_estado()
            else:
                dccpalooza.nuevo_dia()
                dccpalooza.asignar_lineup()

        else:
            print("La opción ingresada no es válida")
    if not dccpalooza.exito_del_concierto:
        print("El concierto se ha quedado sin la cantidad de público "
              "mínima para funcionar, FIN DEL JUEGO :(")
    else:
        print(f"Felicitaciones! Lograste coordinar con éxito el "
              f"DCCPalooza. Público final: {dccpalooza.cant_publico}")


def menu_artista(artista, dccpalooza):
    op = None
    while dccpalooza.funcionando and op != "-1":
        print(" MENU DEL ARTISTA ".center(80, "="))
        print(f"{artista}")
        print(f"¿Qué debe hacer con {artista.nombre}?")
        print("[1] Acción")
        print("[2] Cantar Hit")
        print("[p] Pedir suministro")
        print("[e] Estado del concierto")
        print("[-1] Terminar presentación del artista")
        print("\n")

        op = input("Indique su opción: ")

        if op == "-1":  # Volver atrás
            dccpalooza.line_up.remove(artista)
            dccpalooza.cant_publico -= PUBLICO_FIN_ARTISTA
            print(f"{artista.nombre} terminó su presentación. "
                  f"Se fueron sus fans del concierto...")

        elif op == "p":  # Pasar de día
            artista.recibir_suministros(choice(dccpalooza.suministros))

        elif op == "1" or op == "2":
            if artista.animo >= ANIMO_MINIMO:
                if op == "1":  # Accion
                    artista.ejecutar_accion()
                    dccpalooza.cant_publico += PUBLICO_ACCION
                elif op == "2":  # Cantar hit
                    artista.cantar_hit()
                    dccpalooza.cant_publico += PUBLICO_HIT
                dccpalooza.ejecutar_evento()
            else:
                print("El artista no tiene el animo"
                      " para realizar esas acciones.")

        elif op == "e":
            dccpalooza.imprimir_estado()

        else:
            print("La opción ingresada no es válida.")


if __name__ == '__main__':
    menu_inicio()

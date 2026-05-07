from cliente import Cliente

def menu(cliente: Cliente):
    """
    Un menú simple para permitir al almumno ver los controles
    y sus preguntas y elegir las respuestas
    """
    while True:
        print("\n=== MENU ===")
        print("1. Ver controles")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Lista de controles
            code, controles = cliente.get_controles()
            if code != 200:
                print("Error obteniendo controles")
                continue
            if not controles:
                print("No hay controles disponibles")
                continue

            # Elegir control
            print("\nControles disponibles:")
            for i, c in enumerate(controles):
                print(f"{i}. {c}")
            seleccion = input("Elige un control (número): ")
            idx = int(seleccion)
            nombre_control = controles[idx]
            code, data = cliente.get_preguntas_control(nombre_control)
            if code != 200:
                print("Error obteniendo el control:")
                print(data)
                continue

            # Iterar por las preguntas
            preguntas = data.get("preguntas", [])
            respuestas = []
            print(f"\n=== {nombre_control} ===")
            for indice, pregunta in enumerate(preguntas):
                print(f"\nPregunta {indice + 1}: {pregunta['enunciado']}")
                for num_alternativa, alternativa in enumerate(pregunta["alternativas"]):
                    print(f"  {num_alternativa + 1}. {alternativa}")

                while True:
                    respuesta = input("Tu respuesta (número): ")
                    r_int = int(respuesta) - 1
                    if 0 <= r_int < len(pregunta["alternativas"]):
                        respuestas.append(r_int)
                        break
                    print("Respuesta inválida, intenta de nuevo")

            # Enviar respuestas
            code, msg = cliente.post_respuestas_control(
                nombre_control,
                respuestas,
                cliente.usuario
            )

            print("\nRespuesta del servidor:", msg)

        elif opcion == "2":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    host = "http://localhost"
    port = 4444
    nombre = input("Ingresa tu nombre: ")
    cliente = Cliente(host, port, nombre)
    menu(cliente)
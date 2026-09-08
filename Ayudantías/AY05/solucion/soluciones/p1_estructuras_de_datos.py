from collections import namedtuple, deque


Sistema = namedtuple("Sistema", ["normales", "preferentes", "preferentes_seguidos"])


def crear_sistema():
    return Sistema(deque(), deque(), [0])


def recibir_cliente(sistema, cliente, es_preferente):
    if es_preferente:
        sistema.preferentes.append(cliente)
    else:
        sistema.normales.append(cliente)
    return sistema


def atender_cliente(sistema):
    hay_preferentes = len(sistema.preferentes) > 0
    hay_normales = len(sistema.normales) > 0
    seguidos = sistema.preferentes_seguidos[0]

    if hay_preferentes and (seguidos < 4 or not hay_normales):
        sistema.preferentes.popleft()
        sistema.preferentes_seguidos[0] = seguidos + 1
    elif hay_normales:
        sistema.normales.popleft()
        sistema.preferentes_seguidos[0] = 0

    return sistema


def simular_torneo(obtener_personas, obtener_ganador):
    personas = set(obtener_personas())
    victorias = 0
    distribucion_jugadores = dict()

    while len(personas) != 1:
        ganadores = set()
        derrotados = set()
        pendiente = None

        for persona in personas:
            if pendiente is None:
                pendiente = persona
                continue

            ganador = obtener_ganador(pendiente, persona)

            if ganador == pendiente:
                ganadores.add(pendiente)
                derrotados.add(persona)
            else:
                ganadores.add(persona)
                derrotados.add(pendiente)

            pendiente = None

        distribucion_jugadores[victorias] = derrotados
        victorias += 1
        personas = ganadores

    distribucion_jugadores[victorias] = personas
    return distribucion_jugadores

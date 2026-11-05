HOST = "localhost"
PORT = 8233

# Dimensiones del juego, en píxeles
ANCHO_CANCHA = 640
ALTO_CANCHA = 400
ANCHO_PALETA = 14
ALTO_PALETA = 80
MARGEN_PALETA = 20
TAMAÑO_PELOTA = 28

# Reglas de la partida
DURACION_PARTIDA = 30  # segundos
GOLES_PARA_GANAR = 3

# Física de la pelota
TICKS_POR_SEGUNDO = 30
VELOCIDAD_INICIAL = 7  # píxeles por tick
VELOCIDAD_MAXIMA = 13  # siempre menor que ANCHO_PALETA + TAMAÑO_PELOTA
AUMENTO_POR_REBOTE = 0.5
ESPERA_SAQUE = 1.5  # segundos que la pelota espera en el centro

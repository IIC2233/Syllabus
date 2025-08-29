# Archivo de parámetros para DCCardMaster

DINERO_INICIAL_FACIL = 30
DINERO_INICIAL_NORMAL = 20
DINERO_INICIAL_DIFICIL = 15
ORO_POR_VICTORIA = 20
ORO_POR_RONDA = 5
COSTO_CURAR = 3
COSTO_REVIVIR = 1.5
COSTO_REROLL = 3
COSTO_COMBINACION = 5
MAX_CARTAS_MAZO = 5
CURE_PEPPA = 5
DEF_CAB = 10
CANNON_ABILITY = 20
DIE_PROB = 10
PROB_LARRY_GOD = 15
PROB_LARRY_MID = 20
PROB_BARB = 30
POWER_UP_BARB = 15
PROB_FIRE = 25
PROB_GLOBO = 40
DANO_BOMBA = 100
PROB_LAPIDA = 35

# Paths a los archivos de datos
import os

# Directorio base de datos
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# Archivo de cartas
ARCHIVO_CARTAS = os.path.join(DATA_DIR, 'cartas.csv')

# Archivos de IAs por dificultad
ARCHIVO_IAS_FACIL = os.path.join(DATA_DIR, 'ias_facil.csv')
ARCHIVO_IAS_NORMAL = os.path.join(DATA_DIR, 'ias_normal.csv')
ARCHIVO_IAS_DIFICIL = os.path.join(DATA_DIR, 'ias_dificil.csv')

# Archivo de multiplicadores
ARCHIVO_MULTIPLICADORES = os.path.join(DATA_DIR, 'multiplicadores.csv')

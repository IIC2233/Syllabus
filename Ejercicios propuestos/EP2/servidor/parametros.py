# Parámetros del servidor de DCCubasta.
# Puedes agregar parámetros, pero no eliminar ni renombrar los existentes.

# --- Subasta ---
MAXIMO_POSTORES = 8        # Conexiones simultáneas aceptadas.
MINIMO_POSTORES = 2        # Postores conectados necesarios para iniciar el remate.
LOTES_POR_REMATE = 6       # Lotes que se subastan en una ejecución del servidor.
DURACION_LOTE = 20         # Segundos de subasta de cada lote.
UMBRAL_EXTENSION = 5       # Si una puja llega con menos de estos segundos, el lote se extiende.
EXTENSION_LOTE = 10        # Segundos que dura cada extensión (reemplaza el tiempo restante).
MAXIMO_EXTENSIONES = 3     # Extensiones máximas por lote.
TIEMPO_ENTRE_LOTES = 5     # Segundos de pausa entre el cierre de un lote y el siguiente.
INCREMENTO_MINIMO = 100    # DCCoins mínimos sobre el precio actual para una puja válida.
COMISION_CASA = 0.05       # Fracción del precio final que paga el ganador como comisión.
TOP_RANKING = 5            # Cantidad de postores que muestra el ranking por defecto.
CATEGORIAS = ("Arte", "Antiguedades", "Tecnologia", "Coleccionables", "Rarezas")

# --- Archivos ---
RUTA_CONEXION = "conexion.json"
RUTA_LOTES = "data/lotes.csv"
RUTA_POSTORES = "data/postores.csv"
RUTA_HISTORIAL = "data/historial.csv"
RUTA_REMATES = "data/remates.json"

# --- Protocolo (deben ser idénticos en cliente y servidor) ---
BYTES_LARGO = 4            # Bytes del header con el largo del mensaje (big endian).
BYTES_NUMERO_BLOQUE = 2    # Bytes del número de bloque (little endian).
TAMANO_BLOQUE = 24         # Bytes de contenido por bloque.
CLAVE_CIFRADO = 22331103   # Se convierte a 4 bytes big endian para el cifrado.
MODULO_ROTACION = 5        # La rotación es (largo % MODULO_ROTACION) posiciones.
TAMANO_RECV = 4096         # Máximo de bytes por llamada a recv.

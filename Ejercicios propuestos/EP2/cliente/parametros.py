# Parámetros del cliente de DCCubasta.
# Puedes agregar parámetros, pero no eliminar ni renombrar los existentes.

# --- Consola ---
INTENTOS_INGRESO = 3       # Intentos de ingreso antes de que el cliente termine.
TIMEOUT_RESPUESTA = 5      # Segundos que el cliente espera una respuesta del servidor.
TOP_RANKING = 5            # Cantidad de postores que se piden a la API en el ranking.
PREFIJO_EVENTO = ">> "     # Prefijo con que se imprimen los eventos del servidor.

# --- Archivos ---
RUTA_CONEXION = "conexion.json"

# --- Protocolo (deben ser idénticos en cliente y servidor) ---
BYTES_LARGO = 4            # Bytes del header con el largo del mensaje (big endian).
BYTES_NUMERO_BLOQUE = 2    # Bytes del número de bloque (little endian).
TAMANO_BLOQUE = 24         # Bytes de contenido por bloque.
CLAVE_CIFRADO = 22331103   # Se convierte a 4 bytes big endian para el cifrado.
MODULO_ROTACION = 5        # La rotación es (largo % MODULO_ROTACION) posiciones.
TAMANO_RECV = 4096         # Máximo de bytes por llamada a recv.

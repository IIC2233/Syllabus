# importamos la librería socket
import socket

# generamos el objeto
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ponemos una tupla con (ip, puerto)
host = socket.gethostname()  # en este caso especificamos que la IP será la nuestra
port = 8726
sock.connect((host, port))

# si quiero que se entreguen todos, ocupo en vez de send, sendall
print("Entrega el mensaje que quieres enviar al servidor")
mensaje = input()
mensaje_bytes = mensaje.encode('utf-8')  # pasamos todo a bytes
sock.sendall(mensaje_bytes)

data = sock.recv(4096)  # recibimos 4096 bytes de respuesta (si sobran no importa)
print(data.decode("utf-8"))  # veamos qué nos responden

# cerramos la conexión, sino se ocupan recursos en su computador :(
# SIEMPRE CIERREN SUS CONEXIONES
sock.close()
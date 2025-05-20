import socket

mensaje_base = """
Hola! soy el servidor. Gracias por conectarte
Acabo de recibir el mensaje: """

mensaje_sin_respuesta = "Bueeenas, aquí mandando mi request para saber lo byts que se envian"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8726

sock.bind((host, port))
seguir = True
print("Inicia el servidor")

while True:
    print("Recibo usuario")
    sock.listen()
    socket_cliente, address = sock.accept()
    mensaje_bytes = socket_cliente.recv(4096)
    mensaje = mensaje_bytes.decode("utf-8")

    print(mensaje)

    # aquí manejamos la lógica del servidor
    if mensaje == "FIN":
        socket_cliente.sendall("\n Adios\n ".encode("utf-8"))  
        print("Servidor apagado")
        break

    elif mensaje == mensaje_sin_respuesta:
        pass

    else:
        mensaje = mensaje_base + mensaje
        socket_cliente.sendall(mensaje.encode("utf-8"))
        print("Acabo de enviar la respuesta")

sock.close()

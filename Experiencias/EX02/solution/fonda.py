from dccaja import CajaRegistradora
import copy
import os
import pickle

class Fonda:
    """
    Clase que representa nuestra fonda dieciochera.
    Sus métodos hacen uso de la caja registradora de la ramada.
    """

    def __init__(self, nombre: str) -> None:
        # Guardamos el nombre de la fonda
        self.nombre = nombre
        # Creamos una caja registradora (parte administrativa de la fonda)
        # El argumento "0" indica que el día parte en el día 0
        self.caja = CajaRegistradora(0)

    def _desencriptar_archivo(self, ruta_archivo: str) -> list:
        """
        Método que desencripta el archivo con los productos.
        NO MODIFICAR
        """
        with open(ruta_archivo, "rb") as archivo:
            contenido_desencriptado = pickle.load(archivo)
            return contenido_desencriptado.split("\n")

    def cargar_inventario(self, ruta_productos: str) -> None:
        """
        Carga los productos de la fonda desde un archivo y los muestra.

        INSTRUCCIONES:
        PARTE 1: Debemos modificar este método, agregando try/except o if/else
        según corresponda, para que se pueda ejecutar a pesar de los errores que
        levanta el módulo caja.
        """
        print("🥟 Cargando productos a la fonda...\n")

        # Desencriptamos el archivo con los productos
        productos = self._desencriptar_archivo(ruta_productos)

        # Recorremos cada línea (producto) desencriptado
        for item in productos:
            # Separar cada producto en nombre y precio (se espera formato "nombre,precio")
            nombre, precio = item.split(",")

            try:
                # Intentamos convertir el precio a número decimal
                precio = float(precio)
                # Si funciona, ingresamos el producto a la caja
                self.caja.ingresar_producto(nombre, precio)

            except ValueError:
                # Si no se puede convertir el precio a float → error de formato en el archivo.
                print(f"❌ Error: el precio \"{precio}\" del producto {nombre} "
                      "no es válido. No se agregará al inventario.\n")

            except Exception as e:
                # ⚠️ Nota: usar "except Exception" no es una buena práctica en general,
                # porque atrapa TODO tipo de error (incluso bugs inesperados).
                # Aquí se usa como "red de seguridad" para evitar que el programa se caiga
                # si ocurre algo raro, pero lo ideal sería manejar cada excepción específica.
                print(f"⚠️ Error inesperado al cargar {nombre}: {e}. "
                      "No se agregará al inventario.")

            else:
                # Si no hubo errores, confirmamos que se agregó al stock
                print(f"✅ {nombre} agregado al stock con precio ${precio}.")
          
        print("\n🍷 Inventario listo. ¡A celebrar!\n")

    def cliente_comprar(self, cliente: dict) -> None:
        """
        Procesa la compra de un cliente en la fonda.

        INSTRUCCIONES:
        PARTE 2: Debemos modificarlo para que funcione con la primera compra del restaurante,
        agregando los elementos faltantes que necesite. ¿Qué elementos? Veamos el detalle del
        error para descubrirlo.

        PARTE 3: Debemos seguir modificando el elemento para que funcione aunque hayan errores en 
        los pedidos. ¿Qué errores? Veamos el detalle del error para descubrirlo.
        """
        try:
            # Procesamos la compra con la caja registradora
            # Si hay problemas, aquí se lanzará una excepción
            self.caja.procesar_compra(
                cliente['nombre'], cliente['compras'], cliente['rut']
            )

        except NotADirectoryError as e:
            # Este error ocurre si la carpeta para guardar boletas no existe
            # Ejemplo: "boletas_dia0" aún no creada
            # print(dir(e))  # Usamos dir() para explorar qué atributos tiene el objeto error
            #                   y descubrir qué información podemos extraer (como e.filename)
            # print(f"e.filename = {e.filename}")  # Ruta o archivo que causó el error
            # print(f"type(e.filename) = {type(e.filename)}")

            # Importante: La ruta es boletas_dia/boletas_dia0

            # Guardamos la ruta de la carpeta o archivo faltante
            ruta = e.filename
            print(f"ruta = {ruta}")

            # Creamos la carpeta completa (incluyendo subcarpetas si las hay)
            os.makedirs(ruta, exist_ok=True)
            print(f"Carpeta {ruta} creada. Reintentando compra...")

            # Reintentamos procesar la compra una vez creada la carpeta
            self.caja.procesar_compra(
                cliente['nombre'], cliente['compras'], cliente['rut']
            )

        except KeyError as e:
            # Este error ocurre cuando un cliente intenta comprar un producto
            # que no existe en el inventario de la fonda
            print(e)
            producto_fallido = e.args[0]  # Extraemos el nombre del producto que falló
            print(
                f"❌ El producto {producto_fallido} no existe en la fonda. "
                "Se eliminará de la compra."
            )
            # Creamos una copia del cliente para modificar su lista de compras
            cliente_nuevo = copy.deepcopy(cliente)
            # Removemos el producto problemático de la lista
            cliente_nuevo["compras"].remove(producto_fallido)
            # Reintentamos la compra con la lista corregida
            self.cliente_comprar(cliente_nuevo)
        else:
            # Si no hubo errores, confirmamos que la compra fue exitosa
            print("🎉 Compra realizada con éxito. Boleta guardada.")

    def cerrar_por_el_dia(self) -> None:
        """
        Cierra la fonda por el día, mostrando estadísticas.

        INSTRUCCIONES:
        PARTE 4: El método funciona perfectamente cuando gente compra en un día.
        ¿Pero qué pasa en un día sin ventas? 
        Deberemos arreglarlo con un try/Except o un if/else.

        Hint: Ver el caso de que no haya clientes.
        """
        try:
            # Intentamos cuadrar la caja (calcular totales y estadísticas del día)
            self.caja.cuadrar_caja()

        except ZeroDivisionError:
            # Este error aparece si no hubo clientes → división por cero
            print("🍂 No hubieron clientes hoy, la caja se mantiene igual.")

        finally:
            # Siempre cerramos la caja aunque no haya habido ventas
            self.caja.cerrar_caja()


if __name__ == "__main__":
    # Creamos la fonda principal
    mi_fonda = Fonda("La Gran Fonda del DCC")

    print("\n=== Cargando inventario ===")
    ruta_productos = os.path.join("data", "productos.topsecret")

    # Cargar inventario desde archivo encriptado
    mi_fonda.cargar_inventario(ruta_productos)

    # Mostrar productos disponibles
    mi_fonda.caja.mostrar_productos()

    # Cliente 1 (compra válida)
    print("\n=== Cliente 1 ===")
    cliente_1 = {
        "nombre": "Juanito Cuequero",
        "rut": "11111111-1",
        "compras": ["Empanada de pino", "Mote con huesillo"],
    }
    mi_fonda.cliente_comprar(cliente_1)

    # Cliente 2 (ejemplo con error: producto que no existe)
    print("\n=== Cliente 2 (con error) ===")
    cliente_2 = {
        "nombre": "Rosita Huasa",
        "rut": "22222222-2",
        "compras": ["Anticucho", "Nóctulo"],  # "Nóctulo" no existe en el inventario
    }
    mi_fonda.cliente_comprar(cliente_2)

    # Cerrar el día (caja y estadísticas)
    print("\n=== Cerrar día ===")
    mi_fonda.cerrar_por_el_dia()

    # Nuevo día
    print("\n=== Nuevo día - Sin ventas ===")
    mi_fonda.cerrar_por_el_dia()
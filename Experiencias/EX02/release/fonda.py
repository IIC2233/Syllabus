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
        self.nombre = nombre
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

        productos = self._desencriptar_archivo(ruta_productos)
        for item in productos:
            nombre, precio = item.split(",")
            self.caja.ingresar_producto(nombre, precio)
          
        print("\n🍷 Inventario listo. ¡A celebrar!\n")

    def cliente_comprar(self, cliente: dict) -> None:
        """
        Procesa la compra de un cliente en la fonda.

        INSTRUCCIONES - PARTE 2:
        1. Debemos modificarlo para que funcione con la primera compra del restaurante,
        agregando los elementos faltantes que necesite. ¿Qué elementos? Veamos el detalle del
        error para descubrirlo.

        2. Debemos seguir modificando el elemento para que funcione aunque hayan errores en 
        los pedidos. ¿Qué errores? Veamos el detalle del error para descubrirlo.
        """
        self.caja.procesar_compra(
            cliente['nombre'], cliente['compras'], cliente['rut']
        )
        print("🎉 Compra realizada con éxito. Boleta guardada.")

    def cerrar_por_el_dia(self) -> None:
        """
        Cierra la fonda por el día, mostrando estadísticas.

        INSTRUCCIONES:
        PARTE 3: El método funciona perfectamente cuando gente compra en un día.
        ¿Pero qué pasa en un día sin ventas? 
        Deberemos arreglarlo con un try/Except o un if/else.

        Hint: ¿Qué pasa si no hay clientes?
        """
        self.caja.cuadrar_caja()
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

    # Cliente 1
    print("\n=== Cliente 1 ===")
    cliente_1 = {
        "nombre": "Juanito Cuequero",
        "rut": "11111111-1",
        "compras": ["Empanada de pino", "Mote con huesillo"],
    }
    mi_fonda.cliente_comprar(cliente_1)

    # Cliente 2
    print("\n=== Cliente 2 (con error) ===")
    cliente_2 = {
        "nombre": "Rosita Huasa",
        "rut": "22222222-2",
        "compras": ["Anticucho", "Nóctulo"],
    }
    mi_fonda.cliente_comprar(cliente_2)

    # Cerrar el día (caja y estadísticas)
    print("\n=== Cerrar día ===")
    mi_fonda.cerrar_por_el_dia()

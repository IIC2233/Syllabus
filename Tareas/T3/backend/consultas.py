from typing import Generator, Iterable


def cargar_usuarios(path: str) -> Generator:
    pass


def cargar_productos(path: str) -> Generator:
    pass

def cargar_ordenes(path: str) -> Generator:
    pass


def cargar_ordenes_items(path: str) -> Generator:
    pass


def cargar_proveedores(path: str) -> Generator:
    pass


def cargar_proveedores_productos(path: str) -> Generator:
    pass


# CONSULTAS


# CONSULTAS SIMPLES (1 GENERADOR)


def productos_desde_fecha(generador_productos: Generator,
                            fecha: str, inverso: bool) -> Generator:
    pass


def buscar_orden_por_contenido(generador_ordenes_items: Generator,
                  id_producto: str, cantidad: int) -> Generator:
    pass


def proveedores_por_estado(generador_proveedores: Generator,
                           estado: str) -> Generator:
    pass


def ordenes_segun_estado_orden(generador_ordenes: Generator,
                               estado_orden: str) -> Generator:
    pass


def ordenes_entre_fechas(generador_ordenes: Generator,
                         fecha_inicial: str, fecha_final: str) -> Generator:
    pass


def modificar_estado_orden_ordenes_previas_fecha(generador_ordenes: Generator,
                                                 fecha: str, cambio_estados: dict) -> Generator:
    pass


# CONSULTAS COMPLEJAS (2 o 3 GENERADORES)


def producto_mas_popular(generador_productos: Generator,
                         generador_ordenes: Generator, generador_ordenes_items: Generator,
                         fecha_inicial: str, fecha_final: str, ranking: int) -> Iterable:
    pass


def ordenes_usuario(generador_productos: Generator,
                    generador_ordenes: Generator, generador_ordenes_items: Generator,
                    ids_usuario: list) -> dict:
    pass


def valor_orden(generador_productos: Generator,
                generador_ordenes_items: Generator, id_orden: str) -> float:
    pass


def proveedores_segun_precio_productos(
    generador_productos: Generator,
    generador_proveedores: Generator,
    generador_proveedor_producto: Generator,
    precio: float
) -> list:
    pass


def precio_promedio_segun_estado_orden(generador_ordenes: Generator,
                                       generador_ordenes_items: Generator,
                                       generador_productos: Generator, estado_orden: str) -> float:
    pass


def cantidad_vendida_productos(generador_productos: Generator,
                               generador_ordenes_items: Generator, ids_productos: list) -> dict:
    pass


def ordenes_dirigidas_al_estado(generador_ordenes: Generator,
                                generador_usuarios: Generator, estado: str) -> Generator:
    pass


def ganancias_dadas_por_clientes(generador_productos: Generator,
                                 generador_ordenes: Generator, generador_ordenes_items: Generator,
                                 ids_usuarios: list) -> dict:
    pass


def modificar_estados_ordenes_dirigidas_al_estado(generador_ordenes: Generator,
                                                  generador_usuarios: Generator, estado: str,
                                                  cambio_estados_ordenes: dict) -> Generator:
    pass


def agrupar_items_por_maximo_pedido(generador_productos: Generator,
                                    generador_ordenes_items: Generator) -> Generator:
    pass

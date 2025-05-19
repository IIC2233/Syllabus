from backend.consultas import (
    cargar_usuarios,
    cargar_productos,
    cargar_ordenes,
    cargar_ordenes_items,
    cargar_proveedores,
    cargar_proveedores_productos
)

from typing import Generator


# FUNCTIONS DEFINITION

def obtener_generador_usuarios(path_dataset: str) -> Generator:
    """
    Obtiene un generador de usuarios para un dataset específico.
    
    Args:
        path_dataset (str): Path al dataset de usuarios.
    
    Returns:
        Generator: Generador de usuarios.
    """
    path = os.path.join("data", path_dataset, "usuarios.csv")
    return cargar_usuarios(path)

def obtener_generador_productos(path_dataset: str) -> Generator:
    """
    Obtiene un generador de productos para un dataset específico.
    
    Args:
        path_dataset (str): Path al dataset de productos.
    
    Returns:
        Generator: Generador de productos.
    """
    path = os.path.join("data", path_dataset, "productos.csv")
    return cargar_productos(path)


def obtener_generador_ordenes(path_dataset: str) -> Generator:
    """
    Obtiene un generador de ordenes para un dataset específico.
    
    Args:
        path_dataset (str): Path al dataset de ordenes.
    
    Returns:
        Generator: Generador de ordenes.
    """
    path = os.path.join("data", path_dataset, "ordenes.csv")
    return cargar_ordenes(path)

def obtener_generador_ordenes_items(path_dataset: str) -> Generator:
    """
    Obtiene un generador de ordenes_items para un dataset específico.
    
    Args:
        path_dataset (str): Path al dataset de ordenes_items.
    
    Returns:
        Generator: Generador de ordenes_items.
    """
    path = os.path.join("data", path_dataset, "ordenes_items.csv")
    return cargar_ordenes_items(path)

def obtener_generador_proveedores(path_dataset: str) -> Generator:
    """
    Obtiene un generador de proveedores para un dataset específico.
    
    Args:
        path_dataset (str): Path al dataset de proveedores.
    
    Returns:
        Generator: Generador de proveedores.
    """
    path = os.path.join("data", path_dataset, "proveedores.csv")
    return cargar_proveedores(path)

def obtener_generador_proveedores_productos(path_dataset: str) -> Generator:
    """
    Obtiene un generador de proveedores_productos para un dataset específico.
    
    Args:
        path_dataset (str): Path al dataset de proveedores_productos.
    
    Returns:
        Generator: Generador de proveedores_productos.
    """
    path = os.path.join("data", path_dataset, "proveedores_productos.csv")
    return cargar_proveedores_productos(path)


# TESTS KWARGS

# Test 01: productos_desde_fecha
productos_desde_fecha_S_params = {
    "generador_productos": cargar_productos("data/S/productos.csv"),
    "fecha": "2025-12-31",
    "inverso": False,
}

productos_desde_fecha_M_params = {
    "generador_productos": cargar_productos("data/M/productos.csv"),
    "fecha": "2025-12-30",
    "inverso": False,
}

productos_desde_fecha_L_params = {
    "generador_productos": cargar_productos("data/L/productos.csv"),
    "fecha": "2025-12-31",
    "inverso": False,
}

# Test 02: buscar_orden_por_contenido
buscar_orden_por_contenido_S_params = {
    "generador_ordenes_items": cargar_ordenes_items("data/S/ordenes_items.csv"),
    "id_producto": "c815c892-d334-427f-80de-0cdb89b831fa-9683",
    "cantidad": 10,
}

buscar_orden_por_contenido_M_params = {
    "generador_ordenes_items": cargar_ordenes_items("data/M/ordenes_items.csv"),
    "id_producto": "c717fb7f-b88e-4bc6-be63-0e7fbc8e2728-6663",
    "cantidad": 4,
}

buscar_orden_por_contenido_L_params = {
    "generador_ordenes_items": cargar_ordenes_items("data/L/ordenes_items.csv"),
    "id_producto": "be5b021c-97af-4143-9724-6d291273f3fe-1905",
    "cantidad": 7,
}

# Test 03: proveedores_por_estado
proveedores_por_estado_S_params = {
    "generador_proveedores": cargar_proveedores("data/S/proveedores.csv"),
    "estado": "UT",
}

proveedores_por_estado_M_params = {
    "generador_proveedores": cargar_proveedores("data/M/proveedores.csv"),
    "estado": "UT",
}

proveedores_por_estado_L_params = {
    "generador_proveedores": cargar_proveedores("data/L/proveedores.csv"),
    "estado": "UT",
}

# Test 04: ordenes_segun_estado_orden
ordenes_segun_estado_orden_S_params = {
    "generador_ordenes": cargar_ordenes("data/S/ordenes.csv"),
    "estado_orden": "shipped",
}

ordenes_segun_estado_orden_M_params = {
    "generador_ordenes": cargar_ordenes("data/M/ordenes.csv"),
    "estado_orden": "pending",
}

ordenes_segun_estado_orden_L_params = {
    "generador_ordenes": cargar_ordenes("data/L/ordenes.csv"),
    "estado_orden": "delivered",
}

# Test 05: ordenes_entre_fechas
ordenes_entre_fechas_S_params = {
    "generador_ordenes": cargar_ordenes("data/S/ordenes.csv"),
    "fecha_inicial": "2020-04-08",
    "fecha_final": "2022-12-28",
}

ordenes_entre_fechas_M_params = {
    "generador_ordenes": cargar_ordenes("data/M/ordenes.csv"),
    "fecha_inicial": "-",
    "fecha_final": "2023-11-26",
}

# Test 05: ordenes_entre_fechas
ordenes_entre_fechas_L_params = {
    "generador_ordenes": cargar_ordenes("data/L/ordenes.csv"),
    "fecha_inicial": "2022-05-12",
    "fecha_final": "-",
}


# Test 06: modificar_estado_orden_ordenes_previas_fecha
modificar_estado_orden_ordenes_previas_fecha_S_params = {
    "generador_ordenes": cargar_ordenes("data/S/ordenes.csv"),
    "cambio_estados": {'shipped': 'delivered', 'delivered': 'shipped'},
    "fecha": "2022-01-01",
}

modificar_estado_orden_ordenes_previas_fecha_M_params = {
    "generador_ordenes": cargar_ordenes("data/M/ordenes.csv"),
    "cambio_estados": {'pending': 'delivered', 'delivered': 'pending'},
    "fecha": "2023-01-07",
}

modificar_estado_orden_ordenes_previas_fecha_L_params = {
    "generador_ordenes": cargar_ordenes("data/L/ordenes.csv"),
    "cambio_estados": {'pending': 'delivered', 'delivered': 'pending'},
    "fecha": "2022-12-31",
}

# Test 07: producto_mas_popular
producto_mas_popular_S_params = {
    "generador_productos": cargar_productos("data/S/productos.csv"),
    "generador_ordenes": cargar_ordenes("data/S/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/S/ordenes_items.csv"),
    "fecha_inicial": "2023-01-01",
    "fecha_final": "2023-12-31",
    "ranking": 10,
}

producto_mas_popular_M_params = {
    "generador_productos": cargar_productos("data/M/productos.csv"),
    "generador_ordenes": cargar_ordenes("data/M/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/M/ordenes_items.csv"),
    "fecha_inicial": "2022-06-01",
    "fecha_final": "2024-07-01",
    "ranking": 8
}

producto_mas_popular_L_params = {
    "generador_productos": cargar_productos("data/L/productos.csv"),
    "generador_ordenes": cargar_ordenes("data/L/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/L/ordenes_items.csv"),
    "fecha_inicial": "2021-01-01",
    "fecha_final": "2022-12-31",
    "ranking": 5
}

# Test 08: ordenes_usuario
ordenes_usuario_S_params = {
    "generador_productos": cargar_productos("data/S/productos.csv"),
    "generador_ordenes": cargar_ordenes("data/S/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/S/ordenes_items.csv"),
    "ids_usuario": [
        'c9e1f695-3803-4412-8dca-2efabaa66461-3330',
        '3701a4ad-e134-42f9-9ce9-c34708ecec21-4885',
        'f6e288e5-84de-4422-93ea-51324099de99-5576'
    ]
}

ordenes_usuario_M_params = {
    "generador_productos": cargar_productos("data/M/productos.csv"),
    "generador_ordenes": cargar_ordenes("data/M/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/M/ordenes_items.csv"),
    "ids_usuario": [
        '03da04ce-bb63-4b88-a50b-0153bda60af6-7131',
        '6f302a00-d124-481f-955f-220d7be1e2b5-3388',
        '55ac37ae-c76b-4e4e-b4b7-1cc3302256c3-1305',
        'fe0d8e45-e21e-4df3-aa37-41c0fb6b90f1-8400'
    ]
}

ordenes_usuario_L_params = {
    "generador_productos": cargar_productos("data/L/productos.csv"),
    "generador_ordenes": cargar_ordenes("data/L/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/L/ordenes_items.csv"),
    "ids_usuario": [
        '0ab5a9f9-1395-46f7-a1a9-2675cb8b035a-3335',
        'e674b9e0-bc8e-4875-adab-5891e05b357c-4455',
        '50865e86-5a79-460f-b94f-f25edfac4c7b-7098',
        'fa40234b-4cf9-4cd9-b0b0-525cd8f2132f-7908',
        'ec054636-8040-4b1d-bfd5-7c85671f8020-9139'
    ]
}


# Test 09: valor_orden
valor_orden_S_params = {
    "generador_ordenes_items": cargar_ordenes_items("data/S/ordenes_items.csv"),
    "generador_productos": cargar_productos("data/S/productos.csv"),
    "id_orden": "89ca0f76-69de-4cf8-94c0-4e8fc280f52c-9888"
}

valor_orden_M_params = {
    "generador_ordenes_items": cargar_ordenes_items("data/M/ordenes_items.csv"),
    "generador_productos": cargar_productos("data/M/productos.csv"),
    "id_orden": "653ae671-5d19-4028-aa64-ae71b0c4089e-9748"
}

valor_orden_L_params = {
    "generador_ordenes_items": cargar_ordenes_items("data/L/ordenes_items.csv"),
    "generador_productos": cargar_productos("data/L/productos.csv"),
    "id_orden": "52a562b1-25ba-4f30-bc3a-6e6b6d91b0e9-2482"
}

# Test 10: proveedores_segun_precio_productos
proveedores_segun_precio_productos_S_params = {
    "generador_productos": cargar_productos("data/S/productos.csv"),
    "generador_proveedores": cargar_proveedores("data/S/proveedores.csv"),
    "generador_proveedor_producto": \
        cargar_proveedores_productos("data/S/proveedores_productos.csv"),
    "precio": 10.00,
}

proveedores_segun_precio_productos_M_params = {
    "generador_productos": cargar_productos("data/M/productos.csv"),
    "generador_proveedores": cargar_proveedores("data/M/proveedores.csv"),
    "generador_proveedor_producto": \
        cargar_proveedores_productos("data/M/proveedores_productos.csv"),
    "precio": 20.00,
}

proveedores_segun_precio_productos_L_params = {
    "generador_productos": cargar_productos("data/L/productos.csv"),
    "generador_proveedores": cargar_proveedores("data/L/proveedores.csv"),
    "generador_proveedor_producto": \
        cargar_proveedores_productos("data/L/proveedores_productos.csv"),
    "precio": 72.25,
}

# Test 11: precio_promedio_segun_estado_orden
precio_promedio_segun_estado_orden_S_params = {
    "generador_ordenes": cargar_ordenes("data/S/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/S/ordenes_items.csv"),
    "generador_productos": cargar_productos("data/S/productos.csv"),
    "estado_orden": "cancelled"
}

precio_promedio_segun_estado_orden_M_params = {
    "generador_ordenes": cargar_ordenes("data/M/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/M/ordenes_items.csv"),
    "generador_productos": cargar_productos("data/M/productos.csv"),
    "estado_orden": "cancelled"
}

precio_promedio_segun_estado_orden_L_params = {
    "generador_ordenes": cargar_ordenes("data/L/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/L/ordenes_items.csv"),
    "generador_productos": cargar_productos("data/L/productos.csv"),
    "estado_orden": "pending"
}

# Test 12: cantidad_vendida_productos
cantidad_vendida_productos_S_params = {
    "generador_productos": cargar_productos("data/S/productos.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/S/ordenes_items.csv"),
    "ids_productos": [
        'db0d6856-9eac-4ba7-a1c8-1f2de0936f40-8417',
        '58c3ea57-bd0d-423f-aece-b752124a6c51-3054',
        'f68497fe-1e7f-4cd4-8a8d-07ed71ee3085-4553',
        'f5eabcd8-414c-432d-be6f-9955ae2195aa-7395',
        'eaca2588-d4a5-4ad2-b42d-dd3e19b2ae12-3319'
    ]
}

cantidad_vendida_productos_M_params = {
    "generador_productos": cargar_productos("data/M/productos.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/M/ordenes_items.csv"),
    "ids_productos": [
        'de53a3ff-9daa-4fa0-bec8-c07df8ace5a1-4647',
        'a00f7779-1fc5-4c5a-988e-4a948e8dcbda-4572',
        '4edfa8b9-64f8-44c4-aafb-bdf291e84bbb-6783'
    ]
}

cantidad_vendida_productos_L_params = {
    "generador_productos": cargar_productos("data/L/productos.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/L/ordenes_items.csv"),
    "ids_productos": [
        '98c14e7b-949a-4d0d-a36b-28c47c4002ca-6816',
        '3de20c00-32cb-489e-91de-d52c0a2f2c69-4441',
        '266a1fbd-c03a-44b5-a6c1-75951f5b3d1d-3648',
        '61ffa0ae-595e-445f-ab13-fac63c84a6cc-2901',
        'e0b7cb54-e83c-485b-bacb-4e5aca22817f-4835'
    ]
}

# Test 13: ordenes_dirigidas_al_estado
ordenes_dirigidas_al_estado_S_params = {
    "generador_ordenes": cargar_ordenes("data/S/ordenes.csv"),
    "generador_usuarios": cargar_usuarios("data/S/usuarios.csv"),
    "estado": "OH"
}

ordenes_dirigidas_al_estado_M_params = {
    "generador_ordenes": cargar_ordenes("data/M/ordenes.csv"),
    "generador_usuarios": cargar_usuarios("data/M/usuarios.csv"),
    "estado": "UT"
}

ordenes_dirigidas_al_estado_L_params = {
    "generador_ordenes": cargar_ordenes("data/L/ordenes.csv"),
    "generador_usuarios": cargar_usuarios("data/L/usuarios.csv"),
    "estado": "UT"
}

# Test 14: ganancias_dadas_por_clientes
ganancias_dadas_por_clientes_S_params = {
    "generador_productos": cargar_productos("data/S/productos.csv"),
    "generador_ordenes": cargar_ordenes("data/S/ordenes.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/S/ordenes_items.csv"),
    "ids_usuarios": [
        'c9e1f695-3803-4412-8dca-2efabaa66461-3330',
        '3701a4ad-e134-42f9-9ce9-c34708ecec21-4885',
        'f6e288e5-84de-4422-93ea-51324099de99-5576',
        '3f0af282-df6a-4028-8d03-f4b56c9691f1-9610',
        '33e1ad1b-e93e-410c-8dcf-2a45e0c8bbb2-8469',
        '5a297c71-329f-4371-99c3-edc74c72a812-7307',
        '0a1af343-095a-4cc8-a3a1-34a000430078-9369',
        '271ee5ea-a64b-49ac-946d-dbd7ca86c938-1553',
        '02fa0d40-d907-4b21-8048-0dfc4746a9b9-2245',
        '912759a8-43ba-475b-b87a-2da42df463d0-6338'
    ]
}

ganancias_dadas_por_clientes_M_params = {
    "generador_ordenes": cargar_ordenes("data/M/ordenes.csv"),
    "generador_productos": cargar_productos("data/M/productos.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/M/ordenes_items.csv"),
    "ids_usuarios": [
        '03da04ce-bb63-4b88-a50b-0153bda60af6-7131',
        '6f302a00-d124-481f-955f-220d7be1e2b5-3388',
        '55ac37ae-c76b-4e4e-b4b7-1cc3302256c3-1305',
        'fe0d8e45-e21e-4df3-aa37-41c0fb6b90f1-8400',
        'a2df4492-47f1-47fc-b059-2dc3bfc3ba1f-9834'
    ]
}

ganancias_dadas_por_clientes_L_params = {
    "generador_ordenes": cargar_ordenes("data/L/ordenes.csv"),
    "generador_productos": cargar_productos("data/L/productos.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/L/ordenes_items.csv"),
    "ids_usuarios": [
        '0ab5a9f9-1395-46f7-a1a9-2675cb8b035a-3335',
        'e674b9e0-bc8e-4875-adab-5891e05b357c-4455',
        '50865e86-5a79-460f-b94f-f25edfac4c7b-7098'
    ]
}

# Test 15: modificar_estados_ordenes_dirigidas_al_estado
modificar_estados_ordenes_dirigidas_al_estado_S_params = {
    "generador_ordenes": cargar_ordenes("data/S/ordenes.csv"),
    "generador_usuarios": cargar_usuarios("data/S/usuarios.csv"),
    "estado": "OH",
    "cambio_estados_ordenes": {'pending': 'delivered', 'cancelled': 'delivered'},
}

modificar_estados_ordenes_dirigidas_al_estado_M_params = {
    "generador_ordenes": cargar_ordenes("data/M/ordenes.csv"),
    "generador_usuarios": cargar_usuarios("data/M/usuarios.csv"),
    "estado": "UT",
    "cambio_estados_ordenes": {'pending': 'shipped', 'delivered': 'cancelled'},
}

modificar_estados_ordenes_dirigidas_al_estado_L_params = {
    "generador_ordenes": cargar_ordenes("data/L/ordenes.csv"),
    "generador_usuarios": cargar_usuarios("data/L/usuarios.csv"),
    "estado": "UT",
    "cambio_estados_ordenes": {'shipped': 'delivered', 'cancelled': 'shipped'},
}


# Test 16: agrupar_items_por_maximo_pedido
agrupar_items_por_maximo_pedido_S_params = {
    "generador_productos": cargar_productos("data/S/productos.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/S/ordenes_items.csv"),
}

agrupar_items_por_maximo_pedido_M_params = {
    "generador_productos": cargar_productos("data/M/productos.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/M/ordenes_items.csv"),
}

agrupar_items_por_maximo_pedido_L_params = {
    "generador_productos": cargar_productos("data/L/productos.csv"),
    "generador_ordenes_items": cargar_ordenes_items("data/L/ordenes_items.csv"),
}

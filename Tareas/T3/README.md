# Tarea 3: DCC 🗣️❔❔

`Desarrolla el archivo aquí utilizando lo estipulado en el archivo "README_inicial.md`

# Registro de cambios a la Tarea

+ Viernes 16 de mayo: Se sube la tarea al Syllabus.
+ Viernes 16 de mayo: Se agrega el archivo .pyc a la carpeta T3/.
+ Sábado 17 de mayo: Se arregló el archivo `utilidades.pyc` para calzar con la información del enunciado y se generó una copia de éste en el directorio `backend/`.
+ Lunes 19 de mayo: 
    - Se actualizó el enunciado para remover el atributo `id_producto` del `NamedTuple` `Productos` y corregir otras inconsistencias sobre las consultas, junto a otros puntos.
    - Se actualizaron los tests para estar acordes al enunciado y evitar errores en ellos por inconsistencias.
    - Se agregó el archivo `parametros.py` al directorio base. Esto con el objetivo de que puedan usar las variables definidas en él como _kwargs_ de las funciones de `consultas.py` al momento de ser llamadas por la Interfaz Gráfica. No es necesario que ignoren dicho archivo y no habrá descuento por subirlo al repositorio.
+ Jueves 22 de mayo: Se actualizan los *links* de los datos y tests publicos. Ocurren los siguientes cambios:

    * Datos:
        - Ya no existen entradas, en cualquier archivo `productos.csv`, con  `identificador_del_proveedor` repetidos, todos son unicos.
        - Ya no existen entradas, en cualquier archivo `proveedores_productos.csv`, con  `identificador_del_proveedor` repetidos, todos son unicos.
        - Ya no existen entradas, en cualquier archivo `proveedores.csv`, con  `nombre_proveedor` repetidos, todos son unicos.


    * Tests Públicos:
        - Se arregló el test `test_07_producto_mas_popular_correctitud.py` para calzar con el enunciado.
        - Se adaptó la solución `solution/test_01.py` para calzar con los nuevos datos.
        - Se adaptó la solución `solution/test_10.py` para calzar con los nuevos datos.
        - Se adaptó la solución `solution/test_16.py` para calzar con los nuevos datos.
        - Se adaptaron las descripciones de algunos tests para que calcen con lo que el test verifica.
+ Viernes 23 de mayo: Se actualizan los *links* de los datos y tests publicos. Ocurren los siguientes cambios:

    * Enunciado:
        - Se corrigió la descripción de la función `producto_mas_popular`. Ahora esta dice "Si se produce un empate en popularidad entre dos
        productos, se debe realizar un desempate según el atributo `id_base_datos`, ordenándolos de manera **descendiente**".

    * Datos:
        - Se corrigió el error de que se encuentren productos asociados en `proveedores_productos.csv` pero no se encuentren en `productos.csv`.
        - Se verificó que todos los productos que aparecen en `ordenes_items.csv` aparezcan en `productos.csv`.
        - Puede ser que aparezcan productos en `productos.csv` que posean un `identificador_del_proveedor`, pero que no aparezcan en el archivo `proveedores_productos.csv` -> Esto NO es un error. Asuman que el proveedor que vende dicho producto no está en ese dataset.
        - Puede ser que aparezcan proveedores en `proveedores.csv` que posean un `nombre_proveedor`, pero que no aparezcan en el archivo `proveedores_productos.csv` -> Esto NO es un error. Asuman que el proveedor no vende productos en dicho dataset.

    * Tests Públicos:
        - Se adaptó el test `test_03_proveedores_por_estado_carga_datos.py` para que ahora se verifique el orden en que se retornan los datos, no solo que los datos sean correctos. Sigan el orden que menciona el enunciado.
        - Se adaptó el test `test_00_cargar_datos.py` para que calze con las nuevas versiones de los archivos que se subieron.
        - Se adaptó el test `test_07_cargar_datos.py` para que calze con la modificación del enunciado.
        - Se adaptó el test `test_07_correctitud.py` para incluir un caso relacionado a la modificación del enunciado.
        - Se adaptó el test `test_15_modificar_estados_ordenes_dirigidas_al_estado_correctitud.py` para que calze con el enunciado, el cual menciona que: "Retorna un generador con instancias de `Ordenes` correspondientes a usuarios que poseen una dirección dentro del estado de Estados Unidos entregado (estado), donde los estados de orden son modificados de acuerdo a lo indicado por el diccionario de transición de estados (cambio_estados_ordenes).".
        - Se adaptó el test `test_16_agrupar_items_por_maximo_pedido_carga_datos.py` para que la fecha_actual siempre calce.
        - Se adaptó la solución `test_10.py` para que calze con las nuevas versiones de los archivos que se subieron.
        - Se adaptó la solución `test_15.py` para que calze con la nueva adaptación de su test.
        - Se adaptó la solución `test_16.py` para que calze con las nuevas versiones de los archivos que se subieron.

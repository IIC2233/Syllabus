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
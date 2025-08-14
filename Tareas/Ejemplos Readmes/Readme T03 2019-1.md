# Tarea 03 : TIMBIRICHE 99 :small_red_triangle_down::small_red_triangle:

## Consideraciones generales :bangbang:
**Antes de comenzar a correr el programa**, es necesario realizar un **pequeño** cambio, ya que si no se realizan, el programa no reconocerá a un usuario si éste ya estaba registrado.

En el módulo `main.py` de la carpeta  `Servidor` en la [linea 248 y 249](https://github.com/IIC2233/jitorcas-iic2233-2019-1/blob/03fef9adfadacf062e04f94a821735ba51ffc22f/Tareas/T03/servidor/main.py#L248) deben quedar comentadas. 

### Cosas no implementadas: :x::cry::x:
Lamentablemente no implementé que cuando se encerrara un triángulo, el contador del jugador se reiniciará.

 - **NETWORKING:**
 **Persistencia:** No implementé guardar la imagen del usuario, solo guardo su nombre.
 
  - **FUNCIONALIDADES:**
  **Ventana de Salas:** No es posible agregar una foto. Está implementado el cargador de imagen pero no envía la imagen al servidor. 
   **Partida:** No reinicio el contador si un jugador completa un triángulo.
    **General:** No eliminó la sala cuando queda sin jugadores. Queda disponible, pero con 0 jugadores. Esto debido a que utilicé QListWidget para listar las salas y el método para eliminar los QListWidgetItem están desactualizados o de alguna manera no lo elimina correctamente, por lo mismo preferí dejarlo desconectado a generar un posible error desconocido. 
 - **Bonus:**
 Solo implementé el bonus del tablero triangular.
 - **Descuentos:**
 Tengo lineas de importación que superan los 80 caracteres. 

Sinceramente esos son los métodos que no implementé, intenté abarcar de mejor manera la tarea, sin preocuparme mucho de la interfaz (error cometido en el tarea 2) pero era inevitable, creé unos archivos .png que adornaban la tarea, como el nombre del juego y títulos importantes, sin embargo no me alcanzó el tiempo para implementarlos y los dejé en  `cliente/png juego` si bien utilizo solo una imagen, es necesario descargar la carpeta. 
 
### Cosas implementadas: :white_check_mark: :stuck_out_tongue_closed_eyes: :white_check_mark:
 
 En esta sección comentaré aspectos que considero que deben quedar claros en cuanto a su implementación, su funcionamiento o aspectos agregados a lo pedido en el enunciado. Lo que no está mencionado acá es porque considero que está implementado correctamente. 
  - **MANEJO DE BYTES:**
**General:** En el archivo `filtro.py` se encuentra la función   `filtro_dibujo.py` la cual recibe el path y se obtiene una imagen con filtro. Ya que no pude implementar subir la imagen la función del filtro está en un archivo aparte. 

 - **NETWORKING:**
 **Persistencia:** El servidor solo guardará el nombre del usuario.

 - **FUNCIONALIDADES:**
**Autenticación:**  No entendí muy bien si el servidor debía enviar una respuesta visible al usuario si es que el nombre estaba siendo utilizado. Mi programa solo no permite el ingreso.
   **Partida:** Si un usuario abandona la sala, su puntaje seguirá visible, aunque no esté en la sala, ya que decidí dejar sus triángulos en el tablero.  La forma de armar un triángulo es la siguiente:
   **(EN TU TURNO)**
   1. Haz **click** en el punto que quieres llegar y confirma que su color se cambie a **azul oscuro.**
   2. **Arrastra** el punto que quieres unir al seleccionado.
   3. Si la acción es correcta, entonces la línea se dibujará 
   4. Si se forma un triángulo, entonces se dibujará un **triángulo.**
  
 - **Bonus:**
 **Tablero triangular:** Implementé el tablero triangular.

### Ejecución del código:  :floppy_disk::floppy_disk::floppy_disk:

-   El módulo principal del servidor es  `main.py`  y el módulo principal del cliente es `main.py`

### Librerías: :books: 

**Librerías:**

 - Solo utilicé librerías permitidas,  a diferencia de muchos del curso, yo ocupe **QGraphics** para modelar la escena del juego, la diferencia es grande en cuanto a métodos, pero en esencia es la misma.
 - Algunos métodos importantes para comprender el modelo utilizado son: 
`scene = QGraphicsScene()  `: *crea una instancia de escena en la interfaz*
`item es de clase heredada de QGraphicsItem `
`scene.addItem(item)  `: *agrega item a la interfaz* 
`scene.removeItem(item)  `: *elimina ítem de la interfaz*
` graphicsView es de clase heredada de QGraphicsView `
` graphicsView.setScene(scene)`: *muestra la escena*

 **Librerías propias:**
 
 En esta tarea solo utilicé una librería propia, asociada al servidor 
 
- [**juego.py:**](https://github.com/IIC2233/jitorcas-iic2233-2019-1/blob/4853cbe54ac1c04797f5c0685d5f6a899620cbb4/Tareas/T03/servidor/juego.py#L11) **Funciones:**  *guardar_informacion, obtener_informacion_usuarios, match_colores ,asignar_nombre_sala.*  **Clases:** Juego
***[Estas funciones son utilizadas por el Servidor para realizar el juego de manera eficaz y pertinente]***

### Consideraciones específicas y/o supuestos: :grin: :flushed: 
Consideré que si el jefe del juego decide jugar de nuevo, entonces deberá esperar 5 segundos a que reinicie el contador, pero no puse un contador en el juego, entonces se ve como que no pasa nada, pero luego de 5 segundos comienza el flujo del juego. 

## Referencias de código externo :

 1. Para aprender a usar drag and drop utilicé [este juego](https://github.com/baoboa/pyqt5/blob/master/examples/graphicsview/dragdroprobot/dragdroprobot.py) interactivo. 
 2. Utilicé la ayudantía 13 [2018-2](https://github.com/IIC2233/syllabus-2018-2/blob/a96a11e343c50213a7df1e4cf809fad0ccf6fc6b/Ayudantias/S13%20-%20Networking/Cliente.py#L11) para modelar el chat. 
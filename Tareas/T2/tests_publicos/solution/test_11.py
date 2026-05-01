# Producción de recursos - Carga de datos
from utils import Juguete

# S
CREAR_RECURSOS_S_0_JUGUETES = [Juguete(20,"Raticate",(2,3),"020"),
                               Juguete(38,"Ninetales",(5,),"038"),
                               Juguete(37,"Vulpix",(2,),"037"),
                               Juguete(12,"Butterfree",(3,6),"012")]
CREAR_RECURSOS_S_0_MINUTOS = 10
CREAR_RECURSOS_S_0 = ((13, 2.0), (16, 42.0))

CREAR_RECURSOS_S_1_JUGUETES = [Juguete(20,"Raticate",(2,3),"020"),
                               Juguete(38,"Ninetales",(8,10),"038")]
CREAR_RECURSOS_S_1_MINUTOS = 20
CREAR_RECURSOS_S_1_IDS_ESPERADOS = {20, 38}

# M
CREAR_RECURSOS_M_0_JUGUETES = [Juguete(100,"Voltorb",(1,2,3,10),"100"),
                               Juguete(105,"Marowak",(1,4,5,12),"105"),
                               Juguete(139,"Omastar",(4,7,10),"139"),
                               Juguete(151,"Mew",(2,8,11),"151")]
CREAR_RECURSOS_M_0_SET_OBJETOS = {2, 12, 18, 20}
CREAR_RECURSOS_M_0_MINUTOS = 100
CREAR_RECURSOS_M_0 = ((5, 1100.0), (23, 6.0), (37, 250.0), (39, 55.0))

# L

CREAR_RECURSOS_L_0_JUGUETES = [Juguete(164,"Noctowl",(11,18,19,21,23),"164"),
                               Juguete(200,"Misdreavus",(3,5,11,19,20,23),"200"),
                               Juguete(210,"Granbull",(3,4,6,9,10,15),"210"),
                               Juguete(289,"Slaking",(1,9,13),"289"),
                               Juguete(394,"Prinplup",(7,16),"394")]
CREAR_RECURSOS_L_0_MINUTOS = 230
CREAR_RECURSOS_L_0 = ((60, 23.0), (412, 17.0))
from collections import namedtuple

ResultadoRecurso = namedtuple(
    "ResultadoRecurso",
    ["id_recurso_resultado", "afinidades_necesarias", "cantidad_recurso"],
)

# S — id_recurso=1  (ordenado por id_recurso_resultado ascendente)
# afinidades_necesarias incluye toda la cadena de afinidades requeridas
RECURSOS_APTR_S_0 = [
    ResultadoRecurso(id_recurso_resultado=2,  afinidades_necesarias=(1,),        cantidad_recurso=1),
    ResultadoRecurso(id_recurso_resultado=3,  afinidades_necesarias=(1, 5),      cantidad_recurso=3),
    ResultadoRecurso(id_recurso_resultado=4,  afinidades_necesarias=(1, 3, 5),   cantidad_recurso=3),
    ResultadoRecurso(id_recurso_resultado=5,  afinidades_necesarias=(1,),        cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=6,  afinidades_necesarias=(1, 6),      cantidad_recurso=4),
    ResultadoRecurso(id_recurso_resultado=7,  afinidades_necesarias=(1, 3, 5),   cantidad_recurso=6),
    ResultadoRecurso(id_recurso_resultado=8,  afinidades_necesarias=(1, 3),      cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=9,  afinidades_necesarias=(1, 3),      cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=10, afinidades_necesarias=(1, 3),      cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=11, afinidades_necesarias=(1, 5),      cantidad_recurso=10),
    ResultadoRecurso(id_recurso_resultado=12, afinidades_necesarias=(1, 3, 5),   cantidad_recurso=8),
    ResultadoRecurso(id_recurso_resultado=13, afinidades_necesarias=(1, 3, 4),   cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=14, afinidades_necesarias=(1, 3, 5),   cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=15, afinidades_necesarias=(1, 4, 5),   cantidad_recurso=10),
    ResultadoRecurso(id_recurso_resultado=16, afinidades_necesarias=(1, 3, 5),   cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=17, afinidades_necesarias=(1,),        cantidad_recurso=3),
    ResultadoRecurso(id_recurso_resultado=18, afinidades_necesarias=(1, 6),      cantidad_recurso=1),
    ResultadoRecurso(id_recurso_resultado=19, afinidades_necesarias=(1, 3, 5),   cantidad_recurso=4),
    ResultadoRecurso(id_recurso_resultado=20, afinidades_necesarias=(1, 3, 4),   cantidad_recurso=4),
]

# S — id_recurso=8  (ordenado por id_recurso_resultado ascendente)
RECURSOS_APTR_S_1 = [
    ResultadoRecurso(id_recurso_resultado=10, afinidades_necesarias=(1,),      cantidad_recurso=1),
    ResultadoRecurso(id_recurso_resultado=13, afinidades_necesarias=(1, 4),    cantidad_recurso=1),
    ResultadoRecurso(id_recurso_resultado=14, afinidades_necesarias=(1, 5),    cantidad_recurso=1),
    ResultadoRecurso(id_recurso_resultado=16, afinidades_necesarias=(1, 5),    cantidad_recurso=1),
    ResultadoRecurso(id_recurso_resultado=19, afinidades_necesarias=(1, 3, 5), cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=20, afinidades_necesarias=(1, 4),    cantidad_recurso=2),
]

# M — id_recurso=1  (ordenado por id_recurso_resultado ascendente)
# ACORTADO por tamaño
RECURSOS_APTR_M_0 = [
    ResultadoRecurso(id_recurso_resultado=2,  afinidades_necesarias=(7,),          cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=3,  afinidades_necesarias=(5, 7),        cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=5,  afinidades_necesarias=(3,),          cantidad_recurso=1),
    ResultadoRecurso(id_recurso_resultado=9,  afinidades_necesarias=(2, 7),        cantidad_recurso=1),
    ResultadoRecurso(id_recurso_resultado=10, afinidades_necesarias=(5, 6, 7),     cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=14, afinidades_necesarias=(2, 5, 6, 7),  cantidad_recurso=2),
    ResultadoRecurso(id_recurso_resultado=34, afinidades_necesarias=(3,),          cantidad_recurso=2),
] + [ResultadoRecurso(id_recurso_resultado=0, afinidades_necesarias=(), cantidad_recurso=0)] * 31 + [
    ResultadoRecurso(id_recurso_resultado=40, afinidades_necesarias=(3, 5, 6, 7, 8, 10), cantidad_recurso=32),
]
 
# L — id_recurso=1  (ordenado por id_recurso_resultado ascendente)
# ACORTADO por tamaño
RECURSOS_APTR_L_0 = [
    ResultadoRecurso(id_recurso_resultado=2,   afinidades_necesarias=(11,),                                                              cantidad_recurso=3),
] + [ResultadoRecurso(id_recurso_resultado=0, afinidades_necesarias=(), cantidad_recurso=0)] * (499 - 2) + [
    ResultadoRecurso(id_recurso_resultado=500, afinidades_necesarias=(1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24), cantidad_recurso=6691278),
]

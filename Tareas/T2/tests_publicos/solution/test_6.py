# cadena_creacion — árbol recursivo de recursos e id_juguetes productores

# S — recurso=1  (R1: sin receta, producido solo por J11)
CADENA_CREACION_S_0 = {
    1: {"recursos": {}, "juguetes": (11,)},
}

# S — recurso=2  (R2 = R1*1; R1 sin receta)
CADENA_CREACION_S_1 = {
    2: {
        "recursos": {
            1: {"recursos": {}, "juguetes": (11,)},
        },
        "juguetes": (2,),
    },
}

# M — recurso=1  (R1: sin receta)
CADENA_CREACION_M_0 = {
    1: {"recursos": {}, "juguetes": (58, 110, 130, 147)},
}

# L — recurso=1  (R1: sin receta)
CADENA_CREACION_L_0 = {
    1: {"recursos": {}, "juguetes": (294,)},
}

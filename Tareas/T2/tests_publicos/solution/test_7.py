from collections import namedtuple

JugueteAAparecer = namedtuple("JugueteAAparecer", ["id_juguete", "tiempo"])

# S — id_habitat=1, momento_dia=0
JUGUETES_A_APARECER_S_0 = [
    JugueteAAparecer(id_juguete=1, tiempo=30),
]

# S — id_habitat=2, momento_dia=0
JUGUETES_A_APARECER_S_1 = [
    JugueteAAparecer(id_juguete=28, tiempo=7),
    JugueteAAparecer(id_juguete=1,  tiempo=26),
]

# S — id_habitat=9, momento_dia=0
JUGUETES_A_APARECER_S_2 = [
    JugueteAAparecer(id_juguete=4,  tiempo=1),
    JugueteAAparecer(id_juguete=11, tiempo=34),
    JugueteAAparecer(id_juguete=23, tiempo=53),
    JugueteAAparecer(id_juguete=32, tiempo=59),
    JugueteAAparecer(id_juguete=34, tiempo=59),
]

# M — id_habitat=1, momento_dia=0
JUGUETES_A_APARECER_M_0 = [
    JugueteAAparecer(id_juguete=1, tiempo=70),
]

# M — id_habitat=2, momento_dia=0
JUGUETES_A_APARECER_M_1 = [
    JugueteAAparecer(id_juguete=1,   tiempo=17),
    JugueteAAparecer(id_juguete=20,  tiempo=54),
    JugueteAAparecer(id_juguete=118, tiempo=119),
]

# L — id_habitat=1, momento_dia=0
JUGUETES_A_APARECER_L_0 = [
    JugueteAAparecer(id_juguete=1, tiempo=310),
]

from collections import namedtuple

AhoraEs = namedtuple(
    "AhoraEs",
    ["dia_actual", "hora_actual", "nombre_periodo_dia",
     "hora_inicio_periodo_dia", "hora_fin_periodo_dia"],
)

# S: total_dia=59 min (P1=Madrugada 26 min, P2=Amanecer 33 min)
AHORA_ES_S_0 = AhoraEs(dia_actual=0, hora_actual="00:00", nombre_periodo_dia="Madrugada", hora_inicio_periodo_dia="00:00", hora_fin_periodo_dia="00:26")   # minutos=0
AHORA_ES_S_1 = AhoraEs(dia_actual=0, hora_actual="00:30", nombre_periodo_dia="Amanecer",  hora_inicio_periodo_dia="00:26", hora_fin_periodo_dia="00:59")   # minutos=30
AHORA_ES_S_2 = AhoraEs(dia_actual=1, hora_actual="00:00", nombre_periodo_dia="Madrugada", hora_inicio_periodo_dia="00:00", hora_fin_periodo_dia="00:26")   # minutos=59

# M: total_dia=118 min (P1=Madrugada 39, P2=Amanecer 18, P3=Alba 29, P4=Mañana 32)
AHORA_ES_M_0 = AhoraEs(dia_actual=0, hora_actual="00:00", nombre_periodo_dia="Madrugada", hora_inicio_periodo_dia="00:00", hora_fin_periodo_dia="00:39")   # minutos=0
AHORA_ES_M_1 = AhoraEs(dia_actual=0, hora_actual="00:50", nombre_periodo_dia="Amanecer",  hora_inicio_periodo_dia="00:39", hora_fin_periodo_dia="00:57")   # minutos=50
AHORA_ES_M_2 = AhoraEs(dia_actual=1, hora_actual="01:22", nombre_periodo_dia="Alba",      hora_inicio_periodo_dia="00:57", hora_fin_periodo_dia="01:26")   # minutos=200

# L: total_dia=472 min (16 periodos)
AHORA_ES_L_0 = AhoraEs(dia_actual=0, hora_actual="00:00", nombre_periodo_dia="Madrugada", hora_inicio_periodo_dia="00:00", hora_fin_periodo_dia="00:35")   # minutos=0
AHORA_ES_L_1 = AhoraEs(dia_actual=0, hora_actual="00:40", nombre_periodo_dia="Amanecer",  hora_inicio_periodo_dia="00:35", hora_fin_periodo_dia="01:00")   # minutos=40

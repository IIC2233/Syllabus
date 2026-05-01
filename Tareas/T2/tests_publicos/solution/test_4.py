# juguetes_productivos — id_juguetes más productivos o con productividad > mínimo
# Asunción: tiempo_espera > 0 (ningún juguete tiene tiempo_espera = "00:00")

# S — minimo=None  (J10: 5/1=5.0, J18: 5/1=5.0 → máxima productividad)
JUGUETES_PRODUCTIVOS_S_0 = [10, 18]

# S — minimo=1.0  (prod estrictamente > 1.0)
JUGUETES_PRODUCTIVOS_S_1 = [6, 10, 18, 19, 20, 34]

# M — minimo=None  (J33: 10/1=10.0, J151: 10/1=10.0 → máxima productividad)
JUGUETES_PRODUCTIVOS_M_0 = [33, 151]

# L — minimo=None  (J357: 38 recursos en 34 min → máxima productividad)
JUGUETES_PRODUCTIVOS_L_0 = [357]

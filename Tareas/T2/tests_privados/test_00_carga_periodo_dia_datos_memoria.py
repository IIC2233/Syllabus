import os
from tests_privados.test_tools import IICTest, timeout, max_memory
from backend.consultas import cargar_periodo_dia

# Timeout de seguridad (solo se evalua memoria, no rendimiento): corta ciclos infinitos.
N_SECOND_XL = 5.0

# Limite de memoria: pico_medido_en_XL x FACTOR.
FACTOR = 3
N_MB = 0.0149 * FACTOR

PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestMemoriaPeriodoDia(IICTest):
    """
    Pasan todos los tests de carga, los cuales validan que la consulta utilice una
    cantidad de memoria adecuada (memoria constante O(1) al iterar sobre el dataset XL).
    """

    @timeout(N_SECOND_XL)
    @max_memory(mb=N_MB, debug=False)
    def test_cargar_periodo_dia_memoria(self):
        """
        Iterar cargar_periodo_dia sobre el dataset XL privado no debe superar el limite de memoria.
        """
        for _ in cargar_periodo_dia(os.path.join(PATH_XL, "periodo_dia.csv")):
            pass

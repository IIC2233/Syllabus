import os
from tests_privados.test_tools import IICTest, timeout, max_memory
from backend.consultas import cargar_recurso_recurso

# Timeout de seguridad (solo se evalua memoria, no rendimiento): corta ciclos infinitos.
N_SECOND_XL = 5.0

# Limite de memoria: pico_medido_en_XL x FACTOR.
FACTOR = 3
N_MB = 0.0623 * FACTOR

PATH_XL = os.path.join("tests_privados", "data", "XL")


class TestMemoriaRecursoRecurso(IICTest):
    """
    Pasan todos los tests de carga, los cuales validan que la consulta utilice una
    cantidad de memoria adecuada (memoria constante O(1) al iterar sobre el dataset XL).
    """

    @timeout(N_SECOND_XL)
    @max_memory(mb=N_MB, debug=False)
    def test_cargar_recurso_recurso_memoria(self):
        """
        Iterar cargar_recurso_recurso sobre el dataset XL privado no debe superar el limite de memoria.
        """
        for _ in cargar_recurso_recurso(os.path.join(PATH_XL, "recurso_recurso.csv")):
            pass

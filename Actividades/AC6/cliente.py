import requests
import json

class Cliente:
    """Clase encargada de hacer las requests al servidor"""

    def __init__(self, host: str, port: int, usuario: str):
        """Se inicializa con un host, port y usuario"""
        self.base_url = f"{host}:{port}"
        self.usuario = usuario

    def get_controles(self) -> tuple[int, list]:
        """
        Llama al endpoint del servidor que retorna los nombres de
        archivos de los controles. La respuesta obtenida es en json
        """
        pass

    def get_preguntas_control(self, nombre_control: str) -> tuple[int, dict]:
        """
        Llama al endpoint del servidor que obtiene los detalles
        del control. La respuesta obtenida es en json
        """
        pass

    def post_respuestas_control(
            self,
            nombre_control: str,
            respuestas: list[int],
            alumno: str
        ) -> tuple[int, dict]:
        """
        Envía las respuestas el servidor a través de un requests POST.
        El post debe enviar las respuestas a través del body, y el 
        nombre del alumno en la url rel request
        """
        pass
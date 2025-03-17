import utilidades


class Bonsai:
    def __init__(
        self,
        identificador: str,
        costo_corte: int,
        costo_flor: int,
        estructura: list
    ) -> None:
        self.identificador = identificador
        self.costo_corte = costo_corte
        self.costo_flor = costo_flor
        self.estructura = estructura

    def cargar_bonsai_de_archivo(self, carpeta: str, archivo: str) -> None:
        pass

    def visualizar_bonsai(self, orientacion: str, emojis: bool, guardar_archivo: bool) -> None:
        pass


class DCCortaRamas:
    def modificar_nodo(self, bonsai: Bonsai, identificador: str) -> str:
        pass

    def quitar_nodo(self, bonsai: Bonsai, identificador: str) -> str:
        pass

    def es_simetrico(self, bonsai: Bonsai) -> bool:
        pass

    def emparejar_bonsai(self, bonsai: Bonsai) -> list:
        pass

    def emparejar_bonsai_ahorro(self, bonsai: Bonsai) -> list:
        pass

    def comprobar_solucion(self, bonsai: Bonsai, instrucciones: list) -> list:
        pass

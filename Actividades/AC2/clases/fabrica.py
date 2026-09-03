class Caja:

    def __init__(self, codigo: str, nombre: str, peso: str) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.peso = peso

    def __repr__(self) -> str:
        return f"Caja({self.codigo!r}, {self.nombre!r}, {self.peso!r})"

    def __str__(self) -> str:
        return f"{self.codigo} | {self.nombre} | {self.peso} kg"


class Registro:

    def __init__(self, codigo: str, resultado: str,
                 detalle: str = "-") -> None:
        self.codigo = codigo
        self.resultado = resultado
        self.detalle = detalle

    def __repr__(self) -> str:
        return (
            f"Registro({self.codigo!r}, {self.resultado!r}, "
            f"{self.detalle!r})"
        )

    def __str__(self) -> str:
        return f"{self.codigo:<10}| {self.resultado:<10}| {self.detalle}"


class CajaRechazadaError(Exception):

    def __init__(self, motivo: str) -> None:
        self.motivo = motivo
        super().__init__(f"Caja rechazada: {motivo}")

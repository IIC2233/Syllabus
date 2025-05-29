import json


class Banco:
    def __init__(self, nombre_banco, n_cuenta, saldo, transacciones):
        self.nombre_banco = nombre_banco
        self.n_cuenta = n_cuenta
        self.saldo = saldo
        self.transacciones = transacciones

    def __repr__(self) -> str:
        texto = f'Banco(nombre_banco={repr(self.nombre_banco)}, '\
                f'n_cuenta={repr(self.n_cuenta)}, '\
                f'saldo={repr(self.saldo)}, '\
                f'transacciones={repr(self.transacciones)})'
        return texto


class Transaccion:
    def __init__(self, titulo: str, monto: int, tipo: str):
        self.titulo = titulo
        self.monto = monto
        self.tipo = tipo

    def __repr__(self) -> str:
        texto = self.tipo.capitalize()
        texto += f'(titulo={repr(self.titulo)}, '\
                 f'monto={repr(self.monto)})'
        return texto


def BancoDecoder(data: dict) -> Banco:
    # Si el diccionario corresponde a un Banco,
    # retornamos una instancia de Banco
    if 'nombre_banco' in data:
        return Banco(**data)
    # Si tiene titulo, retornamos una
    # instancia de Transaccion
    if 'titulo' in data:
        return Transaccion(**data)


class BancoEncoder(json.JSONEncoder):
    def default(self, banco: Banco) -> dict:
        info_banco = banco.__dict__.copy()
        info_transacciones = [t.__dict__ for t in banco.transacciones]

        info_banco['transacciones'] = info_transacciones

        return info_banco

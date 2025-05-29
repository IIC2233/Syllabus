import json
import os

from banco import BancoEncoder, BancoDecoder, Transaccion


class DCConsumo:
    def __init__(self, path_data: str | None = None) -> None:
        if not path_data:
            path_data = os.path.join('servidor', 'data.json')
        self.path_data = path_data

        self.data = {}

    def cargar_data(self) -> None:
        '''
        Carga la información de data.json y lo transforma a un diccionario.
        '''
        with open(self.path_data, 'r', encoding='utf-8') as file:
            data = json.load(file, object_hook=BancoDecoder)
            self.data = {banco.nombre_banco: banco for banco in data}

    def guardar_data(self) -> None:
        '''
        Pasa el diccionario a una lista y lo guarda en data.json
        '''
        with open(self.path_data, 'w', encoding='utf-8') as file:
            data = list(self.data.values())
            json.dump(data, file, indent=4, ensure_ascii=False, cls=BancoEncoder)

    def obtener_saldo(self, nombre_banco: str | None = None) -> int:
        '''
        Obtiene el saldo de una cuenta bancaria. Si no se indica una cuenta,
        se entrega la suma de todos los saldos.
        '''
        if nombre_banco and nombre_banco not in self.data:
            raise KeyError(f'Cuenta {nombre_banco} no encontrada')

        if nombre_banco:
            return self.data[nombre_banco].saldo

        total = sum(map(lambda banco: banco.saldo, self.data.values()))
        return total

    def obtener_transacciones(self, nombre_banco: str, cantidad: int | None) -> list:
        '''
        Obtiene las últimas transacciones de una cuenta bancaria.
        Si no se indica una cantidad, se entregan todas las transacciones.
        '''
        if nombre_banco and nombre_banco not in self.data:
            raise KeyError(f'Cuenta {nombre_banco} no encontrada')

        banco = self.data[nombre_banco]
        transacciones = banco.transacciones[::-1]

        if cantidad:
            transacciones = transacciones[:cantidad]

        return [t.__dict__ for t in transacciones]

    def agregar_gasto(self, nombre_banco: str, titulo: str, monto: int) -> None:
        '''
        Agrega un gatos a la lista de transacciones de una cuenta bancaria.
        Además, actualiza el saldo de la cuenta.
        '''
        if nombre_banco not in self.data:
            raise KeyError(f'Cuenta {nombre_banco} no encontrada')

        if titulo is None or monto is None:
            raise TypeError('Faltan argumentos')

        banco = self.data[nombre_banco]
        banco.transacciones.append(Transaccion(titulo, monto, 'gasto'))
        banco.saldo -= monto

        self.guardar_data()


    def ajustar_saldo(self, nombre_banco: str, saldo: int) -> None:
        '''
        Actualiza el saldo de una cuenta bancaria y agrega una
        transacción asociada al ajuste. 
        '''
        if nombre_banco not in self.data:
            raise KeyError(f'Cuenta {nombre_banco} no encontrada')

        if saldo is None:
            raise TypeError('Faltan argumentos')

        banco = self.data[nombre_banco]
        delta = saldo - banco.saldo
        banco.saldo = saldo

        if delta > 0:
            banco.transacciones.append(Transaccion('Ajuste saldo', delta, 'ingreso'))
        else:
            banco.transacciones.append(Transaccion('Ajuste saldo', abs(delta), 'gasto'))

        self.guardar_data()

    def hacer_transferencia(self, nombre_banco: str, destinatario: dict, monto: int) -> None:
        '''
        Realiza una transferencia desde una cuenta bancaria, hasta
        el destinatario indicado. Agrega la transacción asociada y
        actualiza el saldo de la cuenta.
        '''
        if nombre_banco not in self.data:
            raise KeyError(f'Cuenta {nombre_banco} no encontrada')

        if (None in (nombre_banco, monto, destinatario) or
            'nombre' not in destinatario or
            'n_cuenta' not in destinatario):
            raise TypeError('Faltan argumentos')

        banco = self.data[nombre_banco]

        if monto > banco.saldo:
            raise ValueError('Transferencia supera el saldo de la cuenta')

        dest_nombre = destinatario['nombre']
        dest_cuenta = destinatario['n_cuenta']

        self.agregar_gasto(nombre_banco, f'Transferencia {dest_nombre} ({dest_cuenta})', monto)




if __name__ == '__main__':
    dcconsumo = DCConsumo()

    with open(dcconsumo.path_data, 'w', encoding='utf-8') as _file:
        _file.write('''[
    {
        "nombre_banco": "BancoDCC",
        "n_cuenta": 12345678,
        "saldo": 150000,
        "transacciones": [
            {
                "titulo": "Salgo base",
                "monto": 150000,
                "tipo": "ingreso"
            }
        ]
    },
    {
        "nombre_banco": "PepaBank",
        "n_cuenta": 98765432,
        "saldo": 10000000,
        "transacciones": [
            {
                "titulo": "Salgo base",
                "monto": 10000000,
                "tipo": "ingreso"
            }
        ]
    }
]
''')

    dcconsumo.cargar_data()
    print(dcconsumo.data)

    print(dcconsumo.obtener_saldo())
    print(dcconsumo.obtener_saldo('PepaBank'))

    dcconsumo.agregar_gasto('PepaBank', 'Lechuga', 2000)
    dcconsumo.agregar_gasto('PepaBank', 'Gusanos', 5000)
    print(dcconsumo.data)

    dcconsumo.ajustar_saldo('PepaBank', 0)
    dcconsumo.ajustar_saldo('PepaBank', 70000)
    print(dcconsumo.data)

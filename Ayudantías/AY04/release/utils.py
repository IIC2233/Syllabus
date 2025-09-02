from __future__ import annotations


class Fecha:

    def __init__(self, dia: int, mes: int, ano: int):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __gt__(self, otra_fecha: Fecha) -> bool:
        '''
        Definimos el operador > para comparar fechas (overloading). Esto encapsula la
        lógica de orden dentro de la clase Fecha (alta cohesión), evitando
        duplicar código de comparación en otras partes del programa.
        '''
        if not isinstance(otra_fecha, Fecha):
            raise TypeError(f'Argumento de tipo {type(otra_fecha)},'
                            f' cuando se esperaba un {type(self)}.')

        if self.ano > otra_fecha.ano:
            return True
        elif self.ano == otra_fecha.ano:
            if self.mes > otra_fecha.mes:
                return True
            elif self.mes == otra_fecha.mes:
                return self.dia > otra_fecha.dia
        return False

    def __ne__(self, otra_fecha: Fecha) -> bool:
        '''
        Definimos el operador != para comparar fechas (overloading). Esto encapsula la
        lógica de orden dentro de la clase Fecha (alta cohesión), evitando
        duplicar código de comparación en otras partes del programa.
        '''

        if not isinstance(otra_fecha, Fecha):
            raise TypeError(f'Argumento de tipo {type(otra_fecha)},'
                            f' cuando se esperaba un {type(self)}.')

        return not (self.dia == otra_fecha.dia and
                    self.mes == otra_fecha.mes and
                    self.ano == otra_fecha.ano)

    def __str__(self) -> str:
        return f'{self.dia}/{self.mes}/{str(self.ano)[-2:]}'


class Mercaderia:

    def __init__(self, nombre: str, fecha_vencimiento: Fecha,
                 cantidad: int, estacion: str):
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.cantidad = cantidad
        self.estacion = estacion

    def __str__(self) -> str:
        return f'{self.nombre}: {self.estacion[:2]} ({self.fecha_vencimiento})'


def obtener_mercaderias(path, sort):
    mercaderias = []
    with open(path, encoding='utf-8') as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            fecha = Fecha(*(int(i) for i in datos[1].split(";")))
            mercaderia = Mercaderia(datos[0], fecha, int(datos[2]), datos[3])
            mercaderias.append(mercaderia)
    for m in sorted(mercaderias, key=sort):
        yield m

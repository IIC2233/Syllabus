import json
import os

from utils import Conductor, PatenteError


class CargadorArchivos:

    @staticmethod
    def cargar_registro_oficial(path_registro_oficial: str) -> dict:
        registro_oficial = dict()
        with open(path_registro_oficial, 'r') as file:
            registros = json.load(file)
            for nombre_conductor, patente in registros.items():
                registro_oficial[nombre_conductor] = patente
        return registro_oficial

    @staticmethod
    def cargar_conductores(path_conductores: str) -> list:
        conductores = list()
        with open(path_conductores, 'r', encoding="latin-1") as file:
            for line in file:
                conductor = Conductor(*line.strip().split(","))
                conductores.append(conductor)
        return conductores

    def cargar_datos(self, path_registro_oficial: str, path_conductores: str) -> tuple:
        '''TODO: Parte I'''
        registro_oficial = None
        conductores = None
        return registro_oficial, conductores


class DCConductor:

    def __init__(self, registro_oficial: dict, conductores: list) -> None:
        self.registro_oficial = registro_oficial
        self.conductores = conductores
        self.seleccionados = list()

    def chequear_rut(self, conductor: Conductor) -> None:
        '''TODO: Parte II'''
        pass

    def chequear_celular(self, conductor: Conductor) -> None:
        '''TODO: Parte II'''
        pass

    def chequear_nombre(self, conductor: Conductor) -> None:
        '''TODO: Parte II'''
        pass

    def chequear_patente(self, conductor: Conductor) -> None:
        '''TODO: Parte II'''
        pass

    def chequear_conductores_app(self) -> str:
        '''TODO: Parte III'''
        if self.registro_oficial and self.conductores:
            cantidad_errores = 0

            for conductor in self.conductores:
                self.chequear_rut(conductor)
                self.chequear_celular(conductor)
                self.chequear_nombre(conductor)
                self.chequear_patente(conductor)

            return f"La cuenta de datos erroneos fue: {cantidad_errores}."
        return "Falta parte de los datos necesarios para hacer la revision."


if __name__ == '__main__':
    cargador_archivos = CargadorArchivos()

    print(' CASO 1 '.center(50, '-'))
    registro_oficial, conductores = cargador_archivos.cargar_datos(
        os.path.join("data", "regiztro_ofizial.json"),
        os.path.join("data", "conductores.csv")
    )
    dcconductor = DCConductor(registro_oficial, conductores)
    print(dcconductor.chequear_conductores_app(), '\n')


    print(' CASO 2 '.center(50, '-'))
    registro_oficial, conductores = cargador_archivos.cargar_datos(
        os.path.join("data", "registro_oficial.json"),
        os.path.join("data", "conductores.hvs")
    )
    dcconductor = DCConductor(registro_oficial, conductores)
    print(dcconductor.chequear_conductores_app(), '\n')


    print(' CASO 3 '.center(50, '-'))
    registro_oficial, conductores = cargador_archivos.cargar_datos(
        os.path.join("data", "registro_oficial.json"),
        os.path.join("data", "conductores.csv")
    )
    dcconductor = DCConductor(registro_oficial, conductores)
    print(dcconductor.chequear_conductores_app())

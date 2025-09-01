import math
from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_TRAP_CHILENO ,
                        AFINIDAD_STAFF_TRAP_CHILENO , AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_TRAP_CHILENO ,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion,
                 hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL

    @property
    def afinidad_con_publico(self):
        return self._afinidad_con_publico

    @afinidad_con_publico.setter
    def afinidad_con_publico(self, valor):
        '''
        NOTE: La comprobación de que el valor pertenezca al rango
        indicado se puede hacer de distintas forma. Por lo general uno piensa
        en usar if/else, pero en esta ocasión lo hacemos por medio de min/max.
        '''
        valor = max(min(valor, 100), 0)
        self._afinidad_con_publico = valor

    @property
    def afinidad_con_staff(self):
        return self._afinidad_con_staff

    @afinidad_con_staff.setter
    def afinidad_con_staff(self, valor):
        valor = max(min(valor, 100), 0)
        self._afinidad_con_staff = valor

    @property
    def animo(self):
        valor = math.floor(self._afinidad_con_publico * 0.5) + \
                math.floor(self.afinidad_con_staff * 0.5)
        return valor

    def recibir_suministros(self, suministro):
        '''
        NOTE: Recordar que el uso del operador += es equivalente al siguiente
        código, por lo que se hace tanto un llamado al getter como al setter:
        self.afinidad_con_staff = self.afinidad_con_staff + suministro.valor_de_satisfaccion
        '''
        self.afinidad_con_staff += suministro.valor_de_satisfaccion

        if suministro.valor_de_satisfaccion > 0:
            print(f"{self.nombre} recibió un {suministro.nombre} a tiempo!")
        else:
            print(f"{self.nombre} recibió {suministro.nombre} en malas condiciones")

    def cantar_hit(self):
        self.afinidad_con_publico += AFINIDAD_HIT
        print(f"{self.nombre} está tocando su hit: {self.hit_del_momento}!")

    def __str__(self):
        return f'Artista({self.nombre}, {self.animo})'


class ArtistaPop(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accion = "Cambio de vestuario"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_POP
        self._afinidad_con_staff = AFINIDAD_STAFF_POP

    def ejecutar_accion(self):
        self.afinidad_con_publico += AFINIDAD_ACCION_POP
        print(f"{self.nombre} hará un {self.accion}")

    @property
    def animo(self):
        # valor = Artista.animo
        valor = super().animo
        if valor < 10:
            print(f"ArtistaPop peligrando en el concierto. Animo: {valor}")
        return valor

class ArtistaRock(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def ejecutar_accion(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaTrapChileno(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def ejecutar_accion(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaReggaeton(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def ejecutar_accion(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass

if __name__ == '__main__':
    # NOTE: Código creado para probar las funcionalidades antes implementadas

    # 1) Getter y setter de afinidad publico y staff

    artista = Artista('Ado', 'J-pop', 1, 'Odo')
    print('Publico 1:', artista.afinidad_con_publico)

    artista.afinidad_con_publico = 50
    print('Publico 2:', artista.afinidad_con_publico)

    artista.afinidad_con_publico = -50
    print('Publico 3:', artista.afinidad_con_publico)

    artista.afinidad_con_publico = 150
    print('Publico 4:', artista.afinidad_con_publico)

    artista.afinidad_con_publico = 85
    print('Publico 5:', artista.afinidad_con_publico)

    print('\n' + '-' * 20 + '\n')


    # 2) Property animo
    artista = Artista('Ado', 'J-pop', 1, 'Odo')

    artista.afinidad_con_publico = 50
    artista.afinidad_con_staff = 85
    print('Animo 1:', artista.animo)

    artista.afinidad_con_publico = 2
    artista.afinidad_con_staff = 1
    print('Animo 2:', artista.animo)

    print('\n' + '-' * 20 + '\n')


    # 3) Método recibir_suministro
    #    NOTE: Se hardcodean los Suministros para
    #          asegurar que generen el efecto deseado

    from suministro import Suministro

    suministro1 = Suministro('tacos', 80)
    suministro2 = Suministro('cocacola', 50)

    suministro1.valor_de_satisfaccion = 80
    suministro2.valor_de_satisfaccion = -50

    print(suministro1)
    print(suministro2)

    artista = Artista('Ado', 'J-pop', 1, 'Odo')
    artista.afinidad_con_publico = 50
    artista.afinidad_con_staff = 85
    print(artista)

    artista.recibir_suministros(suministro1)
    print(artista)

    artista.recibir_suministros(suministro2)
    print(artista)

    print('\n' + '-' * 20 + '\n')


    # 4) Método cantar_hit

    artista.cantar_hit()
    print(artista)

    print('\n' + '-' * 20 + '\n')


    # 5) Clase ArtistaPop

    artista = ArtistaPop('Ado', 'J-pop', 1, 'Odo')
    print(artista)

    # NOTE: El atributo __dict__ nos permite revisar todos
    #       los atributos de la instancia
    print(artista.__dict__)

    # NOTE: La función help permite ver la documentación de la clase.
    # IMPORTANT: Se encuentra comentada debido a que afecta la ejecución
    #            del código. Se deben usar las flechas para avanzar en el
    #            código y escribir ":q" para salir de la documentación.
    # help(artista)

    print('\n' + '-' * 20 + '\n')


    # 6) Método ejecutar_accion 

    artista = ArtistaPop('Ado', 'J-pop', 1, 'Odo')
    print(artista)

    artista.ejecutar_accion()
    print(artista.animo)

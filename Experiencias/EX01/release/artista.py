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

    def afinidad_con_publico(self):
        # COMPLETAR
        pass

    def afinidad_con_staff(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass

    def recibir_suministros(self, suministro):
        # COMPLETAR
        pass

    def cantar_hit(self):
        # COMPLETAR
        pass

    def __str__(self):
        # COMPLETAR
        pass


class ArtistaPop(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def ejecutar_accion(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


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

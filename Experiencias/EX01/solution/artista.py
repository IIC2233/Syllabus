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
        # 1 ---------- ALUMNO ----------
        return self._afinidad_con_publico
        # 1 ---------- ELIMINAR ----------

    # 2 ---------- ALUMNO ----------
    @afinidad_con_publico.setter
    def afinidad_con_publico(self, valor):
        if AFINIDAD_MIN < valor < AFINIDAD_MAX:
            self._afinidad_con_publico = valor
        else:
            self._afinidad_con_publico = 100 if valor > 100 else 0
    # 2 ---------- ALUMNO ----------

    @property
    def afinidad_con_staff(self):
        # 3 ---------- ALUMNO ----------
        return self._afinidad_con_staff
        # 3 ---------- ALUMNO ----------

    # 4 ---------- ALUMNO ----------
    @afinidad_con_staff.setter
    def afinidad_con_staff(self, valor):
        if AFINIDAD_MIN < valor < AFINIDAD_MAX:
            self._afinidad_con_staff = valor
        else:
            self._afinidad_con_staff = 100 if valor > 100 else 0
    # 4 ---------- ALUMNO ----------

    @property
    def animo(self):
        # 5 ---------- ALUMNO ----------
        return (0.5 * self.afinidad_con_publico +
                0.5 * self.afinidad_con_staff)
        # 5 ---------- ALUMNO ----------

    def recibir_suministros(self, suministro):
        valor = suministro.valor_de_satisfaccion
        self.afinidad_con_staff += valor
        if valor < 0:
            print(f"{self.nombre} recibió {suministro.nombre} en malas "
                  "condiciones. Bajó la afinidad con el staff.")
        else:
            print(f"{self.nombre} recibió un {suministro.nombre} a tiempo! "
                  "Que siga el concierto! Subió la afinidad con el staff")

    def cantar_hit(self):
        # 6 ---------- ALUMNO ----------
        self.afinidad_con_publico += AFINIDAD_HIT
        print(f"{self.nombre} está tocando su hit: {self.hit_del_momento}"
              f"Al público le encanta!")
        # 6 ---------- ALUMNO ----------

    def __str__(self):
        # 7 ---------- ALUMNO ----------
        return (f"Nombre: {self.nombre}\nGenero: "
                f"{self.genero}\nAnimo: {self.animo}")
        # 7 ---------- ALUMNO ----------


class ArtistaPop(Artista):
    # 8 ---------- ALUMNO ----------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._afinidad_con_publico = AFINIDAD_PUBLICO_POP
        self._afinidad_con_staff = AFINIDAD_STAFF_POP
        self.accion = "Cambio de vestuario"

    def ejecutar_accion(self):
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_POP
    # 8 ---------- ALUMNO ----------

    @property
    def animo(self):
        valor_animo = super().animo
        if valor_animo < 10:
            print(
                f"ArtistaPop peligrando en el concierto. Animo: {valor_animo}"
                )
        return valor_animo


class ArtistaRock(Artista):
    # 9 ---------- ALUMNO ----------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._afinidad_con_publico = AFINIDAD_PUBLICO_ROCK
        self._afinidad_con_staff = AFINIDAD_STAFF_ROCK
        self.accion = "Solo de guitarra"

    def ejecutar_accion(self):
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_ROCK
        # 9 ---------- ALUMNO ----------

    @property
    def animo(self):
        valor_animo = super().animo
        if valor_animo < 5:
            print(
                f"ArtistaRock peligrando en el concierto. Animo: {valor_animo}"
                )
        return valor_animo


class ArtistaTrapChileno(Artista):
    # 10 ---------- ALUMNO ----------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._afinidad_con_publico = AFINIDAD_PUBLICO_TRAP_CHILENO 
        self._afinidad_con_staff = AFINIDAD_STAFF_TRAP_CHILENO 
        self.accion = "Malianteo"

    def ejecutar_accion(self):
        print(f"{self.nombre} se va a mandar un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_TRAP_CHILENO 
        # 10 ---------- ALUMNO ----------

    @property
    def animo(self):
        valor_animo = super().animo
        if valor_animo < 20:
            print(
                f"ArtistaTrapChileno peligrando en el concierto. Animo: {valor_animo}"
                )
        return valor_animo


class ArtistaReggaeton(Artista):
    # 11 ---------- ALUMNO ----------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._afinidad_con_publico = AFINIDAD_PUBLICO_REG
        self._afinidad_con_staff = AFINIDAD_STAFF_REG
        self.accion = "Perrear hasta el suelo"

    def ejecutar_accion(self):
        print(f"{self.nombre} va a {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_REG
    # ``2`` ---------- ALUMNO ----------

    @property
    def animo(self):
        valor_animo = super().animo
        if valor_animo < 2:
            print(
                f"ArtistaReggaeton peligrando en el concierto."
                f"Animo: {valor_animo}"
                )
        return valor_animo

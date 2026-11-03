class Partida:
    def __init__(self, jugador_1, jugador_2):
        self.jugadores = {jugador_1: "X", jugador_2: "O"}
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.turno = "X"
        print(f"Nueva partida entre {jugador_1[1]} y {jugador_2[1]}")

    def procesar_jugada(self, jugador, fil, col):
        
        simbolo = self.jugadores[jugador]
        if simbolo != self.turno:
            return {"accion": "error", "mensaje": "No es tu turno"}
        if self.tablero[fil][col]:
            return {"accion": "error", "mensaje": "Casilla ocupada"}

        self.tablero[fil][col] = simbolo

        if self.hay_ganador(simbolo):
            return {"accion": "ganador", "simbolo": simbolo, "tablero": self.tablero}

        if self.tablero_lleno():
            return {"accion": "empate", "tablero": self.tablero}

        self.turno = "O" if self.turno == "X" else "X"
        return {"accion": "turno", "simbolo": self.turno, "tablero": self.tablero}

    def tablero_lleno(self):
        for fila in self.tablero:
            for celda in fila:
                if celda == "":
                    return False
        return True

    def hay_ganador(self, simbolo):
        t = self.tablero

        for i in range(3):
            fila_ganadora = True
            for j in range(3):
                if t[i][j] != simbolo:
                    fila_ganadora = False
                    break
            if fila_ganadora:
                return True

        for j in range(3):
            col_ganadora = True
            for i in range(3):
                if t[i][j] != simbolo:
                    col_ganadora = False
                    break
            if col_ganadora:
                return True

        diag_principal = True
        for i in range(3):
            if t[i][i] != simbolo:
                diag_principal = False
                break
        if diag_principal:
            return True

        diag_secundaria = True
        for i in range(3):
            if t[i][2 - i] != simbolo:
                diag_secundaria = False
                break
        if diag_secundaria:
            return True

        return False

    def obtener_oponente(self, jugador):
        for j in self.jugadores.keys():
            if j != jugador:
                return j
        return None

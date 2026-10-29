def mismo_valor_valido(lista: list) -> str | None:
    '''
    Comprueba si todos los valores de una lista son los mismos.
    En caso de serlo y que el valor sea 'X' u 'O':
    retorna el valor contenido, en caso contrario, retorna None.
    '''
    if (len(set(lista)) == 1) and (lista[0] in ('X', 'O')):
        return lista[0]

def comprobar_ganador_lista_aplanada(tablero: list) -> tuple:
    '''
    Recibe un tablero como una lista 1-dimensional,
    donde los valores de cada jugador se representan como 'X' y 'O'.
    Retorna una tupla que contiene:
     - Bool que indica si hay un ganador o no.
     - Str  que indica el valor repetido.
    '''
    tablero_bidimensional = []

    for i in range(3):        
        tablero_bidimensional.append(tablero[i * 3 : i * 3 + 3])

    return comprobar_ganador_lista_de_listas(tablero_bidimensional)


def comprobar_ganador_lista_de_listas(tablero: list) -> tuple:
    '''
    Recibe un tablero como una lista 2-dimensional,
    donde los valores de cada jugador se representan como 'X' y 'O'.
    Retorna una tupla que contiene:
     - Bool que indica si hay un ganador o no.
     - Str  que indica el valor repetido.
    '''
    for i in range(3):
        valores_fil = []
        valores_col = []
        for j in range(3):
            valores_fil.append(tablero[i][j])
            valores_col.append(tablero[j][i])

        misma_fil = mismo_valor_valido(valores_fil)
        misma_col = mismo_valor_valido(valores_col)

        if misma_fil:
            return True, misma_fil
        if misma_col:
            return True, misma_col


    valores_diag_1 = []
    valores_diag_2 = []

    for i in range(3):
        valores_diag_1.append(tablero[i][i])
        valores_diag_2.append(tablero[i][2 - i])

    misma_diag_1 = mismo_valor_valido(valores_diag_1)
    misma_diag_2 = mismo_valor_valido(valores_diag_2)

    if misma_diag_1:
        return True, misma_diag_1
    if misma_diag_2:
        return True, misma_diag_2

    return False, None


if __name__ == '__main__':
    tablero_test = [
        'O',  None, None,
        'X',  'X',  'X',
        None, None, 'O',
    ]
    print('Caso 1:', comprobar_ganador_lista_aplanada(tablero_test))

    tablero_test = [
        'O',  None, None,
        'X',  'O',  'X',
        None, None, 'O',
    ]
    print('Caso 2:', comprobar_ganador_lista_aplanada(tablero_test))

    tablero_test = [
        None, None, 'X',
        'X',  'O',  'X',
        None, None, 'X',
    ]
    print('Caso 3:', comprobar_ganador_lista_aplanada(tablero_test))

    tablero_test = [
        None, None, None,
        'X',  'O',  'X',
        None, None, 'X',
    ]
    print('Caso 4:', comprobar_ganador_lista_aplanada(tablero_test))

    tablero_test = [
        None, None, None,
        None, None, None,
        None, None, None,
    ]
    print('Caso 5:', comprobar_ganador_lista_aplanada(tablero_test))

    tablero_test = [
        False, False, False,
        False, False, False,
        False, False, False,
    ]
    print('Caso 6:', comprobar_ganador_lista_aplanada(tablero_test))

    tablero_test = [
        '', '', '',
        '', '', '',
        '', '', '',
    ]
    print('Caso 7:', comprobar_ganador_lista_aplanada(tablero_test))

import numpy as np

# Funzione per trovare la sequenza in una riga
def find_xmas(row):
    c = 0
    for i in range(len(row) - 4):
        if np.array_equal(['X', 'M', 'A', 'S'], row[i:i + 4]):
            c += 1
    return c

# Funzione principale
def find_xmas_in_matrix(matrix):
    n, m = matrix.shape
    count = 0

    # Controllo righe
    for row in matrix:
        count += find_xmas(row)

    # Controllo colonne (trasponendo la matrice)
    for col in matrix.T:
        count += find_xmas(col)

    # Controllo diagonali principali
    for offset in range(-n + 1, m):  # Offset per diagonali principali
        diagonal = matrix.diagonal(offset)
        count += find_xmas(diagonal)

    # Controllo diagonali secondarie
    flipped_matrix = np.fliplr(matrix)  # Inverti la matrice orizzontalmente
    for offset in range(-n + 1, m):  # Offset per diagonali secondarie
        diagonal = flipped_matrix.diagonal(offset)
        count += find_xmas(diagonal)

    # Controllo righe, colonne, diagonali al contrario
    reversed_matrix = np.flip(matrix, axis=0)  # Ribalta la matrice
    for row in reversed_matrix:
        count += find_xmas(row)
    for col in reversed_matrix.T:
        count += find_xmas(col)
    for offset in range(-n + 1, m):
        diagonal = reversed_matrix.diagonal(offset)
        count += find_xmas(diagonal)
    flipped_reversed_matrix = np.fliplr(reversed_matrix)
    for offset in range(-n + 1, m):
        diagonal = flipped_reversed_matrix.diagonal(offset)
        count += find_xmas(diagonal)

    return count


def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return mapp

f = open("example.txt", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

matrix = create_matrix(l)
matrix = np.array(matrix)

print(find_xmas_in_matrix(matrix))
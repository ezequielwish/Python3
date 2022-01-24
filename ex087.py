# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados.

# B) A soma dos valores da terceira coluna.

# C) O maior valor da segunda linha.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pair = 0
column_3_total = 0
highest_in_row_2 = 0

for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f'Digite um valor para [{row}, {column}]: '))

for row in range(0, 3):
    for column in range(0, 3):
        print(f'{matrix[row][column]:^5}', end='')
    print()

for row in range(0, 3):
    for column in range(0, 3):
        if matrix[row][column] % 2 == 0:
            pair += matrix[row][column]
        if column == 2:
            column_3_total += matrix[row][column]
        if row == 1:
            if matrix[row][column] > highest_in_row_2:
                highest_in_row_2 = matrix[row][column]

print('Soma dos valores pares:', pair)
print('Soma da terceira coluna:', column_3_total)
print('Maior valor da segunda linha:', highest_in_row_2)

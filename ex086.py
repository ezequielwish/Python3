# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f'Digite um valor para [{row}, {column}]: '))

for row in range(0, 3):
    for column in range(0, 3):
        print(f'{matrix[column][row]:^5}', end='')
    print()

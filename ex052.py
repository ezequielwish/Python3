# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

number = int(input('Digite um número inteiro: '))
divisibles = 0
for c in range(2, number+1):
    if number % c == 0:
        divisibles += 1
    if divisibles > 1:
        break
print('O número É PRIMO.' if divisibles == 1 else 'O número NÃO É PRIMO.')

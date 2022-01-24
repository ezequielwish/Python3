# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.

continue_ = True
numbers = 0
average = 0
highest = 0
lowest = 0
while continue_:
    number = int(input('Digite um número: '))
    if numbers == 0:
        highest = number
        lowest = number
    elif number > highest:
        highest = number
    elif number < lowest:
        lowest = number
    average += number
    numbers += 1
    answer = input('Quer continuar? [S/N] ').strip().upper()
    while answer != 'S' and answer != 'N':
        answer = input('\033[31mResposta inválida!\n\033[mQuer continuar? \033[33m[S/N]\033[34m ').strip().upper()
    if answer == 'N':
        continue_ = False
average /= numbers
print('\033[34mQuantidade de valores:', numbers)
print('Média dos valores:', average)
print('Maior número:', highest)
print('Menor número:', lowest)

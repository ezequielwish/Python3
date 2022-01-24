# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def highest(lst):
    for value in lst:
        print(value, end=' ')
    print()
    print(f'O maior número digitado foi {max(lst)}')


list_ = list()
while True:
    number = int(input('Digite um número: '))
    list_.append(number)
    while True:
        answer = str(input('Mais um? [S/N] ')).strip().upper()
        if answer in ('S', 'N'):
            break
        print('\033[31mResposta inválida! Apenas S ou N.\033[m')
    if answer == 'N':
        break
highest(list_)

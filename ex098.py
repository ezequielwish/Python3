# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e
# passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1

# b) de 10 até 0, de 2 em 2

# c) uma contagem personalizada

from time import sleep


def counting(i, f, p):
    for count in range(i, f, p):
        print(count, end=' => ')
        sleep(0.5)
    print('FIM')


print('De 0 até 10 de 1 em 1: ')
counting(0, 11, 1)
print('-='*20)
print('De 10 até 0 de 2 em 2: ')
counting(10, -1, -2)
print('-='*20)
print('Agora é sua vez: ')
start = int(input('De: '))
end = int(input('Até: '))
step = int(input('Passo: '))
if step < 0:
    end -= 1
if step > 0:
    end += 1
print('-='*20)
print('De {part} até {fim} de {passo} em {passo}:')
counting(start, end, step)
print('-='*20)

# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def draw(lst):
    for count in range(0, 5):
        number = randint(1, 10)
        print(number, end=', ')
        sleep(0.5)
        lst.append(number)
    print('PRONTO!')


def pair_sum(lista):
    total = int()
    for v in lista:
        if v % 2 == 0:
            total += v
    print(total)


list_ = list()
print('Sorteando 5 números: ', end='')
draw(list_)
print(f'Soma dos números pares em {list_}: ', end='')
pair_sum(list_)

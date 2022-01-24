# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

import random

print('O computador está pensando em um número de 0 a 5')
num = random.randint(0, 5)
user_number = int(input('Tente adivinhar o número\n>>> '))
if user_number == num:
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou :c')

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('\033[7;1m=-\033[m'*20)
print(f'\033[7;1m{"MEGA SENA":^40}\033[m')
print('\033[7;1m=-\033[m'*20)
numbers = []
answer = int(input('Quantes jogos quer que eu sorteie? '))
print('\033[7;1m=-\033[m'*20)
for count in range(0, answer):
    for n in range(0, 6):
        while True:
            number = randint(1, 60)
            if number not in numbers:
                break
        numbers.append(number)
    sleep(0.5)
    print(f'\033[33mJogo {count + 1}\033[m: {sorted(numbers)}')
    numbers.clear()
print(f'\033[7;1m{"BOA SORTE!":^40}\033[m')

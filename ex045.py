# Crie um programa que faça o computador jogar Jokenpô com você.

import random

options = ('PEDRA', 'PAPEL', 'TESOURA')
computer = random.choice(options)

print('''Escolha sua jogada:\033[34m
[1] PEDRA
[2] PAPEL
[3] TESOURA\033[m''')
player = int(input('>>> '))
if 1 <= player <= 3:
    player = options[player-1]
    print('O computador jogou:', computer)
    print('Você jogou:', player)
    if computer == player:
        print('\033[33mEMPATE!\033[m')
    elif player == 'PEDRA':
        if computer == 'PAPEL':
            print('\033[31mDERROTA!\033[m')
        else:
            print('\033[32mVITÓRIA!\033[m')
    elif player == 'PAPEL':
        if computer == 'TESOURA':
            print('\033[31mDERROTA!\033[m')
        else:
            print('\033[32mVITÓRIA!\033[m')
    else:
        if computer == 'PEDRA':
            print('\033[31mDERROTA!\033[m')
        else:
            print('\033[32mVITÓRIA!\033[m')
else:
    print('\033[31mOpção inválida!\033[m')

# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random


round_ = 1
wins = 0
while True:
    print(f'\033[34mRound {round_}\033[m')
    computer = random.randint(0, 10)
    while True:
        player_number = int(input('Escolha um número de \033[33m0 a 10\033[m: '))
        if 0 <= player_number <= 10:
            break
        print('\033[31mResposta inválida!\033[m')
    if (computer + player_number) % 2 == 0:
        even_or_odd = 'P'
    else:
        even_or_odd = 'I'
    while True:
        player = input('Par ou Ímpar? \033[33m[P/I]\033[m ').strip().upper()
        if player == 'P' or player == 'I':
            break
        print('\033[31mResposta inválida!\033[m')
    print(f'\033[33mVocê jogou: {player_number}\nComputador: {computer}')
    print(f'Resultado: {computer+player_number} ({"IMPAR" if even_or_odd == "I" else "PAR"})\033[m')
    if player == even_or_odd:
        print('\033[32mVitória sua!\033[m')
        wins += 1
        round_ += 1
    else:
        break
if round_ == 1:
    print('\033[31mVocê perdeu de primeira!.\033[m')
else:
    print('\033[31mVitória do computador!\033[m')
    print('\033[34mVitórias:', wins)

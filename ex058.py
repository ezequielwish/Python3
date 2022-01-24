# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

import random

defeats = 0
computer = random.randint(0, 10)
print('O computador está pensando em um número de 0 a 10.')
while True:
    while True:
        player = int(input('Tente adivinhar o número que o pc está pensando: '))
        if 0 <= player <= 10:
            break
        else:
            print('\033[31mResposta inválida!\033[m')
    if player == computer:
        if defeats == 0:
            print('\033[32mParabéns, Você venceu sem derrotas!\033[m')
            break
        else:
            print('\033[32mParabéns, você venceu!\033[m')
            print('\033[31mDerrotas:', defeats)
            break
    print('Você errou! tente denovo.')
    defeats += 1

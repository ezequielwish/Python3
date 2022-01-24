# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# - considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from time import sleep

print(f'\033[1;33m{"==":-^40}\033[m')
print(f'\033[7;33m{"BANCO NACIONAL":-^40}\033[m')
print(f'\033[1;33m{"==":-^40}\033[m')
withdraw = int(input('Valor do saque: \n>>> R$'))
total = n50 = n20 = n10 = n1 = 0
print(f'\033[1;33m{"CALCULANDO":-^40}\033[m')
print('\033[1;33m<\033[m', end='')
for c in range(1, 39):
    sleep(0.2)
    print(f'\033[1;30;43m \033[m', end='')
while True:
    if withdraw == 0:
        break
    else:
        if withdraw >= 50:
            withdraw -= 50
            n50 += 1
            total += 50
        else:
            if withdraw >= 20:
                withdraw -= 20
                n20 += 1
                total += 20
            else:
                if withdraw >= 10:
                    withdraw -= 10
                    n10 += 1
                    total += 10
                else:
                    if withdraw >= 1:
                        withdraw -= 1
                        n1 += 1
                        total += 1
print('\033[1;33m>\033[m')
sleep(0.5)
print(f'\033[1;33m{"SAQUE":-^40}\033[m')
print(f'''> {n50}x cédulas de R$50.00
> {n20}x cédulas de R$20.00
> {n10}x cédulas de R$10.00
> {n1}x cédulas de R$1.00
\033[1;33m>>>>>>>>>>> Total = R${total:.2f}\033[m''')
sleep(2)
print(f'\033[7;33m{"VOLTE SEMPRE!":-^40}\033[m')

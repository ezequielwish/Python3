# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

number = int(input('Digite o primeiro termo: '))
ratio = int(input('Digite a razão: '))
count = 0
while count < 10:
    print(number, end=' -> ')
    number += ratio
    count += 1
print('ACABOU')

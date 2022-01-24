# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

number = int(input('Digite o primeiro termo: '))
ratio = int(input('Digite a razão: '))
for c in range(0, 10):
    print(number, end=' -> ')
    number += ratio
print('ACABOU')

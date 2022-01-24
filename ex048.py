# Faça um programa que calcule a soma entre
# todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

total = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        total += c
print('A soma entre os números divisíveis por 3 é:', total)

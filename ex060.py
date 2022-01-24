# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

number = int(input('Digite um número: '))
total = 1
while number > 0:
    print(number, end=' -> ')
    total *= number
    number -= 1
print('TOTAL', end=' = ')
print(total)

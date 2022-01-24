# Desenvolva um programa que leia seis números inteiros e mostre a
# soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

total = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        total += num
print('A soma dos pares é:', total)

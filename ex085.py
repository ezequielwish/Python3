# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
# pares e ímpares em ordem crescente.

list_ = [[], []]

for count in range(1, 8):
    number = int(input(f'Digite o {count}º número: '))
    if number % 2 == 0:
        list_[0].append(number)
    else:
        list_[1].append(number)
print('\033[33mNúmeros pares\033[m:', sorted(list_[0]))
print('\033[33mNúmeros ímpares\033[m:', sorted(list_[1]))

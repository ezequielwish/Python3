# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

list_ = []

for values in range(0, 5):
    number = int(input(f'Digite o \033[33m{values + 1}°\033[m número: '))
    if values == 0 or number > list_[-1]:
        list_.append(number)
    else:
        for position, value in enumerate(list_):
            if number <= value:
                list_.insert(position, number)
                break
print('\033[33mLista final\033[m:', list_)

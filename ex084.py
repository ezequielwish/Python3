# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.

# B) Uma listagem com as pessoas mais pesadas.

# C) Uma listagem com as pessoas mais leves.

list_ = []
heaviest = lighter = float()

while True:
    name = str(input(f'Nome da {len(list_)+1}° pessoa: ')).strip().title()
    weight = float(input('Peso: '))
    if len(list_) == 0:
        lighter = weight
        heaviest = weight
    else:
        if weight > heaviest:
            heaviest = weight
        elif weight < lighter:
            lighter = weight
    list_.append([name, weight])
    while True:
        answer = str(input('Quer continuar? \033[33m[S/N]\033[m ')).strip().upper()[0]
        if answer in ('S', 'N'):
            break
        print('\033[31mResposta inválida!\033[m')
    if answer == 'N':
        break

print('\033[33mQuantidade de pessoas\033[m:', len(list_))
print(f'\033[33mCom {heaviest:.2f}Kg a(s) pessoa(s) mais pesada(s)\033[m: ', end='')

for p in list_:
    if p[1] == heaviest:
        print(p[0], end=' ')

print()
print(f'\033[33mCom {lighter:.2f}Kg a(s) pessoa(s) mais leve(s)\033[m: ', end='')

for p in list_:
    if p[1] == lighter:
        print(p[0], end=' ')

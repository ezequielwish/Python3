# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

products = 1
cheapest = ''
cheapest_price = 0
more_than_1000 = 0
total = 0
while True:
    product = input(f'Nome do \033[32m{products}° produto\033[m: ').strip().title()
    price = float(input('Preço: \033[32mR$\033[m').replace(',', '.'))
    total += price
    if products == 1:
        cheapest = product
        cheapest_price = price
    elif price < cheapest_price:
        cheapest = product
        cheapest_price = price
    if price > 1000:
        more_than_1000 += 1
    while True:
        answer = input('Quer continuar? \033[33m[S/N]\033[m ').strip().upper()
        if answer == 'S' or answer == 'N':
            break
        print('\033[31mResposta inválida!\033[m')
    if answer == 'N':
        break
print('\033[34m-=' * 20)
print(f'Total: \033[32mR${total:.2f}\033[34m')
print(f'Quantos custam mais de R$1000.00: \033[32m{more_than_1000}\033[34m')
print(f'Produto mais barato: \033[32m{cheapest}\033[34m')
print('-=' * 20)

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

product = ('Lapiz', 1.25, 'Caneta preta', 1.99, 'Caderno', 25.45,
           'Caneta azul', 1.99, 'Apontador', 0.70, 'Canetinhas coloridas', 15.00,
           'Corretivo', 1.00, 'Caderno de caligrafia', 19.99)

print(f'\033[1;37m{"PRODUTO":<35}PREÇO\033[m')
for c in range(0, len(product)):
    if c % 2 == 0:
        print(f'\033[38m{product[c]:.<35}', end='')
    else:
        print(f'\033[32mR${product[c]:>6.2f}\033[m')

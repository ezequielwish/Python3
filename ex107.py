# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e
# metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from utilities import coin

price = float(input('Digite o preço: R$'))
print(f'O dobro do preço seria R${coin.double(price)}')
print(f'O triplo do preço seria R${coin.triple(price)}')
print(f'O preço com um desconto de 10% seria R${coin.discount(price, 10)}')
print(f'O preço com um juros de 10% seria R${coin.fees(price, 10)}')


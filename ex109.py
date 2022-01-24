# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida
# no desafio 108.

from utilities import coin

price = float(input('Digite o preço: R$'))
print(f'Dobro do preço: {coin.double(price, currency=True)}')
print(f'Triplo do preço: {coin.triple(price, currency=True)}')
print(f'Preço com um desconto de 10%: {coin.discount(price, 10, currency=True)}')
print(f'Preço com um juros de 10%: {coin.fees(price, 10, currency=True)}')

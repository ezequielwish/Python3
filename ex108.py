# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
# números como um valor monetário formatado.

from utilities import coin

price = float(input('Digite o preço: R$'))
print(f'Dobro do preço: {coin.coin(coin.double(price))}')
print(f'Triplo do preço: {coin.coin(coin.triple(price))}')
print(f'Preço com um desconto de 10%: {coin.coin(coin.discount(price, 10))}')
print(f'Preço com um juros de 10%: {coin.coin(coin.fees(price, 10))}')

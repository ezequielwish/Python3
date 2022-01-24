# Crie um pacote chamado 'utilidades' que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
# mantenha tudo funcionando.

from utilities import coin

price = float(input('Digite o preço: R$'))
coin.summary(value=price, disc=10, fee=10, currency=True)

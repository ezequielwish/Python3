# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre
# na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from utilities import coin

price = float(input('Digite o preço: R$'))
coin.summary(value=price, disc=10, fee=10, currency=True)

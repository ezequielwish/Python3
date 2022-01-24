# Dentro do pacote 'utilidades' que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leia dinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilities import data, coin

value = data.moneyput('Digite um valor monetário: R$')
coin.summary(value=value, disc=30, fee=30, currency=True)

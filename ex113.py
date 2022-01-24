# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from utilities import data

integer = data.intput('Digite um número inteiro: ')
float_ = data.floatput('Digite um número Real: ')
print(f'O número inteiro que você digitou foi: {integer}')
print(f'O número real que você digitou foi: {float_}')

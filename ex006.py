# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math

num = int(input('Digite um número: '))
print('O dobro de {} é: {}'.format(num, num*2))
print('O triplo de {} é: {}'.format(num, num*3))
print('A raiz quadrada de {} é: {}'.format(num, math.sqrt(num)))

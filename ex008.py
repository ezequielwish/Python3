# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

meters = int(input('Digite a medida em metros: '))
print('Em kilometros: {}km'.format(meters / 100))
print('Em metros: {}m'.format(meters))
print('Em centímetros: {}cm'.format(meters * 100))
print('Em milímetros: {}mm'.format(meters * 1000))

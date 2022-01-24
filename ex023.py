# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

number = int(input('Digite um número de 0 a 9999: '))
unitys = number // 1 % 10
dozens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000 % 10

print('Unidades:', unitys)
print('Dezenas:', dozens)
print('Centenas:', hundreds)
print('Milhares:', thousands)

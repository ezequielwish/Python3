# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.


side1 = int(input('Tamanho do lado 1: '))
side2 = int(input('Tamanho do lado 2: '))
side3 = int(input('Tamanho do lado 3: '))
if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print('Estas retas PODEM formar um triângulo')
else:
    print('Estas retas NÃO PODEM formar um triângulo.')

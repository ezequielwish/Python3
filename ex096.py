# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(a, b):
    print(a*b)


width = float(input('Largura do terreno: '))
height = float(input('Comprimento do terreno: '))
print(f'Área do terreno: {area(height, width)}m²')

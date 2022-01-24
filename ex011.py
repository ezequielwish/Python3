# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

width = float(input('Largura da parede: '))
height = float(input('Altura da parede: '))
area = width * height
paint = area / 2
print('para pintar {:.2f}m² serão necessários {:.2f}L de tinta'.format(area, paint))

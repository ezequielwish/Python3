# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.
import math

angle = int(input('Digite o ângulo: '))
sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print('Seno: {:.2f}'.format(sin))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tan))

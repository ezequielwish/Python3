# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o catedo adjascente: '))
hyp = math.hypot(co, ca)
print('O valor da hipotenusa é: {:.2f}'.format(hyp))

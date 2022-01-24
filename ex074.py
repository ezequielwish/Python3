# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
# valor que estão na tupla.

from random import randint

sequence = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('\033[33mSequência:\033[m:', sequence)
print('\033[33mMaior valor\033[m:', max(sequence))
print('\033[33mMenor valor\033[m:', min(sequence))

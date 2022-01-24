# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

name = input('Digite seu nome completo: ').strip().title().split()
print('Nome completo:', ' '.join(name))
print('Primeiro nome:', name[0])
print('Último nome:', name[len(name) - 1])

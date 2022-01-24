# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.

thing = input('Digite algo: ')
print('Qual o tipo primitivo? ', type(thing))
print('Só tem espaços? ', thing.isspace())
print('É um número? ', thing.isnumeric())
print('É alfabético? ', thing.isalpha())
print('É alfanumérico? ', thing.isalnum())
print('Está em minúsculo? ', thing.islower())
print('Está em maiúsculo? ', thing.isupper())
print('Está capitalizado? ', thing.istitle())

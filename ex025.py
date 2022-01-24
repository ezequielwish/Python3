# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Digite seu nome completo: '))
is_silva = 'SILVA' in name.upper().split()
print('Tem "Silva" no nome? ', is_silva)

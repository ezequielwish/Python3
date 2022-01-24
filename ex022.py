# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

name = str(input('Digite seu nome completo: '))
lower = name.lower()
upper = name.upper()
lenght = len(name) - name.count(' ')
first_name_lenght = name.find(' ')


print('Nome em minúsculo:', lower)
print('Nome em maiúsculo:', upper)
print('Quantidade de letras:', lenght)
print('Quantidade de letras no primeiro nome:', first_name_lenght)

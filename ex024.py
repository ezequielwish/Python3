# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

city = input('Digite o nome de uma cidade: ')
starts_with_santo = city[:5:].upper() == 'SANTO'
print('Começa com "SANTO"? ', starts_with_santo)

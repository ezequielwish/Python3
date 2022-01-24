# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

phrase = input('Digite uma frase: ').upper().replace(' ', '')
print('É um palíndromo.' if phrase == phrase[::-1] else 'Não é um palíndromo.')

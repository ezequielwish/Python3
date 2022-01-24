# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

text = input('Digite uma frase:').strip().upper()
print('Quantidade de letras "A":', text.count('A'))
print('Primeira aparição:', text.find('A')+1)
print('Última aparição:', text.rfind('A')+1)

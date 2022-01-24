# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais


number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
if number1 == number2:
    print('Os dois números são iguais')
elif number1 > number2:
    print('O primeiro número é maior.')
else:
    print('O segundo número é maior.')

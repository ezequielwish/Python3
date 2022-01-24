# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

number = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais número: ')),
          int(input('Digite o último número: ')))

print(f'Você digitou:', number)
print(f'Quantos 9 apareceram:', number.count(9))
if 3 in number:
    print(f'O primeiro valor 3 apareceu na posição:', number.index(3))
else:
    print('Não foi digitado o valor 3.')
print(f'Os números pares foram: ', end='')
for value in number:
    if value % 2 == 0:
        print(value, end=' ')

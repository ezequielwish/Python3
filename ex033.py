# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

number1 = int(input('Digite o primeiro número: '))
highest = number1
lowest = number1
number2 = int(input('Digite o segundo número: '))
if number2 > highest:
    highest = number2
if number2 < lowest:
    lowest = number2
number3 = int(input('Digite o terceiro número: '))
if number3 > highest:
    highest = number3
if number3 < lowest:
    lowest = number3
print('O maior número foi:', highest)
print('O menor número foi:', lowest)

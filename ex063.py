# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

number = int(input('Quantos elementos da sequência quer ver? '))
count = 3
first = 0
second = 1
print(first, end=' -> ')
print(second, end=' -> ')
while count <= number:
    next_ = first + second
    print(next_, end=' -> ')
    first = second
    second = next_
    count += 1
print('FIM')

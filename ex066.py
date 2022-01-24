# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre elas (desconsiderando o flag).

number = 0
numbers = 0
total = 0
while True:
    number = int(input('Digite um número: [999 para parar] '))
    if number == 999:
        break
    numbers += 1
    total += number
print('Quantidade de números digitados:', numbers)
print('Soma dos números digitados:', total)


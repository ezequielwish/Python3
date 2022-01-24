# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).


number = 0
count = -1
total = -999
while number != 999:
    number = int(input('Digite um número: [999 para parar] '))
    total += number
    count += 1
print('Quantidade de números digitados:', count)
print('Soma dos números digitados:', total)

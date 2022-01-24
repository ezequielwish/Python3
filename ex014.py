# Escreva um programa que converta uma temperatura digitando em graus
# Celsius e converta para graus Fahrenheit.

in_celsius = float(input('Qual a temperatura em Celsius? '))
in_fahrenheit = 9 * in_celsius / 5 + 32
print('A temperatura em Fahrenheit é: {:.2f}°f'.format(in_fahrenheit))

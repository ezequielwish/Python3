# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

days_of_use = int(input('Por quantos dias o carro foi usado? '))
travelled_distance = float(input('Rodou quantos kilômetros? '))
total = days_of_use * 60 + travelled_distance * 0.15
print('O total a pagar pelo aluguel é: R${:.2f}'.format(total))

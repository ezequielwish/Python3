# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distance = int(input('Qual a distância do destino? '))
if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45
print('O valor da viagem é: R${:.2f}'.format(price))

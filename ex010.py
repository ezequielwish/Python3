# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.

wallet = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = 5.51
print('Seus R${:.2f} valem U${:.2f} no dia de hoje.'.format(wallet, wallet/dolar))

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Digite o valor do produto: R$'))
price_with_discount = price - price * 0.05
print('Com desconto de 5% seria: R${:.2f}'.format(price_with_discount))

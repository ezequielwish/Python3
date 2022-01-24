# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

house_value = float(input('Qual o valor total da casa? '))
salary = float(input('Qual o seu salário? '))
months = int(input('Em quantos anos vai pagar? ')) * 12
price_per_month = house_value / months
print('Você terá que pagar {}x de R${:.2f}'.format(months, price_per_month))
if price_per_month > salary * 0.3:
    print('A mensalidade é maior que 30% do seu salário portanto não pode efetuar a compra.')
else:
    print('Parabéns, você está apto para comprar a casa.')

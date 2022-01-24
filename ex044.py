# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço normal
#
# – 3x ou mais no cartão: 20% de juros

value = float(input('Digite o valor do produto: R$'))
print('''Método de pagamento:\033[34m
[1] Dinheiro/cheque
[2] Cartão\033[m''')
option = int(input('>>> '))
if option == 1 or option == 2:
    if option == 1:
        value *= 0.9
    else:
        installments = int(input('Em quantas vezes?\n>>> '))
        if installments < 1:
            print('\033[31mResposta inválida!\033[m')
        elif installments == 1:
            value *= 0.95
        elif installments >= 3:
            value *= 1.2
        print(f'Valor mensal: R${(value/installments):.2f}')
    print(f'Valor total a pagar: R${value:.2f}')
else:
    print('\033[31mOpção inválida!\033[m')

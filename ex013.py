# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Digite o salário do funcionário: R$'))
increased_salary = salary * 1.15
print('O salário com 15% de aumento seria: R${:.2f}'.format(increased_salary))

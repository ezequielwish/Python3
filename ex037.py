# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

number = int(input('Digite um número: '))
print('Pra qual base de conversão?')
print('''
[1] Binário
[2] Octal
[3] Hexadecimal
''')
option = int(input('>>> '))
if option < 1 or option > 3:
    print('\033[31mNúmero inválido!\033[m')
elif option == 1:
    print('Em binário:', bin(number)[2:])
elif option == 2:
    print('Em octal:', oct(number)[2:])
else:
    print('Em Hexadecimal:', hex(number)[2:])

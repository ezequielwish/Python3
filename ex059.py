# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

while True:
    number1 = int(input('\033[33mDigite o primeiro número: '))
    number2 = int(input('Digite o segundo número: '))
    print('''mEscolha a opção desejada:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa\033[m''')
    while True:
        option = int(input('>>> '))
        if 1 <= option <= 5:
            break
        print('\033[31mERRO! Opção inválida!\033[m')
    if option == 1:
        print('Soma dos dois números:', number1 + number2)
    elif option == 2:
        print('Multiplicação dos dois números:', number1 * number2)
    elif option == 3:
        print('O maior número é:', number1 if number1 > number2 else number2)
    elif option == 4:
        pass
    else:
        print('\033[33mAté a próxima ^^\033[m')
        break

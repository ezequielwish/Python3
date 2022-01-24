# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será
# mostrado ou não na tela o processo de cálculo do fatorial.

def factorial(number, show=False):
    """
    Calcula o fatorial de um núumero
    :param number: o número a ser calculado o fatorial
    :param show: mostrar o cálculo
    :return: fatorial
    """
    fact = 1
    for count in range(number, 0, -1):
        fact *= count
        if show:
            print(count, end='')
            if count == 1:
                print(' = ', end='')
            else:
                print(' x ', end='')
    return fact


print(factorial(5, True))

# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

def intput(string):
    """
    Verifica se o que foi digitado é um número
    :param string: texto do input
    :return: valor digitado
    """
    while True:
        read = str(input(string))
        if read.isnumeric():
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return read


# Programa Principal
number = intput('Digite um número: ')
print('Você acabou de digitar o número:', number)

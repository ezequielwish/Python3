# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.

def vote(birth_year):
    """
    Verifica se a pessoa pode votar
    :param birth_year: ano de nascimento da pessoa
    :return: mostra na tela se pode ou não votar
    """
    from datetime import datetime

    year = datetime.now().year
    age = year - birth_year
    if age < 16:
        print(f'\033[32mCom {age} anos não vota.\033[m')
    elif 60 > age > 17:
        print(f'\033[31mCom {age} anos o voto é obrigatório.\033[m')
    else:
        print(f'\033[33mCom {age} anos o voto é opcional.\033[m')


birth = int(input('Qual seu ano de nascimento? '))
vote(birth)

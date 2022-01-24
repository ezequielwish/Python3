# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome
# de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(name_='<unknown>', goals_=0):
    """
    Mostra uma string de quantos gols um jogador fez
    :param name_: nome do jogador
    :param goals_: quantidade de gols
    :return:
    """
    print(f'O jogador {name_} fez {goals_} gol(s) no campeonato.')


name = str(input('Nome do jogador: ')).title().strip()
goals = input('Quantidade de Gols: ')
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
ficha(name, goals)

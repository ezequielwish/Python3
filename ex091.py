# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep as sl
from random import randint as ri
from operator import itemgetter as ig

game = {'Jogador 1': ri(1, 6),
        'Jogador 2': ri(1, 6),
        'Jogador 3': ri(1, 6),
        'Jogador 4': ri(1, 6)}
ranking = {}

print('-=' * 20)
for key, value in game.items():
    print(f'O {key} tirou {value} no dado.')
    sl(1)
print('-=' * 20)
print('Resultados: ')
ranking = sorted(game.items(), key=ig(1), reverse=True)
for key, value in enumerate(ranking):
    print(f'{key + 1}º lugar - {value[0]} com {value[1]}')
    sl(1)

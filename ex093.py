# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
# em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de
# gols feitos durante o campeonato.

data = {}
goals = []

data['Nome'] = str(input('Nome do jogador: ')).strip().title()
matches = int(input(f'Quantas partidas {data["Nome"]} jogou: '))
for count in range(1, matches + 1):
    goals.append(int(input(f'GOLs na partida {count}: ')))
data['Gols'] = goals
data['Total'] = sum(goals)
for key, value in data.items():
    print(f'O campo {key} tem o valor {value}')
print('-='*30)
print(f'O jogador {data["Nome"]} jogou {matches} partidas.')
for count in range(1, matches + 1):
    print(f'    => Na partida {count}, fez {data["Gols"][count - 1]} gols. <=')
print(f'Foi um total de {data["Total"]} gols.')
print('-='*30)

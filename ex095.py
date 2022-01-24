# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.

player = dict()
players = list()
games = list()

while True:
    player['Nome'] = str(input('Qual o nome do jogador? ')).strip().title()
    matches = int(input(f'Quantas partidas {player["Nome"]} jogou? '))
    for c in range(0, matches):
        games.append(int(input(f'Quantos GOLs na partida {c + 1}? ')))
    player['GOLs'] = games[:]
    player['Total'] = sum(games)
    games.clear()
    players.append(player.copy())
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()
        if res in ('S', 'N'):
            break
        print('Resposta inválida! Apenas S ou N.')
    if res == 'N':
        break
print('-'*60)
print('Cod. Jogador                 Gols      Total')
for key, value in enumerate(players):
    print(f'{key + 1})   {value["Nome"]:<24}{value["GOLs"]}      {value["Total"]}')
print('-'*60)
while True:
    details = int(input('Mostrar dados de qual jogador? [0 para parar] '))
    if details > len(players):
        print('Este jogador não existe!')
    elif details == 0:
        break
    for key, value in enumerate(players):
        if key == details + 1:
            print(f'<<< Detalhes do {value["Nome"]} >>>')
            for c in range(0, len(value["GOLs"])):
                print(f'No jogo {c+1} ele fez {value["GOLs"][c]} GOLs')
print('<<< FIM DO PROGRAMA >>>')

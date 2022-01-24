# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

table = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Athletico Paranaense', 'Santos', 'São Paulo',
         'Internacional', 'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia', 'Ceará', 'Cruzeiro',
         'América Mineiro', 'Atlético Goianiense', 'Chapecoense', 'Botafogo', 'Vasco da Gama', 'Red Bull Bragantino')

print('\033[33mVinte primeiros colocados:\033[m', table)
print('\033[33mCinco primeiros colocados:\033[m', table[:5])
print('\033[33mQuatro últimos colocados:\033[m', table[-4:])
print('\033[33mEm ordem alfabética:\033[m', sorted(table))
print(f'\033[33mPosição do Chapecoense:\033[m {table.index("Chapecoense") + 1}º')

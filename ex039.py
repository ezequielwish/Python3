# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

birth = int(input('Digite o ano de nascimento: '))
year_to_go = birth + 18
year_now = datetime.now().year
print('Seu ano de alistamento é: \033[32m{}\033[m'.format(year_to_go))
if year_to_go == year_now:
    print('\033[33mChegou a hora!\033[m')
elif year_to_go < year_now:
    print('\033[31mVocê devia ter ido a {} ano(s)!\033[m'.format(year_now - year_to_go))
else:
    print('\033[32mAinda não é a hora. Volte em {} ano(s).\033[m'.format(year_to_go - year_now))

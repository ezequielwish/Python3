# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import datetime

year = int(input('Digite o ano: [0 para ano atual] '))
if year == 0:
    year = datetime.now().year
if year % 4 == 0:
    print(year, 'é um ano BISSEXTO.')
else:
    print(year, 'NÃO é um ano BISSEXTO.')

# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

year = datetime.now().year
majors = 0
minors = 0
for people in range(1, 8):
    birth = int(input(f'Data de nascimento da {people}° pessoa: '))
    age = year - birth
    if age >= 18:
        majors += 1
    else:
        minors += 1
print('Maiores de idade:', majors)
print('Menores de idade:', minors)

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo,
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos.


older_man_name = ''
older_man_age = 0
ages = 0
womans_under_20 = 0
for people in range(1, 5):
    name = input(f'Nome da {people}° pessoa: ').strip().title()
    age = int(input('Idade: '))
    gender = input(f'Sexo: [M/F] ').strip().upper()[0]
    ages += age
    if gender == 'F':
        if age < 20:
            womans_under_20 += 1
    else:
        if age > older_man_age:
            older_man_age = age
            older_man_name = name
ages /= 4
print('Média das idades:', ages)
print('Homem mais velho:', older_man_name)
print('Mulheres abaixo de 20 anos:', womans_under_20)

#  Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#  o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

people = 1
majors = 0
minors = 0
mans = 0
womans_under_20 = 0
while True:
    while True:
        age = int(input(f'Idade da \033[33m{people}° pessoa\033[m: '))
        if age > 0:
            break
        print('\033[31mIdade inválida!\033[m')
    if age >= 18:
        majors += 1
    while True:
        gender = input('Sexo: \033[33m[F/M]\033[m ').strip().upper()
        if gender == 'F' or gender == 'M':
            break
        print('\033[31mResposta inválida!\033[m')
    if gender == 'M':
        mans += 1
    else:
        if age < 20:
            womans_under_20 += 1

    people += 1
    while True:
        answer = input('Quer continuar? \033[33m[S/N]\033[m ').strip().upper()
        if answer == 'S' or answer == 'N':
            break
        print('\033[31mResposta inválida!\033[m')
    if answer == 'N':
        break
print('-=' * 20)
print('\033[34mMaiores de 18:', majors)
print('Homens:', mans)
print('Mulheres abaixo de 20 anos:', womans_under_20)
print('-=' * 20)

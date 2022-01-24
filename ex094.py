# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas

# B) A média de idade

# C) Uma lista com as mulheres

# D) Uma lista de pessoas com idade acima da média

def line():
    print('-=' * 30)


list_ = list()
data = dict()
age = average = 0
woman = list()

while True:
    data['Nome'] = str(input('Nome: ')).strip().title().split()[0]
    while True:
        data['Sexo'] = str(input('Sexo: \033[33m[F/M]\033[m ')).strip().upper()
        if data['Sexo'] in ('M', 'F'):
            break
        print('\033[31mResposta inválida! Apenas F ou M.\033[m')
    if data['Sexo'] == 'F':
        woman.append(data['Nome'])
    data['Idade'] = int(input('Idade: '))
    age += data['Idade']
    list_.append(data.copy())
    while True:
        answer = str(input('Quer continuar? \033[33m[S/N]\033[m ')).strip().upper()
        if answer in ('S', 'N'):
            break
        print('\033[31mResposta inválida! Apenas S ou N.\033[m')
    if answer == 'N':
        break
average = age / len(list_)
line()
print(f'A) Ao todo temos {len(list_)} pessoas cadastradas.')
print(f'B) A média de idades é de {average:.2f} anos.')
if len(woman) == 0:
    print('C) Nenhuma mulher foi cadastrada.')
elif len(woman) == 1:
    print(f'C) A única mulher cadastrada foi a {woman[0]}.', end='')
else:
    print('C) As mulheres cadastradas foram ', end='')
    for value in woman:
        print(value, end='...')
print()
print('D) Lista das pessoas que estão acima da média:')
line()
for key, value in enumerate(list_):
    if value['Idade'] > average:
        print(f'    Nome: {value["Nome"]} | Sexo: {value["Sexo"]} | Idade: {value["Idade"]}')
line()
print('<<< ENCERRADO >>>')
line()

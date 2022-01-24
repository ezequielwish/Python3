# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dict_ = {}
retirement = int()
dict_['Nome'] = str(input('Nome: ')).strip().title()
while True:
    gender = str(input('Sexo: [F/M] ')).strip().upper()[0]
    if gender in ('F', 'M'):
        break
    print('Resposta inválida!')
if gender == 'M':
    dict_['Sexo'] = 'Masculino'
else:
    dict_['Sexo'] = 'Feminino'
birth = int(input('Ano de nascimento: '))
dict_['Idade'] = datetime.now().year - birth
dict_['CTPS'] = int(input('Carteira de trabalho: [0 se não tiver] '))
if dict_['CTPS'] != 0:
    dict_['Ano de contratação'] = int(input('>>> Ano de contratação: '))
    dict_['Salário'] = 'R$' + str(input('>>> Salário: R$'))
    if dict_['Sexo'] == 'M':
        retirement = dict_['Ano de contratação'] + 30
    else:
        retirement = dict_['Ano de contratação'] + 35
    dict_['Idade em que vai se aposentar'] = (retirement - datetime.now().year) + dict_['Idade']
print('-='*20)
for key, value in dict_.items():
    print(f'{key}: {value}')

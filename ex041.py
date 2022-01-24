# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

from datetime import datetime

birth = int(input('Digite o ano de nascimento: '))
age = datetime.now().year - birth
category = ''

if age <= 9:
    category = 'MIRIM'
elif 9 < age <= 14:
    category = 'INFANTIL'
elif 14 < age <= 19:
    category = 'JUNIOR'
elif 19 < age <= 25:
    category = 'SÊNIOR'
else:
    category = 'MASTER'

print('Idade:', age)
print('Categoria:', category)

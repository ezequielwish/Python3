# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

grade1 = float(input('Primeira nota: '))
grade2 = float(input('Segunda nota: '))
average = (grade1 + grade2) / 2
status = ''
if average < 5:
    status = '\033[31mReprovado\033[m'
elif 5 <= average < 7:
    status = '\033[33mRecuperação\033[m'
else:
    status = '\033[32mAprovado\033[m'
print('Média:', average)
print('Estado:', status)

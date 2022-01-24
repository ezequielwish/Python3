# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

from time import sleep

list_ = []
student = []

while True:
    student.append(str(input(f'Nome do \033[33m{len(list_)+1}° aluno\033[m: ')).strip().upper())
    student.append(float(input('Nota 1: ')))
    student.append(float(input('Nota 2: ')))
    list_.append(student[:])
    student.clear()
    while True:
        answer = str(input('Quer continuar? \033[33m[S/N]\033[m ')).strip().upper()
        if answer in ('S', 'N'):
            break
        print('\033[31mResposta inválida!\033[m')
    if answer == 'N':
        break
print('-='*20)
for position, people in enumerate(list_):
    print(f'{position + 1}) {people[0]:.<30} {(people[1] + people[2]) / 2}')
print('0) SAIR')
print('-='*20)
while True:
    while True:
        details_of = int(input('Escolha o aluno para detalhes: '))
        if 0 <= details_of <= len(list_):
            break
        print('\033[31mOpção inválida!\033[m')
    if details_of == 0:
        break
    else:
        for position, people in enumerate(list_):
            if position == details_of - 1:
                print(f'Nome: {people[0]}\nNota 1: {people[1]}\nNota 2: {people[2]}')
                sleep(3)
print(f'{"VOLTE SEMPRE!":-^40}')

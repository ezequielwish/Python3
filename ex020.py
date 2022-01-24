# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

student1 = input('Primeiro aluno: ')
student2 = input('Segundo aluno: ')
student3 = input('Terceiro aluno: ')
student4 = input('Quarto aluno: ')
students = [student1, student2, student3, student4]
random.shuffle(students)
print('a ordem de apresentação será: \n', students)

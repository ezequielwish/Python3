# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

student1 = input('Primeiro aluno: ')
student2 = input('Segundo aluno: ')
student3 = input('Terceiro aluno: ')
student4 = input('Quarto aluno: ')
winner = random.choice([student1, student2, student3, student4])

print('O aluno escolhido foi:', winner)

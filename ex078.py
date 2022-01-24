# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

list_ = []
for c in range(0, 5):
    list_.append(int(input(f'Digite um número para a posição {c}: ')))
print()
highest = max(list_)
lowest = min(list_)
print('Números digitados:', list_)
print(f'O maior valor foi \033[33m{highest}\033[m na posição:', list_.index(highest))
print(f'O menor valor foi \033[33m{lowest}\033[m na posição:', list_.index(highest))

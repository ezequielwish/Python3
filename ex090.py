# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dict_ = {'name': str(input('Nome: '))}
dict_['average'] = float(input(f'Média de {dict_["name"]}: '))
if dict_['average'] < 5:
    dict_['status'] = 'Reprovado'
elif dict_['average'] <= 6:
    dict_['status'] = 'Recuperação'
elif dict_['average'] <= 10:
    dict_['status'] = 'Aprovado'
print(f'Nome: {dict_["name"]}\nMédia: {dict_["average"]}\nSituação: {dict_["status"]}')

# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
#
# – Quantidade de notas
#
# – A maior nota
#
# – A menor nota
#
# – A média da turma
#
# – A situação (opcional)

def grades(*grade, status=False):
    """
    Cria um dicionário com dados de uma turma
    :param grade: notas dos alunos
    :param status: mostrar se a turma está com uma média boa ou não
    :return: dicionário
    """
    dict_ = {'Quantidade': len(grade), 'Maior': max(grade), 'Menor': min(grade), 'Média': sum(grade) / len(grade)}
    if status:
        if dict_['Média'] > 5:
            dict_['Situação'] = 'Boa'
        else:
            dict_['Situação'] = 'Ruim'
    return dict_


print(grades(1, 4, 5, 6, status=True))

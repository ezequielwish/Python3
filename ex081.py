#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

#  A) Quantos números foram digitados.

#  B) A lista de valores, ordenada de forma decrescente.

#  C) Se o valor 5 foi digitado ou não na lista.

list_ = []

while True:
    number = int(input(f'Digite o {len(list_)+ 1}° número: \033[31m[negativo para parar]\033[m '))
    if number < 0:
        break
    else:
        list_.append(number)
print()
print('\033[33mLista\033[m:', list_)
print('\033[33mLista descrescente: \033[m:', sorted(list_, reverse=True))
print('\033[33mQuantidade de números\033[m:', len(list_))
print('\033[33mExistencia do número 5 na lista\033[m:', 5 in list_)

# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

list_ = []
while True:
    value = int(input('Digite um valor: '))
    if value in list_:
        print('\033[31mEste valor ja foi adicionado.\033[m')
    else:
        list_.append(value)
    while True:
        answer = str(input('Quer continuar? [S,N]')).strip().upper()
        if answer in ('S', 'N'):
            break
        print('\033[31mResposta inválida!\033[m')
    if answer == 'N':
        break
print('Os valores digitados foram:', sorted(list_))

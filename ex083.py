# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.

list_ = []

expression = str(input('Digite a expressão: '))

for character in expression:
    if character == '(':
        list_.append('(')
    elif character == ')':
        if len(list_) > 0:
            list_.pop()
        else:
            list_.append(')')
            break

if len(list_) == 0:
    print('A expressão está \033[32mcorreta\033[m.')
else:
    print('A expressão está \033[31mincorreta\033[m.')

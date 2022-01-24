# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

list_ = []
odd = []
pair = []

while True:
    number = int(input('Digite um número: \033[31m[negativo para parar]\033[m '))
    if number < 0:
        break
    list_.append(number)

for value in list_:
    if value % 2 == 0:
        pair.append(value)
    else:
        odd.append(value)

print()
print('\033[33mLista principal\033[m:', list_)
print('\033[33mLista de pares\033[m:', pair)
print('\033[33mLista de ímpares\033[m:', odd)

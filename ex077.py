# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

words = ('ESCREVA', 'VARIAS', 'PALAVRAS', 'AQUI', 'NESSE', 'ESPAÇO', 'QUE', 'EU', 'IREI', 'ANALIZAR')
for word in words:
    print(f'\033[33mVogais na palavra \033[4m{word}\033[m: ', end='')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
    print()

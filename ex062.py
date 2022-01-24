# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

number = int(input('Digite o primeiro termo: '))
ratio = int(input('Digite a razão: '))
times = 10
count = 1
while times != 0:
    while count <= times:
        print(number, end=' -> ')
        number += ratio
        count += 1
    print('ACABOU')
    count = 1
    answer = int(input('Quer mostrar mais quantos termos? '))
    times = answer

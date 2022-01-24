# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    number = int(input('Digite um número: \033[33m[negativo para fechar]\033[m '))
    if number < 0:
        break
    print('~' * 43)
    for c in range(1, 11):
        print(f'{number} x {c:>2} = {(number*c):>2}')
    print('~' * 43)
print('Até a próxima ^^')

# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

side1 = int(input('Primeiro lado: '))
side2 = int(input('Segundo lado: '))
side3 = int(input('Terceiro lado: '))

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    type_ = ''
    if side1 == side2 == side3:
        type_ = 'EQUILÁTERO'
    elif side1 != side2 and side1 != side3:
        type_ = 'ESCALENO'
    else:
        type_ = 'ISÓSCELES'
    print('Tipo do triângulo: \033[32m{}\033[m'.format(type_))
else:
    print('\033[31mEstes lados não podem formar um triângulo.\033[m')

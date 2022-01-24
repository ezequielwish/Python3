# Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um
# número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

sequence1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze')
sequence2 = ('doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
full = sequence1 + sequence2
while True:
    number = int(input('Digite um número de \033[33m0 a 20\033[m: '))
    if number in range(0, 21):
        break
    else:
        print('\033[31mEste número não está entre 0 e 20.\033[m')
print(f'Você digitou o número {full[number]}.')

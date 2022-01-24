# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
# manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante:
# use cores.

def man(string):
    help(string)


while True:
    command = str(input('Função ou Biblioteca \033[33m>>>\033[m '))
    if command.upper() == 'FIM':
        break
    man(command)
print('\033[33m<<<Fim do programa>>>\033[m')

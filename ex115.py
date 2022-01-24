# Crie um menu em Python, usando modularização.

from ex115 import interface, colors
from time import sleep
from datetime import datetime
from utilities import data

option = int()
people = dict()
db = 'clients.txt'
# Verify if Clientes.txt exists
print(colors.grey(f'[*] Procurando "{db}"...'))
sleep(1)
try:
    with open(db, 'r') as file:
        file.close()
except FileNotFoundError:
    print(colors.grey(f'[*] Criando "{db}"...'))
    with open(db, 'w+') as file:
        file.write('')
        file.close()
    sleep(1)
finally:
    print(colors.grey(f'[*] Abrindo "{db}"...'))
    sleep(1)
# Title
interface.title('<<< CADASTRO DE CLIENTES >>>', color1=3, color2=8)
# Menu
while option != 3:
    interface.options([colors.white('Mostrar lista de clientes'),
                       colors.white('Adicionar cliente'),
                       colors.white('Sair do programa')], 3)
    while True:
        option = data.intput(colors.green('>>> '))
        if option in range(1, 4):
            break
        print(colors.red('ERROR! Invalid option.'))
    # Options
    if option == 1:
        # List Clients from Clientes.txt
        interface.title('LISTA DE CLIENTES', color1=3, color2=8)
        print(colors.green(f'{"Nome":<33}Idade'))
        with open(db, 'r') as file:
            print(file.read())
            file.close()
        print(colors.yellow("-=" * 20))
        sleep(0.5)
    elif option == 2:
        # Add people in Clientes.txt
        interface.title('ADICIONAR', color1=3, color2=8)
        people['name'] = str(input(colors.yellow('Nome do cliente: '))).strip().title()
        year = data.intput(colors.yellow('Ano de nascimento: '))
        # check if the person was born
        while True:
            if year > datetime.now().year:
                print(colors.red('Error! This people does not exist.'))
            else:
                break
        # calculate person's age
        people['age'] = datetime.now().year - year
        # add to file
        with open(db, 'a') as file:
            file.write(f'{people["name"]:<33}{people["age"]} anos\n')
            file.close()
        sleep(0.5)
        print(colors.grey('[*] Adicionado com sucesso!'))
        print(colors.yellow("-=" * 20))
interface.title('<<< FIM DO PROGRAMA >>>', 3, 0)

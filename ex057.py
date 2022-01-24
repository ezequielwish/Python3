# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    gender = input('Digite o seu sexo: [F/M] ').strip().upper()
    if gender == 'F' or gender == 'M':
        break
    print('\033[31mResposta inválida! Apenas F (Feminino) ou M (Masculino).\033[m')

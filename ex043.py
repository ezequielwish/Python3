# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

height = float(input('Digite sua altura em metros: [ex: 1.60] '))
weight = float(input('Digite seu peso em kilos: [ex: 65.6] '))
bmi = weight / (height**2)  # BMI (Body Mass Index) = IMC (Índice de Massa Corpotal)
if bmi < 18.5:
    result = '\033[33mABAIXO DO PESO\033[m'
elif 18.5 < bmi <= 25:
    result = '\033[32mPESO IDEAL\033[m'
elif 25 < bmi <= 30:
    result = '\033[33mSOBREPESO\033[m'
elif 30 < bmi <= 40:
    result = '\033[31mOBESIDADE\033[m'
else:
    result = '\033[41mOBESIDADE MÓRBIDA\033[m'
print(f'IMC: \033[32m{bmi:.2f}\033[m')
print('Status:', result)

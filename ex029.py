# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

speed = int(input('O carro está a quantos km/h? '))
if speed > 80:
    speed_exceeded = speed - 80
    penalty = speed_exceeded * 7
    print('O carro está acima do limite de 80km/h')
    print('A multa por {}km/h acima do limite é de R${:.2f}'.format(speed_exceeded, penalty))
else:
    print('O carro está dentro do limite de 80km/h')

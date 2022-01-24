# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

higher = 0.0
lower = 0.0
for people in range(1, 6):
    weight = float(input(f'Peso da {people}° pessoa: [Kg] '))
    if people == 1:
        higher = weight
        lower = weight
    elif weight > higher:
        higher = weight
    elif weight < lower:
        lower = weight
print(f'A pessoa mais pesada tem: {higher:.1f}Kg')
print(f'A pessoa mais leve tem: {lower:.1f}Kg')

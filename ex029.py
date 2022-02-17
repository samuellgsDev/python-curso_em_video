# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.
#
# Write a program that reads the speed of a car.
# If the speed is above 80km/h, show a message saying that the driver was
# fined. The traffic ticket will be R$7,00 per km over the limit.
#
v = int(input('Enter the speed of the car: '))
fine = (v - 80) * 7
if v > 80:
    print('You were fined!')
    print(f'The traffic ticket will be R${fine:.2f}')
else:
    print('You are safe!')

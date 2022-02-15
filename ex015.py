# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.
#
# Write a program that asks the number of kilometers traveled
# by a rented car and the number of days for which it was rented.
# Calculate the price to pay, knowing that the car
# costs R$60 per day and R$0.15 per km driven.


car = 60
km = 0.15
rent = int(input('how many days you rented the car? '))
km_t = int(input('how many km you traveled? '))
day_car = car * rent
km_car = km_t * km
total = day_car + km_car
print(f'you rented the car for {rent} days and traveled {km_t} km,', end='')
print(f'so the total is R${total:.2f}')

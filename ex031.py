# desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.
#
# develop a program that asks for the distance of a trip in Km.
# Calculate the price of the trip,
# charging R$0,50 per Km for trips of up to 200Km
# and R$0,45 for longer trips.
#
distance = float(input('Enter the distance: '))
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
print(f'The price of the trip is R${price:.2f}')

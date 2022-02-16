# Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome “SANT”.
#
# Create a program that reads the name of a city
# and tells whether or not it starts with the name “SANT”.
#
city = str(input('what city were you born in? ')).strip().lower()
print(city[:4] == 'sant')

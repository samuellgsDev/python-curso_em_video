# Crie um programa que leia o ano de nascimento de sete pessoas.
#  No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
#
# Create a program that reads the birth year of seven people.
#  At the end, show how many people have not yet reached the age of majority
# and how many are older.
#
import datetime
datetime.date.today()
count = 0
for a in range(1, 8):
    year = int(input(f'Enter the year of birth of the {a}º person: '))
    if datetime.date.today().year - year >= 18:
        count += 1
    else:
        count += 0
print('{} people are older than 18 years.'.format(count))
print('{} people are younger than 18 years.'.format(7 - count))

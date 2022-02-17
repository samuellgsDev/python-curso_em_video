# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#
# Develop a program that reads any year and shows if it is a leap year.
#
year = int(input('Enter a year: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'This year {year} is a leap year.')
else:
    print(f'This year {year} is not a leap year.')

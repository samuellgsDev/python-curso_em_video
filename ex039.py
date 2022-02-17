# Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#
# Write a program that reads the birth year of a young person and informs,
# according to his age, whether he will be able to join the military service,
# if it is the exact time to join or if he has already passed the time to join.
# Your program should also show how many years he has left or already passed.
#
import datetime
bith_year = int(input('Enter your birth year: '))
now = datetime.datetime.now()
age = now.year - bith_year
if age == 18:
    print('You will be able to join the military service in the year', end=' ')
    print(now.year)
    print(f'You have {age} years.')
elif age < 18:
    print('You will not be able to join the military ', end=' ')
    print('service in the year', end=' ')
    print(now.year)
    print(f'You have {age} years.')
    print(f'You have {18 - age} years to join the military service.')
elif age > 18:
    print('You have already passed the time to join the military service.')
    print(f'You have {age - 18} years already passed.')

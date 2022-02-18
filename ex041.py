# A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria,
#  de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
#
# The National Swimming Confederation needs a program that
# reads an athlete's year of birth and shows his category,
# according to age:
# – Up to 9 years: MIRIM
# – Up to 14 years old: CHILD
# – Up to 19 years old: JUNIOR
# – Up to 25 years old: SENIOR
# – Over 25 years old: MASTER
#
import datetime
datetime.date.today()
year = int(input('Enter your year of birth: '))
age = datetime.date.today().year - year
if age <= 9:
    print(f'You have {age} years old.', end=' ')
    print('Your category is MIRIM.')
elif age <= 14:
    print(f'You have {age} years old.', end=' ')
    print('Your category is INFANTIL.')
elif age <= 19:
    print(f'You have {age} years old.', end=' ')
    print('Your category is JUNIOR.')
elif age <= 25:
    print(f'You have {age} years old.', end=' ')
    print('Your category is SENIOR.')
else:
    print(f'You have {age} years old.', end=' ')
    print('Your category is MASTER.')

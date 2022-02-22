# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
#
# Develop a program that reads an integer and
# tells if it is or not a prime number.
#
number = int(input('Enter a number: '))
totally = 0
for c in range(1, number + 1):
    if number % c == 0:
        print('\033[031m', end=' ')
        totally += 1
    else:
        print('\033[032m', end=' ')
    print(f'{c}', end=' ')
print(f', \033[034mThe number\033[m \033[032m{number}\033[m ', end='')
print(f'\033[034mhas been divided {totally} time.')
print('END')

# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.
#
# Develop a program that shows the multiplication table of several numbers,
# one at a time, for each value entered by the user. The program will be
# interrupted when the number requested is negative.
#
from time import sleep
print('-' * 30)
print('{:^30}'.format('multiplication table'))
print('-' * 30)
while True:
    num = int(input('Enter a number: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num:2} x {c:2} = {num * c:2}')
        sleep(0.2)
print('-' * 30)
print('End of program')

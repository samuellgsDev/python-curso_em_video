# Crie um programa que leia um número inteiro e
#  mostre na tela se ele é PAR ou ÍMPAR.
#
# make a program that reads an integer and
# shows on the screen if it is even or odd.
#

number = int(input('Enter a number: '))
if number % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
#  primitivo e todas as informações possíveis sobre ele.
# Write a program that reads something on the keyboard and displays its
# primitive type and all possible information about it on the screen.


a = input('Enter something: ')
print(f'The type of {a} is {type(a)}')
print(f'only have space? {a.isspace()}')
print(f'only have numbers? {a.isnumeric()}')
print(f'only have letters? {a.isalpha()}')
print(f'only have alphanumeric? {a.isalnum()}')
print(f'only have capital letters? {a.isupper()}')
print(f'only have small letters? {a.islower()}')
print(f'only have capital letters? {a.istitle()}')

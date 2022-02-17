# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
#
# Make a program that reads the full name of a person,
# and then shows the first and last name separately.
#
name = str(input('Enter your full name: ')).strip()
n = name.split()
print('Nice to meet you !')
print(f'Your first name is {n[0]}')
print(f'Your last name is {n[-1]}')

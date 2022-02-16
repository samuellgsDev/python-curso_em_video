# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem “SILVA” no nome.
#
# Create a program that reads the name of a person
# and tells whether or not it has “SILVA” in the name.
#
name = str(input('Enter your full name: ')).strip()
print(f'Your name has SILVA? {("silva" in name.lower())}')
# or print(f'Your name has SILVA in it? {name.find("silva") != -1}')

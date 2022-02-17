# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
#
# Write a Python program that reads any integer
#  and asks the user to choose which base to convert:
# 1 for binary, 2 for octal and 3 for hexadecimal.
#
number = int(input('Enter a number: '))
print('''[1] Binary
[2] Octal
[3] Hexadecimal''')
option = int(input('Enter the base to convert: '))


if option == 1:
    print(f'{number} in binary is {bin(number)[2:]}')
elif option == 2:
    print(f'{number} in octal is {oct(number)[2:]}')
elif option == 3:
    print(f'{number} in hexadecimal is {hex(number)[2:]}')
else:
    print('Invalid option!')
print('End of program.')

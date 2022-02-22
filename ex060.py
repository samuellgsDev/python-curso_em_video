# Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# develop a program that reads any number and shows its factorial.
#
value = int(input('Enter a value: '))
factorial = 1
for i in range(1, value + 1):
    factorial *= i
print(f'The factorial of {value} is {factorial}')

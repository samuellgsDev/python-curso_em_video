# Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
#
# Write a program that reads two integers and compares them.
# Show on the screen a message:
# – The first value is greater
# – The second value is greater
# – There is no greater value, they are equal
#
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
if number1 > number2:
    print(f'the first number {number1} is greater than', end=' ')
    print(f'the second number {number2}')
elif number2 > number1:
    print(
        f'the second number {number2} is greater than', end=' ')
    print(f'the first number {number1}')
else:
    print(f'The two numbers are equal. {number1} and {number2}')

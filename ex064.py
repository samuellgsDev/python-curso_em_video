# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).
#
# Create a program that reads several integers from the keyboard.
# The program will only stop when the user enters the value 999,
# which is the stop condition.
# At the end, show how many numbers were entered
# and what was the sum between them (disregarding the flag).
#


sum_ = number = count = 0
number = int(input('Enter a number [999 to stop]: '))
while number != 999:
    sum_ += number
    count += 1
    number = int(input('Enter a number [999 to stop]: '))
print(f'you entered {count} and the sum is {sum_ }')

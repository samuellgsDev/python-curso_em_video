# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#
# Write a program that reads an integer N and shows on the screen the first N
# elements of a Fibonacci sequence.
#
# Exemplo: N = 6
# 1 1 2 3 5 8 13
number = int(input('Enter a number: '))
first = 1
second = 1
count = 1
print(f'{first}', end=' -> ')
while count < number:
    print(f'{second}', end=' -> ')
    third = first + second
    first = second
    second = third
    count += 1
print('end')

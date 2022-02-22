# Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
#
# develop a program that reads six integers and shows the sum
# only of those that are even.
# If the value entered is odd, ignore it.
#
sum = 0
for c in range(0, 6):
    n = int(input('Enter a number: '))
    if n % 2 == 0:
        sum += n
print(f'The sum of even numbers is {sum}')

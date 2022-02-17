# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.
#
# Develop a program that reads three numbers
#  and shows which is the biggest and which is the smallest.
#
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))
biigest = n1
if n2 > biigest:
    biigest = n2
if n3 > biigest:
    biigest = n3
smallest = n1
if n2 < smallest:
    smallest = n2
if n3 < smallest:
    smallest = n3
print(f'The biggest number is {biigest}')
print(f'The smallest number is {smallest}')

# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.
#
# develop a program that generates five random numbers
# and puts them in a tuple.Then, show the list of generated numbers
# and also indicate the smallest and largest values that are in the tuple.
#
from random import randint
numbers = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
print(f'the list of generated numbers is: {numbers}')
for n in numbers:
    print(f'{n} ', end='')
print(f'\nThe largest number is {max(numbers)}')
print(f'The smallest number is {min(numbers)}')

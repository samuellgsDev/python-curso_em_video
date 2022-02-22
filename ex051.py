# Desenvolva um programa que leia o primeiro termo e
# a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
#
# Develop a program that reads the first term and
# ratio of an arithmetic progression. At the end,
# show the first 10 terms of this progression.
#

first = int(input('Enter the first term: '))
ratio = int(input('Enter the ratio: '))
for c in range(1, 11):
    print(f'{first}', end=' -> ')
    first += ratio
print('END')

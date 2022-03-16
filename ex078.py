# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.
#
# Develop a program that reads 5 numeric values and stores them in a list.
# At the end, show which was the biggest and smallest value entered and
# their respective positions in the list.
#
listNumbers = []
larg = 0
small = 0

for c in range(0, 5):
    listNumbers.append(int(input(f'Enter a number for position {c}: ')))
    if c == 0:
        larg = listNumbers[c]
        small = listNumbers[c]
    else:
        if listNumbers[c] > larg:
            larg = listNumbers[c]
        if listNumbers[c] < small:
            small = listNumbers[c]
print('-=' * 30)
print('The list is: ', listNumbers)
print(f'The largest value is {larg}', end=' ')
print(f'and its position is {listNumbers.index(larg)}º')
print(f'The smallest value is {small}', end=' ')
print(f'and its position is {listNumbers.index(small)}º')

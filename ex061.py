# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
#
# Redo CHALLENGE 51, reading the first term and ratio of an AP,
#  showing the first 10 terms of the progression using the while structure.
#
first = int(input('Enter the first term: '))
ratio = int(input('Enter the ratio: '))
c = 1
while c <= 10:
    print(f'{first}', end=' -> ')
    first += ratio
    c += 1
print('END')

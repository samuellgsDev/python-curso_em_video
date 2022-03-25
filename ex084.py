# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
#
# Develop a program that reads name and weight of various
# people, storing everything in a list. At the end, show:
# A) How many people were registered.
# B) A list with the people with the heaviest weights.
# C) A list with the people with the lightest weights.
#
list_temp = []
list_ = []
bigger = smaller = 0.0
while True:
    list_temp.append(str(input('Name: ')))
    list_temp.append(float(input('Weight: ')))
    list_.append(list_temp[:])
    list_temp.clear()
    bigger = smaller = 0
    for i in range(len(list_)):
        if list_[i][1] > list_[bigger][1]:
            bigger = i
        if list_[i][1] < list_[smaller][1]:
            smaller = i
    if str(input('Continue? [Y/N] ')).upper() == 'N':
        break
print('-' * 30)
print(f'Total of people: {len(list_)}')
print(f'The heaviest person is {list_[bigger][0]} with {list_[bigger][1]} kg')
print(
    f'The lightest person is {list_[smaller][0]} with {list_[smaller][1]} kg')
print('-' * 30)
for i in range(len(list_)):
    print(f'{list_[i][0]} weighs {list_[i][1]} kg')
print('-' * 30)

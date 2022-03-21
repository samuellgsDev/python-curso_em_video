# crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
#
# Develop a program that reads many numbers and puts them in a list.
# Then, show:
# A) How many numbers were entered.
# B) The list of values, sorted in descending order.
# C) If the value 5 was entered and is or is not in the list.
#
value = []
while True:
    value.append(int(input('Enter a number: ')))
    resp = str(input('Do you want to continue? [Y/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'You entered {len(value)} numbers.')
print(f'The list in descending order is {sorted(value, reverse=True)}')
if 5 in value:
    print('5 is in the list.')
else:
    print('5 is not in the list.')
print('-=' * 30)
print('End of program.')

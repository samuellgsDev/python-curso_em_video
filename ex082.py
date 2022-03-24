# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
#
# Develop a program that reads several numbers and puts them in a list.
# Then, create two extra lists that will contain only the even numbers and
# the odd numbers, respectively.
# At the end, show the content of the three lists generated.
#
num = list()
even = list()
odd = list()
while True:
    num.append(int(input('Enter a number: ')))
    answer = str(input('Do you want to continue? [Y/N] ')).upper()
    if answer == 'N':
        break
for i in range(0, len(num)):
    if num[i] % 2 == 0:
        even.append(num[i])
    else:
        odd.append(num[i])
print(f'The numbers are: {num}')
print(f'The even numbers are: {even}')
print(f'The odd numbers are: {odd}')

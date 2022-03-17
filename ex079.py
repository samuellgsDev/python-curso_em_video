# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente
#
# develop a program that the user can enter multiple numeric values
# ​​and register them in a list.
# If the number already exists there, it will not be added.
# At the end, they will be displayed all the unique values ​​entered,
# in order of ascending
#
number = list()
while True:
    number.append(int(input('Enter a number: ')))
    while True:
        answer = str(input('Do you want to continue? [Y/N] ')).upper()[0]
        if answer in 'YN':
            break
        print('Invalid answer!')
    if answer == 'N':
        break
print('-=' * 30)
print(f'The numbers that you entered are: {sorted(list(set(number)))}')

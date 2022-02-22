# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
#
# Create a program that reads two values ​​and displays a menu on the screen:
# [ 1 ] sum
# [ 2 ] multiply
# [ 3 ] bigger
# [ 4 ] new numbers
# [ 5 ] exit the program
#
value1 = int(input('Enter a value: '))
value2 = int(input('Enter a value: '))
option = 0
while option != 5:
    print('''    [1] sum
    [2] multiply
    [3] bigger
    [4] new numbers
    [5] exit the program''')
    print('-' * 20)
    option = int(input('Enter a option: '))
    print('-' * 20)
    if option == 1:
        print(f'The sum of {value1} and {value2} is {value1 + value2}')
    elif option == 2:
        print(f'The multiply of {value1} and {value2} is {value1 * value2}')
    elif option == 3:
        if value1 > value2:
            print(f'{value1} is bigger than {value2}')
        else:
            print(f'{value2} is bigger than {value1}')
    elif option == 4:
        value1 = int(input('Enter a value: '))
        value2 = int(input('Enter a value: '))
    elif option == 5:
        print('Goodbye!')
    else:
        print('Invalid option!')
    print('-' * 20)
print('End of program!')

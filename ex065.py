# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário  se ele quer ou não continuar a digitar valores.
#
# Create a program that reads several integers from the keyboard.
# At the end of the run, show the average of all values
# ​​and which was the highest and lowest values ​​read. The program
# should ask the user whether or not he wants to continue typing values.
#
count = 0
max = 0
min = 0
sum_ = 0
while True:
    num = int(input('Enter a number: '))
    count += 1
    sum_ += num
    if count == 1:
        max = num
        min = num
    else:
        if num > max:
            max = num
        if num < min:
            min = num
    cont = input('Do you want to continue ? [Y/N] ').upper()
    if cont == 'N':
        break
print(f'The average of all values is {sum_ / count}')
print(f'The highest value is {max}')
print(f'The lowest value is {min}')

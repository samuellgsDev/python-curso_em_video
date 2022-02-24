# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre elas (desconsiderando o flag).
#
# Develop a program that reads integers from the keyboard.
# The program will stop only when the user enters the value 999,
# which is the condition of stopping. At the end, show how many numbers
# were entered and what was the sum of them (ignoring the flag).
#
count = sum_ = 0
while True:
    num = int(input('Enter a number: '))
    if num == 999:
        break
    count += 1
    sum_ += num
print(f'You entered {count} numbers and the sum is {sum_}')

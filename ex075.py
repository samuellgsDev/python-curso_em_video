# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
#
# Develop a program that reads four values ​​by the keyboard
# and stores them in a tuple. At the end, show:
# A) How many times appeared the value 9.
# B) In which position was the first value 3.
# C) Which were the even numbers.
#
number = (int(input('Type a number: ')),
          int(input('Type another number: ')),
          int(input('Type another number: ')),
          int(input('Type another number: ')))
print(f'You typed the numbers: {number}')
print(f'The number 9 appeared {number.count(9)} times')
if 3 in number:
    print(f'The first number 3 was typed in position {number.index(3) + 1}º')
else:
    print('The number 3 was not typed')
print('The even numbers were: ', end='')
for n in number:
    if n % 2 == 0:
        print(n, end=' ')
print()

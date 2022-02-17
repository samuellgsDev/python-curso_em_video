# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo
#
# develop a program that reads the length of three lines
# and tells the user if they can or cannot form a triangle.
#
leg1 = float(input('Enter the length of the first line: '))
leg2 = float(input('Enter the length of the second line: '))
leg3 = float(input('Enter the length of the third line: '))
if leg1 < leg2 + leg3 and leg2 < leg1 + leg3 and leg3 < leg1 + leg2:
    print('You can form a triangle')
else:
    print('You can not form a triangle')

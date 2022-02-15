# Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa.
#
# Write a program that reads the length of the opposite
# and adjacent sides of a right triangle.
#  Calculate and display the length of the hypotenuse.
#
import math
co = float(input('enter the length of the opposite side: '))
ca = float(input('enter the length of the adjacent side: '))
h = math.hypot(co, ca)
print(f'the length of the hypotenuse is: {h:.2f}')

# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#
# Write a program that reads any angle and
# displays the sine, cosine and tangent of that angle on the screen.
#
import math
ang = float(input('enter an angle: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'sin({ang}): {sen:.2f}')
print(f'cos({ang}): {cos:.2f}')
print(f'tan({ang}): {tan:.2f}')

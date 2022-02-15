#  Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
# Write a program that converts a temperature by typing in degrees Celsius
# and converts it to degrees Fahrenheit.

c = float(input('write the temperature in degrees Celsius: '))
f = (c * 1.8) + 32
print('the temperature in degrees Fahrenheit is: {:.2f}'.format(f))

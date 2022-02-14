# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros.
# Write a program that reads a value in meters and displays
#  it converted in centimeters and millimeters.

value = float(input("Enter a value in meters: "))
centimeters = value * 100
millimeters = value * 1000
print(f'{value} meters is {centimeters} centimeters and {millimeters}', end='')
print(" millimeters")

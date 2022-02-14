# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
#  sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
# Write a program that reads the width and height of a wall in meters,
# calculates its area and the amount of paint needed to paint it,
# knowing that each liter of paint paints an area of ​​2 square meters.

width = float(input("Enter the width of the wall: "))
height = float(input("Enter the height of the wall: "))
area = width * height
paint = area / 2
print(f'your wall has a dimension of {width}m x {height}m')
print(f"The area of the wall is {area:.2f}m²", end="")
print(f" and you need {paint:.2f} liters of paint")

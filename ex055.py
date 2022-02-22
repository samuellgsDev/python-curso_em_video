# Faça um programa que leia o peso de cinco pessoas.
#  No final, mostre qual foi o maior e o menor peso lidos.
#
# Create a program that reads the weight of five people.
#  At the end, show which was the biggest and the smallest weight read.
#
for c in range(1, 6):
    weight = float(input(f'Enter the weight of the {c}º person: '))
    if c == 1:
        larger = weight
        smaller = weight
    else:
        if weight > larger:
            larger = weight
        if weight < smaller:
            smaller = weight
print(f'The biggest weight is {larger} kg.')
print(f'The smallest weight is {smaller} kg.')

# Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados.
#
# Write a program that reads a number from 0 to 9999 and
# displays each of the separate digits on the screen.
#

n = int(input('Enter a number between 0 and 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'unit: {u}')
print(f'set of ten: {d}')
print(f'hundred: {c}')
print(f'chiliad: {m}')

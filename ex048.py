# Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
#
# Write a program that calculates the sum of all the multiples of three
# that are between 1 and 500.
#

sum = 0
count = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        sum += i
        count += 1
print(f'the sum of all {count} the requested values is ', end='')
print(f'{sum}.')

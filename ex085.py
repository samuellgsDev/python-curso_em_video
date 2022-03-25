# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
#
# Develop a program that the user can enter seven numeric values
# and register them in a single list that maintains
# separated the even and odd numbers.
# At the end, show the even and odd numbers in ascending order.
#
list_princ = list()
list_even = list()
list_odd = list()
for c in range(1, 8):
    list_princ.append(int(input(f'Enter the {c}º number: ')))
for c in list_princ:
    if c % 2 == 0:
        list_even.append(c)
    else:
        list_odd.append(c)
list_even.sort()
list_odd.sort()
print(f'The even numbers are: {list_even}')
print(f'The odd numbers are: {list_odd}')
# End of exercice

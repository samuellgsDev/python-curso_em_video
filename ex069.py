# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
#
# Create a program that reads the age and gender of multiple people.
# For each person registered, the program should ask
# if the user wants to continue or not. At the end, show:
# A) how many people are over 18 years old.
# B) how many men were registered.
# C) how many women are under 20 years old.
#
tot18 = totM = totW20 = 0
while True:
    age = int(input("enter your age: "))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Enter your gender: [M/F] ')).strip().upper()[0]
    if age >= 18:
        tot18 += 1
    if gender == 'M':
        totM += 1
    if gender == 'F' and age < 20:
        totW20 += 1
    answer = ' '
    while answer not in 'YN':
        answer = str(
            input('do you want to continue? [Y/N] ')).strip().upper()[0]
    if answer == 'N':
        break
print(f'Total of people over 18 years old: {tot18}')
print(f'in total we have {totM} registered men')
print(f'and we have {totW20} women under 20')

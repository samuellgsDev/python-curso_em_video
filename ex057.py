# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
#
# Develop a program that reads a person's gender,
# but only accepts 'M' or 'F' values.
# If it is wrong, ask for the typing again until you have a correct value.
#
gender = str(input('What is your gender ? [M/F] ')).strip().upper()[0]
while gender not in 'MmFf':
    print('Invalid data.', end=' ')
    gender = str(input('please inform your gender: [M/F] ')).strip().upper()[0]
print(gender)

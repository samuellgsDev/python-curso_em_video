# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
#
# Develop a program that reads the name, age and gender of 4 people.
# At the end of the program, show: the average age of the group,
# what is the name of the oldest man and how many women are under 20.
#
sum_age = 0.0
average = 0
older_man = 0
older_name = ''
total_women_20 = 0
for c in range(1, 5):
    print(f'-----------{c}º person -------------')
    name = str(input(f'what is the name of the {c}st person? ')).strip()
    age = int(input(f'how old is the {c}st person? '))
    gender = str(
        input(f'what is the gender of the {c}st person? [M/F] ')).strip()
    sum_age += age
    print('-'*30)
    if c == 1 and gender in 'Mm':
        older_man = age
        older_name = name
    if gender in 'Mm' and age > older_man:
        older_man = age
        older_name = name
    if gender in 'Ff' and age < 20:
        total_women_20 += 1
average = (sum_age / 4)
print(f'the average age of the group is {average} years')
print(f'the oldest man is {age} years old and his name is {name}')
print(f'in total there are {total_women_20} women under the age of 20')

# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente
#
# Develop a program that reads the name and two grades of several students
# and stores everything in a list.
# At the end, show a bulletin containing the average of each student
# and allow the user to show the grades of each student individually
#
List_ = list()
while True:
    name = (str(input('Name: ')))
    grade1 = (float(input('Grade 1: ')))
    grade2 = (float(input('Grade 2: ')))
    average = (grade1 + grade2) / 2
    List_.append([name, [grade1, grade2], average])
    option = (str(input('Querey another student? [Y/N] ')))
    if option in 'Nn':
        break
print('-' * 30)
print(f'{"Nº":<4}{"Name":<10}{"Average":<8}')
print('-' * 30)
for i, a in enumerate(List_):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    option = str(input('Show the grades of wich student?  (999 to stop) '))
    print('-' * 30)
    if int(option) in range(len(List_)):
        print(f'The grades of {List_[int(option)][0]}', end='')
        print(f'are: {List_[int(option)][1]}')
    if option == '999':
        print('finished')
        break
    print('-' * 30)
print('Welcome back!')

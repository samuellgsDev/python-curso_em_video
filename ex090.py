# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
#
# Develop a program that reads the name and average of a student,
# storing also the situation in a dictionary.
# At the end, show the content of the structure on the screen.
#
student = dict()
student['name'] = str(input('Name: '))
student['average'] = float(input(f'Average of {student["name"]}: '))
if student['average'] >= 7:
    student['situation'] = 'Passed'
elif student['average'] >= 5 and student['average'] < 7:
    student['situation'] = 'retake test'
else:
    student['situation'] = 'Failed'
for k, v in student.items():
    print(f'{k} = {v}')

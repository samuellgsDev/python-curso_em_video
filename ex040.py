# Crie um programa que leia duas notas de um aluno e calcule sua média,
#  mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
#
# Create a program that reads two grades from a student
# and calculates their average,showing a message at the end,
# according to the average achieved:
# – Average below 5.0: FAIL
# – Average between 5.0 and 6.9: RECOVERY
# – Average 7.0 or higher: APPROVED
#
grade1 = float(input('Enter the first grade: '))
grade2 = float(input('Enter the second grade: '))
average = (grade1 + grade2) / 2
if average < 5:
    print('FAIL')
    print(f'Your average is {average}.')
    print(f'you would need {5 - average} to pass.')
elif average >= 5 and average <= 6.9:
    print('RECOVERY')
    print(f'Your average is {average:.1f}')
    print('you need to do a recuperation and', end=' ')
    print(f'you need {7 - average:.1f} to pass.')
else:
    print('APPROVED')
    print(f'Your average is {average:.1f}')
    print('Congratulations! You passed!')

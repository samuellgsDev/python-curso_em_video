# O mesmo professor do desafio 19 quer sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.
#
# The same teacher from challenge 19 wants to draw
#  the order of presentation of students' work.
#  Make a program that reads the names of the four students
#  and shows the order drawn.
#
import random
import time
student = str(input('enter the name of the student: '))
student2 = str(input('enter the name of the second student: '))
student3 = str(input('enter the name of the third student: '))
student4 = str(input('enter the name of the fourth student: '))
sorted = random.sample([student, student2, student3, student4], 4)
print('raffling the names..')
time.sleep(2)
print(f'The order is: {sorted}')

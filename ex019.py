# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos
# e escrevendo na tela o nome do escolhido.
#
# A teacher wants to draw one of his four students to erase the board
#  Make a program that helps him, reading the name of the students
# and writing the name of the chosen one on the screen.
#
import random
import time
student = str(input('enter the name of the student: '))
student2 = str(input('enter the name of the second student: '))
student3 = str(input('enter the name of the third student: '))
student4 = str(input('enter the name of the fourth student: '))
sorted = random.choice([student, student2, student3, student4])
print('raffling the names..')
time.sleep(2)
print(f'{sorted} was drawn!')

#  Escreva um programa que faça o computador “pensar” em um número inteiro
#  entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
#
# Write a program that makes the computer “think” of an integer
#  between 0 and 5 and ask the user to try to find
# which number the computer chose.
#  The program should write to the screen if the user won or lost.
#
from random import randint

print('I will think of a number between 0 and 5. Try to guess', end=' ')
print(' what the number is.')
pc = randint(0, 5)
number = int(input('Your guess: '))
if number == pc:
    print('You won!')
else:
    print('You lost!')
    print(f'The number was {pc}')

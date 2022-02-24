# Faça um programa que jogue par ou ímpar com o computador
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
#
# Develop a program that plays even or odd with the computer
# The game will only be interrupted when the player loses,
# showing the total number of consecutive victories
# he has achieved at the end of the game.
#
from random import randint
from time import sleep
pc = 0
user = 0
print('-' * 30)
print('{:^30}'.format('Even or Odd'))
print('-' * 30)
while True:
    num = int(input('Enter a number between 0 and 10: '))
    pc = randint(0, 10)
    tot = pc + num
    choice = ' '
    while choice not in 'EeOo':
        choice = str(input('Even or Odd? [E/O] ')).strip().upper()[0]
    print(f'You chose {num} and the computer chose {pc}. total = {tot}')
    sleep(1)
    if choice == 'E' and tot % 2 == 0:
        print('You won!')
        user += 1
    elif choice == 'O' and tot % 2 == 1:
        print('You won!')
        user += 1
    else:
        print('You lost!')
        break
print(f'You won {user} times.')
print('-' * 30)
print('End of program')

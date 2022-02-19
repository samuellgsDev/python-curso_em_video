# Crie um programa que faça o computador jogar Jokenpô com você.
#
# Develop a program that makes the computer play Jokenpô with you.
#
from random import randint
from time import sleep
print('-=-' * 20)
print('Let\'s play Jokenpô!')
print('-=-' * 20)
print('''[0] stone
[2] paper
[3] scissors''')
print('-=-' * 20)
player = int(input('Choose your option: '))
jokenpo = ['stone', 'paper', 'scissors']
pc = randint(0, 2)
print('-=-' * 20)
print(f'You chose: {jokenpo[player]}')
print('x-' * 20)
sleep(1)
print(f'Computer chose: {jokenpo[pc]}')
print('-=-' * 20)
if pc == player:
    print('Tie!')
elif pc == 0 and player == 2:
    print('You win!')
elif pc == 1 and player == 0:
    print('You win!')
elif pc == 2 and player == 1:
    print('You win!')
else:
    print('You lose!')
print('-=-' * 20)
print('Thanks for playing!')

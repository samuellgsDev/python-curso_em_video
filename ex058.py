# Melhore o jogo do exercicio 28 onde o computador
# vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.
#
# Improve the game of CHALLENGE 28 where
# the computer will “think” of a number between 0 and 10.
# Only now the player will try to guess until he gets it right,
# showing at the end how many guesses were needed to win.
#
from random import randint
import time

hint = 0

pc = randint(0, 10)
print('I ll think of a number between 0 and 10.', end=' ')
print('Try to guess which number I thought of')
print('thinking...')
time.sleep(2)
print('What was the number I thought? ')
try_ = False
while not try_:
    player = int(input('Enter a number between 0 and 10: '))
    hint += 1
    if player == pc:
        print(f'You won with {hint} tries!')
        try_ = True
    else:
        if player > pc:
            print(f'The number is lower than {player}')
        else:
            print(f'The number is higher than {player}')
print('Congratulations!')

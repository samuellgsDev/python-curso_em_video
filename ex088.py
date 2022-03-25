# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
#
# The program will help a player of the MEGA SENA to create palpites.
# The program will ask how many games will be generated
# and will sort 6 numbers between 1 and 60 for each game,
# registering everything in a list.
#
from random import randint
List = list()
print('-' * 30)
print('{:^30}'.format('MEGA SENA'))
print('-' * 30)
n = int(input('How many games do you want to play? '))
for i in range(n):
    List.append([randint(1, 60) for c in range(6)])
print('-' * 30)
print('{:^30}'.format('Your games:'))
print('-' * 30)
for i in range(n):
    print(f'Game {i+1}: {List[i]}')
print('-' * 30)
print('{:^30}'.format('End of the program'))
print('-' * 30)

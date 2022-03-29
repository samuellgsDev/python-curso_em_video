# Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
#
# Develop a program that plays 4 players and has random results.
# Save these results in a dictionary in Python.
# At the end, put this dictionary in order,
# knowing that the winner took the biggest number on the dice.
#
from random import randint
from time import sleep
from operator import itemgetter
game = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)}
print(' Drawn numbers: ')
ranking = list()
for k, v in game.items():
    print(f'{k} sorted {v}')
    sleep(0.5)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('-' * 30)
print(' Ranking: ')
for i, v in enumerate(ranking):
    print(f'{i+1}º place: {v[0]} with {v[1]}')
    sleep(0.5)

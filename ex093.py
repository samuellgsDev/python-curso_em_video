# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.
#
# Develop a program that manages the performance of a football player.
# The program will read the player's name and the number of games he played.
# Then, it will read the number of goals scored in each game.
# At the end, all this will be saved in a dictionary,
# including the total number of goals scored during the championship.
#
football_player = dict()
match = list()
football_player['nome'] = str(input('Nome do Jogador: '))
n_games = int(input(f'Quantas partidas {football_player["nome"]} jogou? '))
for c in range(0, n_games):
    match.append(int(input(f'  Quantos gols na partida {c + 1}? ')))
football_player['gols'] = match[:]
football_player['total'] = sum(match)
print('-=' * 30)
for k, v in football_player.items():
    print(f'  - {k}: {v}')
print('-=' * 30)
print(f'O jogador {football_player["nome"]} jogou ', end=' ')
print(f'{len(football_player["gols"])} partidas', end=' ')
for i, v in enumerate(football_player['gols']):
    print(f'\n  => Na partida {i + 1}, fez {v} gols.', end=' ')
print(f'\n  => Total de gols: {football_player["total"]}')

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(p=',desconhecido', g=0):  # p = player; g = gols
    print(f'O jogador {p} fez {g} gol[s] no campeonato')


player = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if player.strip() == '':
    ficha(gols=g)
else:
    ficha(player, gols)

# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
#
# Develop a tuple filled with the first 20 positions
# of the Brazilian Football Championship, in order of
# ranking. Then, show:
# a) The 5 first teams.
# b) The last 4 teams.
# c) Teams in alphabetical order.
# d) Where is the Chapecoense team.
#
teams = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense',
         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense',
         'Avaí')
print('-=' * 30)
print(f'teams of the Brazilian Football Championship: {teams}')
print('-=' * 30)
print(f'The 5 first teams: {teams[:5]}')
print('-=' * 30)
print(f'The last 4 teams: {teams[-4:]}')
print('-=' * 30)
print(f'Teams in alphabetical order: {sorted(teams)}')
print('-=' * 30)
print(f'Where is the Chapecoense team: {teams.index("Chapecoense") + 1}º')

# Melhore o DESAFIO 61, perguntando para o usuário se ele quer
# mostrar mais alguns termos.O programa encerrará
# quando ele disser que quer mostrar 0 termos.
#
# Improve CHALLENGE 61 by asking the user if they
# want to show some more terms. The program will terminate
# when it says it wants to display 0 terms.
#
first = int(input('Enter the first term: '))
ratio = int(input('Enter the ratio: '))
term = first
count = 1
tot = 0
more = 10
while count != 0:
    tot += more
    while count <= tot:
        print('{}'.format(term), end=' -> ')
        term += ratio
        count += 1
    print('STOP')
    more = int(input('How many terms do you want to see? '))
    if more == 0:
        break
print(f'progression finished with {tot} terms')

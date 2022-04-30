# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep
c = ('\033[n',  # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[0;30;46m',  # 6 - ciano
     '\033[0;30;47m',  # 7 - branco
     )


def ajuda(com):
    titulo('Acessando o manual do comando ' + com, 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    size = len(msg) + 4
    print(c[cor], end='')
    print('-'*size)
    print(msg)
    print('-'*size)
    print(c[0], end='')
    sleep(1)


command = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    command = str(input("Função ou biblioteca: "))
    if command.upper() == 'FIM':
        break
    else:
        ajuda(command)
print('Até logo!' + '\n' + 3)

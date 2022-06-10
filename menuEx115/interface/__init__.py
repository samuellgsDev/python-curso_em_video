# módulo de interface ex115
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor,', end='')
            print('digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=50):
    print('-' * tam)


def titulo(msg):
    print("-" * 50)
    print(f'{msg:^50}')
    print("-" * 50)


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1  # contador
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    opc = leiaInt('Escolha uma opção: ')
    return opc

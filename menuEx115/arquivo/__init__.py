# módulo de arquivo para ex115

from menuEx115.interface import titulo


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo!')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    else:
        titulo('LISTA DE USUÁRIOS')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Arquivo não encontrado!')
    else:
        try:
            a.write(f'{nome} - {idade}\n')
        except:
            print('Erro ao cadastrar!')
        else:
            print(f'Novo usuário {nome} cadastrado com sucesso!')
            a.close()

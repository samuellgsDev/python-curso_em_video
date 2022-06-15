# Vamos criar um menu em Python, usando modularização.
from menuEx115.interface import *
from menuEx115.arquivo import *
from time import sleep

arq = 'usuarios.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['Cadastro de usuários', 'Cadastrar usuário', 'Sair'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        titulo('NOVO USUÁRIO')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print('Saindo do sistema...')
        break
    else:
        print("Opção inválida")
        print('\033[31mERRO: por favor, digite uma opção válida.\033[m')
    sleep(2)

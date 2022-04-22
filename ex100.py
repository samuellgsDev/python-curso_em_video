# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
def sorteia():
    from random import randint
    lista = []
    for i in range(0, 5):
        lista.append(randint(1, 10))
    return lista


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    return soma


lista = sorteia()
print(f'Lista: {lista}')
print(f'Soma dos pares: {somaPar(lista)}')

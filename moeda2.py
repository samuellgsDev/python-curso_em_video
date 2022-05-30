# módulo do exercicio 108


def aumentar(n):
    return n + (n * 10 / 100)


def diminuir(n):
    return n - (n * 10 / 100)


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

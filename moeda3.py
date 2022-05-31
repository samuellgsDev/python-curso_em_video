# módulo do exercicio 109

def aumentar(n, p, formatado=False):
    res = n + (n * p / 100)
    return res if formatado is False else moeda(res)


def diminuir(n, p, formatado=False):
    res = n - (n * p / 100)
    return res if formatado is False else moeda(res)


def dobro(n, formatado=False):
    res = n * 2
    return res if formatado is False else moeda(res)


def metade(n, formatado=False):
    res = n / 2
    return res if formatado is False else moeda(res)


def moeda(n=0, moeda='R$',):
    res = f'{moeda}{n:.2f}'.replace('.', ',')
    return res

# módulo do exercicio 111 e 112

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


def resumo(n, a, d):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t{diminuir(n, d, True)}')
    print('-' * 30)

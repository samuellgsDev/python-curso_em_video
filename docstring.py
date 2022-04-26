def contador(i, f, p):
    # aprendendo a criar Docstring
    """"" 
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """

    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 100, 2)
help(contador)

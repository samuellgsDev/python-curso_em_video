# modulo para o exercicio 112

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[31mERRO! Digite um número válido.\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    """substituir o input e retornar apenas numero inteiro

    Args:
        msg (int): digite um número inteiro

    Returns:
        int: número inteiro digitado
    """
    ok = False
    value = 0
    while True:
        number = str(input(msg))
        if number.isnumeric():
            value = int(number)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return value

# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
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


number = leiaInt('Digite um número inteiro: ')
print(f'você acabou de digitar o número {number}')

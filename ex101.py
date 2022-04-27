# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    global nasc
    nasc = date.today().year - ano
    print(f'você tem {nasc} anos')
    if nasc > 18:
        print('Você é obrigado a VOTAR')
    elif 18 > nasc >= 16:
        print('Seu voto é OPCIONAL')
    elif nasc < 16:
        print('Seu voto foi NEGADO')


nasc = int(input('Em que ano você nasceu? '))
voto(nasc)

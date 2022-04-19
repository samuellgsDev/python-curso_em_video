# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    print(f'Analisando os valores passados...')
    for i in num:
        print(f'{i} ', end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')


maior(2, 9, 4, 5, 7, 1, 35, 56, 32, 54, 67)

# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:considere que o caixa eletronico possui cédulas de R$50, R$20, R$10 e R$1
#
# Develop a program that simulates the operation of an ATM.
# At the beginning, ask the user what will be
# the amount to be withdrawn (integer)
# and the program will inform how many bills of each amount will be delivered.
# NOTE: consider that the cashier has bills of R$50, R$20, R$10 and R$1.
#
print('=' * 40)
print('{:^40}'.format('BANK'))
print('=' * 40)
value = int(input('What is the value to be withdrawn? '))
total = value
bankNote = 50
tot_bank_note = 0
while True:
    if total >= bankNote:
        total -= bankNote
        tot_bank_note += 1
    else:
        if tot_bank_note > 0:
            print(f'total of {tot_bank_note} bank notes of R${bankNote}')
        if bankNote == 50:
            bankNote = 20
        elif bankNote == 20:
            bankNote = 10
        elif bankNote == 10:
            bankNote = 1
        tot_bank_note = 0
        if total == 0:
            break
print('-'*30)
print('{:^30}'.format('THANK YOU'))

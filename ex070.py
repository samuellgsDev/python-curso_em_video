# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
#
# Develop a program that reads the name and price of multiple products.
# The program should ask if the user will continue or not.
# At the end, show:
# A) what is the total spent on the purchase.
# B) how many products cost more than R$1000.
# C) what is the name of the cheapest product.
#
print('-' * 30)
print(('{:^30}').format('SUPERSTORE'))
print('-' * 30)
total = totThousand = count = 0.0
namelowest = ''
while True:
    product = str(input('Which product do you want to register? '))
    price = float(input('What is the price of the product ? R$ '))
    count += 1
    total += price
    if price <= 1000:
        totThousand += 1
    if count == 1:
        lowest = price
        namelowest = product
    else:
        if price < lowest:
            lowest = price
            namelowest = product
    answer = ' '
    while answer not in 'YN':
        answer = str(
            input('Do you want to continue? [Y/N] ')).upper().strip()[0]
    if answer == 'N':
        break
print(f'The total spent is R$ {total:.2f}')
print(
    f'The total of products that cost more than R$ 1000 is {totThousand:.0f}')
print(f'The name of the cheapest product is {namelowest} and ', end='')
print(f'the price is R$ {lowest:.2f}')

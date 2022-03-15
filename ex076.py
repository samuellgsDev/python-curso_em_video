# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.
#
# Develop a program that has a unique tuple with product names and
# their respective prices, in sequence.
# At the end, show a list of prices, organizing the data in a table.
#
list = ('Pencil', 1.75,
        'Erase', 2.00,
        'Notebook', 15.90,
        'Pencil case', 25.00,
        'Backpack', 120.32,
        'Pen', 3.75,
        'book', 34.90)

print('-' * 40)
print(f'{"Price listing":^40}')
print('-' * 40)
for i in range(0, len(list)):
    if i % 2 == 0:
        print(f'{list[i]:.<30}', end='')
    else:
        print(f'R$ {list[i]:>7.2f}')
print('-' * 40)
#

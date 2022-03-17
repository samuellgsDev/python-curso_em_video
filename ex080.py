# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
#
# develop a program that the user can type five numeric values
# and register them in a list,
# without using the sort() function.
# At the end, show the list ordered in the screen.
#
lista = []
for c in range(0, 5):
    n = int(input('Enter a number: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('added to end of list...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'added to position {pos} of list...')
                break
            pos += 1
print('-=' * 30)
print(f'The list is: {lista}')

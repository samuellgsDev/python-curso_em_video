# Refaça o exercicio 9, mostrando a tabuada de um número que o usuário escolher
# só que agora utilizando um laço for.
#
# Redo exercise 9, showing the multiplication table of a number
# that the user chooses, only now using a for loop.
#
number = int(input("Enter a number: "))
for c in range(1, 11):
    print(f'{number} x {c} = {number*c}')

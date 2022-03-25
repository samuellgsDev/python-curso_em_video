# Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
#
# Develop a program that declares a matrix of 3×3
# and fills it with values read by the keyboard.
# At the end, show the matrix on the screen, with the correct format.
#
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for L in range(0, 3):
    for c in range(0, 3):
        matrix[L][c] = int(input(f'Enter the value for [{L}, {c}]: '))
for L in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[L][c]}]', end=' ')
    print()
# End of exercice

# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
#
# Improve the previous exercise, showing at the end:
# A) The sum of all even numbers entered.
# B) The sum of the third column.
# C) The biggest value of the second row.
#
Matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_even = 0
sum_third_col = 0
biggest_second_row = 0
for L in range(0, 3):
    for c in range(0, 3):
        Matrix[L][c] = int(input(f'Enter the value for [{L}, {c}]: '))
for L in range(0, 3):
    for c in range(0, 3):
        print(f'[{Matrix[L][c]}]', end=' ')
    print()
for L in range(0, 3):
    for c in range(0, 3):
        if Matrix[L][c] % 2 == 0:
            sum_even += Matrix[L][c]
        if c == 2:
            sum_third_col += Matrix[L][c]
        if L == 1:
            if Matrix[L][c] > biggest_second_row:
                biggest_second_row = Matrix[L][c]
print(f'The sum of all even numbers entered is: {sum_even}')
print(f'The sum of the third column is: {sum_third_col}')
print(f'The biggest value of the second row is: {biggest_second_row}')

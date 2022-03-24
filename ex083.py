# Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.
#
# Develop a program where the user enters any expression
# that uses parentheses. Your application should
# analyze if the expression passed is correctly
# opened and closed in the correct order.
#
expression = str(input('Enter an expression: '))
open_parentheses = 0
close_parentheses = 0
for i in range(0, len(expression)):
    if expression[i] == '(':
        open_parentheses += 1
    elif expression[i] == ')':
        close_parentheses += 1
if open_parentheses == close_parentheses:
    print('The expression is correct.')
else:
    print('The expression is incorrect.')

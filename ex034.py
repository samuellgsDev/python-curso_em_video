# Escreva um programa que pergunte o salário de um funcionário
#  e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
#  calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
#
# Develop a program that asks for the salary of a employee
# and calculates the value of his/her increase.
#  For salaries greater than R$1250,00,
#  calculate a increase of 10%. For the others, the increase is of 15%.
#
salary = float(input('Enter your salary: R$ '))
if salary > 1250:
    new_salary = salary + (salary * 0.10)
    print(f'Your new salary is R${new_salary:.2f}')
else:
    new_salary = salary + (salary * 0.15)
    print(f'Your new salary is R${new_salary:.2f}')

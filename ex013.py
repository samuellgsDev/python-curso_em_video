# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.
# Create a program that reads the salary of a employee
# and shows his new salary, with 15% increase.

salary = float(input("Enter the salary of the employee: "))
new_salary = salary + (salary * 0.15)
print(f"The new salary of the employee is R${new_salary:.2f}")

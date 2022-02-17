# Escreva um programa para aprovar o empréstimo bancário para a compra de uma
# casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o empréstimo será negado.
#
# Write a program to approve the bank loan for the purchase of a house.
# Ask the value of the home, the buyer's salary and how many years he will pay.
# The monthly installment cannot exceed 30% of salary or else
# the loan will be denied.
#
price = float(input('Enter the value of the house: R$ '))
salary = float(input('Enter your salary: R$ '))
years = int(input('Enter the number of years you will pay: '))
monthly_payment = price / (years * 12)
if monthly_payment <= salary * 0.3:
    print('Your loan is approved!')
else:
    print('Your loan is denied!')

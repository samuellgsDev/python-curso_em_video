# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
# # Create a program that reads how much money a person has in his wallet
# and shows how many dollars he can buy.

money = float(input("Enter how much money you have: R$ "))
dollars = float(input("Enter the dollar's value: $ "))
buy = money / dollars
print(f"You can buy ${buy:.2f} dollars")

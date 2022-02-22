# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.
# Write a program that reads the price of a product and shows its new price,
# with 5% discount.

price = float(input("Enter the price of the product: R$ "))
new_price = price - (price * 0.05)
print(f"The new 5% discounted product price is R${new_price:.2f}")

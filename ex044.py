# Elabore um programa que calcule o valor a ser pago por um produto,
#  considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
#
# Create a program that calculates the amount to be paid for a product,
# considering its normal price and payment terms:
# – cash/check: 10% discount
# – cash on card: 5% discount
# – up to 2x on the card: formal price
# – 3x or more on the card: 20% interest
#
product_price = float(input('Enter the product price: R$ '))
cash_payment = product_price - (product_price * 0.10)
cash_on_card = product_price - (product_price * 0.05)
two_payments = product_price
three_payments = product_price + (product_price * 0.20)
print('''[1] - Pay in cash
[2] - Pay in card
[3] - Pay in two payments
[4] - Pay in three payments''')
payment_option = int(input('Enter your option: '))
if payment_option == 1:
    print(f'The price to be paid is {cash_payment:.2f}')
elif payment_option == 2:
    print(f'The price to be paid is {cash_on_card:.2f}')
elif payment_option == 3:
    print(f'The price to be paid is {two_payments:.2f}')
elif payment_option == 4:
    print(f'The price to be paid is {three_payments:.2f}')
else:
    print('Invalid option')

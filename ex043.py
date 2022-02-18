# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#  calcule seu Índice de Massa Corporal (IMC)
#  e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
#
# Develop a logic that reads a person's weight and height,
# calculates their Body Mass Index (BMI) and shows their status,
# according to the table below:
# – BMI below 18.5: Underweight
# – Between 18.5 and 25: Ideal Weight
# – 25 to 30: Overweight
# – 30 to 40: Obesity
# – Above 40: Morbid Obesity
#
weight = float(input('Enter your weight: Kg '))
height = float(input('Enter your height: m '))
imc = weight / (height ** 2)
print(f'Your IMC is {imc:.2f}')
if imc < 18.5:
    print('Underweight')
elif imc >= 18.5 and imc <= 25:
    print('Ideal Weight')
elif imc > 25 and imc <= 30:
    print('Overweight')
elif imc > 30 and imc <= 40:
    print('Obesity')
else:
    print('Morbid Obesity')

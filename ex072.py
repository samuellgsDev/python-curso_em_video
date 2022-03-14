# Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.
#
# Develop a program that has a fully populated pair
# with an extended count from zero to twenty.
# Your program should read a number from the keyboard (between 0 and 20)
# and display it in full.
#
cont = ('zero', 'one', 'two', 'three', 'four ', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
        'nineteen', 'twenty')
while True:
    number = int(input('Enter a number between 0 and 20: '))
    if number >= 0 and number <= 20:
        print(cont[number])
        break
    else:
        print('Invalid number!')
        continue
print('End of program.')

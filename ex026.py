# Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.
#
# Create a program that reads a phrase by the keyboard
# and shows how many times the letter “A” appears,
# where it appears first and where it appears last.
#
phrase = str(input('Enter a phrase: ')).strip()
print(f'The phrase has {phrase.count("a")} "a" letters.')
print(f'The phrase has the first "a" letter in position {phrase.find("a")}.')
print(f'The phrase has the last "a" letter in position {phrase.rfind("a")}.')

# Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.
#
# Create a program that reads any sentence
# and says if it is a palindrome, disregarding the spaces.
#
phrase = str(input('Enter a phrase: ')).strip().upper()
world = phrase.split()
join_ = ''.join(world)
invert = ''
for letter in range(len(join_) - 1, -1, -1):
    invert += join_[letter]
if invert == join_:
    print('Yes, it is a palindrome.')
else:
    print('No, it is not a palindrome.')

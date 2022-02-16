# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.
#
# Create a program that reads a person's full name and displays:
# – The name in all uppercase and lowercase letters.
# – How many letters in total (excluding spaces).
# – How many letters are in the first name
#

name = str(input('Whats your full name? ')).strip()
print(f'your name in uppercase: {name.upper()}')
print(f'your name in lowercase: {name.lower()}')
print(f'your name has {len(name) - name.count(" ")} letters')
print(f'your first name has {len(name.split()[0])} letters')

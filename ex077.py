# Crie um programa que tenha uma tupla com várias palavras
# Depois disso, você deve mostrar, para cada palavra,quais são as suas vogais.
#
# Develop a program that has a tuple with many words
# then, for each word, show which are its vowels.
#
words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador',
         'futuro')
for p in words:
    print(f'\nIn the word {p.upper()} we have ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\nEND!')

# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
#
# Develop a program that reads name, gender and age of several people
# storing each person's data in a dictionary
# and all dictionaries in a list.
# At the end, show:
# A) How many people were registered
#  The average age
# C) A list of women
# D) A list of people older than average
#
people_ = list()
people = dict()
average = sum_ = 0
while True:
    people.clear()
    people['name'] = str(input('Nome: '))
    while True:
        people['gender'] = str(input('Sexo: [M/F] ')).upper()[0]
        if people['gender'] in 'MF':
            break
        print('Errro, Digite apenas M ou F ')
    people['age'] = int(input('Idade: '))
    sum_ += people['age']
    people_.append(people.copy())
    while True:
        answer = str(input('Quer continuar? [S/N] ')).upper()[0]
        if answer in 'SN':
            break
        print('Errro, Digite apenas S ou N ')
    if answer == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(people_)} pessoas cadastradas.')
print(f'B) A média de idade é de {sum_ / len(people_):.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in people_:
    if p['gender'] in 'Ff':
        print(f'{p["name"]}', end=' ')
print()
print('D) Lista de pessoas que estão acima da média')
for p in people_:
    if p['age'] >= average:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<< ENCERRADO >>')

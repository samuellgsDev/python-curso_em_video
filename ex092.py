# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.
#
# Develop a program that reads name, birth year, and work permit card
# and registers (with age) in a dictionary.
# If for some reason the CTPS is different from ZERO,
# the dictionary will also receive the year of hire and the salary.
# Calculate and add, besides the age,
# how many years the person will be retired.
#
from datetime import date
from typing import Any
dados: dict[str, Any] = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentar'] = dados['idade'] + \
        ((dados['contratacao'] + 35) - date.today().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k}: {v}')
print('FIM')

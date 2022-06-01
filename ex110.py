# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
import moeda4

preco = float(input('Digite o preço: R$ '))
print(f'O resumo de {moeda4.moeda(preco)} é: {moeda4.resumo(preco, 20, 10)}')

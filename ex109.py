# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda3
preco = int(input('Digite o preço: R$ '))
print(
    f'A metade de {moeda3.moeda(preco)} é {moeda3.metade(preco, True)}')
print(
    f'O dobro de {moeda3.moeda(preco)} é {moeda3.dobro(preco, True)}')
print(
    f'Aumentando 10%, temos {moeda3.aumentar(preco, 10, True)}')
print(
    f'Diminuindo 13%, temos {moeda3.diminuir(preco, 13, True)}')

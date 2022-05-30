# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import moeda2
preco = int(input('Digite o preço: R$ '))
print(
    f'A metade de {moeda2.moeda(preco)} é {moeda2.moeda(moeda2.metade(preco))}')
print(
    f'O dobro de {moeda2.moeda(preco)} é {moeda2.moeda(moeda2.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda2.moeda(moeda2.aumentar(preco))}')
print(f'Diminuindo 10%, temos {moeda2.moeda(moeda2.diminuir(preco))}')

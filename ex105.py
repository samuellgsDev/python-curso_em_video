# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação(opcional)
#
def notas(*num,  situ=False):
    """função para avaliar notas e situação de vários alunos

    Args:
        situ ( optional): Valor opcional para saber se deve ou não avaliar a situação 

    Returns:
        dicionário: valor retornado com várias informações
    """
    answer = dict()
    answer['total'] = len(num)
    answer['bigger'] = max(num)
    answer['smaller'] = min(num)
    answer['avarage'] = sum(num)/len(num)
    if situ:
        print(answer)
        if answer['avarage'] >= 7:
            print('boa')
        elif answer['avarage'] >= 5:
            print('razoavel')
        else:
            print('ruim')

    return notas


resp = notas(5.5, 2.5, 1.5, situ=True)
print(resp)

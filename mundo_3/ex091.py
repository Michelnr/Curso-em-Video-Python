# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint

def rolagem_dado():
    resultado_dado = randint(1, 6)
    return resultado_dado

resultado = rolagem_dado
print(resultado)
resultados_dados = {}
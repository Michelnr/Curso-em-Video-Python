# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint

resultados = {}

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
dados_quantidade = 0
dados_resultado = 0

while dados_quantidade < 4:
    dados_resultado = randint(1,6)
    if dados_resultado not in resultados.values():
        dados_quantidade += 1
        resultados[f'Jogador {dados_quantidade}'] = dados_resultado

print(resultados)
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

####### ASSISTIR A AULA #########
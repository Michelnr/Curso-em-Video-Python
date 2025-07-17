# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint

resultados = {}

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
j = 0
while j < 4:
    j += 1
    resultados[f'Jogador-{j}'] = randint(1,10)


# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

####### ASSISTIR A AULA #########
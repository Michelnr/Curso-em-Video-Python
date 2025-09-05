# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogo = {}
placar = []

j = 0
while j < 4:
    j += 1
    jogo[f'Jogador {j}'] = randint(1,6)
print(10*'-','Rolagem de dados:',10*'-')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('\n')

placar = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(10*'-','Vencedores',10*'-')
for i, v in enumerate(placar):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}.')
    sleep(1)

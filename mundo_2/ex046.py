# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 ate 0 com uma pausa de 1 segundo.
from time import sleep

for contagem in range(10, -1, -1):
    print(f'{contagem}')
    sleep(1)
print('Feliz ano novo!')

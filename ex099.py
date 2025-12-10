# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep

def maior(numeros):
    numero_maior = max(numeros)
    '''numero_maior = numeros[0]
    for n in numeros:
        if numero_maior < n:
            numero_maior = n'''
    print(20*'=-=')
    print('Analisando os valores passados...')
    print(f"Foram informados {len(numeros)} números!")
    print('Os números são:', end=' ')
    for num in numeros:
        print(num, end=' ')
        sleep(0.5)
    print(f"\nO maior número é: {numero_maior}")
    print(20*'=-=')


numeros_random = []
for numero in range(randint(2,10)):
    numeros_random.append(randint(0, 100))

maior(numeros_random)
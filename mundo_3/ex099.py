# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint

def maior(numeros):
    numero_maior = max(numeros)
    '''numero_maior = numeros[0]
    for n in numeros:
        if numero_maior < n:
            numero_maior = n'''
    print(f"Foram informados {len(numeros)} números!")
    print(f"O maior número é: {numero_maior}")


numeros_random = []
for numero in range(0,10000):
    numeros_random.append(randint(0, 1000000000))

maior(numeros_random)
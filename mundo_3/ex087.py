"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

from random import randint

matriz = [[], [], []]

for lista in range(0, len(matriz)):
    for n in range(0,3):
        matriz[lista].append(randint(0, 100))

soma_par = 0 # A) A soma_par de todos os valores pares digitados.
for lista in range(0, len(matriz)):
    for n in matriz[lista]:
        if n % 2 ==0:
            soma_par += n

soma_3c = 0 # B) A soma dos valores da terceira coluna.
for num_3c in matriz[2]:
    soma_3c += num_3c

print('-='*7, ' Esse são os valores da Matiz ', '-='*7)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-='*30)

print(f'A) A soma de todos os valores pares digitados: {soma_par}')
print(f'B) A soma dos valores da terceira coluna: {soma_3c}')
print(f'C) O maior valor da segunda linha: {max(matriz[1])}') # C) O maior valor da segunda linha.
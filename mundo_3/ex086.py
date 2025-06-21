"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3 × 3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

matriz = [[], [], []]

for l in range(0,3):
    for n in range(0, 3):
        matriz[n].append(int(input(f'Informe um valor para [{l}, {n}]: ')))
print('-=' * 30)
for p in range(0,3):
    print(matriz[p])
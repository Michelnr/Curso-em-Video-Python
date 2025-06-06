# Faça um programa que leia 5 valores numericos e guarde em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []

while len(numeros) != 5:
    numeros.append(int(input(f"Digite um valor para a posição {len(numeros)}: ")))

print(f"\nVocê digitou os valores: ", end='')
for digi in numeros:
    print(digi, end=' ')
print(f"\nO menor numero é, {max(numeros)}, nas posições {numeros.index(max(numeros), 0, len(numeros))}", end='')
print(f"\nO menor numero é, {min(numeros)}, nas posições {numeros.index(min(numeros), 0, len(numeros))}", end='')

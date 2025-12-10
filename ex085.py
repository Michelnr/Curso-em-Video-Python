"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""
from random import randint

lista_numero = [[], []] #0 = PAR, 1 = IMPAR
for c in range(1,8):
    #numero = int(input(f"Informe o numero {c}º número: "))
    numero = (randint(1, 100))
    if numero % 2 == 0:
        lista_numero[0].append(numero)
    else:
        lista_numero[1].append(numero)

lista_numero[0].sort()
lista_numero[1].sort()

print(f'Números pares -----> {lista_numero[0]}')
print(f'Números Impares ---> {lista_numero[1]}')
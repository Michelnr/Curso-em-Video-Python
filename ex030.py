# Crie um programa que leia se um n1 inteiro e mostre na tela se ele é par ou impar
# Numeros impares divididos por 2 sempre restam 1, numero pares sempre restam 0.
from random import randint

numero = randint(1,1000)
resultado = numero % 2

if resultado == 0:
    print(f'O numero {numero} é PAR')
else:
    print(f'O numero {numero} é IMPAR')

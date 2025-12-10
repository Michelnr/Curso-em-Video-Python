# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia():
    print(20*'=-=')
    print('Escolhendo os números...', end=' ')
    while True:
        num_escolhido = randint(0, 100)
        if num_escolhido not in numeros:
            numeros.append(num_escolhido)
        if len(numeros) == 6:
            break

    for num in numeros:
        print(num, end=' ')
        sleep(0.5)

    print(f'\n{20*'---'}')

def somaPar():
    som_num_par = 0
    print('Os números somados foram:', end=' ')
    for num in numeros:
        if num % 2 == 0:
            som_num_par += num
            print(num, end=' ')
            sleep(0.5)
    print(f'= {som_num_par}')
    print(20 * '=-=')

numeros = []

sorteia()
somaPar()

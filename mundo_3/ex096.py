'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(lar, com):
    area = com * lar
    print(f'A área do terreno é {area}m².')

largura = int(input('Informe a largura do terreno (m²): '))
comprimento = int(input('Informe o comprimento do terreno (m²): '))
area(largura, comprimento)

'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(lar, com):
    areaterreno = com * lar
    print(f'A área do terreno {lar}m² X {com}m² é {areaterreno}m².')

largura = float(input('Informe a largura do terreno (m²): '))
comprimento = float(input('Informe o comprimento do terreno (m²): '))
area(largura, comprimento)

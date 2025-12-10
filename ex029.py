#Escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar  80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7.00 por cada km a cima do limite
from random import randint

velocidade_carro = randint(40,160) #O sistema simula a velocidade de um carro.

if velocidade_carro > 80: #verifica se esta dentro do limite
    print(f'Sua velocidade está em {velocidade_carro} ultrapassou o limite de 80Km/h')
    print(f'Sua multa é R${7*(velocidade_carro-80)}, pois esta a {velocidade_carro-80}Km/h fora do limite.')
else:
    print(f'Esta em {velocidade_carro}Km/h esta dentro do limite de velocidade.')

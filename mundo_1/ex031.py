#desenvolva um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens ate 200Km e R$0.45 para viagens mais longas
from random import randint

km = randint(0,400) #float(input('Qual a quilometragem da viagem? '))

if km <= 200:
    print(f'A viagem tem {km:.0f}Km e vai custar R${km*0.50}')
else:
    print(f'A viagem tem {km:.0f}Km e vai custar R${km*0.45}')

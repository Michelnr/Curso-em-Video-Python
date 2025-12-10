#Essa scrip calcula o Seno o Cosseno e a tagente de um n1.
from math import cos, radians, sin, tan

angulo = float(input('Entre com o ângulo que deseja: '))

seno = sin(radians(angulo))
print(f'O Seno de {angulo} é: {seno:.2f}')

cosseno = cos(radians(angulo))
print(f'O Cosseno de {angulo} é: {cosseno:.2f}')

tangente = tan(radians(angulo))
print(f'A Tangente de {angulo} é: {tangente:.2f}')
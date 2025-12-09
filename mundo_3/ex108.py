# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que
# consiga mostrar os números como um valor monetário formatado.
from modulos.numeros import matematica

valor_moeda = float(input('Informe o valor: R$'))

# aumento o valor em 10%
print(f'{matematica.formatoMoeda(valor_moeda)} + 10% = {matematica.formatoMoeda(matematica.aumentar10(valor_moeda))}')

# diminui o valor em 10%
print(f'{matematica.formatoMoeda(valor_moeda)} - 10% = {matematica.formatoMoeda(matematica.diminui10(valor_moeda))}')

# dobre o valor
print(f'{matematica.formatoMoeda(valor_moeda)} X 2 = {matematica.formatoMoeda(matematica.dobro(valor_moeda))}')

# divide o valor por 2
print(f'{matematica.formatoMoeda(valor_moeda)} % 2 = {matematica.formatoMoeda(matematica.metade(valor_moeda))}')
# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que
# consiga mostrar os números como um valor monetário formatado.
from modulos.numeros import moeda

valor_moeda = float(input('Informe o valor: R$'))

# aumento o valor em 10%
print(f'{moeda.formatoMoeda(valor_moeda)} + 10% = {moeda.formatoMoeda(moeda.aumentar10(valor_moeda, 10))}')

# diminui o valor em 10%
print(f'{moeda.formatoMoeda(valor_moeda)} - 10% = {moeda.formatoMoeda(moeda.diminui10(valor_moeda, 10))}')

# dobre o valor
print(f'{moeda.formatoMoeda(valor_moeda)} X 2 = {moeda.formatoMoeda(moeda.dobro(valor_moeda))}')

# divide o valor por 2
print(f'{moeda.formatoMoeda(valor_moeda)} % 2 = {moeda.formatoMoeda(moeda.metade(valor_moeda))}')
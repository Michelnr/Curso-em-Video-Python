# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from modulos.numeros import moeda

valor_moeda = float(input('Informe o valor: R$'))

# aumento o valor em 10%
print(f'{moeda.formatoMoeda(valor_moeda)} + 10% = {moeda.aumentar10(valor_moeda, 10, True)}')

# diminui o valor em 10%
print(f'{moeda.formatoMoeda(valor_moeda)} - 10% = {moeda.diminui10(valor_moeda, 10)}')

# dobre o valor
print(f'{moeda.formatoMoeda(valor_moeda)} X 2 = {moeda.dobro(valor_moeda)}')

# divide o valor por 2
print(f'{moeda.formatoMoeda(valor_moeda)} % 2 = {moeda.metade(valor_moeda)}')
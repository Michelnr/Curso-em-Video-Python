# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas
# dessas funções.
from modulos.numeros import moeda

valor_moeda = float(input('Informe o valor: R$'))

# aumento o valor em 10%
print(f'R${valor_moeda} + 10% = R${moeda.aumentar10(valor_moeda):.2f}')

# diminui o valor em 10%
print(f'R${valor_moeda} - 10% = R${moeda.diminui10(valor_moeda):.2f}')

# dobre o valor
print(f'R${valor_moeda} * 2 = R${moeda.dobro(valor_moeda):.2f}')

# divide o valor por 2
print(f'R${valor_moeda} / 2 = R${moeda.metade(valor_moeda):.2f}')
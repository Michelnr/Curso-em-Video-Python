# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas
# dessas funções.
from modulos import numeros

valor_moeda = int(input('Informe o valor: R$'))

# aumento o valor em 10%
print(f'R${valor_moeda} + 10% = R${numeros.aumentar10(valor_moeda):.2f}')

# diminui o valor em 10%
print(f'R${valor_moeda} - 10% = R${numeros.diminui10(valor_moeda):.2f}')

# dobre o valor
print(f'R${valor_moeda} * 2 = R${numeros.dobro(valor_moeda):.2f}')

# divide o valor por 2
print(f'R${valor_moeda} / 2 = R${numeros.metade(valor_moeda):.2f}')
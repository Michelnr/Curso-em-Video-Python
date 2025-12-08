# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que
# consiga mostrar os números como um valor monetário formatado.
from modulos import numeros

valor_moeda = int(input('Informe o valor: R$'))

# aumento o valor em 10%
valor_moeda_mais10 = valor_moeda
numeros.aumentar10(valor_moeda_mais10)
print(f'{valor_moeda} + 10% = {numeros.formatoMoeda(valor_moeda_mais10):.2f}')

# diminui o valor em 10%
valor_moeda_menos10 = valor_moeda
numeros.diminui10(valor_moeda_menos10)
print(f'{valor_moeda} - 10% = {numeros.diminui10(valor_moeda_menos10):.2f}')

# dobre o valor
valor_moeda_dobro = valor_moeda
numeros.dobro(valor_moeda_dobro)
print(f'{valor_moeda} * 2 = {numeros.dobro(valor_moeda_dobro):.2f}')

# divide o valor por 2
valor_moeda_metade = valor_moeda
numeros.metade(valor_moeda_metade)
print(f'{valor_moeda} / 2 = {numeros.metade(valor_moeda_metade):.2f}')
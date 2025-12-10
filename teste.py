from modulos.numeros import moeda

valor_moeda = float(input('Informe o valor: R$'))

# aumento o valor em 10%
print(moeda.formatoMoeda(moeda.aumentar10(valor_moeda)))
#print(f'{matematica.formatoMoeda(valor_moeda)} + 10% = {matematica.aumentar10(valor_moeda)}')
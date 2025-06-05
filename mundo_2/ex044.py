# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#
# -À vista dinheiro/cheque: 10% de desconto
# -À vista no cartão: 5% de desconto
# -Em ate 2x no cartão: Preço normal
# -3x ou mais no cartão: 20% de juros

valor_produto = float(input('Qual o valor do produto? '))
print(f'Escolha uma opção de pagamento:\n'
      f'1 - Dinheiro/Cheque = 10% de desconto\n'
      f'2 - Cartão a vista = 5% de desconto\n'
      f'3 - Parcelado 2x = Sem Desconto\n'
      f'4 - Parcelado 3x a 5x = 20% de juros')
forma_pagamento = int(input('Qual a formade paramento? '))

if forma_pagamento == 1:
    print(f'O produto teve um desconto de 10%.\n'
          f'Preço: R${valor_produto}\n'
          f'Preço com desconto = R${valor_produto*0.90}')
elif forma_pagamento == 2:
    print(f'O Produto teve um desconto de 5%\n'
          f'Preço: R${valor_produto}\n'
          f'Preço com desconto = R${valor_produto*0.95}')
elif forma_pagamento == 3:
    print(f'Preço do produto = R${valor_produto}\n'
          f'Valor da parcela = R${valor_produto/2}')
elif forma_pagamento == 4:
    print(f'Parcelamentos de 3x ou mais tem juros de 20%.\n'
          f'Valor do produto = R${valor_produto}\n'
          f'3 Parcelas = R${(valor_produto*1.2)/3}\n'
          f'4 Parcelas = R${valor_produto*1.20/4}\n'
          f'5 Parcelas = R${valor_produto*1.20/5}\n')

    parcela = int(input('Em quantas parcelas? '))
    if parcela == 3:
        print(f'Valor do produto = R${valor_produto}\n'
              f'Valor da parcela = R${valor_produto*1.2/parcela}')
    elif parcela == 4:
        print(f'Valor do produto = R${valor_produto}\n'
              f'Valor da parcela = R${valor_produto*1.2/parcela}')
    elif parcela == 5:
        print(f'Valor do produto = R${valor_produto}\n'
              f'Valor da parcela = R${valor_produto*1.2/parcela}')

# Crie um programa que leia o nome e o preço de varios produtos.
# o programadeverá perguntar se o usuário vai continuar . No final, mostre:
#
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$1000
# c) Qual é o nome do produto mais barato

b_produto = ''
b_valor = valor = total = contagem = 0

while True:
    produto = str(input('Produto: ')).strip().capitalize()
    valor = float(input('Valor: R$ '))
    if b_valor == 0 or b_valor > valor:
        b_valor = valor
        b_produto = produto

    if valor > 1000:
        contagem += 1

    total += valor

    menu = ' '
    while menu not in 'NS':
        menu = str(input('Deseja registrar outro produto? (S/N) ')).strip().upper()[0]
    if menu == 'N':
        break

print(f'\nTotal do compra: R${total:.2f}\n'
      f'Foram comprados {contagem} produtos que custam mais de R$1000,00\n'
      f'O produto mais barato é {b_produto} e custa R${b_valor:.2f}')

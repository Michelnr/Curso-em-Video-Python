# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('lapis', 2,
            'Caneta', 4,
            'Borracha', 3,
            'Caderno', 7,
            'Mochila', 50,
            'estojo', 10)

print('-'*40)
print(f'{"LISTA DE COMPRAS":^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>8.2f}')
print('-'*40)

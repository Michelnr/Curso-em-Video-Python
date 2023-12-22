alugueldia = int(input('Quantos dias de aluguel? '))
kmrodado = float(input('Quantos quilometros rodados? '))

preço = (60*alugueldia) + (0.15*kmrodado)

print(f'Preço do aluguel custa {preço:.2f}R$')
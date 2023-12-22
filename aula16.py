# Aula de tuplas
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[3])

# utilizando a função sorted consegue colocar em ordem.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))

# quando utilizar 1:3 por exeplo significa que vai pegar de 1 ate 2 o numero 3 é ignorado.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3])

# Quando é utilizado um numero negativo a contagem é feita de traz para frente e o -1 corresponde au ultimo.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2])

# Quando o fatiamento é utilizado com o numero negativo para frante a posição é utilizada mas para traz não.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2:])
print(lanche[:-2])

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for posi, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posi}')

# Ao somar duas Tuplas elas são colocadas uma seguida da outra.
a = (4, 2, 3, 5, 1)
b = (7, 9, 6, 8, 10)
c = a + b
print(c)


from random import shuffle

pessoa1 = str(input('Primeira pessoa: '))
pessoa2 = str(input('Segunda pessoa: '))
pessoa3 = str(input('Terceira pessoa: '))
pessoa4 = str(input('Quarta pessoa: '))

lista = [pessoa1, pessoa2, pessoa3, pessoa4]
shuffle(lista)

print(f'A ordem será: {lista}')
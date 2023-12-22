from random import randint
numeros = (randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))
print(f'Os numeros sorteados foram {sorted(numeros)}')
print(f'O maior numero é {max(numeros)}\n'
      f'O menor numero é {min(numeros)}')
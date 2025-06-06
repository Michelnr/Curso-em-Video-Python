n = int(input('Digite um número para calcular seu Fatorial: '))
contador = n
fatorial = 1
print(f'O calculo do Fatorial do {n}! é: ', end = '')
while contador > 0:
    print(contador, end ='')
    print(' X ' if contador > 1 else ' = ', end ='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}', end='')

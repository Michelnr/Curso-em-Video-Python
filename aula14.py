n1 = 1
par = 0
impar = 0

while n1 != 0: #"while not in" pode ser usado para string.
    n1 = int(input('Infomer um numero: '))
    if n1 != 0:
        if n1 % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} numeros PARES e {impar} numeros IMPARES')
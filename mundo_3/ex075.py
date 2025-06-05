# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = (int(input('Digite o primeiro numero: ')),
           int(input('Digite o Segundo numero: ')),
           int(input('Digite o terceiro numero: ')),
           int(input('Digite o quarto numero: ')))
if 9 in numeros:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')
else:
    print('Não possui numero 9')
if 3 in numeros:
    print(f'O valor 3 apareceu primeiro na posição {numeros.index(3)+1}')
else:
    print('Não possui numero 3')
print(f'Numeros Pares: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')

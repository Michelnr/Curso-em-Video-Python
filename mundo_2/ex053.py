# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
frase_sep = frase.split()
frase_junt = ''.join(frase_sep)
frase_invert = ''

for palindromo in range(len(frase_junt) - 1, -1, -1):
    frase_invert += frase_junt[palindromo]
print(f'O inverso de {frase_junt} é o inverso de {frase_invert}.')
if frase_junt == frase_junt:
    print(f'Temos um Palindromo')
else:
    print(f'Não temos um palindromo')

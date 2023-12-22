# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Melissa', 'Talita', 'Michel', 'Liz', 'Yasmin', 'Maria', 'Micael')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letras in p:
        if letras.lower() in 'aeiouy':
            print(letras, end=' ')

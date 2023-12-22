# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Qual a razão: '))
contador = 1
while contador != 11:
    print(f'{primeiro} -> ', end='')
    primeiro += razao
    contador += 1
print('Acabou!')

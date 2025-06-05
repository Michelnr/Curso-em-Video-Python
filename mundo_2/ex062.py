# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# o programa encerra quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
contador = 1
while contador != 11:
    print(f'{primeiro_termo} ', end='')
    if contador != 10:
        print('-> ', end='')
    primeiro_termo += razao
    contador += 1
    if contador == 11:
        menu = int(input('\nDeseja que motre mais Quantos? [0 = Sair]: '))
        if menu != '0':
            contador -= menu
print('Acabou!')

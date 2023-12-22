# Crie um programa que tenha uma tupla totalmente preencjida com uma contagem por extenso, de zero a vinte.
#
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostraá-lo por extenso.
nu_est = ('zero', 'um', 'dois', 'treis', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    nu = int(input('[Sair = -1] - Informe um numero entre 0 e 20: '))
    if nu <= 20:
        print(f'Você digitou numero {nu_est[nu]}')
    elif nu > 20:
        print('Tente novamente: ')
    menu = str(input('Deseja continuar? S/N ')).strip().upper()
    if menu == 'N':
        break

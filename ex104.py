# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(numero_informado):
    print(20*'__')
    while True:
        num_str = str(input(f'{numero_informado}'))
        if num_str.isnumeric() == True:
            return num_str
            break
        else:
            print('\033[31mERRO! Digite um número válido\033[0m')


numero = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {numero}')
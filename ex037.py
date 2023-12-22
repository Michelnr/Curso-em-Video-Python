# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
#-1 para binário
#-2 para octal
#-3 para hexadecimal

numero = int(input('Informe um número inteiro: '))
print('Informe o n1 correspondente a conversão desejada:\n'
      '1 - Binario\n'
      '2 - Octal\n'
      '3 - Hexadecimal')
escolha = int(input('Digite o número: '))

if escolha == 1:
    numero=bin(numero)
    print(f'Este numero em binario é: {numero[2:]}')
elif escolha == 2:
    numero=oct(numero)
    print(f'Este numero em Octal é: {numero[2:]}')
elif escolha == 3:
    numero=hex(numero)
    print(f'Este numero em hexadecimal é: {numero[2:]}')
else:
    print('ERRO - Você precisa escolher entre as 3 opções!')

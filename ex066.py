# Crie um programa que leia varios números inteiros pelo teclado.
# o programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma_par entre eles. (Desconsiderando o flag)

soma = contador = 0

while True:
    numero = int(input('Digite um numero: (sair = 999) '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'Foram digitados {contador} números e a soma é {soma}')

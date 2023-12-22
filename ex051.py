# desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# no final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Qual a razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for pa in range(primeiro_termo, decimo + razao, razao):
    print(f'{pa} -> ', end='')
print('Acabou!')

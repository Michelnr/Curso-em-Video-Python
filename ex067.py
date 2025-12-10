# Faça um programa que mostre a tabuada de varias números, um de cada vez,
# para cada valor digitado pelo usuario.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Qual o número deseja ver a tabuada? (-1 = sair) '))
    if numero < 0:
        break
    for nu_tab in range(1,11):
        print(f'{numero} X {nu_tab} = {numero * nu_tab}')
        nu_tab += 1
print('Programa Finalizado!')

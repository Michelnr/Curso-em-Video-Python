# refaça o desafio 009, mostrando a tabuada de um número que o usuário escolha,
# só agora utilizando um laço for.
numero = int(input('Qual taboada deseja saber? '))
for n_tabu in range(1,11):
    print(f'{numero} x {n_tabu} = {numero*n_tabu}')

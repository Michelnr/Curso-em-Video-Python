# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça para digitar novamente ate ter um valor correto.
m = 0
f = 0
sexo = ''

while sexo != 'C':
    sexo = str(input(f'M = Masculino\nF = Feminino\nC = Concluir\n'
                     f'Informe seu sexo: ')).upper().strip()
    if sexo == 'M':
        m += 1
    elif sexo == 'F':
        f += 1
    elif sexo == 'C':
        print('\033[32mPrograma concluido\033[m, veja abaixo a conclusão!')
    else:
        print('\033[31mERRO\033[m, informe o valor correto!')
        print(sexo)
print(f'Esse é o total de pessoas:\n'
      f'Homens = {m}\n'
      f'Mulheres = {f}\n'
      f'Total de pessoas = {m+f}')

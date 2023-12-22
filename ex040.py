# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a mádia atingida:
#
# -Média abaixo de 5.0: REPROVADO
# -Media entre 5.0 e 6.9: RECUPERAÇÃO
# -Média acima de 7.0: APROVADO

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1+nota2)/2

if media < 5.0:
    print(f'Sua media foi {media:.2f} - REPROVADO')
elif 5.0 <= media <= 6.9:
    print(f'Sua media foi {media:.2f} - RECUPERAÇÂO')
else:
    print(f'Sua media foi {media:.2f} - APROVADO')

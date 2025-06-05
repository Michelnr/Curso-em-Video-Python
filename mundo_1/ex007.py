nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print(f'Aluno aprovado com media {media:.2f}!')
else:
    print(f'Aluno reprovado com media {media:.2f}!')

#print(f'Nota 1: {nota1}\nNota 2: {nota2}\nNota Total: {nota1+nota2}\nA media: {media :.5}')

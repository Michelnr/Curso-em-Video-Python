# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

def notas(*valor_notas, sit=False):
    '''
    -> Pode ser informada varias notas e o programa vai verificar:
    1 - quantas notas foram informadas
    2 - qual a maior nota
    3 - Qual a menor nota
    4 - Qual a media das notas
    sit = Qual a situação do aluno
    '''
    cad_notas = {}
    cad_notas['Total'] = len(valor_notas)
    cad_notas['Maior'] = max(valor_notas)
    cad_notas['Menor'] = min(valor_notas)
    cad_notas['Media'] = sum(valor_notas)/len(valor_notas)
    
    if sit == True:
        if 7 <= cad_notas['Media'] < 10:
            cad_notas['Situação'] = 'Excelente'
        elif 5 <= cad_notas['Media'] < 7:
            cad_notas['Situação'] = 'BOA'
        else:
            cad_notas['Situação'] = 'RUIM'

    return cad_notas
           

# Programa Principal
resp = notas(5.5, 2.5, 10, 8.5, sit=True)
print(resp)
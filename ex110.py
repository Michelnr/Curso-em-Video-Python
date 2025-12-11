# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from modulos.numeros.moeda import resumo

valor = float(input('Por favor, informe o valor para analise: '))
porcentagemAumento = int(input('Informe a % do aumento:  '))
porcentagemReducao = int(input('Informe a % da redução:  '))

print(resumo(valor, porcentagemAumento, porcentagemReducao))
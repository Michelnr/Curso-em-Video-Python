# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
from datetime import datetime

cadastro_funci = {"funcionario":[], }

nome_funci = str(input('Informe o nome: '))
ano_nascimento = int(input('Informe seu ano de nascimento: '))
carteira_ctps = int(input('Informe o numero da CTPS: '))

# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
if carteira_ctps != 0:
    ano_contrato = int(input("Informe o ano da contratação: "))
    Salario_brunto = float(input("Informe o valor do salário: R$"))

# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
## 65 anos por idade, com 15 anos de contribuição.
ano_hoje = datetime.now()
ano_hoje = ano_hoje.year

idade_funci = ano_hoje-ano_nascimento

print(30*"---")
print(f'Nome: ', nome_funci)
print(f'Nascimento: ', ano_nascimento)
print(f'Numero CTPS: ', carteira_ctps)
print(f'Anos de inicio: ', ano_contrato)
print(f'Salario bruto: ', Salario_brunto)
print(f'Ano Atual: ', ano_hoje)
print(f'Idade: ', idade_funci)

####### ASSISTIR A AULA #######
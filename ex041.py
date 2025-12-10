# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# -Ate 9 anor: MIRIM
# -Ate 14 anor: INFANTIL
# -Ate 19 anos: JUNIOR
# -Ate 25 anos: SÊNIOR
# -ACIMA: MASTER
from datetime import date

ano_nasci = int(input('Qual seu ano de nascimento? '))

idade = date.today().year-ano_nasci

if idade <= 9:
    print(f'Sua idade é de {idade} anos, então sua categoria é MIRIM')
elif idade <= 14:
    print(f'Sua idade é de {idade} anos, então sua categoria é INFANTIL')
elif idade <= 19:
    print(f'Sua idade é de {idade} anos, então sua categoria é JUNIOR')
elif idade <= 25:
    print(f'Sua idade é de {idade} anos, então sua categoria é SÊNIOR')
else:
    print(f'Sua idade é de {idade} anos, então sua categoria é MASTER')

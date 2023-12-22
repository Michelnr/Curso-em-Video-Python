print('='*35)
print(f'        Banco Curso em Video')
print('='*35)
saque = int(input('Informe o valor do saque: R$'))
total = saque
nota = 200
contador = 0

while True:
    if total >= nota:
        total -= nota
        contador += 1
    else:
        print(f'{contador} notas de {nota}')
        if nota == 200:
            nota = 100
        elif nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        contador = 0
        if total == 0:
            break

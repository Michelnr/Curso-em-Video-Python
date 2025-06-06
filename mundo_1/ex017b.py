from math import hypot

cateto_ad = float(input('Qual o Cateto Adjacente? '))
cateto_op = float(input('Qual o Cateto Aposto? '))
hipotenusa = hypot(cateto_op, cateto_ad)

print(f'A hipotenusa mede {hipotenusa:.2f}')
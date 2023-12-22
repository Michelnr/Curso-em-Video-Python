cateto_ad = float(input('Qual o Cateto Adjacente? '))
cateto_op = float(input('Qual o Cateto Aposto? '))

hipotenusa = (cateto_ad ** 2 + cateto_op ** 2) ** (1/2)

print(f'A Hipotenusa mede {hipotenusa:.2f}.')

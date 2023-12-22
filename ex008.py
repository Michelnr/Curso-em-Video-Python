#Converte o Metros para Centimetros e Milimetros.

mt = float(input('Quantos metros? '))
km = mt*0.001
hm = mt*0.01
dam = mt*0.1
#Metros
dm = mt*10
ct = mt*100
mm = mt*1000

print(f'Valor em quilometros: {km:.3f}km\n'
      f'Valor em hm: {hm:.3f}hm\n'
      f'Valor em dam: {dam:.3f}dam\n'
      f'Valor em Metros: {mt:.0f}mt\n'
      f'Valor em Centimetros: {ct:.0f}cm\n'
      f'Valor em Milimetros {mm:.0f}mm')
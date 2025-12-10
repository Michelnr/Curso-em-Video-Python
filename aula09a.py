#FATIAMENTO de String;
#Colocar um valor entre couchetes correspondente a ordem numerica mostra a determinada letra.
print('Numero : 1')
frase = 'Curso em Video Python'
print(frase[9]);
print(f'\n')

#Nesse comando o fatiamento acontece em os caractes 9 a 13 o ultimo é desconsiderado.
print('Numero : 2')
print(frase[9:14]);
print(f'\n')

#Esse comando faz o fatiamento pulando de 2 em 2
print('Numero : 3')
print(frase[9:21:2]);
print(f'\n')

#Fatiamento de todos os caracteres ate o informado.
print('Numero : 4')
print(frase[:5]);
print(f'\n')

#Fatiamento de todos os caracteres a partir do informado.
print('Numero : 5')
print(frase[15:]);
print(f'\n')

#Fatiamento sem dizer o final ou o inicio.
print('Numero : 6')
print(frase[9::3]);
print(frase[:9:3]);
print(f'\n')

#ANALISE de String
#O comando LEN conta quantos caracteres possui uma string
#(Lembrando que espaços vazios tambem contam)
print('Numero : 7')
print(len(frase));
print(f'\n')

#O comando count mostra quandos carateres do informado possuem em uma string
#No segundo comando tem uma modificação mostrando como fatiar neste comando
#(Lembrando que o Python discrimina maiusculas e minusculas.
print('Numero : 8')
print(frase.count('o'));
print(frase.count('o',0,13));
print(f'\n')

#Comando que busca a posição do que foi informado.
#No segundo exeplo a palavra não existe então o sistema retorna -1
print('Numero : 9')
print(frase.find('deo'));
print(frase.find('android'));
print(f'\n')

#o comando IN funciona da mesma forma que o comando FIND porem retorna TRUE
#Lembrado que o Python discrimina maiusculas e minusculas.
print('Numero : 10')
print('Curso' in frase);
print(f'\n')

#TANSFORMAÇÃO:
print('Numero : 11')
print(frase.replace('Python','Android'));
print(f'\n')

#Transforma MINUSCULO em MAIUSCULO
print('Numero : 12')
print(frase.upper());
print(f'\n')

#Transforma tudo MAIUSCULO em MINUSCULO
print('Numero : 13')
print(frase.lower());
print(f'\n')

#Trasforma todas as letras em MINUSCULAS com excessão da primeira
print('Numero : 14')
print(frase.capitalize());
print(f'\n')

#Transforma a letra depois de um espaço em MAIUSCULA
print('Numero : 15')
print(frase.title());
print(f'\n')

#Remove os espaços em abranco no INICIO e no FIM de um texto
print('Numero : 16')
print(frase.strip());
print(frase.rstrip()); #Para remover os espaços apenas a Direita.
print(frase.lstrip()); #Para remover os espaços apenas a Esquerda.
print(f'\n')

#DIVISÂO DE STRING
#Divide a String atraves dos espaços.
print('Numero : 17')
print(frase.split())
print(f'\n')

#JUNÇÃO
#Junta uma frase substituindo os espaços em branco pelo o que tiver entro os parenteses
print('Numero : 18')
'-'.join(frase)
print(f'\n')

#Cor no print com o comando\033[m

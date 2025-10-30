'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) 
Saída:
 ~~~~~~~~~
Ola, Mundo!
 ~~~~~~~~~'''

def escrita(palavra):
    tam = len(palavra) + 4
    print('~'*tam)
    print('|',palavra,'|')
    print('~'*tam)

texto = input('Escreva a plavra: ').title().strip()
escrita(texto)
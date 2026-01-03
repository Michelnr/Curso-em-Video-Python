# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento.\033[0m')
else:
    print('\033[32mO site Pudim está acessível!\033[0m')
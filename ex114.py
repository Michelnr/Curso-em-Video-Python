# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib.request
import urllib.error

# Definimos o site
url = 'https://www.pudim.com.br'

# Criamos um "disfarce" (User-Agent de um navegador real)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

try:
    # Criamos a requisição com o disfarce
    req = urllib.request.Request(url, headers=headers)
    
    # Tentamos abrir
    site = urllib.request.urlopen(req)
    
except urllib.error.HTTPError as erro:
    # Se der 403, cairá aqui
    print(f'\033[31mErro de HTTP: {erro.code} - {erro.reason}\033[0m')
    
except urllib.error.URLError as erro:
    # Se houver erro de rede/URL
    print(f'\033[31mErro de URL: {erro.reason}\033[0m')
    
else:
    print('\033[32mO site Pudim está acessível com sucesso!\033[0m')

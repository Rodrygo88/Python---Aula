print("====== DESAFIO 114 ======") 

import requests

url = "https://www.pudim.com.br"

if requests.get(url).status_code == 200:
    print("O servidor está disponível.")
else:
    print("O servidor está indisponível.")
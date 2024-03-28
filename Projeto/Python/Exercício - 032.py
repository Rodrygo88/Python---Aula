print("====== DESAFIO 032 ======")
import datetime
import math
num = int(input("Digite um ano: (Digite 0 para pegar o ano atul) "))

atual = datetime.datetime.now()
data = atual.date()

if num == 0:
    num = data.year
    
teste =  num%4
teste2 = num%100
teste3 = num%400
if teste == 0 and teste2 != 0 or teste3 == 0:
    print("Ano é BISSEXTO!")
else:
    print("Ano NÃO é BISSEXTO!")    
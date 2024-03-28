print("====== DESAFIO 041 ======")

import datetime
import time

nascimento = int(input("Ano de nascimento: "))

atual = datetime.datetime.now()
data = atual.date()
data = data.year

idade =  data - nascimento

print(f"Sua idade é de {idade} anos")
print("Carregando...")
time.sleep(3)

if idade <= 9:
    print("É um atleta MIRIM! ")
elif idade <= 14:
    print("É um atleta INFATIL! ")
elif idade <= 19:
    print("É um atleta JUNIOR! ")
elif idade <= 25:
    print("É um atleta SÊNIOR! ")
else:
    print("É um aluno MASTER!!!")

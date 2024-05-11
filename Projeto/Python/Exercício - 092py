print("====== DESAFIO 092 ======") 

import datetime

pessoa = {}

pessoa["nome"] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
pessoa["idade"] = datetime.date.today().year - ano
pessoa["ctps"] = int(input("Carteira de trabalho: (Não tiver, digite 0) "))

if pessoa["ctps"] != 0:
    pessoa["contratação"] = int(input("Ano de contratação: "))
    pessoa["salario"] = float(input("Salário: R$"))

    pessoa["aposentar"] = (pessoa["contratação"] - ano) + 30


for k, v in pessoa.items():
    print(f"{k} tem o valor {v}")
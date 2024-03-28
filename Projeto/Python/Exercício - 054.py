print("====== DESAFIO 054 ======")
import datetime

atual = datetime.datetime.now()
data = atual.date()
atual = data.year

maior = 0
menor = 0

for c in range(0, 7):
    ano = int(input(f"Ano de nascimento da {c+1}º pessoa:" ))
    idade = atual - ano

    if idade >= 21:
        maior += 1
    else:
        menor += 1


print(f"Tem {maior} maiores de idade!")
print(f"Tem {menor} menores de idade!")
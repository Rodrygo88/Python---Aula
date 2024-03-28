print("====== DESAFIO 039 ======")
import datetime

ano = int(input("Ano de nascimento: "))

atual = datetime.datetime.now()
data = atual.date()
data = data.year

idade = data - ano

if idade == 18:
    print("Você FEZ 18 anos, é a hora de se alistar!")

elif idade < 18:
    ano2 = 18 - idade
    print(f"Você AINDA NÃo tem 18 anos ainda, vai precisar se alistar daqui {ano2} anos, em {data+ano2}.")
else:
    ano2 = idade - 18
    print(f"Você JÁ tem mais de 18 anos e ja passou {ano2} anos sem se alistar, era em {data-ano2}, regularize agora! ")
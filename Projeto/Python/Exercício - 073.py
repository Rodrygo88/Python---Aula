print("====== DESAFIO 073 ======")

tabela = (
    "Bahia", "Atlético-GO", "São Paulo", "Atlético-MG", "Palmeiras", "Chapecoense", "Botafogo", "Corinthians", "Criciúma", "Cruzeiro", "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Gremio", "Internacional", "Juventude","Bragantino", "Vasco da Gama", "EC Vitória"
    )

print("====== TOP 5 ======")
for cont, time in enumerate(tabela[0:5]):
    print(f"{cont+1}º lugar: {time}")
print("=================== \n")

print("====== ÚLTIMOS 4 ======")
for cont, time in enumerate(tabela[16:]):
    print(f"{cont+17}º lugar: {time}")
print("=================== \n")

print("====== TODOS EM ORDEM ======")
for cont, time in enumerate(sorted(tabela)):
    print(f"{cont+1}º lugar: {time}")
print("=================== \n")

print("====== CADE? ======")
for cont, time in enumerate(tabela):
    if time == "Chapecoense":
        print(f"A Chapecoense está na posição: {cont+1}º lugar")
print("===================")
print("====== DESAFIO 071 ======")

print("-- Caixa Eletrônico --")

valor = int(input("Valor a ser sacado: R$"))

notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0

while True:
    if valor >= 50:
        notas_50 += 1
        valor -= 50
    if valor >= 20 and valor < 50:
        notas_20 += 1
        valor -= 20
    if valor >= 10 and valor < 20:
        notas_10 += 1
        valor -= 10
    if valor >= 1 and valor < 10:
        notas_1 += 1
        valor -= 1

    if valor == 0:
        break

print("Saida: ")
print(f"{notas_50} cédulas de R$50")
print(f"{notas_20} cédulas de R$20") 
print(f"{notas_10} cédulas de R$10")
print(f"{notas_1} cédulas de R$1")